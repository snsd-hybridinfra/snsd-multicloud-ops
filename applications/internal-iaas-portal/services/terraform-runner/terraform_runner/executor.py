from __future__ import annotations

import hashlib
import ipaddress
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlsplit

from .config import Settings
from .supply_chain import (
    SupplyChainError,
    load_supply_chain,
    sanitized_attestation,
    sha256_file as supply_chain_file_sha256,
    validate_module_source,
    validate_plan_json,
)


ALLOWED_MODULES = {
    "openstack-dev-vm-small": {
        "product_id": "DEV-OS-VM-S",
        "module_version": "1.0.0",
        "artifact_digest": "sha256:97f4ece588f80e2ea24524e07d5662c5d6d93b78bcccf75bb935fad99ae090f0",
        "flavor_setting": "flavor_small",
    },
    "openstack-dev-vm-medium": {
        "product_id": "DEV-OS-VM-M",
        "module_version": "1.0.0",
        "artifact_digest": "sha256:624d5ff0d50bfc97c733a48b78d2d4e4f3cdf4633898a1b5e52ad4003f28a10a",
        "flavor_setting": "flavor_medium",
    },
    "openstack-dev-vm-large": {
        "product_id": "DEV-OS-VM-L",
        "module_version": "1.0.0",
        "artifact_digest": "sha256:b09a0e5e839100bfb09e09469738eca9195418bf2e93153e5f03bcc21db2deae",
        "flavor_setting": "flavor_large",
    },
    "openstack-dev-k3s-small": {
        "product_id": "DEV-OS-K3S-S",
        "module_version": "1.0.0",
        "artifact_digest": "sha256:fa1542d73dd9f6c3e7981bd9fe6d0c18564180055f7890ed98aa6575e3286960",
        "configuration_digest": "sha256:27ae92895d90f49a118c2fa5db7e897173e15fa002796090765872769c4a6e18",
        "flavor_setting": "flavor_medium",
        "service_profile": "K3S_SINGLE_NODE",
    },
    "openstack-dev-k3s-medium": {
        "product_id": "DEV-OS-K3S-M",
        "module_version": "1.0.0",
        "artifact_digest": "sha256:12867fb8f7fef31fe34d63305b13555fb1ef3fd37ea789daa6e67b9a4ba5b03a",
        "configuration_digest": "sha256:27ae92895d90f49a118c2fa5db7e897173e15fa002796090765872769c4a6e18",
        "flavor_setting": "flavor_large",
        "service_profile": "K3S_SINGLE_NODE",
    },
}


class TerraformExecutionError(RuntimeError):
    def __init__(self, message: str, code: str = "APPLY_FAILED"):
        super().__init__(message)
        self.code = code


def _private_endpoint(endpoint: str) -> bool:
    host = urlsplit(endpoint).hostname if "://" in endpoint else endpoint
    try:
        return ipaddress.ip_address(str(host)).is_private
    except ValueError:
        return False


def module_content_digest(module_directory: Path) -> str:
    digest = hashlib.sha256()
    files = sorted(path for path in module_directory.rglob("*") if path.is_file())
    for path in files:
        relative = path.relative_to(module_directory).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class Executor:
    def __init__(self, settings: Settings):
        self.settings = settings

    def _terraform_artifact_authority(
        self, module_name: str, source: Path
    ) -> tuple[dict[str, Any], dict[str, Any], Path, str, Path]:
        """Resolve and validate locked Terraform CLI, provider and module bytes."""

        try:
            lock = load_supply_chain(
                Path(self.settings.terraform_supply_chain_lock).resolve(),
                Path(self.settings.terraform_catalog).resolve(),
            )
            locked_policy = lock["modules"].get(module_name)
            if locked_policy is None:
                raise SupplyChainError("module is absent from the supply-chain lock")
            local_policy = ALLOWED_MODULES[module_name]
            for field in ("product_id", "module_version", "artifact_digest"):
                if local_policy.get(field) != locked_policy.get(field):
                    raise SupplyChainError("runner allow-list differs from the machine lock")
            module_validation = validate_module_source(
                source, module_name, locked_policy, module_content_digest
            )

            terraform_path = Path(self.settings.terraform_bin)
            if not terraform_path.is_absolute():
                resolved = shutil.which(self.settings.terraform_bin)
                if not resolved:
                    raise SupplyChainError("approved Terraform CLI is unavailable")
                terraform_path = Path(resolved)
            terraform_path = terraform_path.resolve()
            expected_terraform = self.settings.terraform_binary_sha256
            if not re.fullmatch(r"[0-9a-f]{64}", expected_terraform):
                raise SupplyChainError("Terraform CLI SHA-256 approval is missing")
            if supply_chain_file_sha256(terraform_path) != f"sha256:{expected_terraform}":
                raise SupplyChainError("Terraform CLI digest mismatch")

            mirror_root = Path(self.settings.terraform_provider_mirror_root).resolve()
            provider_package = Path(self.settings.openstack_provider_package).resolve()
            if not mirror_root.is_dir() or not provider_package.is_file():
                raise SupplyChainError("approved provider filesystem mirror is unavailable")
            if mirror_root != provider_package.parent and mirror_root not in provider_package.parents:
                raise SupplyChainError("provider package is outside the approved mirror")
            expected_provider = self.settings.openstack_provider_package_sha256
            if not re.fullmatch(r"[0-9a-f]{64}", expected_provider):
                raise SupplyChainError("provider package SHA-256 approval is missing")
            provider_digest = supply_chain_file_sha256(provider_package)
            if provider_digest != f"sha256:{expected_provider}":
                raise SupplyChainError("OpenStack provider package digest mismatch")
        except (OSError, SupplyChainError) as exc:
            raise TerraformExecutionError(str(exc), "POLICY_DENIED") from exc
        return lock, module_validation, terraform_path, provider_digest, mirror_root

    def _inspect_plan(
        self,
        terraform_bin: str,
        workspace: Path,
        environment: dict[str, str],
        policy: dict[str, Any],
        operation: str,
        *,
        failure_code: str,
    ) -> dict[str, Any]:
        raw = self._command(
            [terraform_bin, "show", "-json", "tfplan"],
            workspace,
            environment,
            failure_code=failure_code,
        )
        try:
            parsed = json.loads(raw)
            return validate_plan_json(parsed, policy, operation)
        except (json.JSONDecodeError, SupplyChainError) as exc:
            raise TerraformExecutionError(str(exc), "POLICY_DENIED") from exc

    def _saved_plan_apply(
        self,
        terraform_bin: str,
        workspace: Path,
        environment: dict[str, str],
        policy: dict[str, Any],
        operation: str,
        *,
        failure_code: str,
        apply_failure_code: str | None = None,
        before_apply: Callable[[], None] | None = None,
    ) -> dict[str, Any]:
        plan_command = [terraform_bin, "plan"]
        if operation == "DESTROY":
            plan_command.append("-destroy")
        plan_command.extend(["-input=false", "-out=tfplan", "-no-color"])
        self._command(
            plan_command,
            workspace,
            environment,
            failure_code=failure_code,
        )
        validation = self._inspect_plan(
            terraform_bin,
            workspace,
            environment,
            policy,
            operation,
            failure_code=failure_code,
        )
        if before_apply is not None:
            before_apply()
        self._command(
            [terraform_bin, "apply", "-input=false", "-auto-approve", "tfplan"],
            workspace,
            environment,
            failure_code=apply_failure_code or failure_code,
        )
        return validation

    def _validate_job(self, job: dict[str, Any]) -> None:
        module_name = str(job.get("module_name", ""))
        policy = ALLOWED_MODULES.get(module_name)
        if policy is None:
            raise TerraformExecutionError(
                "job requested a module outside the allow-list", "POLICY_DENIED"
            )
        values = job.get("input_values") or {}
        required = {
            "request_id",
            "owner_id",
            "project_name",
            "workload_purpose",
            "product_id",
            "product_version",
            "expires_at",
            "approved_by",
            "required_tags",
        }
        if not required.issubset(values):
            raise TerraformExecutionError("job is missing approved inputs", "POLICY_DENIED")
        if (
            job.get("product_code") != policy["product_id"]
            or job.get("module_version") != policy["module_version"]
            or job.get("artifact_digest") != policy["artifact_digest"]
        ):
            raise TerraformExecutionError(
                "job does not match the signed product catalog", "POLICY_DENIED"
            )
        if policy.get("configuration_digest") and values.get(
            "configuration_digest"
        ) != policy.get("configuration_digest"):
            raise TerraformExecutionError(
                "job does not match the approved Ansible configuration",
                "POLICY_DENIED",
            )
        self._validate_blueprint_manifest(job, values, policy)
        tags = values.get("required_tags") or {}
        required_tags = {
            "RequestId",
            "OwnerId",
            "ProductId",
            "ExpiresAt",
            "ManagedBy",
            "Exposure",
        }
        if (
            not required_tags.issubset(tags)
            or tags.get("RequestId") != job.get("request_id")
            or tags.get("ManagedBy") != "terraform-runner"
            or tags.get("Exposure") != "private-only"
        ):
            raise TerraformExecutionError("mandatory ownership tags are invalid", "POLICY_DENIED")

    def _validate_blueprint_manifest(
        self,
        job: dict[str, Any],
        values: dict[str, Any],
        policy: dict[str, Any],
    ) -> None:
        blueprint_id = values.get("blueprint_id")
        manifest_digest = values.get("manifest_digest")
        manifest = values.get("resolved_manifest")
        if blueprint_id is None:
            if manifest_digest is not None or manifest is not None:
                raise TerraformExecutionError(
                    "orphan blueprint manifest metadata", "POLICY_DENIED"
                )
            return
        if blueprint_id != "VM_APPLICATION_STACK" or not isinstance(manifest, dict):
            raise TerraformExecutionError(
                "blueprint is outside the runner allow-list", "POLICY_DENIED"
            )
        unsigned = {key: value for key, value in manifest.items() if key != "manifest_digest"}
        calculated = "sha256:" + hashlib.sha256(
            json.dumps(
                unsigned,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            ).encode("utf-8")
        ).hexdigest()
        expected_plan = [
            {"component_id": "COMPUTE_VM", "binding_status": "EXECUTION_PROFILE_BOUND_LOCAL"},
            {"component_id": "NETWORK_POLICY", "binding_status": "POLICY_BOUND_LOCAL"},
            {"component_id": "OPERATIONS_PROFILE", "binding_status": "POLICY_BOUND_LOCAL"},
        ]
        size_profiles = {
            "SMALL": "DEV-OS-VM-S",
            "STANDARD": "DEV-OS-VM-M",
            "LARGE": "DEV-OS-VM-L",
        }
        if (
            calculated != manifest_digest
            or manifest.get("manifest_digest") != manifest_digest
            or manifest.get("blueprint_id") != blueprint_id
            or manifest.get("environment") not in {"DEV", "TEST", "STG"}
            or size_profiles.get(str(manifest.get("size"))) != policy["product_id"]
            or manifest.get("duration_hours") is None
            or manifest.get("selected_execution_profile") != policy["product_id"]
            or manifest.get("network_profile") != "PRIVATE_APPLICATION"
            or manifest.get("component_plan") != expected_plan
            or manifest.get("deployment_transaction") != "ALL_OR_NOTHING"
            or manifest.get("rollback_component_order")
            != ["OPERATIONS_PROFILE", "NETWORK_POLICY", "COMPUTE_VM"]
            or manifest.get("resolution_status") != "RESOLVED_LOCAL"
            or manifest.get("blocking_components") != []
            or manifest.get("runtime_authorized") is not False
        ):
            raise TerraformExecutionError(
                "blueprint manifest validation failed", "POLICY_DENIED"
            )
        tags = values.get("required_tags") or {}
        if (
            tags.get("BlueprintId") != blueprint_id
            or tags.get("ManifestDigest") != manifest_digest
            or values.get("product_id") != policy["product_id"]
            or job.get("product_code") != policy["product_id"]
        ):
            raise TerraformExecutionError(
                "blueprint ownership tags are invalid", "POLICY_DENIED"
            )

    def _report_payload(self, status: str, job: dict[str, Any], **values: Any) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "status": status,
            "resource_id": job.get("resource_id"),
            "details": {},
            "outputs": {},
            "validation_passed": False,
        }
        payload.update(values)
        return payload

    def run(self, job: dict[str, Any], report: Callable[[dict[str, Any]], Any]) -> None:
        operation = str(job.get("operation", "APPLY"))
        try:
            self._validate_job(job)
            if self.settings.runner_mode == "mock":
                self._report_progress(job, report)
                result = self._run_mock(job)
            elif self.settings.runner_mode == "terraform":
                result = self._run_terraform(job, report)
            else:
                raise TerraformExecutionError(
                    "RUNNER_MODE must be mock or terraform", "POLICY_DENIED"
                )
        except Exception as exc:
            failed = "PROVISION_FAILED" if operation == "APPLY" else "TERMINATION_FAILED"
            failure_code = getattr(
                exc,
                "code",
                "APPLY_FAILED" if operation == "APPLY" else "DESTROY_FAILED",
            )
            report(
                self._report_payload(
                    failed,
                    job,
                    error=str(exc)[:4000],
                    failure_code=failure_code,
                )
            )
            return
        finally:
            if self.settings.runner_mode == "terraform":
                self._cleanup_workspace(job)

        if operation == "DESTROY":
            report(self._report_payload("TERMINATED", job, validation_passed=True, outputs=result))
            return
        endpoint = str(result.get("endpoint", ""))
        actual_id = str(result.get("primary_resource_id", ""))
        if not actual_id or not endpoint or not _private_endpoint(endpoint):
            report(
                self._report_payload(
                    "PROVISION_FAILED",
                    job,
                    outputs=result,
                    error="post-apply validation rejected resource outputs",
                    failure_code="POLICY_DENIED",
                )
            )
            return
        if (
            ALLOWED_MODULES[str(job["module_name"])].get("service_profile")
            == "K3S_SINGLE_NODE"
            and result.get("bootstrap_status") != "READY"
        ):
            report(
                self._report_payload(
                    "PROVISION_FAILED",
                    job,
                    outputs=result,
                    error="k3s bootstrap requires a separate restricted runtime validation",
                    failure_code="BOOTSTRAP_VALIDATION_REQUIRED",
                )
            )
            return
        report(
            self._report_payload(
                "RUNNING",
                job,
                endpoint=endpoint,
                display_name=str(result.get("display_name", job["module_name"])),
                details={
                    "actual_resource_id": actual_id,
                    "provisioner": "Mock Terraform Runner"
                    if self.settings.runner_mode == "mock"
                    else "OpenStack Terraform Runner",
                    "module": str(job["module_name"]),
                    "module_version": str(job["module_version"]),
                    "project_name": str(job["input_values"]["project_name"]),
                    "network_exposure": "PRIVATE_ONLY",
                    "floating_ip": False,
                    "monitoring_status": "NOT_ONBOARDED",
                    "bootstrap_status": str(
                        result.get("bootstrap_status", "NOT_APPLICABLE")
                    ),
                },
                outputs=result,
                validation_passed=True,
            )
        )

    def _report_progress(
        self, job: dict[str, Any], report: Callable[[dict[str, Any]], Any]
    ) -> None:
        progress = "PROVISIONING" if job["operation"] == "APPLY" else "TERMINATING"
        report(
            self._report_payload(
                progress,
                job,
                details={"network_exposure": "PRIVATE_ONLY", "monitoring_status": "PENDING"},
            )
        )

    def _cleanup_workspace(self, job: dict[str, Any]) -> None:
        work_root = Path(self.settings.work_root).resolve()
        workspace = (work_root / str(job["job_id"])).resolve()
        if workspace.parent == work_root and workspace.exists():
            shutil.rmtree(workspace)

    def _run_mock(self, job: dict[str, Any]) -> dict[str, Any]:
        time.sleep(max(0.0, self.settings.mock_delay_seconds))
        suffix = hashlib.sha256(str(job["request_id"]).encode("utf-8")).hexdigest()[:8]
        if job["operation"] == "DESTROY":
            return {"destroyed": True}
        size = {
            "openstack-dev-vm-small": "Small",
            "openstack-dev-vm-medium": "Medium",
            "openstack-dev-vm-large": "Large",
            "openstack-dev-k3s-small": "Small",
            "openstack-dev-k3s-medium": "Medium",
        }[job["module_name"]]
        if ALLOWED_MODULES[str(job["module_name"])].get("service_profile") == "K3S_SINGLE_NODE":
            return {
                "primary_resource_id": f"os-mockk3s-{suffix}",
                "endpoint": f"https://10.250.2.{int(suffix[:2], 16) % 240 + 10}:6443",
                "display_name": f"{job['input_values']['project_name']} / OpenStack k3s PaaS {size}",
                "network_exposure": "PRIVATE_ONLY",
                "floating_ip": False,
                "bootstrap_status": "READY",
                "monitoring_status": "NOT_ONBOARDED",
            }
        return {
            "primary_resource_id": f"os-mockvm-{suffix}",
            "endpoint": f"10.250.1.{int(suffix[:2], 16) % 240 + 10}",
            "display_name": f"{job['input_values']['project_name']} / OpenStack 개발 VM {size}",
            "network_exposure": "PRIVATE_ONLY",
            "floating_ip": False,
            "monitoring_status": "NOT_ONBOARDED",
        }

    def _run_terraform(
        self, job: dict[str, Any], report: Callable[[dict[str, Any]], Any]
    ) -> dict[str, Any]:
        if not self.settings.deployment_authorized:
            raise TerraformExecutionError(
                "OpenStack deployment requires explicit runtime authorization", "POLICY_DENIED"
            )
        module_name = str(job["module_name"])
        policy = ALLOWED_MODULES[module_name]
        if (
            job["operation"] == "APPLY"
            and policy.get("service_profile") == "K3S_SINGLE_NODE"
            and not self.settings.k3s_configuration_authorized
        ):
            raise TerraformExecutionError(
                "k3s configuration requires separate runtime authorization",
                "BOOTSTRAP_VALIDATION_REQUIRED",
            )
        flavor_name = str(getattr(self.settings, str(policy["flavor_setting"])))
        image_name = (
            self.settings.approved_k3s_image_name
            if policy.get("service_profile") == "K3S_SINGLE_NODE"
            else self.settings.approved_image_name
        )
        image_setting = (
            "TF_OPENSTACK_APPROVED_K3S_IMAGE_NAME"
            if policy.get("service_profile") == "K3S_SINGLE_NODE"
            else "TF_OPENSTACK_APPROVED_IMAGE_NAME"
        )
        required_config = {
            "OS_CLIENT_CONFIG_FILE": self.settings.clouds_config_file,
            "OS_CLOUD": self.settings.cloud_name,
            "TF_OPENSTACK_NETWORK_ID": self.settings.network_id,
            image_setting: image_name,
            "TF_OPENSTACK_KEYPAIR_NAME": self.settings.keypair_name,
            str(policy["flavor_setting"]): flavor_name,
        }
        missing = [name for name, value in required_config.items() if not value]
        if not self.settings.security_group_ids:
            missing.append("TF_OPENSTACK_SECURITY_GROUP_IDS")
        if missing:
            raise TerraformExecutionError(
                "runner environment is incomplete: " + ", ".join(missing), "POLICY_DENIED"
            )
        clouds_file = Path(self.settings.clouds_config_file).resolve()
        if not clouds_file.is_file():
            raise TerraformExecutionError("OpenStack clouds.yaml is unavailable", "POLICY_DENIED")
        if (
            job["operation"] == "APPLY"
            and policy.get("service_profile") == "K3S_SINGLE_NODE"
        ):
            self._validate_k3s_configuration_inputs(policy)

        module_root = Path(self.settings.module_root).resolve()
        source = (module_root / module_name).resolve()
        if source.parent != module_root or not source.is_dir():
            raise TerraformExecutionError("approved module directory is missing", "POLICY_DENIED")
        if module_content_digest(source) != str(job["artifact_digest"]):
            raise TerraformExecutionError(
                "Terraform module content does not match the approved artifact digest",
                "POLICY_DENIED",
            )
        lock, module_validation, terraform_path, provider_digest, mirror_root = (
            self._terraform_artifact_authority(module_name, source)
        )
        locked_policy = lock["modules"][module_name]

        work_root = Path(self.settings.work_root).resolve()
        workspace = (work_root / str(job["job_id"])).resolve()
        if workspace.parent != work_root:
            raise TerraformExecutionError("invalid job workspace", "POLICY_DENIED")
        if workspace.exists():
            shutil.rmtree(workspace)
        shutil.copytree(source, workspace)

        state_root = Path(self.settings.state_root).resolve()
        state_file = (state_root / str(job["state_key"])).resolve()
        if state_root not in state_file.parents:
            raise TerraformExecutionError("invalid Terraform state key", "POLICY_DENIED")
        state_file.parent.mkdir(parents=True, exist_ok=True)

        values = dict(job["input_values"])
        values.update(
            {
                "openstack_cloud": self.settings.cloud_name,
                "target_region": self.settings.target_region,
                "network_id": self.settings.network_id,
                "security_group_ids": list(self.settings.security_group_ids),
                "approved_image_name": image_name,
                "keypair_name": self.settings.keypair_name,
                "flavor_name": flavor_name,
            }
        )
        (workspace / "approved.auto.tfvars.json").write_text(
            json.dumps(values, ensure_ascii=False), encoding="utf-8"
        )

        environment = os.environ.copy()
        environment["OS_CLIENT_CONFIG_FILE"] = str(clouds_file)
        environment["OS_CLOUD"] = self.settings.cloud_name
        environment["OS_REGION_NAME"] = self.settings.target_region
        cli_config = workspace / "terraform.rc"
        mirror_hcl = str(mirror_root).replace("\\", "/").replace('"', '\\"')
        cli_config.write_text(
            "provider_installation {\n"
            "  filesystem_mirror {\n"
            f'    path    = "{mirror_hcl}"\n'
            '    include = ["registry.terraform.io/terraform-provider-openstack/openstack"]\n'
            "  }\n"
            "}\n",
            encoding="utf-8",
        )
        environment["TF_CLI_CONFIG_FILE"] = str(cli_config)
        environment["TF_IN_AUTOMATION"] = "1"
        environment["TF_INPUT"] = "0"
        environment["CHECKPOINT_DISABLE"] = "1"
        terraform_bin = str(terraform_path)
        raw_version = self._command(
            [terraform_bin, "version", "-json"],
            workspace,
            environment,
            failure_code="PLAN_FAILED",
        )
        try:
            terraform_version = str(json.loads(raw_version).get("terraform_version", ""))
        except json.JSONDecodeError as exc:
            raise TerraformExecutionError("Terraform version output is invalid", "POLICY_DENIED") from exc
        if terraform_version != lock["engine"]["version"]:
            raise TerraformExecutionError("Terraform CLI version differs from the machine lock", "POLICY_DENIED")
        self._command(
            [
                terraform_bin,
                "init",
                "-input=false",
                f"-backend-config=path={state_file}",
            ],
            workspace,
            environment,
            failure_code="PLAN_FAILED",
        )
        self._command(
            [terraform_bin, "validate", "-no-color"],
            workspace,
            environment,
            failure_code="PLAN_FAILED",
        )
        if job["operation"] == "DESTROY":
            plan_validation = self._saved_plan_apply(
                terraform_bin,
                workspace,
                environment,
                locked_policy,
                "DESTROY",
                failure_code="DESTROY_FAILED",
                before_apply=lambda: self._report_progress(job, report),
            )
            return {
                "destroyed": True,
                "supply_chain_attestation": sanitized_attestation(
                    module_validation=module_validation,
                    plan_validation=plan_validation,
                    terraform_version=terraform_version,
                    terraform_sha256=f"sha256:{self.settings.terraform_binary_sha256}",
                    provider_sha256=provider_digest,
                ),
            }

        plan_validation = self._saved_plan_apply(
            terraform_bin,
            workspace,
            environment,
            locked_policy,
            "APPLY",
            failure_code="PLAN_FAILED",
            apply_failure_code="APPLY_FAILED",
            before_apply=lambda: self._report_progress(job, report),
        )
        raw_outputs = self._command(
            [terraform_bin, "output", "-json"],
            workspace,
            environment,
            failure_code="APPLY_FAILED",
        )
        raw_state = self._command(
            [terraform_bin, "show", "-json"],
            workspace,
            environment,
            failure_code="APPLY_FAILED",
        )
        parsed = json.loads(raw_outputs)
        result = {name: item.get("value") for name, item in parsed.items()}
        self._validate_openstack_state(
            job, json.loads(raw_state), result, flavor_name, image_name
        )
        if policy.get("service_profile") == "K3S_SINGLE_NODE":
            try:
                result.update(self._run_ansible_k3s(job, result, workspace))
            except TerraformExecutionError as configuration_error:
                try:
                    self._saved_plan_apply(
                        terraform_bin,
                        workspace,
                        environment,
                        locked_policy,
                        "DESTROY",
                        failure_code="ROLLBACK_FAILED",
                    )
                except TerraformExecutionError as rollback_error:
                    raise TerraformExecutionError(
                        f"k3s configuration failed and automatic Terraform rollback failed: {rollback_error}",
                        "ROLLBACK_FAILED",
                    ) from configuration_error
                raise TerraformExecutionError(
                    "k3s configuration failed; the Nova instance and port were automatically destroyed",
                    "CONFIGURATION_FAILED",
                ) from configuration_error
        result["supply_chain_attestation"] = sanitized_attestation(
            module_validation=module_validation,
            plan_validation=plan_validation,
            terraform_version=terraform_version,
            terraform_sha256=f"sha256:{self.settings.terraform_binary_sha256}",
            provider_sha256=provider_digest,
        )
        return result

    def _validate_k3s_configuration_inputs(self, policy: dict[str, Any]) -> None:
        if not self.settings.k3s_configuration_authorized:
            raise TerraformExecutionError(
                "k3s configuration requires separate runtime authorization",
                "BOOTSTRAP_VALIDATION_REQUIRED",
            )
        required = {
            "TF_K3S_ANSIBLE_REMOTE_USER": self.settings.ansible_remote_user,
            "TF_K3S_ANSIBLE_PRIVATE_KEY_FILE": self.settings.ansible_private_key_file,
            "TF_K3S_ANSIBLE_KNOWN_HOSTS_FILE": self.settings.ansible_known_hosts_file,
            "TF_K3S_BINARY_PATH": self.settings.k3s_binary_path,
            "TF_K3S_BINARY_SHA256": self.settings.k3s_binary_sha256,
            "TF_K3S_AIRGAP_IMAGES_PATH": self.settings.k3s_airgap_images_path,
            "TF_K3S_AIRGAP_IMAGES_SHA256": self.settings.k3s_airgap_images_sha256,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            raise TerraformExecutionError(
                "k3s configuration environment is incomplete: " + ", ".join(missing),
                "POLICY_DENIED",
            )
        ansible_root = Path(self.settings.ansible_root).resolve()
        if not ansible_root.is_dir() or module_content_digest(ansible_root) != policy.get(
            "configuration_digest"
        ):
            raise TerraformExecutionError(
                "Ansible configuration does not match the approved digest",
                "POLICY_DENIED",
            )
        for label, value in (
            ("private key", self.settings.ansible_private_key_file),
            ("known-hosts authority", self.settings.ansible_known_hosts_file),
            ("k3s binary", self.settings.k3s_binary_path),
            ("k3s air-gap archive", self.settings.k3s_airgap_images_path),
        ):
            if not Path(value).resolve().is_file():
                raise TerraformExecutionError(f"approved {label} is unavailable", "POLICY_DENIED")
        for label, value in (
            ("TF_K3S_BINARY_SHA256", self.settings.k3s_binary_sha256),
            ("TF_K3S_AIRGAP_IMAGES_SHA256", self.settings.k3s_airgap_images_sha256),
        ):
            if not re.fullmatch(r"[0-9a-f]{64}", value):
                raise TerraformExecutionError(f"{label} must be a SHA-256 digest", "POLICY_DENIED")
        for path_value, expected in (
            (self.settings.k3s_binary_path, self.settings.k3s_binary_sha256),
            (self.settings.k3s_airgap_images_path, self.settings.k3s_airgap_images_sha256),
        ):
            actual = file_sha256(Path(path_value).resolve())
            if actual != expected:
                raise TerraformExecutionError(
                    "approved k3s artifact digest validation failed", "POLICY_DENIED"
                )

    def _run_ansible_k3s(
        self, job: dict[str, Any], result: dict[str, Any], workspace: Path
    ) -> dict[str, Any]:
        host = urlsplit(str(result.get("endpoint", ""))).hostname
        if not host or not _private_endpoint(host):
            raise TerraformExecutionError(
                "Ansible target must be the validated private Nova endpoint",
                "CONFIGURATION_FAILED",
            )
        ansible_root = Path(self.settings.ansible_root).resolve()
        playbook = ansible_root / "playbooks" / "configure-k3s.yaml"
        inventory = workspace / "ansible-inventory.json"
        extra_vars = workspace / "ansible-extra-vars.json"
        inventory.write_text(
            json.dumps(
                {
                    "all": {
                        "children": {
                            "k3s_nodes": {
                                "hosts": {
                                    "approved-k3s-target": {
                                        "ansible_host": host,
                                        "ansible_user": self.settings.ansible_remote_user,
                                    }
                                }
                            }
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        quotas = (
            {
                "k3s_quota_requests_cpu": "1",
                "k3s_quota_requests_memory": "2Gi",
                "k3s_quota_limits_cpu": "2",
                "k3s_quota_limits_memory": "3Gi",
                "k3s_quota_pods": "20",
            }
            if job["module_name"] == "openstack-dev-k3s-small"
            else {
                "k3s_quota_requests_cpu": "2",
                "k3s_quota_requests_memory": "4Gi",
                "k3s_quota_limits_cpu": "4",
                "k3s_quota_limits_memory": "6Gi",
                "k3s_quota_pods": "40",
            }
        )
        extra_vars.write_text(
            json.dumps(
                {
                    "k3s_binary_source": str(Path(self.settings.k3s_binary_path).resolve()),
                    "k3s_binary_sha256": self.settings.k3s_binary_sha256,
                    "k3s_airgap_images_source": str(
                        Path(self.settings.k3s_airgap_images_path).resolve()
                    ),
                    "k3s_airgap_images_sha256": self.settings.k3s_airgap_images_sha256,
                    **quotas,
                }
            ),
            encoding="utf-8",
        )
        environment = os.environ.copy()
        environment["ANSIBLE_CONFIG"] = str(ansible_root / "ansible.cfg")
        environment["ANSIBLE_ROLES_PATH"] = str(ansible_root / "roles")
        environment["ANSIBLE_HOST_KEY_CHECKING"] = "True"
        environment["ANSIBLE_SSH_ARGS"] = (
            f"-o UserKnownHostsFile={Path(self.settings.ansible_known_hosts_file).resolve()} "
            "-o StrictHostKeyChecking=yes -o IdentitiesOnly=yes"
        )
        self._command(
            [
                self.settings.ansible_playbook_bin,
                "--inventory",
                str(inventory),
                "--limit",
                "approved-k3s-target",
                "--private-key",
                str(Path(self.settings.ansible_private_key_file).resolve()),
                "--extra-vars",
                f"@{extra_vars}",
                str(playbook),
            ],
            workspace,
            environment,
            failure_code="CONFIGURATION_FAILED",
        )
        return {
            "bootstrap_status": "READY",
            "configuration_provisioner": "ANSIBLE",
            "validated_components": [
                "k3s-api",
                "coredns",
                "metrics-server",
                "local-path-provisioner",
                "dev-resourcequota",
                "dev-limitrange",
                "dev-default-deny",
            ],
        }

    def _validate_openstack_state(
        self,
        job: dict[str, Any],
        state: dict[str, Any],
        result: dict[str, Any],
        flavor_name: str,
        image_name: str,
    ) -> None:
        resources = state.get("values", {}).get("root_module", {}).get("resources", [])
        resource_types = [str(item.get("type", "")) for item in resources]
        if sorted(resource_types) != [
            "openstack_compute_instance_v2",
            "openstack_networking_port_v2",
        ]:
            raise TerraformExecutionError(
                "post-apply state contains resources outside the approved boundary",
                "POLICY_DENIED",
            )
        instance = next(
            item.get("values", {})
            for item in resources
            if item.get("type") == "openstack_compute_instance_v2"
        )
        port = next(
            item.get("values", {})
            for item in resources
            if item.get("type") == "openstack_networking_port_v2"
        )
        metadata = instance.get("metadata") or {}
        required_tags = job["input_values"]["required_tags"]
        if (
            str(instance.get("power_state", "")).lower() != "active"
            or instance.get("image_name") != image_name
            or instance.get("flavor_name") != flavor_name
            or instance.get("key_pair") != self.settings.keypair_name
            or port.get("network_id") != self.settings.network_id
            or not port.get("port_security_enabled")
            or set(port.get("security_group_ids") or []) != set(self.settings.security_group_ids)
            or any(metadata.get(key) != value for key, value in required_tags.items())
            or result.get("floating_ip") is not False
            or not _private_endpoint(str(result.get("endpoint", "")))
        ):
            raise TerraformExecutionError(
                "post-apply OpenStack policy validation failed", "POLICY_DENIED"
            )

    @staticmethod
    def _command(
        command: list[str],
        cwd: Path,
        environment: dict[str, str],
        *,
        failure_code: str,
    ) -> str:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
            timeout=1800,
        )
        if completed.returncode != 0:
            output = (completed.stderr or completed.stdout or "execution command failed")[-4000:]
            raise TerraformExecutionError(output, failure_code)
        return completed.stdout
