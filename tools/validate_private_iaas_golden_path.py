#!/usr/bin/env python3
"""Read-only Stage B validation for the private OpenStack IaaS golden path."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = Path("docs/platform/private-iaas-golden-path.yaml")
REQUEST_CODE = Path("applications/internal-iaas-portal/services/request-api/request_api/main.py")
PRODUCT_DOC = Path("applications/internal-iaas-portal/docs/interface-contracts/product-provisioning.md")
REQUIRED_FILES = (
    CONTRACT,
    Path("applications/internal-iaas-portal/terraform/catalog.json"),
    Path("applications/internal-iaas-portal/zero-trust-protection-profile.yaml"),
    REQUEST_CODE,
    Path("applications/internal-iaas-portal/services/approval-api/approval_api/main.py"),
    Path("applications/internal-iaas-portal/services/terraform-runner/terraform_runner/executor.py"),
    PRODUCT_DOC,
)
EXPECTED_PRODUCTS = {
    "DEV-OS-VM-S",
    "DEV-OS-VM-M",
    "DEV-OS-VM-L",
    "DEV-OS-K3S-S",
    "DEV-OS-K3S-M",
}
EXPECTED_REQUEST = {
    "PENDING": {"APPROVED", "CANCELLED", "REJECTED"},
    "APPROVED": {"GRANTED"},
    "GRANTED": {"EXPIRED", "REVOKED"},
}
EXPECTED_RESOURCE = {
    "PROVISIONING": {"PROVISION_FAILED", "RUNNING", "TERMINATING"},
    "RUNNING": {"TERMINATING"},
    "PROVISION_FAILED": {"PROVISIONING", "TERMINATING"},
    "TERMINATING": {"TERMINATED", "TERMINATION_FAILED"},
    "TERMINATION_FAILED": {"TERMINATING"},
}
EXPECTED_LOCAL_SCOPE = {
    "positive",
    "negative",
    "bypass",
    "persistence",
    "post_apply_policy_failure",
    "verified_rollback",
    "rollback_failure",
    "operator_retry",
    "recovery_audit",
}
EXPECTED_FAILURE_RECOVERY = {
    "post_apply_failure_action": "AUTOMATIC_DESTROY",
    "success_claim_requires": "TERRAFORM_STATE_EMPTY",
    "rollback_failure_status": "ROLLBACK_FAILED",
    "retry_requires_operator_action": True,
    "grant_allowed_after_failure": False,
    "audit_stream": "provisioning-job",
    "runtime_validation_status": "NOT_VALIDATED",
}


@dataclass
class Result:
    passes: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    def require(self, condition: bool, message: str) -> None:
        (self.passes if condition else self.failures).append(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def code_mapping(path: Path, name: str) -> dict[str, set[str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        target = node.target if isinstance(node, ast.AnnAssign) else None
        if isinstance(target, ast.Name) and target.id == name and node.value is not None:
            value = ast.literal_eval(node.value)
            return {str(key): {str(item) for item in items} for key, items in value.items()}
    raise ValueError(f"{name} is missing from {path}")


def normalized_machine(value: Any) -> dict[str, set[str]]:
    if not isinstance(value, dict):
        return {}
    return {
        str(key): {str(item) for item in items}
        for key, items in value.items()
        if isinstance(items, list)
    }


def validate(root: Path) -> Result:
    result = Result()
    for relative in REQUIRED_FILES:
        result.require((root / relative).is_file(), f"required Stage B file exists: {relative.as_posix()}")
    if result.failures:
        return result

    try:
        contract = load_json(root / CONTRACT)
        catalog = load_json(root / Path(contract["sources"]["catalog"]["path"]))
        profile = load_json(root / Path(contract["sources"]["protection_profile"]["path"]))
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        result.failures.append(f"Stage B authority cannot be loaded: {exc}")
        return result

    result.require(contract.get("schema_version") == "1.0.0", "Stage B contract schema is pinned")
    result.require(contract.get("status") == "LOCAL_INTEGRATION_CONTRACT_VALIDATED", "Stage B status remains local-contract only")
    result.require(contract.get("selected_blueprint") == "VM_APPLICATION_STACK", "initial golden path selects the approved VM application blueprint")
    result.require(contract.get("selected_execution_profile") == "DEV-OS-VM-S", "initial golden path pins the smallest private VM execution profile")
    result.require(
        contract.get("blueprint_resolution_status")
        == "VM_APPLICATION_REQUEST_PATH_LOCAL_IMPLEMENTED",
        "one blueprint request path is locally implemented without runtime overclaim",
    )
    result.require(contract.get("deployment_authorized") is False, "architecture contract does not authorize live deployment")
    result.require(contract.get("runtime_validation_status") == "NOT_VALIDATED", "OpenStack runtime is not overclaimed")

    for source_name in ("catalog", "protection_profile"):
        source = contract["sources"][source_name]
        result.require(sha256(root / Path(source["path"])) == source.get("sha256"), f"{source_name} source digest matches")

    result.require(catalog.get("provider") == "openstack", "catalog provider is OpenStack")
    result.require(catalog.get("deployment_authorized") is False, "catalog defaults live deployment to denied")
    result.require(set(catalog.get("products", {})) == EXPECTED_PRODUCTS, "catalog contains exactly the five approved internal execution profiles")
    result.require(profile.get("deployment_status") == "NOT_AUTHORIZED", "protection profile keeps deployment unauthorized")
    result.require(profile.get("runtime_validation_status") == "NOT_VALIDATED", "protection profile keeps runtime unvalidated")

    machines = contract.get("state_machines", {})
    contract_request = normalized_machine(machines.get("request"))
    contract_resource = normalized_machine(machines.get("resource"))
    result.require(contract_request == EXPECTED_REQUEST, "contract request and Grant state machine is exact")
    result.require(contract_resource == EXPECTED_RESOURCE, "contract resource state machine is exact")
    try:
        code_request = code_mapping(root / REQUEST_CODE, "BASE_TRANSITIONS")
        code_resource = code_mapping(root / REQUEST_CODE, "RESOURCE_TRANSITIONS")
    except (OSError, SyntaxError, ValueError) as exc:
        result.failures.append(f"state machine code cannot be inspected: {exc}")
    else:
        result.require(code_request == EXPECTED_REQUEST, "request code matches the Stage B contract")
        result.require(code_resource == EXPECTED_RESOURCE, "resource code matches the Stage B contract")

    result.require(machines.get("job_success_path") == ["QUEUED", "PLANNING", "APPLYING", "SUCCEEDED"], "apply job success path is fixed")
    result.require(machines.get("destroy_success_path") == ["QUEUED", "PLANNING", "DESTROYING", "TERMINATED"], "destroy job success path is fixed")

    local = contract.get("local_acceptance", {})
    result.require(local.get("portal_validator") == "22_PASS_0_FAIL", "portal static validator result is recorded")
    result.require(local.get("portal_test_suite") == "183_PASS_9_DEPENDENCY_DEPRECATION_WARNINGS", "portal full local test result is recorded")
    result.require(local.get("recovery_focused_suite") == "68_PASS_2_DEPENDENCY_DEPRECATION_WARNINGS", "focused recovery test result is recorded")
    result.require(set(local.get("test_scope", [])) == EXPECTED_LOCAL_SCOPE, "local acceptance covers the required recovery behavior classes")
    result.require(local.get("runtime_credit") == "NONE", "local tests receive no runtime credit")
    result.require(
        contract.get("failure_recovery") == EXPECTED_FAILURE_RECOVERY,
        "post-apply recovery remains fail-closed and non-runtime-validated",
    )
    result.require(len(contract.get("live_gates", [])) >= 7, "live execution has explicit gates")
    result.require(len(contract.get("stop_conditions", [])) >= 7, "live execution has explicit stop conditions")

    documentation = (root / PRODUCT_DOC).read_text(encoding="utf-8")
    for token in ("Request/Grant", "Resource:", "Runner job:", "resource_status", "GRANTED"):
        result.require(token in documentation, f"product contract documents separated lifecycle: {token}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = validate(args.root.resolve())
    for message in result.passes:
        print(f"[PASS] {message}")
    for message in result.failures:
        print(f"[FAIL] {message}")
    print(f"Private IaaS golden-path summary: passed={len(result.passes)} failed={len(result.failures)}")
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
