from __future__ import annotations

import hashlib
import json
from pathlib import Path

from terraform_runner.config import Settings
from terraform_runner.executor import (
    ALLOWED_MODULES,
    Executor,
    TerraformExecutionError,
    module_content_digest,
)


MODULE_PRODUCTS = {
    "openstack-dev-vm-small": (
        "DEV-OS-VM-S",
        "sha256:97f4ece588f80e2ea24524e07d5662c5d6d93b78bcccf75bb935fad99ae090f0",
    ),
    "openstack-dev-vm-medium": (
        "DEV-OS-VM-M",
        "sha256:624d5ff0d50bfc97c733a48b78d2d4e4f3cdf4633898a1b5e52ad4003f28a10a",
    ),
    "openstack-dev-vm-large": (
        "DEV-OS-VM-L",
        "sha256:b09a0e5e839100bfb09e09469738eca9195418bf2e93153e5f03bcc21db2deae",
    ),
    "openstack-dev-k3s-small": (
        "DEV-OS-K3S-S",
        "sha256:fa1542d73dd9f6c3e7981bd9fe6d0c18564180055f7890ed98aa6575e3286960",
    ),
    "openstack-dev-k3s-medium": (
        "DEV-OS-K3S-M",
        "sha256:12867fb8f7fef31fe34d63305b13555fb1ef3fd37ea789daa6e67b9a4ba5b03a",
    ),
}


def job(operation: str = "APPLY", module: str = "openstack-dev-vm-small") -> dict:
    product_code, digest = MODULE_PRODUCTS.get(
        module, ("DEV-OS-VM-S", MODULE_PRODUCTS["openstack-dev-vm-small"][1])
    )
    item = {
        "job_id": "job-1",
        "request_id": "request-1",
        "operation": operation,
        "product_code": product_code,
        "product_version": 1,
        "module_name": module,
        "module_version": "1.0.0",
        "artifact_digest": digest,
        "resource_id": "WRK-request1",
        "state_key": "requests/request-1/terraform.tfstate",
        "input_values": {
            "request_id": "request-1",
            "owner_id": "user-1",
            "project_name": "payment-api-test",
            "workload_purpose": "saas-application-development",
            "product_id": product_code,
            "product_version": 1,
            "expires_at": "2026-08-13T23:59:59+09:00",
            "approved_by": "approver-1",
            "required_tags": {
                "RequestId": "request-1",
                "OwnerId": "user-1",
                "ProductId": product_code,
                "ExpiresAt": "2026-08-13T23:59:59+09:00",
                "ManagedBy": "terraform-runner",
                "Exposure": "private-only",
            },
        },
    }
    if "k3s" in module:
        item["input_values"]["configuration_digest"] = (
            "sha256:27ae92895d90f49a118c2fa5db7e897173e15fa002796090765872769c4a6e18"
        )
    return item


def test_mock_runner_uses_same_progress_and_validated_result_contract() -> None:
    reports: list[dict] = []
    Executor(Settings(runner_mode="mock", mock_delay_seconds=0)).run(job(), reports.append)
    assert [item["status"] for item in reports] == ["PROVISIONING", "RUNNING"]
    assert reports[-1]["validation_passed"] is True
    assert reports[-1]["endpoint"].startswith("10.")
    assert reports[-1]["details"]["module"] == "openstack-dev-vm-small"
    assert reports[-1]["details"]["network_exposure"] == "PRIVATE_ONLY"
    assert reports[-1]["details"]["floating_ip"] is False


def test_mock_destroy_reports_termination() -> None:
    reports: list[dict] = []
    Executor(Settings(runner_mode="mock", mock_delay_seconds=0)).run(
        job(operation="DESTROY"), reports.append
    )
    assert [item["status"] for item in reports] == ["TERMINATING", "TERMINATED"]


def test_mock_runner_supports_all_openstack_compute_skus() -> None:
    for module in MODULE_PRODUCTS:
        reports: list[dict] = []
        Executor(Settings(runner_mode="mock", mock_delay_seconds=0)).run(
            job(module=module), reports.append
        )
        assert [item["status"] for item in reports] == ["PROVISIONING", "RUNNING"]
        assert reports[-1]["endpoint"].startswith(("10.", "https://10."))
        assert reports[-1]["validation_passed"] is True


def test_mock_k3s_reports_validated_bootstrap_without_exposing_credentials() -> None:
    reports: list[dict] = []
    Executor(Settings(runner_mode="mock", mock_delay_seconds=0)).run(
        job(module="openstack-dev-k3s-small"), reports.append
    )
    assert reports[-1]["details"]["bootstrap_status"] == "READY"
    assert reports[-1]["endpoint"].startswith("https://10.")
    assert "token" not in str(reports[-1]).lower()
    assert "kubeconfig" not in str(reports[-1]).lower()


def test_runner_rejects_arbitrary_module() -> None:
    reports: list[dict] = []
    Executor(Settings(runner_mode="mock", mock_delay_seconds=0)).run(
        job(module="../../malicious"), reports.append
    )
    assert [item["status"] for item in reports] == ["PROVISION_FAILED"]
    assert reports[0]["failure_code"] == "POLICY_DENIED"


def test_terraform_mode_is_fail_closed_without_runtime_authorization() -> None:
    reports: list[dict] = []
    Executor(Settings(runner_mode="terraform", deployment_authorized=False)).run(
        job(), reports.append
    )
    assert [item["status"] for item in reports] == ["PROVISION_FAILED"]
    assert reports[0]["failure_code"] == "POLICY_DENIED"
    assert "explicit runtime authorization" in reports[0]["error"]


def test_real_k3s_apply_requires_separate_configuration_authorization() -> None:
    reports: list[dict] = []
    Executor(Settings(runner_mode="terraform", deployment_authorized=True)).run(
        job(module="openstack-dev-k3s-small"), reports.append
    )
    assert [item["status"] for item in reports] == ["PROVISION_FAILED"]
    assert reports[0]["failure_code"] == "BOOTSTRAP_VALIDATION_REQUIRED"
    assert "separate runtime authorization" in reports[0]["error"]


def test_approved_module_digest_matches_repository_content() -> None:
    root = Path(__file__).resolve().parents[2]
    assert set(ALLOWED_MODULES) == set(MODULE_PRODUCTS)
    for module, (_, digest) in MODULE_PRODUCTS.items():
        assert module_content_digest(root / "terraform/modules" / module) == digest


def _real_k3s_settings(tmp_path: Path) -> Settings:
    root = Path(__file__).resolve().parents[2]
    clouds = tmp_path / "clouds.yaml"
    private_key = tmp_path / "runner-key"
    known_hosts = tmp_path / "known_hosts"
    binary = tmp_path / "k3s"
    images = tmp_path / "k3s-airgap-images-amd64.tar.zst"
    terraform_binary = tmp_path / "terraform"
    provider_mirror = tmp_path / "provider-mirror"
    provider_package = provider_mirror / "terraform-provider-openstack_v3.4.0"
    clouds.write_text("clouds: {}", encoding="utf-8")
    private_key.write_text("external-test-key-path", encoding="utf-8")
    known_hosts.write_text("10.250.2.20 ssh-ed25519 test-key", encoding="utf-8")
    binary.write_bytes(b"pinned-k3s-binary")
    images.write_bytes(b"pinned-k3s-airgap-images")
    terraform_binary.write_bytes(b"pinned-terraform-cli")
    provider_mirror.mkdir()
    provider_package.write_bytes(b"pinned-openstack-provider")
    return Settings(
        runner_mode="terraform",
        terraform_bin=str(terraform_binary),
        terraform_binary_sha256=hashlib.sha256(terraform_binary.read_bytes()).hexdigest(),
        terraform_supply_chain_lock=str(root / "terraform/supply-chain-lock.json"),
        terraform_catalog=str(root / "terraform/catalog.json"),
        terraform_provider_mirror_root=str(provider_mirror),
        openstack_provider_package=str(provider_package),
        openstack_provider_package_sha256=hashlib.sha256(provider_package.read_bytes()).hexdigest(),
        deployment_authorized=True,
        k3s_configuration_authorized=True,
        module_root=str(root / "terraform/modules"),
        work_root=str(tmp_path / "work"),
        state_root=str(tmp_path / "state"),
        clouds_config_file=str(clouds),
        cloud_name="approved-cloud",
        target_region="RegionOne",
        network_id="network-1",
        security_group_ids=("sg-1",),
        approved_k3s_image_name="approved-base-image",
        keypair_name="approved-keypair",
        flavor_medium="approved-medium",
        ansible_root=str(root / "ansible"),
        ansible_remote_user="automation-user",
        ansible_private_key_file=str(private_key),
        ansible_known_hosts_file=str(known_hosts),
        k3s_binary_path=str(binary),
        k3s_binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),
        k3s_airgap_images_path=str(images),
        k3s_airgap_images_sha256=hashlib.sha256(images.read_bytes()).hexdigest(),
    )


def _terraform_output() -> str:
    values = {
        "primary_resource_id": "instance-1",
        "endpoint": "https://10.250.2.20:6443",
        "display_name": "test / OpenStack k3s PaaS Small",
        "floating_ip": False,
        "network_exposure": "PRIVATE_ONLY",
        "bootstrap_status": "CONFIGURATION_REQUIRED",
        "monitoring_status": "NOT_ONBOARDED",
    }
    return json.dumps({key: {"value": value} for key, value in values.items()})


def _terraform_state(item: dict) -> str:
    return json.dumps(
        {
            "values": {
                "root_module": {
                    "resources": [
                        {
                            "type": "openstack_compute_instance_v2",
                            "values": {
                                "power_state": "active",
                                "image_name": "approved-base-image",
                                "flavor_name": "approved-medium",
                                "key_pair": "approved-keypair",
                                "metadata": item["input_values"]["required_tags"],
                            },
                        },
                        {
                            "type": "openstack_networking_port_v2",
                            "values": {
                                "network_id": "network-1",
                                "port_security_enabled": True,
                                "security_group_ids": ["sg-1"],
                            },
                        },
                    ]
                }
            }
        }
    )


def _terraform_plan(operation: str = "APPLY") -> str:
    action = "create" if operation == "APPLY" else "delete"
    return json.dumps(
        {
            "resource_changes": [
                {
                    "type": resource_type,
                    "provider_name": "registry.terraform.io/terraform-provider-openstack/openstack",
                    "change": {"actions": [action]},
                }
                for resource_type in (
                    "openstack_networking_port_v2",
                    "openstack_compute_instance_v2",
                )
            ]
        }
    )


def test_approved_k3s_runs_terraform_then_ansible(monkeypatch, tmp_path: Path) -> None:
    item = job(module="openstack-dev-k3s-small")
    commands: list[list[str]] = []

    def fake_command(command, cwd, environment, *, failure_code):
        commands.append(command)
        if command[0] == "ansible-playbook":
            return "PLAY RECAP approved-k3s-target ok=20 changed=8 failed=0"
        if command[1:] == ["version", "-json"]:
            return json.dumps({"terraform_version": "1.9.8"})
        if "output" in command:
            return _terraform_output()
        if "show" in command and "tfplan" in command:
            return _terraform_plan("DESTROY" if "-destroy" in " ".join(" ".join(item) for item in commands) else "APPLY")
        if "show" in command:
            return _terraform_state(item)
        return ""

    monkeypatch.setattr(Executor, "_command", staticmethod(fake_command))
    reports: list[dict] = []
    Executor(_real_k3s_settings(tmp_path)).run(item, reports.append)
    assert [value["status"] for value in reports] == ["PROVISIONING", "RUNNING"]
    assert reports[-1]["details"]["bootstrap_status"] == "READY"
    assert reports[-1]["outputs"]["configuration_provisioner"] == "ANSIBLE"
    apply_index = next(index for index, value in enumerate(commands) if "apply" in value)
    ansible_index = next(
        index for index, value in enumerate(commands) if value[0] == "ansible-playbook"
    )
    assert apply_index < ansible_index
    assert not any("-destroy" in value for value in commands)
    assert reports[-1]["outputs"]["supply_chain_attestation"]["decision"] == "PASSED"


def test_ansible_failure_triggers_automatic_terraform_destroy(
    monkeypatch, tmp_path: Path
) -> None:
    item = job(module="openstack-dev-k3s-small")
    commands: list[list[str]] = []

    def fake_command(command, cwd, environment, *, failure_code):
        commands.append(command)
        if command[0] == "ansible-playbook":
            raise TerraformExecutionError("bounded configuration failure", failure_code)
        if command[1:] == ["version", "-json"]:
            return json.dumps({"terraform_version": "1.9.8"})
        if "output" in command:
            return _terraform_output()
        if "show" in command and "tfplan" in command:
            operation = "DESTROY" if any("-destroy" in value for value in commands) else "APPLY"
            return _terraform_plan(operation)
        if "show" in command:
            return _terraform_state(item)
        return ""

    monkeypatch.setattr(Executor, "_command", staticmethod(fake_command))
    reports: list[dict] = []
    Executor(_real_k3s_settings(tmp_path)).run(item, reports.append)
    assert [value["status"] for value in reports] == ["PROVISIONING", "PROVISION_FAILED"]
    assert reports[-1]["failure_code"] == "CONFIGURATION_FAILED"
    ansible_index = next(
        index for index, value in enumerate(commands) if value[0] == "ansible-playbook"
    )
    destroy_index = next(index for index, value in enumerate(commands) if "-destroy" in value)
    assert ansible_index < destroy_index
