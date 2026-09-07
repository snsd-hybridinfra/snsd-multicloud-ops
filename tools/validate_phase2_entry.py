#!/usr/bin/env python3
"""Validate bounded Phase 2 entry and the ZT-VIS-002 partial runtime package."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_zero_trust import validate_schema_instance  # noqa: E402

PACKAGE = Path("docs/zero-trust/packages/zt-vis-002-package.yaml")
PACKAGE_SCHEMA = Path("schemas/zt-vis-002-package.schema.json")
PREFLIGHT = Path("docs/zero-trust/phase-2-entry-preflight.yaml")
PREFLIGHT_SCHEMA = Path("schemas/phase-2-entry-preflight.schema.json")
DEPLOYMENT_CONTRACT = Path("docs/zero-trust/phase-2-visibility-deployment-contract.yaml")
DEPLOYMENT_CONTRACT_SCHEMA = Path("schemas/phase-2-visibility-deployment-contract.schema.json")
READINESS_CONTRACT = Path("docs/zero-trust/phase-2-visibility-readiness-contract.yaml")
READINESS_CONTRACT_SCHEMA = Path("schemas/phase-2-visibility-readiness-contract.schema.json")
P1_DECISION = Path("docs/zero-trust/recovery/P1-ACC-001/acceptance-decision-with-gaps.yaml")
P1_EXCEPTION = Path("docs/zero-trust/exceptions/p1-rv-freshness-001.yaml")
FLOW = Path("docs/zero-trust/package-flow.yaml")
ROADMAP = Path("docs/zero-trust/final-roadmap.yaml")
EXECUTION = Path("docs/zero-trust/final-execution-plan.yaml")
DEPENDENCY = Path("docs/zero-trust/target-architecture/implementation-dependency-map.yaml")
PORTAL_CATALOG = Path("applications/internal-iaas-portal/terraform/catalog.json")
PORTAL_PROFILE = Path("applications/internal-iaas-portal/zero-trust-protection-profile.yaml")
GRAFANA_CONTRACT = Path("applications/internal-iaas-portal/docs/interface-contracts/grafana-dashboard.md")
REQUIRED_PATHS = (
    PACKAGE, PACKAGE_SCHEMA, PREFLIGHT, PREFLIGHT_SCHEMA, DEPLOYMENT_CONTRACT,
    DEPLOYMENT_CONTRACT_SCHEMA, READINESS_CONTRACT, READINESS_CONTRACT_SCHEMA,
    P1_DECISION, P1_EXCEPTION,
    FLOW, ROADMAP, EXECUTION, DEPENDENCY, PORTAL_CATALOG, PORTAL_PROFILE,
    GRAFANA_CONTRACT,
)


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    missing = [str(path) for path in REQUIRED_PATHS if not (root / path).is_file()]
    if missing:
        return [f"required Phase 2 authority is missing: {path}" for path in missing]

    try:
        package = load(root / PACKAGE)
        package_schema = load(root / PACKAGE_SCHEMA)
        preflight = load(root / PREFLIGHT)
        preflight_schema = load(root / PREFLIGHT_SCHEMA)
        deployment_contract = load(root / DEPLOYMENT_CONTRACT)
        deployment_contract_schema = load(root / DEPLOYMENT_CONTRACT_SCHEMA)
        readiness_contract = load(root / READINESS_CONTRACT)
        readiness_contract_schema = load(root / READINESS_CONTRACT_SCHEMA)
        decision = load(root / P1_DECISION)
        exception = load(root / P1_EXCEPTION)
        flow = load(root / FLOW)
        roadmap = load(root / ROADMAP)
        execution = load(root / EXECUTION)
        dependency = load(root / DEPENDENCY)
        portal_catalog = load(root / PORTAL_CATALOG)
        portal_profile = load(root / PORTAL_PROFILE)
        grafana_contract = (root / GRAFANA_CONTRACT).read_text(encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)]

    errors.extend(f"package schema: {item}" for item in validate_schema_instance(package, package_schema))
    errors.extend(f"preflight schema: {item}" for item in validate_schema_instance(preflight, preflight_schema))
    errors.extend(
        f"deployment contract schema: {item}"
        for item in validate_schema_instance(deployment_contract, deployment_contract_schema)
    )
    errors.extend(
        f"readiness contract schema: {item}"
        for item in validate_schema_instance(readiness_contract, readiness_contract_schema)
    )

    phase1 = flow.get("phase_1_acceptance", {})
    if (
        decision.get("decision") != "ACCEPTED_WITH_GAPS"
        or exception.get("exception_id") != "P1-RV-FRESHNESS-001"
        or exception.get("status") != "ACCEPTED_TEMPORARY"
        or phase1.get("completion_status") != "COMPLETED_WITH_GAPS"
        or phase1.get("accepted_exception") != "P1-RV-FRESHNESS-001"
        or phase1.get("deferred_final_risk") != "STALE_RV_EVIDENCE"
    ):
        errors.append("Phase 2 entry must retain the accepted-with-gaps Phase 1 boundary and deferred RV freshness risk")
    phase2_entry = decision.get("phase_2_entry", {})
    if phase2_entry.get("live_mutation_authorized") is not False or phase2_entry.get("live_validator_authorized") is not False:
        errors.append("Phase 2 entry decision must not authorize live mutation or live validation")

    phase2 = next((item for item in roadmap.get("phases", []) if item.get("id") == "PHASE_2"), {})
    if phase2.get("current_status") != "IN_PROGRESS":
        errors.append("Phase 2 roadmap state must be IN_PROGRESS")
    in_progress = [item.get("action_id") for item in execution.get("actions", []) if item.get("current_status") == "IN_PROGRESS"]
    if in_progress != ["P2-VIS-001"]:
        errors.append(f"P2-VIS-001 must be the only in-progress action, got {in_progress}")

    expected_dependency = {
        "package_state": "PRESENT",
        "phase": "PHASE_2_CURRENT",
        "implementation_status": "PARTIALLY_IMPLEMENTED",
        "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
        "runtime_validation_status": "PARTIALLY_VALIDATED",
        "runtime_acceptance_status": "PARTIALLY_ACCEPTED",
        "evidence_status": "PARTIAL_RUNTIME_RECORDED",
        "maturity_status": "UNASSESSED",
        "roadmap_status": "IN_PROGRESS_PARTIAL_RUNTIME",
        "protected": True,
    }
    if dependency.get("package_status", {}).get("ZT-VIS-002") != expected_dependency:
        errors.append("dependency map must preserve the bounded ZT-VIS-002 partial-runtime state")

    if portal_catalog.get("provider") != "openstack" or portal_catalog.get("authority_state") != "LOCAL_CANDIDATE" or portal_catalog.get("deployment_authorized") is not False:
        errors.append("portal catalog must remain an undeployed OpenStack local candidate")
    for product_id, product in portal_catalog.get("products", {}).items():
        resources = set(product.get("allowed_resource_types", []))
        if resources != {"openstack_networking_port_v2", "openstack_compute_instance_v2"}:
            errors.append(f"{product_id} exceeds the fixed private OpenStack port/instance resource boundary")
    denied = set(portal_catalog.get("denied_capabilities", []))
    if not {"floating_ip", "create_network", "create_identity", "arbitrary_hcl"}.issubset(denied):
        errors.append("portal catalog must deny public networking, identity creation, and arbitrary infrastructure")
    if portal_profile.get("provider") != "OPENSTACK" or portal_profile.get("deployment_status") != "NOT_AUTHORIZED" or portal_profile.get("runtime_validation_status") != "NOT_VALIDATED":
        errors.append("portal protection profile must remain OpenStack, deployment-not-authorized, and runtime-not-validated")
    for phrase in ("Grafana 익명 접근을 활성화하지 않는다", "API key", "마스킹된 라벨"):
        if phrase not in grafana_contract:
            errors.append(f"Grafana integration contract is missing boundary: {phrase}")

    source_authorities = package.get("source_authorities", [])
    for reference in source_authorities:
        if reference.startswith((".runtime/", "platform/")):
            errors.append(f"protected local state cannot be a package source authority: {reference}")
        elif not (root / reference).is_file():
            errors.append(f"package source authority is missing: {reference}")
    if set(package.get("protected_non_authorities", [])) != {".runtime/zero-trust/zt-vis-002", "platform"}:
        errors.append("protected runtime and user-owned platform trees must remain explicit non-authorities")
    expected_live_gates = {
        "OpenStack quota and monitoring VM sizing": "BOUNDED_DEPLOYMENT_EXECUTED",
        "Private network, security groups, image and flavor inputs": "BOUNDED_DEPLOYMENT_EXECUTED",
        "Digest-pinned component artifacts": "RUNTIME_ARTIFACT_LOAD_VERIFIED",
        "Persistent storage, retention and restore design": "RUNTIME_RESTART_PERSISTENCE_AND_STACK_RECOVERY_VALIDATED_SNAPSHOT_RESTORE_PENDING",
        "Authenticated proxy and administrator role design": "RUNTIME_MTLS_AND_AUTHENTICATION_VALIDATED",
        "Separate live deployment and validator authorization": "LIVE_VALIDATOR_PARTIAL_STATUS_PROMOTED",
    }
    actual_live_gates = {item.get("gate"): item.get("status") for item in package.get("live_gates", [])}
    if actual_live_gates != expected_live_gates:
        errors.append("ZT-VIS-002 live gates must record the accepted validator while preserving the package-promotion boundary")
    if len(preflight.get("live_deployment_blockers", [])) < 6:
        errors.append("live deployment must remain NO-GO until all prerequisite classes are recorded")
    if any(preflight.get(field) is not False for field in ("runtime_executed", "live_target_changed", "package_runtime_promoted", "maturity_assessed", "compliance_assessed")):
        errors.append("Phase 2 preflight must not claim runtime, mutation, promotion, maturity, or compliance")

    if (
        deployment_contract.get("contract_status") != "BOUNDED_DEPLOYMENT_AND_LIVE_VALIDATOR_PARTIALLY_ACCEPTED"
        or deployment_contract.get("provider") != "OPENSTACK"
        or deployment_contract.get("deployment_authorized") is not True
        or deployment_contract.get("runtime_validation_status") != "PARTIALLY_VALIDATED"
    ):
        errors.append("P2-VIS deployment contract must record the conservative partial runtime promotion without claiming completion")
    topology = deployment_contract.get("topology", {})
    if (
        topology.get("public_endpoint_allowed") is not False
        or topology.get("floating_ip_allowed") is not False
        or topology.get("existing_network_resources_only") is not True
    ):
        errors.append("P2-VIS topology must remain private, without floating IP, on approved existing network resources")
    if set(deployment_contract.get("components", [])) != {"Grafana", "Loki", "Alloy", "Prometheus", "Blackbox Exporter"}:
        errors.append("P2-VIS component contract must retain the fixed five-component visibility stack")
    secrets = deployment_contract.get("secret_contract", {})
    if (
        secrets.get("openstack_configuration") != "EXTERNAL_CLOUDS_YAML"
        or secrets.get("repository_credentials_allowed") is not False
        or secrets.get("terraform_state_tracked") is not False
        or secrets.get("kubeconfig_tracked") is not False
    ):
        errors.append("P2-VIS secret and state contract must keep credentials and runtime state outside Git")
    expected_cases = {"POSITIVE", "NEGATIVE", "BYPASS", "PERSISTENCE", "ROLLBACK", "EVIDENCE_INTEGRITY"}
    actual_cases = {item.get("case_type") for item in deployment_contract.get("acceptance_cases", [])}
    if actual_cases != expected_cases or len(deployment_contract.get("acceptance_cases", [])) != len(expected_cases):
        errors.append("P2-VIS deployment contract must define exactly the six required acceptance case classes")
    if deployment_contract.get("live_gates") != package.get("live_gates"):
        errors.append("P2-VIS deployment contract and package live gates must remain synchronized")
    if set(deployment_contract.get("protected_non_authorities", [])) != set(package.get("protected_non_authorities", [])):
        errors.append("P2-VIS deployment contract must preserve the package non-authority boundary")
    prerequisite = deployment_contract.get("infrastructure_prerequisite", {})
    if (
        deployment_contract.get("prerequisite_runtime_executed") is not True
        or deployment_contract.get("live_target_changed") is not True
        or prerequisite.get("cinder_lvm_status") != "RUNTIME_VALIDATED"
        or prerequisite.get("full_infrastructure_rollback_executed") is not False
    ):
        errors.append("P2-VIS contract must preserve the validated Cinder prerequisite and unexecuted full rollback boundary")
    false_claims = ("central_monitoring_completed", "maturity_assessed", "compliance_assessed")
    if (
        deployment_contract.get("runtime_executed") is not True
        or deployment_contract.get("package_runtime_promoted") is not True
        or any(deployment_contract.get(field) is not False for field in false_claims)
    ):
        errors.append("P2-VIS deployment contract must record partial runtime promotion without claiming completion, maturity, or compliance")
    access = deployment_contract.get("access_contract", {})
    data = deployment_contract.get("data_contract", {})
    if (
        access.get("authentication_method") != "MUTUAL_TLS_AT_PROXY_PLUS_GRAFANA_LOGIN"
        or set(access.get("role_separation", [])) != {"VISIBILITY_VIEWER", "VISIBILITY_ADMINISTRATOR", "RECOVERY_OPERATOR"}
        or access.get("oidc_status") != "DEFERRED_TO_P2_OIDC_001"
        or access.get("design_status") != "RUNTIME_MTLS_AND_AUTHENTICATION_VALIDATOR_PASSED"
    ):
        errors.append("P2-VIS access design must preserve private mTLS, Grafana login, role separation, and deferred OIDC")
    if (
        data.get("retention_design_selected") is not True
        or data.get("retention_approved") is not False
        or data.get("primary_storage") != "DEDICATED_CINDER_VOLUME"
        or data.get("restore_method") != "REATTACH_PRESERVED_VOLUME_TO_REBUILT_MONITORING_VM"
        or data.get("rollback_checkpoint") != "CINDER_SNAPSHOT_BEFORE_BOUNDED_DEPLOYMENT_TEST"
        or data.get("backup_restore_approved") is not False
        or data.get("design_status") != "RUNTIME_RESTART_PERSISTENCE_AND_STACK_RECOVERY_VALIDATED_SNAPSHOT_RESTORE_PENDING"
    ):
        errors.append("P2-VIS data design must select 14-day Cinder retention while keeping runtime retention and restore acceptance open")
    if (
        readiness_contract.get("status") != "NO_APPLY_PLAN_VALIDATED_LIVE_DEPLOYMENT_PENDING"
        or readiness_contract.get("external_input_contract", {}).get("review_status") != "AUTHENTICATED_NO_APPLY_PLAN_POLICY_VALIDATED"
        or set(readiness_contract.get("remaining_gates", [])) != {
            "VERIFY_PROXY_TRUST_MATERIAL_ON_DEPLOYED_TARGET",
            "AUTHORIZE_LIVE_DEPLOYMENT",
            "AUTHORIZE_LIVE_VALIDATOR",
        }
        or readiness_contract.get("package_runtime_promoted") is not False
        or any(readiness_contract.get(field) is not False for field in false_claims)
    ):
        errors.append("P2-VIS readiness must record only the no-apply preflight while retaining proxy-runtime, deployment, and validator gates")

    if (root / ".git").exists():
        tracked = subprocess.run(
            ["git", "ls-files", ".runtime"], cwd=root, capture_output=True,
            text=True, encoding="utf-8", errors="replace",
        )
        if tracked.returncode != 0:
            errors.append("git ls-files .runtime failed")
        elif tracked.stdout.strip():
            errors.append("tracked .runtime content cannot support Phase 2 entry")
    return errors


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"[FAIL] {error}")
    if errors:
        print(f"Phase 2 entry summary: passed=0, failed={len(errors)}")
        return 1
    print("[PASS] Phase 2 records ZT-VIS-002 as partially implemented, validated, and accepted while P2-VIS-001 completion remains open.")
    print("Phase 2 entry summary: passed=1, failed=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
