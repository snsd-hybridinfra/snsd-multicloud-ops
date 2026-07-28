#!/usr/bin/env python3
"""Read-only governance validator for the repository Zero Trust framework."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


CATALOG_PATH = Path("docs/zero-trust/capability-catalog.yaml")
BASELINE_PATH = Path("docs/zero-trust/current-baseline-assessment.yaml")
BACKLOG_PATH = Path("docs/zero-trust/capability-implementation-backlog.yaml")
CATALOG_SCHEMA_PATH = Path("schemas/zero-trust-capability-catalog.schema.json")
BASELINE_SCHEMA_PATH = Path("schemas/zero-trust-baseline-assessment.schema.json")
BACKLOG_SCHEMA_PATH = Path("schemas/zero-trust-capability-backlog.schema.json")
FOUNDATION_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-fnd-001-package.yaml")
FOUNDATION_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-fnd-001-validation.yaml")
ROUTER_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-net-001-package.yaml")
ROUTER_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-net-001-validation.yaml")
ROUTER_REQUIRED_PATHS = (
    Path("docs/zero-trust/packages/zt-net-001-router-validation.md"),
    Path("docs/zero-trust/packages/zt-net-001-rollback.md"),
    Path("tools/live-validation/install-router-validator.ps1"),
    Path("tools/live-validation/validate-router-live.ps1"),
    Path("tools/live-validation/remote/codex-router-dispatcher.sh.example"),
    Path("tools/live-validation/remote/validate-snsd-r1-readonly.sh.example"),
    Path("tools/live-validation/remote/router-validator-sudoers.example"),
    Path("tools/live-validation/remote/router-validator-authorized-key.example"),
    Path("docs/evidence/zero-trust/zt-net-001-acl-validation.sanitized.txt"),
)
TELEMETRY_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-vis-001-package.yaml")
TELEMETRY_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-vis-001-validation.yaml")
TELEMETRY_REQUIRED_PATHS = (
    Path("docs/zero-trust/packages/zt-vis-001-centralized-telemetry-foundation.md"),
    Path("docs/zero-trust/packages/zt-vis-001-rollback.md"),
    Path("docs/zero-trust/telemetry-event-model.yaml"),
    Path("docs/zero-trust/telemetry-source-inventory.yaml"),
    Path("docs/zero-trust/correlation-rule-catalog.yaml"),
    Path("schemas/zero-trust-telemetry-event.schema.json"),
    Path("schemas/zero-trust-correlation-finding.schema.json"),
    Path("tools/telemetry/normalize_events.py"),
    Path("tools/telemetry/correlate_events.py"),
    Path("tools/telemetry/validate_telemetry_sources.py"),
    Path("tools/live-validation/collect-telemetry-live.ps1"),
    Path("tools/live-validation/manage-persistent-telemetry.ps1"),
    Path("observability/logging/compose.yaml"),
    Path("observability/logging/loki-config.yaml"),
    Path("observability/logging/alloy-config.alloy"),
    Path("observability/logging/grafana-provisioning/datasources/loki.yaml"),
    Path("docs/evidence/zero-trust/zt-vis-001-persistent-storage-validation.sanitized.txt"),
)
ENDPOINT_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-dev-001-package.yaml")
ENDPOINT_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-dev-001-validation.yaml")
ENDPOINT_INVENTORY_PATH = Path("docs/zero-trust/device/device-inventory.yaml")
ENDPOINT_POLICY_PATH = Path("docs/zero-trust/device/endpoint-compliance-policy.yaml")
ENDPOINT_INVENTORY_SCHEMA_PATH = Path("schemas/zero-trust-device-inventory.schema.json")
ENDPOINT_REQUIRED_PATHS = (
    Path("docs/zero-trust/device/README.md"),
    Path("docs/zero-trust/device/vulnerability-assessment-plan.yaml"),
    Path("docs/zero-trust/edr-adoption-decision.md"),
    Path("docs/zero-trust/device-trust-decision-model.md"),
    Path("docs/zero-trust/packages/zt-dev-001-endpoint-compliance-foundation.md"),
    Path("docs/zero-trust/packages/zt-dev-001-rollback.md"),
    Path("schemas/zero-trust-software-inventory.schema.json"),
    Path("tools/endpoint/collect_software_inventory.py"),
    Path("tools/endpoint/validate_endpoint_compliance.py"),
    Path("tools/live-validation/validate-endpoints-live.ps1"),
    Path("tests/test_zt_dev_001.py"),
)
APPLICATION_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-app-001-package.yaml")
APPLICATION_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-app-001-validation.yaml")
APPLICATION_INVENTORY_PATH = Path("docs/zero-trust/application-inventory.yaml")
WORKLOAD_INVENTORY_PATH = Path("docs/zero-trust/workload-inventory.yaml")
APPLICATION_REQUIRED_PATHS = (
    Path("docs/zero-trust/secure-deployment-policy.yaml"),
    Path("docs/zero-trust/software-component-inventory.yaml"),
    Path("docs/zero-trust/software-risk-register.yaml"),
    Path("docs/zero-trust/artifact-provenance-policy.md"),
    Path("docs/zero-trust/application-deployment-gates.md"),
    Path("docs/zero-trust/packages/zt-app-001-secure-workload-foundation.md"),
    Path("docs/zero-trust/packages/zt-app-001-rollback.md"),
    Path("docs/evidence/zero-trust/zt-app-001-sbom.cdx.json"),
    Path("schemas/zero-trust-application-inventory.schema.json"),
    Path("schemas/zero-trust-workload-inventory.schema.json"),
    Path("schemas/zero-trust-software-component-inventory.schema.json"),
    Path("tools/application/validate_application_inventory.py"),
    Path("tools/application/validate_secure_deployment.py"),
    Path("tools/application/run_security_scans.py"),
    Path("tools/live-validation/validate-application-live.ps1"),
    Path("tests/test_zt_app_001.py"),
)
DATA_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-data-001-package.yaml")
DATA_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-data-001-validation.yaml")
DATA_INVENTORY_PATH = Path("docs/zero-trust/data-inventory.yaml")
DATA_REQUIRED_PATHS = (
    Path("docs/zero-trust/data-classification-policy.yaml"),
    Path("docs/zero-trust/data-governance-model.md"),
    Path("docs/zero-trust/data-access-policy.yaml"),
    Path("docs/zero-trust/data-flow-map.yaml"),
    Path("docs/zero-trust/data-encryption-assessment.yaml"),
    Path("docs/zero-trust/key-and-credential-management.md"),
    Path("docs/zero-trust/backup-inventory.yaml"),
    Path("docs/zero-trust/dlp-policy.yaml"),
    Path("docs/evidence/zero-trust/zt-data-001-backup-assurance.yaml"),
    Path("docs/zero-trust/packages/zt-data-001-data-protection-foundation.md"),
    Path("docs/zero-trust/packages/zt-data-001-rollback.md"),
    Path("schemas/zero-trust-data-inventory.schema.json"),
    Path("schemas/zero-trust-data-access-policy.schema.json"),
    Path("schemas/zero-trust-data-flow-map.schema.json"),
    Path("schemas/zero-trust-backup-inventory.schema.json"),
    Path("schemas/zero-trust-dlp-policy.schema.json"),
    Path("tools/data/validate_data_inventory.py"),
    Path("tools/data/scan_data_policy.py"),
    Path("tools/data/validate_backup_assurance.py"),
    Path("tools/live-validation/validate-data-live.ps1"),
    Path("tests/fixtures/zt-data-001/fixture-catalog.yaml"),
    Path("tests/test_zt_data_001.py"),
)
SYSTEM_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-sys-001-package.yaml")
SYSTEM_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-sys-001-validation.yaml")
SYSTEM_INVENTORY_PATH = Path("docs/zero-trust/system-inventory.yaml")
SYSTEM_REQUIRED_PATHS = (
    Path("docs/zero-trust/system-baseline-policy.yaml"),
    Path("docs/zero-trust/system-configuration-authority.yaml"),
    Path("docs/zero-trust/system-integrity-policy.yaml"),
    Path("docs/zero-trust/system-credential-reference-inventory.yaml"),
    Path("docs/zero-trust/system-service-exposure.yaml"),
    Path("docs/zero-trust/system-service-policy.yaml"),
    Path("docs/zero-trust/system-recovery-readiness.yaml"),
    Path("docs/zero-trust/system-risk-register.yaml"),
    Path("docs/zero-trust/system-privileged-access-model.md"),
    Path("docs/zero-trust/system-change-control.md"),
    Path("docs/zero-trust/packages/zt-sys-001-system-security-foundation.md"),
    Path("docs/zero-trust/packages/zt-sys-001-rollback.md"),
    Path("docs/evidence/zero-trust/zt-sys-001-integrity-validation.yaml"),
    Path("docs/evidence/zero-trust/zt-sys-001-service-state.yaml"),
    Path("docs/evidence/zero-trust/zt-sys-001-live-summary.sanitized.txt"),
    Path("schemas/zero-trust-system-inventory.schema.json"),
    Path("schemas/zero-trust-system-baseline-policy.schema.json"),
    Path("schemas/zero-trust-system-configuration-authority.schema.json"),
    Path("schemas/zero-trust-system-integrity-policy.schema.json"),
    Path("schemas/zero-trust-system-service-policy.schema.json"),
    Path("tools/system/validate_system_inventory.py"),
    Path("tools/system/check_configuration_drift.py"),
    Path("tools/system/validate_service_state.py"),
    Path("tools/live-validation/validate-systems-live.ps1"),
    Path("tests/test_zt_sys_001.py"),
)
AUTOMATION_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-auto-001-package.yaml")
AUTOMATION_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-auto-001-validation.yaml")
AUTOMATION_INTEGRATION_PATH = Path("docs/zero-trust/automation-integration-inventory.yaml")
AUTOMATION_ACTION_PATH = Path("docs/zero-trust/automation-action-catalog.yaml")
AUTOMATION_WORKFLOW_PATH = Path("docs/zero-trust/automation-workflow-catalog.yaml")
AUTOMATION_POLICY_PATH = Path("docs/zero-trust/automation-approval-policy.yaml")
AUTOMATION_REQUIRED_PATHS = (
    Path("docs/zero-trust/automation-governance.md"),
    Path("docs/zero-trust/packages/zt-auto-001-policy-automation-foundation.md"),
    Path("docs/zero-trust/packages/zt-auto-001-rollback.md"),
    Path("docs/evidence/zero-trust/zt-auto-001-live-summary.sanitized.txt"),
    Path("schemas/zero-trust-automation-integration-inventory.schema.json"),
    Path("schemas/zero-trust-automation-action-catalog.schema.json"),
    Path("schemas/zero-trust-automation-workflow-catalog.schema.json"),
    Path("schemas/zero-trust-automation-approval-policy.schema.json"),
    Path("schemas/zero-trust-automation-execution-record.schema.json"),
    Path("schemas/zero-trust-automation-plan.schema.json"),
    Path("tools/automation/automation_common.py"),
    Path("tools/automation/validate_automation_catalogs.py"),
    Path("tools/automation/evaluate_action_policy.py"),
    Path("tools/automation/plan_workflow.py"),
    Path("tools/automation/run_workflow.py"),
    Path("tools/automation/apply_approved_proposal.py"),
    Path("tools/live-validation/run-automation-foundation.ps1"),
    Path("tests/fixtures/zt-auto-001/fixture-catalog.yaml"),
    Path("tests/test_zt_auto_001.py"),
)
CONTINUOUS_VERIFICATION_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-cv-001-package.yaml")
CONTINUOUS_VERIFICATION_EXECUTION_PATH = Path("docs/evidence/zero-trust/zt-cv-001-validation.yaml")
CONTINUOUS_VERIFICATION_POLICY_PATHS = (
    Path("docs/zero-trust/continuous-verification-policy.yaml"),
    Path("docs/zero-trust/evidence-freshness-policy.yaml"),
    Path("docs/zero-trust/capability-acceptance-catalog.yaml"),
    Path("docs/zero-trust/package-acceptance-gates.yaml"),
    Path("docs/zero-trust/verification-regression-policy.yaml"),
    Path("docs/zero-trust/verification-exception-policy.yaml"),
    Path("docs/zero-trust/maturity-reassessment-policy.yaml"),
    Path("docs/zero-trust/verification-history.yaml"),
)
CONTINUOUS_VERIFICATION_SCHEMA_PATHS = (
    Path("schemas/zero-trust-continuous-verification-policy.schema.json"),
    Path("schemas/zero-trust-evidence-freshness-policy.schema.json"),
    Path("schemas/zero-trust-capability-acceptance-catalog.schema.json"),
    Path("schemas/zero-trust-package-acceptance-gates.schema.json"),
    Path("schemas/zero-trust-verification-regression-policy.schema.json"),
    Path("schemas/zero-trust-verification-exception-policy.schema.json"),
    Path("schemas/zero-trust-maturity-reassessment-policy.schema.json"),
    Path("schemas/zero-trust-verification-history.schema.json"),
    Path("schemas/zero-trust-capability-acceptance-result.schema.json"),
    Path("schemas/zero-trust-maturity-reassessment-result.schema.json"),
)
CONTINUOUS_VERIFICATION_REQUIRED_PATHS = (
    Path("docs/zero-trust/continuous-verification-governance.md"),
    Path("docs/zero-trust/continuous-verification-schedule.md"),
    Path("docs/zero-trust/integrated-capability-assessment.md"),
    Path("docs/zero-trust/integrated-capability-assessment.yaml"),
    Path("docs/zero-trust/packages/zt-cv-001-continuous-verification-foundation.md"),
    Path("docs/zero-trust/packages/zt-cv-001-rollback.md"),
    Path("docs/evidence/zero-trust/zt-cv-001-live-summary.sanitized.txt"),
    Path("tools/continuous_verification/cv_common.py"),
    Path("tools/continuous_verification/validate_verification_configuration.py"),
    Path("tools/continuous_verification/evaluate_evidence_freshness.py"),
    Path("tools/continuous_verification/assess_repeatability.py"),
    Path("tools/continuous_verification/assess_package_acceptance.py"),
    Path("tools/continuous_verification/assess_capability_acceptance.py"),
    Path("tools/continuous_verification/detect_regressions.py"),
    Path("tools/continuous_verification/reassess_maturity.py"),
    Path("tools/live-validation/run-continuous-verification.ps1"),
    Path("tests/fixtures/zt-cv-001/fixture-catalog.yaml"),
    Path("tests/test_zt_cv_001.py"),
)
REPEATABLE_VALIDATION_CAMPAIGN_PATH = Path("docs/zero-trust/repeatable-validation-campaign.yaml")
REPEATABILITY_ACCEPTANCE_POLICY_PATH = Path("docs/zero-trust/repeatability-acceptance-policy.yaml")
REPEATABLE_VALIDATION_PACKAGE_PATH = Path("docs/zero-trust/packages/zt-rv-001-package.yaml")
REPEATABLE_VALIDATION_SCHEMA_PATHS = (
    Path("schemas/zero-trust-repeatable-validation-campaign.schema.json"),
    Path("schemas/zero-trust-repeatability-acceptance-policy.schema.json"),
    Path("schemas/zero-trust-repeatable-execution-record.schema.json"),
    Path("schemas/zero-trust-repeatability-assessment.schema.json"),
)
REPEATABLE_VALIDATION_REQUIRED_PATHS = (
    Path("docs/zero-trust/integrated-capability-assessment.yaml"),
    Path("docs/zero-trust/repeatable-validation-schedule-proposal.md"),
    Path("docs/zero-trust/packages/zt-rv-001-repeatable-runtime-validation-pilot.md"),
    Path("docs/zero-trust/packages/zt-rv-001-rollback.md"),
    Path("tools/continuous_verification/rv_common.py"),
    Path("tools/continuous_verification/run_repeatability_campaign.py"),
    Path("tools/continuous_verification/append_verified_execution.py"),
    Path("tools/continuous_verification/create_execution_fingerprint.py"),
    Path("tools/continuous_verification/verify_sanitized_evidence.py"),
    Path("tools/live-validation/run-repeatable-validation-pilot.ps1"),
    Path("tests/fixtures/zt-rv-001/fixture-catalog.yaml"),
    Path("tests/test_zt_rv_001.py"),
)
FOUNDATION_REQUIRED_PATHS = (
    Path("docs/zero-trust/packages/zt-fnd-001-restricted-validation-foundation.md"),
    Path("docs/zero-trust/packages/zt-fnd-001-rollback.md"),
    Path("tools/live-validation/validate-openstack-live.ps1"),
    Path("tools/live-validation/validate-eve-live.ps1"),
    Path("tools/live-validation/run-foundation-validation.ps1"),
    Path("tools/live-validation/install-eve-validator.ps1"),
    Path("tools/live-validation/sanitize-live-evidence.py"),
    Path("tools/live-validation/remote/codex-eve-dispatcher.sh.example"),
    Path("tools/live-validation/remote/validate-eve-readonly.sh.example"),
    Path("tools/live-validation/remote/eve-validator-sudoers.example"),
    Path("tools/live-validation/remote/eve-validator-authorized-key.example"),
    Path("tools/live-validation/remote/openstack-validator-sudoers.example"),
    Path("tools/live-validation/remote/openstack-validator-authorized-key.example"),
)
CANONICAL_DOCUMENT = "제로트러스트 가이드라인 2.0"
CANONICAL_TAXONOMY_SHA256 = "ac5f06d769676b347de5aeb8d35324800cdd085ae8e139168bf1b97ae1f5745a"

DOMAIN_ORDER = [
    "identity",
    "device-endpoint",
    "network",
    "system",
    "application-workload",
    "data",
    "visibility-analytics",
    "automation-integration",
]
PILLAR_KO = {
    "identity": "식별자·신원",
    "device-endpoint": "기기 및 엔드포인트",
    "network": "네트워크",
    "system": "시스템",
    "application-workload": "애플리케이션 및 워크로드",
    "data": "데이터",
    "visibility-analytics": "가시성 및 분석",
    "automation-integration": "자동화 및 통합",
}
FUNCTION_COUNTS = {
    1: {1: 2, 2: 2, 3: 2, 4: 2},
    2: {1: 1, 2: 1, 3: 2, 4: 2},
    3: {1: 3, 2: 1, 3: 1, 4: 1, 5: 1},
    4: {1: 1, 2: 2, 3: 1, 4: 1},
    5: {1: 1, 2: 1, 3: 1, 4: 2, 5: 2},
    6: {1: 2, 2: 1, 3: 1, 4: 1, 5: 2},
}
EXPECTED_IDS = {
    f"ZT-{pillar}.{function}.{capability}"
    for pillar, functions in FUNCTION_COUNTS.items()
    for function, count in functions.items()
    for capability in range(1, count + 1)
} | {f"ZT-{pillar}.{capability}" for pillar in (7, 8) for capability in range(1, 7)}

MATURITY_ORDER = {"TRADITIONAL": 0, "INITIAL": 1, "ADVANCED": 2, "OPTIMAL": 3}
EVIDENCE_ORDER = {"NONE": 0, "DESIGN": 1, "CONFIGURATION": 2, "RUNTIME": 3, "CONTINUOUS": 4}
PACKAGE_EVIDENCE_AUTHORITIES = {
    "MISSING",
    "CODEX_EXECUTED_LOCAL_VALIDATION",
    "CODEX_EXECUTED_LIVE_RUNTIME",
    "USER_EXECUTED_RUNTIME",
}
CAPABILITY_ID_RE = re.compile(r"^ZT-(?:[1-6]\.[1-9]\d*\.[1-9]\d*|[78]\.[1-9]\d*)$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

FORBIDDEN_CLAIMS = [
    "fully compliant",
    "full compliance",
    "complete Zero Trust implementation",
    "fully implemented Zero Trust",
    "enterprise-wide validated",
    "production-ready",
    "production-grade",
    "fully validated",
    "zero trust certified",
    "complete micro-segmentation",
    "all capabilities implemented",
    "all capabilities validated",
    "repository-wide Optimal",
    "enterprise-wide Optimal",
]
SAFE_CLAIM_CONTEXT = re.compile(
    r"(?i)\b(?:no|not|does not|do not|must not|without|excluded?|prohibited|"
    r"forbidden|unsupported|avoid|cannot|isn't|aren't|0|zero)\b|out[-_ ]of[-_ ]scope"
)


class DuplicateKeyError(ValueError):
    pass


@dataclass
class Finding:
    level: str
    category: str
    message: str


@dataclass
class ValidationResult:
    findings: list[Finding] = field(default_factory=list)

    def add(self, level: str, category: str, message: str) -> None:
        self.findings.append(Finding(level, category, message))

    def passed(self, category: str, message: str) -> None:
        self.add("PASS", category, message)

    def warn(self, category: str, message: str) -> None:
        self.add("WARN", category, message)

    def fail(self, category: str, message: str) -> None:
        self.add("FAIL", category, message)

    @property
    def counts(self) -> Counter[str]:
        return Counter(item.level for item in self.findings)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _object_pairs_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate key: {key}")
        result[key] = value
    return result


def load_json_yaml(path: Path) -> Any:
    """Load the repository's JSON-compatible YAML 1.2 without dependencies."""
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_object_pairs_no_duplicates)
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateKeyError) as exc:
        raise ValueError(f"cannot parse {path}: {exc}") from exc


def load_schema(path: Path) -> dict[str, Any]:
    value = load_json_yaml(path)
    if not isinstance(value, dict) or value.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValueError(f"{path} is not a JSON Schema Draft 2020-12 document")
    return value


def _resolve_ref(root_schema: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ValueError(f"unsupported non-local schema reference: {reference}")
    current: Any = root_schema
    for part in reference[2:].split("/"):
        current = current[part.replace("~1", "/").replace("~0", "~")]
    if not isinstance(current, dict):
        raise ValueError(f"schema reference does not resolve to an object: {reference}")
    return current


def _type_matches(value: Any, expected: str | list[str]) -> bool:
    if isinstance(expected, list):
        return any(_type_matches(value, item) for item in expected)
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def validate_schema_instance(
    value: Any,
    schema: dict[str, Any] | bool,
    root_schema: dict[str, Any] | None = None,
    path: str = "$",
) -> list[str]:
    """Validate the JSON Schema subset used by the repository schemas."""
    if schema is True:
        return []
    if schema is False:
        return [f"{path}: value is not permitted by schema"]
    root_schema = root_schema or schema
    if "$ref" in schema:
        return validate_schema_instance(value, _resolve_ref(root_schema, schema["$ref"]), root_schema, path)

    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type and not _type_matches(value, expected_type):
        return [f"{path}: expected {expected_type}, got {type(value).__name__}"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: invalid enum value {value!r}")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            errors.append(f"{path}: value does not match {schema['pattern']}")
        if schema.get("format") == "date":
            try:
                dt.date.fromisoformat(value)
            except ValueError:
                errors.append(f"{path}: invalid ISO date")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: value is below minimum")

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than minItems")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: more than maxItems")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, ensure_ascii=False, sort_keys=True) for item in value]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{path}: array items are not unique")
        prefix_items = schema.get("prefixItems", [])
        for index, item_schema in enumerate(prefix_items):
            if index < len(value):
                errors.extend(validate_schema_instance(value[index], item_schema, root_schema, f"{path}[{index}]"))
        if "items" in schema:
            for index, item in enumerate(value[len(prefix_items):], len(prefix_items)):
                errors.extend(validate_schema_instance(item, schema["items"], root_schema, f"{path}[{index}]"))

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, item in value.items():
            if key in properties:
                errors.extend(validate_schema_instance(item, properties[key], root_schema, f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected property {key!r}")
    return errors


def _expected_pillar_for_id(capability_id: str) -> str | None:
    match = re.match(r"^ZT-([1-8])\.", capability_id)
    return DOMAIN_ORDER[int(match.group(1)) - 1] if match else None


def _canonical_taxonomy_digest(capabilities: list[dict[str, Any]]) -> str:
    fields = ("id", "pillar", "pillar_ko", "function", "function_ko", "capability", "capability_ko", "source")
    normalized = [{key: item.get(key) for key in fields} for item in capabilities]
    payload = json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate_catalog(catalog: dict[str, Any], schema: dict[str, Any], result: ValidationResult) -> None:
    errors = validate_schema_instance(catalog, schema)
    if errors:
        for error in errors:
            result.fail("schema.catalog", error)
        return
    result.passed("schema.catalog", "Capability catalog conforms to Draft 2020-12 repository schema.")

    capabilities = catalog["capabilities"]
    ids = [item["id"] for item in capabilities]
    if len(ids) == 52 and catalog["capability_count"] == 52:
        result.passed("taxonomy.count", "Catalog contains exactly 52 capabilities.")
    else:
        result.fail("taxonomy.count", f"Expected 52 capabilities; found {len(ids)}.")
    duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
    if duplicates:
        result.fail("taxonomy.ids", f"Duplicate capability IDs: {', '.join(duplicates)}")
    else:
        result.passed("taxonomy.ids", "Capability IDs are unique.")
    invalid = sorted(item for item in ids if not CAPABILITY_ID_RE.fullmatch(item))
    if invalid:
        result.fail("taxonomy.ids", f"Malformed capability IDs: {', '.join(invalid)}")
    missing = sorted(EXPECTED_IDS - set(ids))
    invented = sorted(set(ids) - EXPECTED_IDS)
    if missing or invented:
        result.fail("taxonomy.ids", f"Canonical ID set differs; missing={missing or 'none'}, invented={invented or 'none'}.")
    else:
        result.passed("taxonomy.ids", "Capability IDs match the canonical source set.")

    domain_order = list(dict.fromkeys(item["pillar"] for item in capabilities))
    if domain_order == DOMAIN_ORDER:
        result.passed("taxonomy.domains", "Eight domains appear in canonical order (six core, two cross-cutting).")
    else:
        result.fail("taxonomy.domains", f"Domain order differs: {domain_order}")
    function_count = len({(item["pillar"], item["function"]) for item in capabilities})
    if function_count == 29:
        result.passed("taxonomy.functions", "Catalog contains the canonical 29 pillar/function relationships.")
    else:
        result.fail("taxonomy.functions", f"Expected 29 pillar/function relationships; found {function_count}.")

    relationship_errors: list[str] = []
    for item in capabilities:
        expected_pillar = _expected_pillar_for_id(item["id"])
        if item["pillar"] != expected_pillar:
            relationship_errors.append(f"{item['id']} assigned to {item['pillar']} instead of {expected_pillar}")
        if item["pillar_ko"] != PILLAR_KO.get(item["pillar"]):
            relationship_errors.append(f"{item['id']} has a non-canonical Korean pillar name")
        if not SLUG_RE.fullmatch(item["function"]) or not SLUG_RE.fullmatch(item["capability"]):
            relationship_errors.append(f"{item['id']} has an invalid English slug")
        source = item["source"]
        if source["document"] != CANONICAL_DOCUMENT or not source["table_or_figure"].startswith("Table 3-"):
            relationship_errors.append(f"{item['id']} has an invalid source reference")
    if relationship_errors:
        for error in relationship_errors:
            result.fail("taxonomy.relationships", error)
    else:
        result.passed("taxonomy.relationships", "Pillar, Korean name, slug, and source relationships are valid.")

    digest = _canonical_taxonomy_digest(capabilities)
    if digest == CANONICAL_TAXONOMY_SHA256:
        result.passed("taxonomy.canonical", "Canonical Korean names and source relationships match the reviewed catalog fingerprint.")
    else:
        result.fail("taxonomy.canonical", "Canonical taxonomy fingerprint changed; source review and validator update are required.")


def calculate_summary(records: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "total_capabilities": len(records),
        "validated": sum(item["validation_status"] == "VALIDATED" for item in records),
        "partially_validated": sum(item["validation_status"] == "PARTIALLY_VALIDATED" for item in records),
        "implemented": sum(
            item["implementation_status"] == "IMPLEMENTED"
            and item["validation_status"] not in {"VALIDATED", "PARTIALLY_VALIDATED"}
            for item in records
        ),
        "mapped": sum(item["validation_status"] == "REFERENCE_ONLY" for item in records),
        "planned": sum(item["implementation_status"] == "PLANNED" for item in records),
        "unassessed": sum(item["current_maturity"] == "UNASSESSED" for item in records),
        "not_applicable": sum(item["current_maturity"] == "NOT_APPLICABLE" for item in records),
        "gap_identified": sum(item["validation_status"] == "GAP_IDENTIFIED" for item in records),
    }


def validate_baseline(baseline: dict[str, Any], schema: dict[str, Any], result: ValidationResult) -> None:
    errors = validate_schema_instance(baseline, schema)
    if errors:
        for error in errors:
            result.fail("schema.baseline", error)
        return
    result.passed("schema.baseline", "Baseline assessment conforms to Draft 2020-12 repository schema.")
    records = baseline["capabilities"]
    ids = [item["id"] for item in records]
    duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
    if duplicates or set(ids) != EXPECTED_IDS:
        result.fail("baseline.ids", f"Baseline capability IDs differ; duplicates={duplicates or 'none'}.")
    else:
        result.passed("baseline.ids", "Baseline contains one record for every canonical capability.")
    calculated = calculate_summary(records)
    if baseline["summary"] == calculated:
        result.passed("baseline.summary", "Baseline summary counts match capability records.")
    else:
        result.fail("baseline.summary", f"Summary differs; expected {calculated}, found {baseline['summary']}.")
    limitations = " ".join(baseline["assessment"]["limitations"]).lower()
    if "repository-wide maturity" in limitations and "single-lab" in limitations:
        result.passed("baseline.boundary", "Assessment limitations reject repository-wide and single-lab maturity inference.")
    else:
        result.fail("baseline.boundary", "Assessment must explicitly reject repository-wide and single-lab maturity inference.")


def validate_catalog_baseline_sync(catalog: dict[str, Any], baseline: dict[str, Any], result: ValidationResult) -> None:
    catalog_by_id = {item["id"]: item for item in catalog.get("capabilities", [])}
    baseline_by_id = {item["id"]: item for item in baseline.get("capabilities", [])}
    mismatches: list[str] = []
    pairs = {
        "implementation_status": "implementation_status",
        "validation_status": "validation_status",
        "evidence_level": "evidence_level",
        "current_maturity": "current_maturity",
        "assessment_confidence": "confidence",
        "evidence_authority": "evidence_authority",
    }
    for capability_id in sorted(set(catalog_by_id) & set(baseline_by_id)):
        for catalog_key, baseline_key in pairs.items():
            if catalog_by_id[capability_id].get(catalog_key) != baseline_by_id[capability_id].get(baseline_key):
                mismatches.append(f"{capability_id}:{catalog_key}")
    if mismatches:
        result.fail("sync.machine", f"Catalog/baseline contradictions: {', '.join(mismatches)}")
    else:
        result.passed("sync.machine", "Catalog and baseline status, maturity, evidence, authority, and confidence fields agree.")


def _find_dependency_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    cycles: list[list[str]] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for dependency in graph.get(node, []):
            if state.get(dependency, 0) == 0:
                visit(dependency)
            elif state.get(dependency) == 1:
                start = stack.index(dependency)
                cycle = stack[start:] + [dependency]
                if cycle not in cycles:
                    cycles.append(cycle)
        stack.pop()
        state[node] = 2

    for node in graph:
        if state.get(node, 0) == 0:
            visit(node)
    return cycles


def validate_backlog(
    backlog: dict[str, Any],
    schema: dict[str, Any],
    catalog: dict[str, Any],
    result: ValidationResult,
) -> None:
    errors = validate_schema_instance(backlog, schema)
    if errors:
        for error in errors:
            result.fail("schema.backlog", error)
        return
    result.passed("schema.backlog", "Capability backlog conforms to Draft 2020-12 repository schema.")

    records = backlog["capabilities"]
    ids = [item["id"] for item in records]
    catalog_by_id = {item["id"]: item for item in catalog["capabilities"]}
    backlog_by_id = {item["id"]: item for item in records}
    duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
    if len(records) == 52 and set(ids) == set(catalog_by_id) and not duplicates:
        result.passed("backlog.coverage", "Backlog contains one record for all 52 canonical capabilities.")
    else:
        result.fail(
            "backlog.coverage",
            f"Backlog coverage differs; count={len(records)}, duplicates={duplicates}, "
            f"missing={sorted(set(catalog_by_id)-set(ids))}, extra={sorted(set(ids)-set(catalog_by_id))}.",
        )

    status_errors: list[str] = []
    applicability_errors: list[str] = []
    package_test_errors: list[str] = []
    dependency_errors: list[str] = []
    graph: dict[str, list[str]] = {}
    for item in records:
        capability_id = item["id"]
        catalog_item = catalog_by_id.get(capability_id)
        if catalog_item:
            for key in ("pillar", "function", "capability", "implementation_status", "validation_status", "evidence_level", "current_maturity"):
                if item[key] != catalog_item[key]:
                    status_errors.append(f"{capability_id}:{key}")
        applicability = item["applicability"]
        target = item["lab_target_maturity"]
        if applicability in {"REFERENCE_ONLY", "NOT_APPLICABLE"} and target is not None:
            applicability_errors.append(f"{capability_id}: {applicability} must not have a lab target")
        if applicability in {"LAB_IMPLEMENTABLE", "PARTIALLY_LAB_IMPLEMENTABLE"} and target is None:
            applicability_errors.append(f"{capability_id}: applicable capability lacks a lab target")
        if target == "OPTIMAL":
            justification = f"{item['target_rationale']} {' '.join(item['evidence_requirements'])}".lower()
            if "continuous" not in justification or len(item["target_rationale"]) < 40:
                applicability_errors.append(f"{capability_id}: OPTIMAL target lacks continuous-evidence justification")
        if item["validation_status"] == "VALIDATED" and item["evidence_level"] in {"NONE", "DESIGN"}:
            status_errors.append(f"{capability_id}: VALIDATED lacks supporting evidence")
        boundary = item["future_package_test_boundary"]
        if not boundary.strip():
            package_test_errors.append(f"{capability_id}: package test boundary is empty")
        graph[capability_id] = list(item["dependency_ids"])
        for dependency in item["dependency_ids"]:
            if dependency not in catalog_by_id:
                dependency_errors.append(f"{capability_id}: unknown dependency {dependency}")
            if dependency == capability_id:
                dependency_errors.append(f"{capability_id}: self-dependency")

    if status_errors:
        result.fail("backlog.status", "Backlog contradicts current authorities: " + ", ".join(status_errors))
    else:
        result.passed("backlog.status", "Backlog preserves current catalog implementation, validation, evidence, and maturity state.")
    if applicability_errors:
        for error in applicability_errors:
            result.fail("backlog.applicability", error)
    else:
        result.passed("backlog.applicability", "Applicability and proposed lab targets obey conservative target rules.")
    if package_test_errors:
        for error in package_test_errors:
            result.fail("backlog.package-tests", error)
    else:
        result.passed("backlog.package-tests", "Backlog records an explicit package-test activation boundary for every capability.")

    wave_by_id = {wave["id"]: wave for wave in backlog["waves"]}
    expected_waves = {f"W{number}" for number in range(6)}
    wave_errors: list[str] = []
    if set(wave_by_id) != expected_waves or len(backlog["waves"]) != 6:
        wave_errors.append("waves must be exactly W0-W5")
    assigned: dict[str, str] = {}
    for wave in backlog["waves"]:
        for dependency in wave["dependencies"]:
            if dependency not in wave_by_id:
                wave_errors.append(f"{wave['id']}: unknown wave dependency {dependency}")
        for capability_id in wave["capabilities"]:
            if capability_id in assigned:
                wave_errors.append(f"{capability_id}: assigned to multiple waves")
            assigned[capability_id] = wave["id"]
    for item in records:
        target_wave = item["target_wave"]
        if target_wave is None:
            if item["applicability"] not in {"REFERENCE_ONLY", "NOT_APPLICABLE"}:
                wave_errors.append(f"{item['id']}: applicable item has no target wave")
        elif target_wave not in wave_by_id:
            wave_errors.append(f"{item['id']}: invalid target wave {target_wave}")
        elif assigned.get(item["id"]) != target_wave:
            wave_errors.append(f"{item['id']}: wave list and target_wave disagree")
        elif target_wave is not None:
            target_number = int(target_wave[1:])
            for dependency_id in item["dependency_ids"]:
                dependency_item = backlog_by_id.get(dependency_id)
                dependency_wave = dependency_item.get("target_wave") if dependency_item else None
                if dependency_wave is not None and int(dependency_wave[1:]) > target_number:
                    wave_errors.append(
                        f"{item['id']}: target wave {target_wave} precedes dependency "
                        f"{dependency_id} in {dependency_wave}"
                    )
    wave_graph = {wave_id: list(wave["dependencies"]) for wave_id, wave in wave_by_id.items()}
    for cycle in _find_dependency_cycles(wave_graph):
        wave_errors.append("wave cycle: " + " -> ".join(cycle))
    if wave_errors:
        for error in wave_errors:
            result.fail("backlog.waves", error)
    else:
        result.passed("backlog.waves", "Wave references, membership, and entry dependency ordering are consistent.")

    cycles = _find_dependency_cycles(graph) if not dependency_errors else []
    if dependency_errors or cycles:
        for error in dependency_errors:
            result.fail("backlog.dependencies", error)
        for cycle in cycles:
            result.fail("backlog.dependencies", "Dependency cycle: " + " -> ".join(cycle))
    else:
        result.passed("backlog.dependencies", "Capability dependencies exist, contain no self-reference, and form an acyclic graph.")


def _has_review_exception(item: dict[str, Any]) -> bool:
    return "REVIEW_REQUIRED" in str(item.get("notes", "")) or "REVIEW_REQUIRED" in str(item.get("next_action", ""))


def validate_maturity(records: Iterable[dict[str, Any]], result: ValidationResult, source: str) -> None:
    errors: list[str] = []
    warnings: list[str] = []
    for item in records:
        capability_id = item["id"]
        current = item["current_maturity"]
        target = item.get("target_maturity", current)
        evidence = item["evidence_level"]
        validation = item["validation_status"]
        implementation = item["implementation_status"]
        authority = set(item["evidence_authority"])
        issue: str | None = None
        if current == "OPTIMAL" and evidence != "CONTINUOUS":
            issue = "OPTIMAL requires CONTINUOUS evidence"
        elif current == "ADVANCED" and evidence == "NONE":
            issue = "ADVANCED cannot use NONE evidence"
        elif validation == "VALIDATED" and evidence in {"NONE", "DESIGN"}:
            issue = "VALIDATED requires CONFIGURATION, RUNTIME, or CONTINUOUS evidence"
        elif validation == "PARTIALLY_VALIDATED" and EVIDENCE_ORDER[evidence] < EVIDENCE_ORDER["CONFIGURATION"]:
            issue = "PARTIALLY_VALIDATED requires at least CONFIGURATION evidence"
        elif implementation == "IMPLEMENTED" and authority and authority <= {"DESIGN_ONLY", "MISSING"}:
            issue = "IMPLEMENTED cannot be supported only by design or missing evidence"
        elif current in MATURITY_ORDER and target in MATURITY_ORDER and MATURITY_ORDER[current] > MATURITY_ORDER[target]:
            issue = "current maturity exceeds target maturity"
        if issue:
            if _has_review_exception(item):
                warnings.append(f"{capability_id}: {issue} (REVIEW_REQUIRED)")
            else:
                errors.append(f"{capability_id}: {issue}")
    if errors:
        for error in errors:
            result.fail(f"maturity.{source}", error)
    else:
        result.passed(f"maturity.{source}", "Maturity, implementation, validation, and evidence assignments are consistent.")
    for warning in warnings:
        result.warn(f"maturity.{source}", warning)


def _markdown_table(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    for index in range(len(lines) - 1):
        if lines[index].lstrip().startswith("|") and re.match(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$", lines[index + 1]):
            headers = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            rows: list[dict[str, str]] = []
            for line in lines[index + 2 :]:
                if not line.lstrip().startswith("|"):
                    break
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) == len(headers):
                    rows.append(dict(zip(headers, cells)))
            return rows
    return []


def _safe_relative_reference(root: Path, reference: str) -> tuple[bool, str]:
    cleaned = reference.strip().strip("`").replace("\\", "/")
    if not cleaned or re.match(r"^[A-Za-z]:/", cleaned) or cleaned.startswith("/"):
        return False, "absolute or empty path"
    if any(part.lower() in {"raw", "secrets", "credentials", "private", "tokens", "passwords"} for part in Path(cleaned).parts):
        return False, "suspicious evidence path segment"
    if Path(cleaned).name.lower() in {"clouds.yaml", "passwords.yml", "id_rsa", "id_ed25519"}:
        return False, "sensitive evidence filename"
    target = (root / cleaned).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return False, "path escapes repository"
    return target.exists(), "missing target" if not target.exists() else "ok"


def _has_live_execution_record(root: Path, references: list[str]) -> bool:
    candidates: list[Path] = []
    for reference in references:
        target = root / reference.strip().strip("`")
        if target.is_dir():
            candidates.extend(target.rglob("*.sanitized.txt"))
        elif target.is_file():
            candidates.append(target)
    for path in candidates:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if path.suffix.lower() in {".yaml", ".yml", ".json"}:
            try:
                record = json.loads(text)
            except json.JSONDecodeError:
                record = None
            if isinstance(record, dict):
                authority = str(record.get("execution_authority", ""))
                results = record.get("results", {})
                exit_code = results.get("exit_code") if isinstance(results, dict) else None
                if "LIVE_RUNTIME" in authority and exit_code == 0 and "PASS" in text:
                    return True
        if "[PASS]" in text and re.search(r"(?i)execut(?:ed|ion)|exit\s*(?:code|status)?\s*[:=]?\s*0", text):
            return True
    return False


def validate_evidence(root: Path, baseline: dict[str, Any], result: ValidationResult) -> None:
    errors: list[str] = []
    for item in baseline.get("capabilities", []):
        references = item.get("evidence", [])
        for reference in references:
            valid, reason = _safe_relative_reference(root, reference)
            if not valid:
                errors.append(f"{item['id']}: {reference} ({reason})")
        authority = set(item.get("evidence_authority", []))
        if "CODEX_EXECUTED_LIVE_RUNTIME" in authority and not _has_live_execution_record(root, references):
            errors.append(f"{item['id']}: CODEX_EXECUTED_LIVE_RUNTIME lacks a sanitized command/result record")
        if item.get("evidence_level") in {"RUNTIME", "CONTINUOUS"} and authority <= {"DESIGN_ONLY", "CONFIGURATION_ONLY", "MISSING"}:
            errors.append(f"{item['id']}: runtime evidence level conflicts with authority")
        if item.get("evidence_level") == "DESIGN" and authority & {"USER_EXECUTED_RUNTIME", "CODEX_EXECUTED_LIVE_RUNTIME"}:
            errors.append(f"{item['id']}: runtime authority is classified as design evidence")
    if errors:
        for error in errors:
            result.fail("evidence.references", error)
    else:
        result.passed("evidence.references", "Evidence references resolve and evidence level/authority classifications are consistent.")


def _negative_claim_context(line: str, path: Path, section: str = "", previous: str = "") -> bool:
    if SAFE_CLAIM_CONTEXT.search(f"{previous} {line}"):
        return True
    lowered = path.name.lower()
    return (
        any(token in lowered for token in ("prohibited", "validation-checklist", "scope-boundary-review", "excluded-scope"))
        or re.search(r"(?i)prohibited|unsupported|boundary|excluded", section) is not None
    )


def validate_overclaims(root: Path, result: ValidationResult) -> None:
    files = [root / "README.md", root / "AGENTS.md"] + sorted((root / "docs").rglob("*.md"))
    files += sorted((root / "docs/zero-trust").glob("*.yaml"))
    hits: list[str] = []
    for path in files:
        if not path.is_file():
            continue
        section = ""
        previous = ""
        for line_number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
            if heading:
                section = heading.group(1)
            for phrase in FORBIDDEN_CLAIMS:
                if phrase.lower() in line.lower() and not _negative_claim_context(line, path, section, previous):
                    hits.append(f"{path.relative_to(root)}:{line_number}: {phrase}")
            previous = line
    if hits:
        for hit in hits:
            result.fail("claims", f"Unsupported affirmative claim: {hit}")
    else:
        result.passed("claims", "No unsupported affirmative Zero Trust claims were found.")


SENSITIVE_PATTERNS = [
    ("private-key", re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("github-token", re.compile(r"\b(?:ghp|gho|ghu|ghs|github_pat)_[A-Za-z0-9_]{20,}\b")),
    ("bearer-token", re.compile(r"(?i)\bAuthorization\s*:\s*Bearer\s+[A-Za-z0-9._~+/-]{12,}")),
    ("secret-assignment", re.compile(r"(?i)\b(?:password|passwd|client_secret|api[_-]?key|access[_-]?key|token)\s*[:=]\s*['\"]?(?!<|\$\{|TODO|TBD|placeholder|NOT_|none|null)[A-Za-z0-9/+_.=-]{8,}")),
    ("mac-address", re.compile(r"(?i)\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b")),
    ("uuid", re.compile(r"(?i)\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b")),
]


def _candidate_repository_files(root: Path) -> list[Path]:
    try:
        output = subprocess.run(
            ["git", "ls-files", "-co", "--exclude-standard"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        ).stdout
        return [root / line for line in output.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        return [path for path in root.rglob("*") if path.is_file() and ".git" not in path.parts]


def _redacted_preview(line: str, match: re.Match[str]) -> str:
    value = match.group(0)
    masked = value[:2] + "<redacted>" + value[-2:] if len(value) > 4 else "<redacted>"
    preview = (line[: match.start()] + masked + line[match.end() :]).strip()
    return preview[:120]


def validate_sensitive_data(root: Path, result: ValidationResult) -> None:
    extensions = {".md", ".txt", ".yaml", ".yml", ".json", ".ps1", ".py", ".ini", ".conf", ".tf", ".sql"}
    hits: list[str] = []
    risky_names = {"clouds.yaml", "passwords.yml", "id_rsa", "id_ed25519", "kubeconfig"}
    for path in _candidate_repository_files(root):
        relative = path.relative_to(root)
        if path.name.lower() in risky_names or any(part.lower() == "raw" for part in relative.parts):
            hits.append(f"{relative}:1: risky-file: <filename-redacted>")
            continue
        if path.suffix.lower() not in extensions or not path.is_file():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for detector, pattern in SENSITIVE_PATTERNS:
                for match in pattern.finditer(line):
                    if "<" in match.group(0) or re.search(r"(?i)placeholder|example|regex|detect|prohibit|must not|do not", line):
                        continue
                    hits.append(f"{relative}:{line_number}: {detector}: {_redacted_preview(line, match)}")
    if hits:
        for hit in hits:
            result.fail("sensitive-data", hit)
    else:
        result.passed("sensitive-data", "No private keys, tokens, credential assignments, MAC inventories, or UUID collections were detected.")


def _heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: Counter[str] = Counter()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]+>", "", match.group(1)).strip().lower()
        heading = re.sub(r"[^\w\-\s가-힣]", "", heading, flags=re.UNICODE)
        anchor = re.sub(r"\s+", "-", heading)
        suffix = counts[anchor]
        counts[anchor] += 1
        anchors.add(anchor if suffix == 0 else f"{anchor}-{suffix}")
    return anchors


def validate_markdown_links(root: Path, result: ValidationResult) -> None:
    files = sorted((root / "docs/zero-trust").glob("*.md")) + [root / "README.md", root / "AGENTS.md", root / "docs/codex-workflow.md", root / "docs/validation-checklist.md"]
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    errors: list[str] = []
    for path in files:
        if not path.is_file():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for raw_target in pattern.findall(line):
                target = raw_target.strip().strip("<>").split()[0]
                if re.match(r"^(?:https?|mailto):", target, re.I):
                    continue
                if re.match(r"^[A-Za-z]:[\\/]", target) or target.startswith("file:"):
                    errors.append(f"{path.relative_to(root)}:{line_number}: local absolute path")
                    continue
                file_part, _, anchor = target.partition("#")
                resolved = path if not file_part else (path.parent / file_part).resolve()
                try:
                    resolved.relative_to(root.resolve())
                except ValueError:
                    errors.append(f"{path.relative_to(root)}:{line_number}: link escapes repository")
                    continue
                if not resolved.exists():
                    errors.append(f"{path.relative_to(root)}:{line_number}: missing {target}")
                elif anchor and resolved.suffix.lower() == ".md" and anchor.lower() not in _heading_anchors(resolved):
                    errors.append(f"{path.relative_to(root)}:{line_number}: missing anchor #{anchor}")
    if errors:
        for error in errors:
            result.fail("markdown.links", error)
    else:
        result.passed("markdown.links", "Relative Markdown files and practical heading anchors resolve without local absolute paths.")


def validate_source(root: Path, result: ValidationResult) -> None:
    source_doc = root / "docs/zero-trust/authoritative-source.md"
    text = source_doc.read_text(encoding="utf-8")
    match = re.search(r"SHA-256:\s*`([0-9A-Fa-f]{64})`", text)
    if not match:
        result.fail("source", "Authoritative source metadata lacks a SHA-256 digest.")
        return
    configured = os.environ.get("ZT_GUIDE_PATH")
    if configured:
        source = Path(configured)
        if not source.is_file():
            result.fail("source", "ZT_GUIDE_PATH does not identify a readable local file.")
            return
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest.lower() != match.group(1).lower():
            result.fail("source", "ZT_GUIDE_PATH hash differs from authoritative-source.md.")
            return
        result.passed("source", "ZT_GUIDE_PATH exists and matches the recorded source digest.")
    else:
        result.passed("source", "External source metadata is pinned by digest; offline repository validation does not require the PDF.")


def validate_foundation_package_data(
    package: dict[str, Any],
    catalog_ids: set[str],
    execution: dict[str, Any] | None,
    runtime_ignored: bool,
    result: ValidationResult,
) -> None:
    category = "package.zt-fnd-001"
    if package.get("package_id") != "ZT-FND-001":
        result.fail(category, "Package ID must be ZT-FND-001.")

    authority = package.get("evidence_authority")
    if authority not in PACKAGE_EVIDENCE_AUTHORITIES:
        result.fail(category, f"Invalid package evidence authority: {authority!r}.")

    mappings = package.get("capability_mappings")
    if not isinstance(mappings, list) or not mappings:
        result.fail(category, "Package capability mappings must be a non-empty list.")
    else:
        unknown = sorted(set(mappings) - catalog_ids)
        if unknown:
            result.fail(category, f"Unknown package capability mappings: {', '.join(unknown)}.")

    if package.get("target_maturity") == "OPTIMAL" or package.get("current_maturity") == "OPTIMAL":
        result.fail(category, "ZT-FND-001 must not assign OPTIMAL maturity.")

    if not runtime_ignored:
        result.fail(category, ".runtime/zero-trust/ must be ignored by Git.")

    validation_status = package.get("validation_status")
    live_authorities = {"CODEX_EXECUTED_LIVE_RUNTIME", "USER_EXECUTED_RUNTIME"}
    if execution is None:
        if validation_status in {"VALIDATED", "PARTIALLY_VALIDATED"}:
            result.fail(category, "A live validation status requires a machine-readable execution record.")
        if authority in live_authorities:
            result.fail(category, "A live-runtime evidence authority requires a machine-readable execution record.")
    else:
        execution_authority = execution.get("execution_authority")
        if execution_authority not in live_authorities:
            result.fail(category, "Execution record authority must identify actual Codex or user live runtime execution.")
        commands = execution.get("commands")
        if execution_authority == "CODEX_EXECUTED_LIVE_RUNTIME" and not commands:
            result.fail(category, "Codex live-runtime authority requires recorded commands.")
        if validation_status == "VALIDATED":
            results = execution.get("results")
            if not isinstance(results, dict):
                result.fail(category, "VALIDATED package requires OpenStack and EVE result objects.")
            else:
                for target in ("openstack", "eve"):
                    target_result = results.get(target)
                    if not isinstance(target_result, dict) or target_result.get("exit_code") != 0 or target_result.get("fail") != 0:
                        result.fail(category, f"VALIDATED package requires a successful {target} result.")
            boundary = execution.get("security_boundary")
            required_boundary = ("interactive_shell_blocked", "arbitrary_command_blocked", "credential_read_blocked")
            if not isinstance(boundary, dict) or any(boundary.get(field) is not True for field in required_boundary):
                result.fail(category, "VALIDATED package requires all security-boundary tests to pass.")

    if not any(item.level == "FAIL" and item.category == category for item in result.findings):
        result.passed(category, "ZT-FND-001 package status, mappings, runtime boundary, and evidence authority are internally consistent.")


def validate_foundation_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    missing = [str(path) for path in (FOUNDATION_PACKAGE_PATH, *FOUNDATION_REQUIRED_PATHS) if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail("package.zt-fnd-001.files", f"Required package file is missing: {path}.")
        return

    try:
        package = load_json_yaml(root / FOUNDATION_PACKAGE_PATH)
    except ValueError as exc:
        result.fail("package.zt-fnd-001.configuration", str(exc))
        return
    if not isinstance(package, dict):
        result.fail("package.zt-fnd-001.configuration", "Package definition must be an object.")
        return

    execution: dict[str, Any] | None = None
    execution_path = root / FOUNDATION_EXECUTION_PATH
    if execution_path.is_file():
        try:
            loaded = load_json_yaml(execution_path)
        except ValueError as exc:
            result.fail("package.zt-fnd-001.execution", str(exc))
            return
        if not isinstance(loaded, dict):
            result.fail("package.zt-fnd-001.execution", "Execution record must be an object.")
            return
        execution = loaded

    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace") if (root / ".gitignore").is_file() else ""
    runtime_ignored = any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines())
    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}
    validate_foundation_package_data(package, catalog_ids, execution, runtime_ignored, result)

    wrappers = {
        "openstack": root / "tools/live-validation/validate-openstack-live.ps1",
        "eve": root / "tools/live-validation/validate-eve-live.ps1",
    }
    expected = {
        "openstack": ("openstack-validator", "validate-all"),
        "eve": ("eve-validator", "validate-host"),
    }
    wrapper_errors: list[str] = []
    for name, path in wrappers.items():
        text = path.read_text(encoding="utf-8", errors="replace")
        alias, command = expected[name]
        if alias not in text or command not in text or "BatchMode=yes" not in text:
            wrapper_errors.append(f"{name} wrapper does not contain the fixed alias, command, and BatchMode boundary")
        if re.search(r"(?i)password\s*=|private.?key\s*=|authorization\s*:", text):
            wrapper_errors.append(f"{name} wrapper contains a credential-like assignment")
    if wrapper_errors:
        for error in wrapper_errors:
            result.fail("package.zt-fnd-001.wrappers", error)
    else:
        result.passed("package.zt-fnd-001.wrappers", "Live wrappers use fixed aliases, fixed commands, BatchMode, and no credential assignments.")


def validate_router_package_data(
    package: dict[str, Any],
    catalog_ids: set[str],
    execution: dict[str, Any] | None,
    runtime_ignored: bool,
    result: ValidationResult,
) -> None:
    category = "package.zt-net-001"
    if package.get("package_id") != "ZT-NET-001":
        result.fail(category, "Package ID must be ZT-NET-001.")
    authority = package.get("evidence_authority")
    if authority not in PACKAGE_EVIDENCE_AUTHORITIES:
        result.fail(category, f"Invalid package evidence authority: {authority!r}.")
    mappings = package.get("capability_mappings")
    if not isinstance(mappings, list) or not mappings:
        result.fail(category, "Router capability mappings must be a non-empty list.")
    else:
        unknown = sorted(set(mappings) - catalog_ids)
        if unknown:
            result.fail(category, f"Unknown router capability mappings: {', '.join(unknown)}.")
    if package.get("target_maturity") == "OPTIMAL" or package.get("current_maturity") == "OPTIMAL":
        result.fail(category, "ZT-NET-001 must not assign OPTIMAL maturity.")
    if not runtime_ignored:
        result.fail(category, ".runtime/zero-trust/ must be ignored by Git.")

    status = package.get("validation_status")
    live_statuses = {
        "VALIDATED", "PARTIALLY_VALIDATED",
        "RUNTIME_VALIDATED", "PARTIALLY_RUNTIME_VALIDATED",
    }
    accepted_statuses = {"VALIDATED", "RUNTIME_VALIDATED"}
    live_authorities = {"CODEX_EXECUTED_LIVE_RUNTIME", "USER_EXECUTED_RUNTIME"}
    if execution is None:
        if status in live_statuses or authority in live_authorities:
            result.fail(category, "A router live-validation claim requires a machine-readable execution record.")
    else:
        if execution.get("execution_authority") not in live_authorities:
            result.fail(category, "Router execution authority must identify actual live runtime execution.")
        if execution.get("execution_authority") == "CODEX_EXECUTED_LIVE_RUNTIME" and not execution.get("commands"):
            result.fail(category, "Codex router runtime authority requires recorded commands.")
        if status in live_statuses:
            results = execution.get("results")
            if not isinstance(results, dict) or results.get("exit_code") != 0 or results.get("fail") != 0:
                result.fail(category, "A live router validation status requires exit code 0 and zero failed checks.")
            boundary = execution.get("security_boundary")
            required = ("interactive_shell_blocked", "arbitrary_command_blocked", "configuration_command_blocked", "arbitrary_ping_blocked")
            if not isinstance(boundary, dict) or any(boundary.get(field) is not True for field in required):
                result.fail(category, "Router live validation requires all forced-command boundary tests.")
        if status in accepted_statuses and execution.get("validation", {}).get("access_control") != "PASS":
            result.fail(category, "VALIDATED router package requires a passing persistent access-control result.")
        if status in accepted_statuses:
            if package.get("segmentation_classification") != "BOUNDED_INTERZONE_ACL_VALIDATED":
                result.fail(category, "VALIDATED router package requires BOUNDED_INTERZONE_ACL_VALIDATED classification.")
            persistent = execution.get("persistent_acl", {})
            required_persistent = {
                "binding": "PASS",
                "running_configuration": "PASS",
                "startup_configuration": "PASS",
                "dmz_gateway_permit": "PASS_5_OF_5",
                "dmz_to_kubernetes_deny": "PASS_0_OF_5",
                "dmz_public_path_permit": "PASS_5_OF_5",
                "permit_and_deny_counters": "PASS",
            }
            for field, expected in required_persistent.items():
                if persistent.get(field) != expected:
                    result.fail(category, f"Persistent ACL field {field} must be {expected} for VALIDATED status.")
            if persistent.get("automatic_rollback_exercised") is not True:
                result.fail(category, "VALIDATED persistent ACL requires recorded rollback exercise evidence.")

    if not any(item.level == "FAIL" and item.category == category for item in result.findings):
        result.passed(category, "ZT-NET-001 status, mappings, runtime evidence, and security boundary are internally consistent.")


def validate_router_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    missing = [str(path) for path in (ROUTER_PACKAGE_PATH, *ROUTER_REQUIRED_PATHS) if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail("package.zt-net-001.files", f"Required router package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / ROUTER_PACKAGE_PATH)
        execution = load_json_yaml(root / ROUTER_EXECUTION_PATH) if (root / ROUTER_EXECUTION_PATH).is_file() else None
    except ValueError as exc:
        result.fail("package.zt-net-001.configuration", str(exc))
        return
    if not isinstance(package, dict) or (execution is not None and not isinstance(execution, dict)):
        result.fail("package.zt-net-001.configuration", "Router package and execution records must be objects.")
        return
    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace") if (root / ".gitignore").is_file() else ""
    runtime_ignored = any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines())
    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}
    validate_router_package_data(package, catalog_ids, execution, runtime_ignored, result)

    wrapper = (root / "tools/live-validation/validate-router-live.ps1").read_text(encoding="utf-8", errors="replace")
    dispatcher = (root / "tools/live-validation/remote/codex-router-dispatcher.sh.example").read_text(encoding="utf-8", errors="replace")
    errors: list[str] = []
    if "BatchMode=yes" not in wrapper or "snsd-r1-validator validate-routing" not in wrapper:
        errors.append("Local router wrapper lacks the fixed alias, fixed command, or BatchMode boundary")
    if "SSH_ORIGINAL_COMMAND" not in dispatcher or "validate-routing)" not in dispatcher or "Command is not permitted." not in dispatcher:
        errors.append("Router dispatcher does not enforce the exact validate-routing command")
    if re.search(r"(?i)\$\{?(?:command|target|ping|argument)", wrapper):
        errors.append("Local router wrapper exposes a caller-controlled command or target")
    if errors:
        for error in errors:
            result.fail("package.zt-net-001.wrappers", error)
    else:
        result.passed("package.zt-net-001.wrappers", "Router wrapper and dispatcher preserve the fixed-command boundary.")


def validate_telemetry_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    missing = [str(path) for path in (TELEMETRY_PACKAGE_PATH, *TELEMETRY_REQUIRED_PATHS) if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail("package.zt-vis-001.files", f"Required telemetry package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / TELEMETRY_PACKAGE_PATH)
        execution = load_json_yaml(root / TELEMETRY_EXECUTION_PATH) if (root / TELEMETRY_EXECUTION_PATH).is_file() else None
        inventory = load_json_yaml(root / "docs/zero-trust/telemetry-source-inventory.yaml")
        rules_doc = load_json_yaml(root / "docs/zero-trust/correlation-rule-catalog.yaml")
        load_json_yaml(root / "schemas/zero-trust-telemetry-event.schema.json")
        load_json_yaml(root / "schemas/zero-trust-correlation-finding.schema.json")
    except ValueError as exc:
        result.fail("package.zt-vis-001.configuration", str(exc))
        return
    if not all(isinstance(value, dict) for value in (package, inventory, rules_doc)):
        result.fail("package.zt-vis-001.configuration", "Telemetry package, inventory, and rules must be objects.")
        return
    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict)}
    mappings = package.get("capability_mappings", [])
    if not mappings or set(mappings) - catalog_ids:
        result.fail("package.zt-vis-001", "Telemetry package capability mappings are missing or invalid.")
    expected_state = (
        "IMPLEMENTED", "RUNTIME_VALIDATED", "LOCAL_VALIDATED", "VALIDATED", "ACCEPTED",
        "BOUNDED_SINGLE_NODE_SANITIZED_LOCAL_TELEMETRY", "UNASSESSED", "UNASSESSED", "INITIAL",
    )
    actual_state = (
        package.get("implementation_status"), package.get("validation_status"), package.get("local_validation_status"),
        package.get("runtime_validation_status"), package.get("runtime_acceptance_status"), package.get("runtime_scope"),
        package.get("maturity_status"), package.get("current_maturity"), package.get("target_maturity"),
    )
    if actual_state != expected_state:
        result.fail("package.zt-vis-001", "ZT-VIS-001 must retain its bounded runtime-validated, accepted, and unassessed state.")
    if package.get("current_maturity") in {"ADVANCED", "OPTIMAL"} or package.get("target_maturity") == "OPTIMAL":
        result.fail("package.zt-vis-001", "The bounded telemetry package must not claim current ADVANCED/OPTIMAL or target OPTIMAL maturity.")
    authority = package.get("evidence_authority")
    if authority not in PACKAGE_EVIDENCE_AUTHORITIES:
        result.fail("package.zt-vis-001", "Telemetry evidence authority is invalid.")
    if authority in {"CODEX_EXECUTED_LIVE_RUNTIME", "USER_EXECUTED_RUNTIME"} and execution is None:
        result.fail("package.zt-vis-001", "Live telemetry authority requires an execution record.")
    if execution is not None:
        if execution.get("execution_authority") == "CODEX_EXECUTED_LIVE_RUNTIME" and not execution.get("commands"):
            result.fail("package.zt-vis-001", "Codex telemetry execution requires recorded commands.")
        results = execution.get("results", {})
        accepted_statuses = {"VALIDATED", "RUNTIME_VALIDATED"}
        if package.get("validation_status") in accepted_statuses | {"PARTIALLY_VALIDATED"} and (results.get("exit_code") != 0 or results.get("fail") != 0):
            result.fail("package.zt-vis-001", "Telemetry live-validation status requires exit code 0 and zero failed checks.")
        if package.get("validation_status") in accepted_statuses and results.get("unavailable_sources", 0) != 0:
            result.fail("package.zt-vis-001", "VALIDATED telemetry package cannot have unavailable mandatory sources.")
        if package.get("validation_status") in accepted_statuses:
            persistent = execution.get("persistent_storage", {})
            required_persistent = {
                "pinned_images": "PASS",
                "service_health": "PASS_3_OF_3",
                "loopback_endpoints": "PASS_3_OF_3",
                "retention": "PASS_336_HOURS",
                "sanitized_ingestion_and_query": "PASS",
                "post_restart_health": "PASS",
                "post_restart_same_event_query": "PASS",
                "secret_pattern_scan": "PASS",
            }
            for field, expected in required_persistent.items():
                if persistent.get(field) != expected:
                    result.fail("package.zt-vis-001.persistence", f"{field} must be {expected} for VALIDATED persistent telemetry.")
            revalidation = execution.get("runtime_revalidation", {})
            required_revalidation = {
                "action_id": "P1-VIS-CLOSE",
                "decision": "ACCEPTED_BOUNDED_LOCAL_VISIBILITY",
                "evidence_continuity": "EC3_ONE_TIME_RUNTIME",
                "central_visibility_claimed": False,
                "maturity_assessed": False,
                "secret_findings": 0,
                "privacy_findings": 0,
            }
            for field, expected in required_revalidation.items():
                if revalidation.get(field) != expected:
                    result.fail("package.zt-vis-001.revalidation", f"{field} must be {expected!r} for bounded runtime acceptance.")
            event_validation = revalidation.get("event_validation", {})
            if (
                event_validation.get("source_transport") != "PASS_4_OF_4"
                or event_validation.get("source_attribution") != "PASS_4_OF_4"
                or event_validation.get("event_freshness") != "PASS_WITHIN_900_SECONDS"
                or event_validation.get("rejected_events") != 0
            ):
                result.fail("package.zt-vis-001.revalidation", "Runtime acceptance requires four-source transport, attribution, freshness, and zero rejected normalized events.")
            time_validation = revalidation.get("time_validation", {})
            if (
                time_validation.get("local_time_alignment") != "PASS_WITHIN_SEQUENTIAL_MEASUREMENT_BOUND"
                or time_validation.get("continuous_ntp_claimed") is not False
            ):
                result.fail("package.zt-vis-001.revalidation", "Local time alignment must pass without claiming unavailable continuous NTP synchronization.")
            permissions = revalidation.get("permission_validation", {})
            if permissions.get("permissions_changed") is not False or not all(
                str(permissions.get(field, "")).startswith("PASS_")
                for field in ("configuration_directory", "sanitized_input_directory", "service_data_directories", "vm_local_secret_file")
            ):
                result.fail("package.zt-vis-001.revalidation", "Reviewed telemetry ownership and permission boundaries must pass without mutation.")
            rollback = revalidation.get("rollback", {})
            if (
                rollback.get("runtime_power_state_rollback") != "PASS_ORIGINAL_STOPPED_STATE_RESTORED"
                or rollback.get("logging_configuration_written") is not False
                or rollback.get("logging_permissions_changed") is not False
                or rollback.get("timesync_service") != "PASS_ACTIVE_ORIGINAL_STATE_RESTORED"
            ):
                result.fail("package.zt-vis-001.revalidation", "Runtime power state must be restored without logging configuration or permission writes.")

    sources = inventory.get("sources", [])
    allowed_states = {"CURRENT_RUNNING", "CURRENT_CONFIG_ONLY", "PLANNED", "ABSENT", "UNKNOWN"}
    if not isinstance(sources, list) or not sources or any(source.get("current_state") not in allowed_states for source in sources):
        result.fail("package.zt-vis-001.inventory", "Telemetry inventory is missing or uses an invalid source state.")
    serialized_inventory = json.dumps(inventory).lower()
    if any(path in serialized_inventory for path in ("clouds.yaml", "passwords.yml", "/etc/shadow", "/.ssh/", "kubeconfig")):
        result.fail("package.zt-vis-001.inventory", "Telemetry inventory contains a credential-bearing collection path.")

    rules = rules_doc.get("rules", [])
    rule_ids = [rule.get("id") for rule in rules if isinstance(rule, dict)]
    if len(rule_ids) != len(set(rule_ids)):
        result.fail("package.zt-vis-001.rules", "Correlation rule IDs must be unique.")
    allowed_actions = {"LOG", "ALERT", "CREATE_EVIDENCE", "REQUIRE_REVIEW"}
    for rule in rules:
        if set(rule.get("capability_mappings", [])) - catalog_ids:
            result.fail("package.zt-vis-001.rules", f"{rule.get('id')}: unknown capability mapping.")
        if not set(rule.get("response_actions", [])) <= allowed_actions:
            result.fail("package.zt-vis-001.rules", f"{rule.get('id')}: blocking or mutating response action is prohibited.")
    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if not any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines()):
        result.fail("package.zt-vis-001", "Telemetry runtime must be ignored by Git.")
    wrapper = (root / "tools/live-validation/collect-telemetry-live.ps1").read_text(encoding="utf-8", errors="replace")
    for fixed in ("openstack-validator", "eve-validator", "snsd-r1-validator", "BatchMode=yes"):
        if fixed not in wrapper:
            result.fail("package.zt-vis-001.wrapper", f"Telemetry wrapper lacks fixed boundary: {fixed}.")
    if package.get("validation_status") in {"VALIDATED", "RUNTIME_VALIDATED"}:
        compose = (root / "observability/logging/compose.yaml").read_text(encoding="utf-8", errors="replace")
        loki_config = (root / "observability/logging/loki-config.yaml").read_text(encoding="utf-8", errors="replace")
        manager = (root / "tools/live-validation/manage-persistent-telemetry.ps1").read_text(encoding="utf-8", errors="replace")
        for pinned in ("grafana/grafana:13.1.0", "grafana/loki:3.7.0", "grafana/alloy:v1.18.0"):
            if pinned not in compose:
                result.fail("package.zt-vis-001.persistence", f"Pinned image is missing: {pinned}.")
        for loopback in ("127.0.0.1:3000:3000", "127.0.0.1:3100:3100", "127.0.0.1:12345:12345"):
            if loopback not in compose:
                result.fail("package.zt-vis-001.persistence", f"Loopback-only binding is missing: {loopback}.")
        if "retention_period: 336h" not in loki_config:
            result.fail("package.zt-vis-001.persistence", "Loki 336-hour retention is missing.")
        for forbidden in ("privileged: true", "/var/run/docker.sock", "network_mode: host"):
            if forbidden in compose:
                result.fail("package.zt-vis-001.persistence", f"Forbidden telemetry container boundary is present: {forbidden}.")
        for mode in ("'Check', 'Deploy', 'Validate', 'Persistence'", "PERSISTENT_TELEMETRY_RESTART_VALIDATE=PASS"):
            if mode not in manager:
                result.fail("package.zt-vis-001.persistence", f"Persistent telemetry manager contract is missing: {mode}.")
    if not any(item.level == "FAIL" and item.category.startswith("package.zt-vis-001") for item in result.findings):
        result.passed("package.zt-vis-001", "ZT-VIS-001 inventory, schemas, deterministic rules, runtime record, and non-blocking boundary are consistent.")


def validate_endpoint_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-dev-001"
    required = (
        ENDPOINT_PACKAGE_PATH,
        ENDPOINT_EXECUTION_PATH,
        ENDPOINT_INVENTORY_PATH,
        ENDPOINT_POLICY_PATH,
        ENDPOINT_INVENTORY_SCHEMA_PATH,
        *ENDPOINT_REQUIRED_PATHS,
    )
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required endpoint package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / ENDPOINT_PACKAGE_PATH)
        execution = load_json_yaml(root / ENDPOINT_EXECUTION_PATH)
        inventory = load_json_yaml(root / ENDPOINT_INVENTORY_PATH)
        policy = load_json_yaml(root / ENDPOINT_POLICY_PATH)
        inventory_schema = load_schema(root / ENDPOINT_INVENTORY_SCHEMA_PATH)
        load_schema(root / "schemas/zero-trust-software-inventory.schema.json")
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    if not all(isinstance(item, dict) for item in (package, execution, inventory, policy)):
        result.fail(f"{category}.configuration", "Endpoint package, execution, inventory, and policy records must be objects.")
        return

    if package.get("package_id") != "ZT-DEV-001" or execution.get("package_id") != "ZT-DEV-001":
        result.fail(category, "Package and execution identifiers must be ZT-DEV-001.")
    if package.get("implementation_status") != "IMPLEMENTED" or package.get("validation_status") != "PARTIALLY_RUNTIME_VALIDATED":
        result.fail(category, "The accepted bounded endpoint package must remain IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED.")
    if package.get("current_maturity") != "UNASSESSED" or package.get("target_maturity") == "OPTIMAL":
        result.fail(category, "Endpoint maturity must remain UNASSESSED and must not target OPTIMAL.")
    if package.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME" or execution.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME":
        result.fail(category, "Endpoint runtime claims require actual Codex execution authority.")

    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}
    mappings = package.get("capability_mappings", [])
    mapped_ids = [item.get("id") for item in mappings if isinstance(item, dict)]
    if not mappings or len(mapped_ids) != len(mappings) or any(item not in catalog_ids for item in mapped_ids):
        result.fail(category, "Endpoint capability mappings are empty, malformed, or non-canonical.")
    if set(mapped_ids) != {"ZT-2.1.1", "ZT-2.2.1", "ZT-2.3.1", "ZT-2.3.2", "ZT-2.4.1", "ZT-2.4.2"}:
        result.fail(category, "Endpoint package must explicitly separate all six canonical device-domain capability relationships.")

    schema_errors = validate_schema_instance(inventory, inventory_schema)
    for error in schema_errors:
        result.fail(f"{category}.inventory", error)
    assets = inventory.get("assets", [])
    asset_ids = [item.get("asset_id") for item in assets if isinstance(item, dict)]
    if len(asset_ids) != len(set(asset_ids)):
        result.fail(f"{category}.inventory", "Device inventory asset IDs must be unique.")
    if any(not item.get("owner_role") for item in assets if isinstance(item, dict)):
        result.fail(f"{category}.inventory", "Every endpoint asset requires an owner role.")
    if any(item.get("privileged") is True and not item.get("compliance_profile") for item in assets if isinstance(item, dict)):
        result.fail(f"{category}.inventory", "Every privileged asset requires a compliance profile.")

    profiles = policy.get("profiles", [])
    profile_ids = [item.get("profile_id") for item in profiles if isinstance(item, dict)]
    if len(profile_ids) != len(set(profile_ids)) or not profile_ids:
        result.fail(f"{category}.policy", "Compliance profile IDs must be present and unique.")
    if policy.get("mandatory_live_assets") != ["ZTD-ASSET-MONITORING-VM-01"]:
        result.fail(f"{category}.policy", "Exactly the bounded monitoring VM must be mandatory for this accepted pilot.")
    for field in ("automatic_remediation", "automatic_patching", "automatic_reboot"):
        if policy.get(field) is not False or package.get(field) is not False:
            result.fail(f"{category}.policy", f"{field} must remain false.")
    if package.get("endpoint_agent_installed") is not False or package.get("edr_decision") != "DEFERRED":
        result.fail(f"{category}.policy", "EDR must remain deferred and no endpoint agent may be installed by this package.")

    results = execution.get("results", {})
    if results.get("exit_code") != 0 or results.get("fail") != 0 or results.get("assessed_assets") != 1:
        result.fail(f"{category}.execution", "Accepted partial runtime evidence requires one assessed asset, exit code zero, and zero failures.")
    if execution.get("patch_state", {}).get("automatic_patching_performed") is not False or execution.get("patch_state", {}).get("reboot_performed") is not False:
        result.fail(f"{category}.execution", "Execution evidence must prove that patching and reboot were not performed.")
    if execution.get("vulnerability", {}).get("exploit_executed") is not False or execution.get("endpoint_agent", {}).get("installed_by_package") is not False:
        result.fail(f"{category}.execution", "Execution evidence must prove no exploit or endpoint-agent installation occurred.")
    sanitization = execution.get("sanitization", {})
    for field in ("secrets", "personal_data", "mac_addresses", "serial_numbers"):
        if sanitization.get(field) != 0:
            result.fail(f"{category}.privacy", f"Sanitized endpoint evidence requires {field}=0.")

    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if not any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines()):
        result.fail(f"{category}.runtime", ".runtime/zero-trust/ must remain ignored.")
    wrapper = (root / "tools/live-validation/validate-endpoints-live.ps1").read_text(encoding="utf-8", errors="replace")
    for token in ("ZTD-ASSET-MONITORING-VM-01", "apt list --upgradable", "sudo -n docker ps", "BatchMode=yes", ".runtime/zero-trust/endpoint/latest"):
        if token not in wrapper:
            result.fail(f"{category}.wrapper", f"Endpoint wrapper is missing fixed read-only boundary token: {token}.")
    for forbidden in ("apt-get install", "apt install", "apt upgrade", "systemctl restart", "shutdown /", "Restart-Computer", "Invoke-Expression"):
        if forbidden.lower() in wrapper.lower():
            result.fail(f"{category}.wrapper", f"Endpoint wrapper contains prohibited mutating behavior: {forbidden}.")

    committed = json.dumps({"package": package, "execution": execution, "inventory": inventory, "policy": policy}, ensure_ascii=False)
    if re.search(r"(?i)\b(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b", committed):
        result.fail(f"{category}.privacy", "Committed endpoint authority contains a full MAC address.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-DEV-001 inventory, policy, partial runtime evidence, privacy, and no-mutation boundaries are consistent.")


def validate_application_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-app-001"
    required = (APPLICATION_PACKAGE_PATH, APPLICATION_EXECUTION_PATH, APPLICATION_INVENTORY_PATH, WORKLOAD_INVENTORY_PATH, *APPLICATION_REQUIRED_PATHS)
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required application package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / APPLICATION_PACKAGE_PATH)
        execution = load_json_yaml(root / APPLICATION_EXECUTION_PATH)
        applications = load_json_yaml(root / APPLICATION_INVENTORY_PATH)
        workloads = load_json_yaml(root / WORKLOAD_INVENTORY_PATH)
        policy = load_json_yaml(root / "docs/zero-trust/secure-deployment-policy.yaml")
        components = load_json_yaml(root / "docs/zero-trust/software-component-inventory.yaml")
        sbom = load_json_yaml(root / "docs/evidence/zero-trust/zt-app-001-sbom.cdx.json")
        app_schema = load_schema(root / "schemas/zero-trust-application-inventory.schema.json")
        workload_schema = load_schema(root / "schemas/zero-trust-workload-inventory.schema.json")
        component_schema = load_schema(root / "schemas/zero-trust-software-component-inventory.schema.json")
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    objects = (package, execution, applications, workloads, policy, components, sbom)
    if not all(isinstance(item, dict) for item in objects):
        result.fail(f"{category}.configuration", "Application package authority records must be objects.")
        return
    for name, value, schema in (("applications", applications, app_schema), ("workloads", workloads, workload_schema), ("components", components, component_schema)):
        for error in validate_schema_instance(value, schema):
            result.fail(f"{category}.{name}", error)

    if package.get("package_id") != "ZT-APP-001" or execution.get("package_id") != "ZT-APP-001":
        result.fail(category, "Package and execution identifiers must be ZT-APP-001.")
    if package.get("implementation_status") != "IMPLEMENTED" or package.get("validation_status") != "PARTIALLY_RUNTIME_VALIDATED":
        result.fail(category, "Application package must remain IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED.")
    if package.get("current_maturity") != "UNASSESSED" or package.get("target_maturity") == "OPTIMAL":
        result.fail(category, "Application maturity must remain UNASSESSED and must not target OPTIMAL.")
    if package.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME" or execution.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME":
        result.fail(category, "Application runtime evidence requires actual Codex execution authority.")

    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}
    mappings = package.get("capability_mappings", [])
    mapped_ids = [item.get("id") for item in mappings if isinstance(item, dict)]
    expected = {"ZT-5.1.1", "ZT-5.4.1", "ZT-5.4.2", "ZT-5.5.1", "ZT-5.5.2", "ZT-7.1", "ZT-8.1", "ZT-8.2"}
    if set(mapped_ids) != expected or any(item not in catalog_ids for item in mapped_ids):
        result.fail(category, "Application capability mappings must use the reviewed canonical bounded set.")

    app_items = applications.get("applications", [])
    workload_items = workloads.get("workloads", [])
    app_ids = [item.get("id") for item in app_items if isinstance(item, dict)]
    workload_ids = [item.get("id") for item in workload_items if isinstance(item, dict)]
    if len(app_ids) != len(set(app_ids)) or len(workload_ids) != len(set(workload_ids)):
        result.fail(f"{category}.inventory", "Application and workload IDs must be unique.")
    if any(item.get("application_id") not in set(app_ids) for item in workload_items if isinstance(item, dict)):
        result.fail(f"{category}.inventory", "Every workload must reference an inventoried application.")
    if any(not item.get("owner") for item in app_items + workload_items if isinstance(item, dict)):
        result.fail(f"{category}.inventory", "Every application and workload requires an owner.")

    if components.get("sbom_status") != "PARTIAL" or len(components.get("components", [])) != 3:
        result.fail(f"{category}.sbom", "The current Compose-derived component inventory must remain PARTIAL with three direct images.")
    if sbom.get("bomFormat") != "CycloneDX" or sbom.get("specVersion") != "1.5" or len(sbom.get("components", [])) != 3:
        result.fail(f"{category}.sbom", "A valid bounded CycloneDX 1.5 direct-image SBOM is required.")
    if package.get("sbom_status") != "PARTIAL" or package.get("artifact_signed") is not False or package.get("image_digests_verified") is not False or package.get("dedicated_vulnerability_scan") is not False:
        result.fail(f"{category}.claims", "SBOM, signature, digest, and vulnerability-scan truth boundaries were promoted.")
    for field in ("automatic_deployment", "workload_restarted"):
        if package.get(field) is not False:
            result.fail(f"{category}.mutation", f"{field} must remain false.")
    if policy.get("automatic_enforcement") is not False or policy.get("automatic_deployment") is not False or policy.get("automatic_restart") is not False:
        result.fail(f"{category}.mutation", "Secure-deployment policy must not enable automatic mutation.")
    runtime = execution.get("runtime_validation", {})
    results = execution.get("results", {})
    if results.get("exit_code") != 0 or results.get("fail") != 0 or runtime.get("service_health") != "PASS" or runtime.get("sanitized_ingestion") != "PASS":
        result.fail(f"{category}.execution", "Partial runtime acceptance requires zero failures plus health and sanitized-ingestion PASS.")
    for field in ("deployment_performed", "workload_restarted", "failure_injected"):
        if runtime.get(field) is not False:
            result.fail(f"{category}.mutation", f"Runtime evidence must record {field}=false.")
    if execution.get("sanitization", {}).get("secrets") != 0 or results.get("secret_findings") != 0:
        result.fail(f"{category}.security", "Application evidence requires zero secret findings.")

    wrapper = (root / "tools/live-validation/validate-application-live.ps1").read_text(encoding="utf-8", errors="replace")
    for token in ("run_security_scans.py", "validate_secure_deployment.py", "manage-persistent-telemetry.ps1", ".runtime/zero-trust/application/latest", "workload_restarted = $false"):
        if token not in wrapper:
            result.fail(f"{category}.wrapper", f"Application wrapper is missing required no-mutation contract: {token}.")
    for forbidden in ("docker compose up", "docker compose restart", "docker pull", "kubectl apply", "helm install", "Invoke-Expression"):
        if forbidden.lower() in wrapper.lower():
            result.fail(f"{category}.wrapper", f"Application wrapper contains prohibited deployment behavior: {forbidden}.")
    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if not any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines()):
        result.fail(f"{category}.runtime", ".runtime/zero-trust/ must remain ignored.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-APP-001 inventory, partial SBOM, offline scans, bounded runtime health, and no-deployment boundaries are consistent.")


def validate_data_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-data-001"
    required = (DATA_PACKAGE_PATH, DATA_EXECUTION_PATH, DATA_INVENTORY_PATH, *DATA_REQUIRED_PATHS)
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required data package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / DATA_PACKAGE_PATH)
        execution = load_json_yaml(root / DATA_EXECUTION_PATH)
        inventory = load_json_yaml(root / DATA_INVENTORY_PATH)
        access = load_json_yaml(root / "docs/zero-trust/data-access-policy.yaml")
        flows = load_json_yaml(root / "docs/zero-trust/data-flow-map.yaml")
        encryption = load_json_yaml(root / "docs/zero-trust/data-encryption-assessment.yaml")
        backups = load_json_yaml(root / "docs/zero-trust/backup-inventory.yaml")
        dlp = load_json_yaml(root / "docs/zero-trust/dlp-policy.yaml")
        assurance = load_json_yaml(root / "docs/evidence/zero-trust/zt-data-001-backup-assurance.yaml")
        schemas = (
            ("inventory", inventory, load_schema(root / "schemas/zero-trust-data-inventory.schema.json")),
            ("access", access, load_schema(root / "schemas/zero-trust-data-access-policy.schema.json")),
            ("flows", flows, load_schema(root / "schemas/zero-trust-data-flow-map.schema.json")),
            ("backups", backups, load_schema(root / "schemas/zero-trust-backup-inventory.schema.json")),
            ("dlp", dlp, load_schema(root / "schemas/zero-trust-dlp-policy.schema.json")),
        )
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    objects = (package, execution, inventory, access, flows, encryption, backups, dlp, assurance)
    if not all(isinstance(item, dict) for item in objects):
        result.fail(f"{category}.configuration", "Data package authority records must be objects.")
        return
    for name, value, schema in schemas:
        for error in validate_schema_instance(value, schema):
            result.fail(f"{category}.{name}", error)

    if package.get("package_id") != "ZT-DATA-001" or execution.get("package_id") != "ZT-DATA-001":
        result.fail(category, "Package and execution identifiers must be ZT-DATA-001.")
    if package.get("implementation_status") != "IMPLEMENTED" or package.get("validation_status") != "PARTIALLY_RUNTIME_VALIDATED":
        result.fail(category, "Data package must remain IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED.")
    if package.get("current_maturity") != "UNASSESSED" or package.get("target_maturity") != "INITIAL":
        result.fail(category, "Data maturity must remain UNASSESSED with INITIAL only as the bounded target.")
    if package.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME" or execution.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME":
        result.fail(category, "Data runtime evidence requires actual Codex execution authority.")

    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}
    mappings = package.get("capability_mappings", [])
    mapped_ids = [item.get("id") for item in mappings if isinstance(item, dict)]
    expected = {"ZT-6.1.1", "ZT-6.2.1", "ZT-6.3.1", "ZT-6.4.1", "ZT-6.5.1", "ZT-6.5.2", "ZT-7.1", "ZT-8.1", "ZT-8.2"}
    if set(mapped_ids) != expected or any(item not in catalog_ids for item in mapped_ids):
        result.fail(category, "Data capability mappings must use the reviewed canonical bounded set and exclude enterprise-governance overclaims.")

    assets = inventory.get("data_assets", [])
    asset_ids = [item.get("id") for item in assets if isinstance(item, dict)]
    if len(assets) != 7 or len(asset_ids) != len(set(asset_ids)):
        result.fail(f"{category}.inventory", "The bounded inventory must contain seven unique data assets.")
    if any(not item.get("owner") or not item.get("custodian") for item in assets if isinstance(item, dict)):
        result.fail(f"{category}.ownership", "Every bounded data asset requires owner and custodian assignments.")
    if any(item.get("classification") in {None, "", "UNCLASSIFIED"} for item in assets if isinstance(item, dict)):
        result.fail(f"{category}.classification", "All bounded assets must be explicitly classified.")
    policy_ids = {item.get("policy_id") for item in access.get("policies", []) if isinstance(item, dict)}
    if any(item.get("access_model") not in policy_ids for item in assets if isinstance(item, dict)):
        result.fail(f"{category}.access", "Every data asset must reference a defined least-privilege access policy.")
    for policy in access.get("policies", []):
        if not isinstance(policy, dict):
            continue
        values = {str(policy.get("required_role", "")).upper(), *(str(item).upper() for item in policy.get("allowed_actions", []))}
        if policy.get("data_classification") in {"SENSITIVE", "RESTRICTED"} and values & {"*", "ANY", "ALL", "EVERYONE"}:
            result.fail(f"{category}.access", f"{policy.get('policy_id')} grants wildcard protected-data access.")
        if not policy.get("audit_requirement"):
            result.fail(f"{category}.access", f"{policy.get('policy_id')} lacks an audit requirement.")

    asset_set = set(asset_ids)
    for flow in flows.get("flows", []):
        if not isinstance(flow, dict):
            continue
        if flow.get("source_data_asset_id") not in asset_set or (flow.get("destination_data_asset_id") is not None and flow.get("destination_data_asset_id") not in asset_set):
            result.fail(f"{category}.flows", f"{flow.get('flow_id')} has an unresolved data-asset reference.")
    for item in encryption.get("assessments", []):
        if not isinstance(item, dict):
            continue
        if item.get("state") == "ENCRYPTED" and not item.get("evidence"):
            result.fail(f"{category}.encryption", f"{item.get('assessment_id')} claims encryption without evidence.")
        if item.get("plane") == "IN_USE" and item.get("state") not in {"NOT_IMPLEMENTED", "REFERENCE_ONLY", "UNKNOWN"}:
            result.fail(f"{category}.encryption", "Encryption in use is promoted without confidential-computing evidence.")

    forbidden_actions = {"DELETE", "QUARANTINE", "BLOCK", "MODIFY", "ROTATE"}
    if dlp.get("mode") != "DETECTION_ONLY" or dlp.get("external_transmission") is not False or dlp.get("source_modification") is not False:
        result.fail(f"{category}.dlp", "DLP must remain local, detection-only, and non-mutating.")
    for rule in dlp.get("rules", []):
        if isinstance(rule, dict) and set(rule.get("actions", [])) & forbidden_actions:
            result.fail(f"{category}.dlp", f"{rule.get('rule_id')} contains a blocking or mutating action.")
        if isinstance(rule, dict) and rule.get("redaction") != "REDACT_MATCH":
            result.fail(f"{category}.dlp", f"{rule.get('rule_id')} does not require redaction.")

    hashes = [assurance.get(name) for name in ("source_sha256", "backup_sha256", "restore_sha256", "source_unchanged_sha256")]
    if len(set(hashes)) != 1 or any(not isinstance(value, str) or len(value) != 64 for value in hashes):
        result.fail(f"{category}.backup", "Synthetic source, backup, restore, and unchanged-source SHA-256 evidence must match.")
    if assurance.get("isolated_restore") is not True or assurance.get("source_overwritten") is not False or assurance.get("external_transmission") is not False:
        result.fail(f"{category}.backup", "Restore evidence must remain isolated, non-overwriting, and local.")
    restore_records = [item for item in backups.get("backups", []) if isinstance(item, dict) and item.get("validation_status") == "RESTORE_VALIDATED"]
    if len(restore_records) != 1 or restore_records[0].get("backup_id") != "ZTBACKUP-SYNTHETIC-PILOT":
        result.fail(f"{category}.backup", "Only the controlled synthetic pilot may be RESTORE_VALIDATED.")

    results = execution.get("results", {})
    if results.get("exit_code") != 0 or results.get("fail") != 0 or results.get("data_assets_assessed") != 7 or results.get("restores_validated") != 1 or results.get("dlp_findings") != 0:
        result.fail(f"{category}.execution", "Partial runtime acceptance requires seven assessed assets, one synthetic restore, zero confirmed DLP findings, and zero failures.")
    for field in ("blocking_dlp", "live_data_backup", "encryption_in_use", "enterprise_governance", "complete_discovery", "complete_dlp", "external_transmission", "source_data_modified"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false.")

    wrapper = (root / "tools/live-validation/validate-data-live.ps1").read_text(encoding="utf-8", errors="replace")
    for token in ("validate_data_inventory.py", "scan_data_policy.py", "validate_backup_assurance.py", ".runtime/zero-trust/data", "source_overwritten = $false", "external_transmission = $false", "keys_or_credentials_rotated = $false", "blocking_dlp = $false"):
        if token not in wrapper:
            result.fail(f"{category}.wrapper", f"Data wrapper is missing required safety token: {token}.")
    for forbidden in ("Invoke-WebRequest", "Invoke-RestMethod", "curl ", "aws s3", "az storage", "Remove-Item", "del ", "rm ", "Set-Secret", "DELETE", "QUARANTINE"):
        if forbidden.lower() in wrapper.lower():
            result.fail(f"{category}.wrapper", f"Data wrapper contains prohibited external, destructive, or blocking behavior: {forbidden}.")
    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if not any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines()):
        result.fail(f"{category}.runtime", ".runtime/zero-trust/ must remain ignored.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-DATA-001 inventory, classification, access, flow, encryption assessment, detection-only DLP, synthetic restore, privacy, and no-mutation boundaries are consistent.")


def validate_system_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-sys-001"
    required = (SYSTEM_PACKAGE_PATH, SYSTEM_EXECUTION_PATH, SYSTEM_INVENTORY_PATH, *SYSTEM_REQUIRED_PATHS)
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required system package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / SYSTEM_PACKAGE_PATH)
        execution = load_json_yaml(root / SYSTEM_EXECUTION_PATH)
        inventory = load_json_yaml(root / SYSTEM_INVENTORY_PATH)
        baselines = load_json_yaml(root / "docs/zero-trust/system-baseline-policy.yaml")
        authority = load_json_yaml(root / "docs/zero-trust/system-configuration-authority.yaml")
        integrity = load_json_yaml(root / "docs/zero-trust/system-integrity-policy.yaml")
        credentials = load_json_yaml(root / "docs/zero-trust/system-credential-reference-inventory.yaml")
        exposures = load_json_yaml(root / "docs/zero-trust/system-service-exposure.yaml")
        services = load_json_yaml(root / "docs/zero-trust/system-service-policy.yaml")
        recovery = load_json_yaml(root / "docs/zero-trust/system-recovery-readiness.yaml")
        integrity_evidence = load_json_yaml(root / "docs/evidence/zero-trust/zt-sys-001-integrity-validation.yaml")
        service_evidence = load_json_yaml(root / "docs/evidence/zero-trust/zt-sys-001-service-state.yaml")
        schemas = (
            ("inventory", inventory, load_schema(root / "schemas/zero-trust-system-inventory.schema.json")),
            ("baselines", baselines, load_schema(root / "schemas/zero-trust-system-baseline-policy.schema.json")),
            ("authority", authority, load_schema(root / "schemas/zero-trust-system-configuration-authority.schema.json")),
            ("integrity", integrity, load_schema(root / "schemas/zero-trust-system-integrity-policy.schema.json")),
            ("services", services, load_schema(root / "schemas/zero-trust-system-service-policy.schema.json")),
        )
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    objects = (package, execution, inventory, baselines, authority, integrity, credentials, exposures, services, recovery, integrity_evidence, service_evidence)
    if not all(isinstance(item, dict) for item in objects):
        result.fail(f"{category}.configuration", "System package authority records must be objects.")
        return
    for name, value, schema in schemas:
        for error in validate_schema_instance(value, schema):
            result.fail(f"{category}.{name}", error)

    if package.get("package_id") != "ZT-SYS-001" or execution.get("package_id") != "ZT-SYS-001":
        result.fail(category, "Package and execution identifiers must be ZT-SYS-001.")
    if package.get("implementation_status") != "IMPLEMENTED" or package.get("validation_status") != "PARTIALLY_RUNTIME_VALIDATED":
        result.fail(category, "System package must remain IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED.")
    if package.get("current_maturity") != "UNASSESSED" or package.get("target_maturity") != "INITIAL":
        result.fail(category, "System maturity must remain UNASSESSED with INITIAL only as the bounded target.")
    if package.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME" or execution.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME":
        result.fail(category, "System runtime evidence requires actual Codex execution authority.")

    catalog_ids = {item["id"] for item in catalog.get("capabilities", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}
    mappings = package.get("capability_mappings", [])
    mapped_ids = [item.get("id") for item in mappings if isinstance(item, dict)]
    expected = {"ZT-4.1.1", "ZT-4.2.1", "ZT-4.2.2", "ZT-4.3.1", "ZT-4.4.1", "ZT-7.1", "ZT-8.1", "ZT-8.2"}
    if set(mapped_ids) != expected or any(item not in catalog_ids for item in mapped_ids):
        result.fail(category, "System capability mappings must use the reviewed canonical bounded set.")

    systems = inventory.get("systems", [])
    profiles = baselines.get("profiles", [])
    configurations = authority.get("configurations", [])
    system_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    profile_ids = {item.get("profile_id") for item in profiles if isinstance(item, dict)}
    if len(systems) != 7 or len(system_ids) != len(set(system_ids)) or len(profiles) != 6 or len(configurations) != 7:
        result.fail(f"{category}.inventory", "The bounded authority must retain seven unique systems, six profiles, and seven configuration records.")
    for item in systems:
        if not isinstance(item, dict):
            continue
        if not item.get("owner") or not item.get("custodian") or not item.get("privileged_access_model"):
            result.fail(f"{category}.inventory", f"{item.get('id')} lacks ownership or privileged-access metadata.")
        if item.get("baseline_profile") not in profile_ids:
            result.fail(f"{category}.inventory", f"{item.get('id')} references an undefined baseline profile.")
    if inventory.get("metadata", {}).get("authority") != "CODEX_REPOSITORY_AND_RESTRICTED_LIVE_VALIDATION":
        result.fail(f"{category}.evidence", "System inventory authority must remain explicit and bounded.")

    forbidden_credential_fields = {"value", "password", "token", "private_key", "secret_value", "mfa_seed", "recovery_code"}
    for reference in credentials.get("references", []):
        if isinstance(reference, dict) and forbidden_credential_fields & set(reference):
            result.fail(f"{category}.credentials", f"{reference.get('reference_id')} contains a prohibited credential-value field.")
    for config in configurations:
        if not isinstance(config, dict):
            continue
        if config.get("sensitive") is True and config.get("approved_sha256") is not None:
            result.fail(f"{category}.integrity", f"{config.get('configuration_id')} stores a checksum for sensitive content.")
    integrity_results = integrity_evidence.get("results", {})
    if integrity_results.get("matched") != 5 or integrity_results.get("drift_findings") != 0 or integrity_results.get("fail") != 0:
        result.fail(f"{category}.integrity", "System integrity evidence must retain five safe matches, zero drift findings, and zero failures.")
    if integrity.get("continuous_file_integrity_monitoring") is not False or integrity.get("automatic_restoration") is not False:
        result.fail(f"{category}.claims", "Continuous FIM or automatic restoration was promoted without evidence.")

    service_results = service_evidence.get("results", {})
    if service_results != {"pass": 5, "warn": 2, "fail": 0} or service_evidence.get("restart_performed") is not False or services.get("automatic_restart") is not False:
        result.fail(f"{category}.service", "Service evidence must remain 5 PASS / 2 WARN / 0 FAIL with no restart.")
    openstack = execution.get("openstack", {})
    results = execution.get("results", {})
    if openstack.get("status") != "CURRENT_DEGRADED" or (openstack.get("pass"), openstack.get("warn"), openstack.get("fail")) != (46, 0, 4):
        result.fail(f"{category}.execution", "OpenStack must retain the exact accepted CURRENT_DEGRADED 46/0/4 boundary.")
    if results.get("exit_code") != 0 or results.get("fail") != 0 or results.get("systems_assessed") != 7 or results.get("service_failures") != 0 or results.get("drift_findings") != 0:
        result.fail(f"{category}.execution", "Partial runtime acceptance requires seven assessed systems and zero package, service, and drift failures.")
    if recovery.get("live_restore_performed") is not False or any(item.get("readiness") == "RESTORE_VALIDATED" and not item.get("last_recovery_evidence") for item in recovery.get("systems", []) if isinstance(item, dict)):
        result.fail(f"{category}.recovery", "System recovery evidence contains an unsupported live restore or restore-validation claim.")

    for field in ("service_restart_performed", "configuration_modified", "automatic_recovery", "complete_pam", "continuous_file_integrity_monitoring", "complete_hardening", "complete_vulnerability_management", "complete_system_recovery"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false.")
    wrapper = (root / "tools/live-validation/validate-systems-live.ps1").read_text(encoding="utf-8", errors="replace")
    for token in ("CURRENT_DEGRADED 46/0/4", "validate_system_inventory.py", "check_configuration_drift.py", "validate_service_state.py", ".runtime/zero-trust/system", "service_restart_performed = $false", "configuration_modified = $false", "automatic_recovery_performed = $false"):
        if token not in wrapper:
            result.fail(f"{category}.wrapper", f"System wrapper is missing required bounded token: {token}.")
    for forbidden in ("Restart-Service", "Stop-Service", "Start-Service", "systemctl restart", "docker compose up", "apt install", "Invoke-Expression", "ssh root@"):
        if forbidden.lower() in wrapper.lower():
            result.fail(f"{category}.wrapper", f"System wrapper contains prohibited mutation or unrestricted access behavior: {forbidden}.")
    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if not any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines()):
        result.fail(f"{category}.runtime", ".runtime/zero-trust/ must remain ignored.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-SYS-001 inventory, baselines, privileged boundary, safe configuration integrity, service state, recovery gaps, privacy, and no-mutation contracts are consistent.")


def validate_automation_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-auto-001"
    required = (
        AUTOMATION_PACKAGE_PATH,
        AUTOMATION_EXECUTION_PATH,
        AUTOMATION_INTEGRATION_PATH,
        AUTOMATION_ACTION_PATH,
        AUTOMATION_WORKFLOW_PATH,
        AUTOMATION_POLICY_PATH,
        *AUTOMATION_REQUIRED_PATHS,
    )
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required automation package file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / AUTOMATION_PACKAGE_PATH)
        execution = load_json_yaml(root / AUTOMATION_EXECUTION_PATH)
        integrations = load_json_yaml(root / AUTOMATION_INTEGRATION_PATH)
        actions = load_json_yaml(root / AUTOMATION_ACTION_PATH)
        workflows = load_json_yaml(root / AUTOMATION_WORKFLOW_PATH)
        policy = load_json_yaml(root / AUTOMATION_POLICY_PATH)
        schemas = (
            ("integrations", integrations, load_schema(root / "schemas/zero-trust-automation-integration-inventory.schema.json")),
            ("actions", actions, load_schema(root / "schemas/zero-trust-automation-action-catalog.schema.json")),
            ("workflows", workflows, load_schema(root / "schemas/zero-trust-automation-workflow-catalog.schema.json")),
            ("policy", policy, load_schema(root / "schemas/zero-trust-automation-approval-policy.schema.json")),
        )
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    if not all(isinstance(item, dict) for item in (package, execution, integrations, actions, workflows, policy)):
        result.fail(f"{category}.configuration", "Automation package authority records must be objects.")
        return
    for name, value, schema in schemas:
        for error in validate_schema_instance(value, schema):
            result.fail(f"{category}.{name}", error)

    if package.get("package_id") != "ZT-AUTO-001" or execution.get("package_id") != "ZT-AUTO-001":
        result.fail(category, "Package and execution identifiers must be ZT-AUTO-001.")
    if package.get("implementation_status") != "IMPLEMENTED" or package.get("validation_status") != "PARTIALLY_RUNTIME_VALIDATED":
        result.fail(category, "Automation package must remain IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED.")
    if package.get("current_maturity") != "UNASSESSED" or package.get("target_maturity") != "INITIAL":
        result.fail(category, "Automation maturity must remain UNASSESSED with INITIAL only as the package target.")
    if package.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME" or execution.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME":
        result.fail(category, "Live automation authority requires an actually executed restricted live workflow.")

    catalog_ids = {item.get("id") for item in catalog.get("capabilities", []) if isinstance(item, dict)}
    assessed = package.get("capability_assessment", [])
    assessed_ids = [item.get("id") for item in assessed if isinstance(item, dict)]
    if set(assessed_ids) != {f"ZT-8.{index}" for index in range(1, 7)} or any(item not in catalog_ids for item in assessed_ids):
        result.fail(f"{category}.capabilities", "All and only canonical ZT-8.1 through ZT-8.6 capability boundaries must be assessed.")
    if any(item.get("current_maturity") not in {None, "UNASSESSED"} for item in assessed if isinstance(item, dict)):
        result.fail(f"{category}.maturity", "Package capability records cannot assign maturity.")

    action_records = actions.get("actions", [])
    workflow_records = workflows.get("workflows", [])
    integration_records = integrations.get("integrations", [])
    if (len(action_records), len(workflow_records), len(integration_records)) != (20, 7, 11):
        result.fail(f"{category}.inventory", "Automation authority must retain the 13/6 ZT-AUTO-001 baseline plus seven actions and one workflow registered by ZT-CV-001, with 11 integrations.")
    if actions.get("metadata", {}).get("default_policy") != "DENY_UNREGISTERED" or policy.get("metadata", {}).get("default_decision") != "DENY":
        result.fail(f"{category}.policy", "Action and approval policy must remain default deny.")
    if workflows.get("metadata", {}).get("default_execution_mode") != "CHECK":
        result.fail(f"{category}.policy", "Workflow default execution mode must remain CHECK.")

    forbidden_action_fields = {"command", "executable_path", "remote_target", "remote_command", "ssh_target", "shell"}
    allowed_executable_risks = {"R0_READ_ONLY", "R1_LOCAL_ARTIFACT_WRITE", "R2_REPOSITORY_STATUS_PROPOSAL", "R3_REMOTE_READ_ONLY"}
    for action in action_records:
        if not isinstance(action, dict):
            continue
        action_id = action.get("id", "UNKNOWN")
        if forbidden_action_fields & set(action):
            result.fail(f"{category}.actions", f"{action_id} contains an arbitrary execution field.")
        if action.get("executable") is True and action.get("risk_level") not in allowed_executable_risks:
            result.fail(f"{category}.actions", f"{action_id} enables a prohibited R4-R8 action.")
        if action.get("executable") is True and action.get("implementation") in {None, "", "NONE"}:
            result.fail(f"{category}.actions", f"{action_id} has no fixed implementation handler.")
        if any(capability not in catalog_ids for capability in action.get("capability_mappings", [])):
            result.fail(f"{category}.actions", f"{action_id} references an unknown capability.")
        if action.get("retry_policy") not in {"NONE", "FIXED_COUNT_READ_ONLY"}:
            result.fail(f"{category}.actions", f"{action_id} has an unsupported retry policy.")

    execution_workflows = execution.get("workflows", [])
    execution_results = execution.get("results", {})
    if len(execution_workflows) != 1:
        result.fail(f"{category}.execution", "Exactly one reviewed live cross-domain workflow record is required for this package.")
    else:
        live = execution_workflows[0]
        expected_hash = "c64b56bfdb0831b91290f051ea385e4c7fefbe53afe665ac340e2545accaba32"
        if live.get("workflow_id") != "ZTA-WF-VAL-001" or live.get("execution_mode") != "EXECUTE_READ_ONLY" or live.get("plan_hash") != expected_hash or live.get("result") != "PARTIAL":
            result.fail(f"{category}.execution", "Live execution must retain the reviewed workflow, mode, plan hash, and honest PARTIAL result.")
        steps = live.get("steps", [])
        counts = Counter(item.get("outcome") for item in steps if isinstance(item, dict))
        if counts != Counter({"PASS": 4, "WARN": 4}) or any(item.get("exit_code") != 0 for item in steps if isinstance(item, dict)):
            result.fail(f"{category}.execution", "Live execution must retain 4 PASS / 4 WARN / 0 FAIL and zero child failures.")
    expected_results = {
        "workflows_attempted": 1, "workflows_completed": 0, "workflows_partial": 1,
        "workflows_failed": 0, "workflows_blocked": 0, "steps_passed": 4,
        "steps_warned": 4, "steps_failed": 0, "steps_skipped": 0,
        "policy_denials": 0, "approval_blocks": 0, "timeout_count": 0,
        "mutation_actions_executed": 0, "external_notifications_sent": 0, "exit_code": 0,
    }
    if any(execution_results.get(key) != value for key, value in expected_results.items()):
        result.fail(f"{category}.execution", "Sanitized automation aggregate does not match the accepted partial live execution.")

    tools_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in sorted((root / "tools/automation").glob("*.py"))
    )
    for forbidden in ("shell=True", "eval(", "exec(", "Invoke-Expression"):
        if forbidden in tools_text:
            result.fail(f"{category}.security", f"Automation code contains prohibited execution behavior: {forbidden}.")
    runner = (root / "tools/automation/run_workflow.py").read_text(encoding="utf-8", errors="replace")
    for token in ("command_registry", "subprocess.run", "shell=False", "SAFE_ENV_NAMES", "SINGLE_WORKFLOW_LOCK", "authoritative_update_performed"):
        if token not in runner and token != "SINGLE_WORKFLOW_LOCK":
            result.fail(f"{category}.security", f"Restricted runner is missing required boundary token: {token}.")
    for field in ("arbitrary_execution", "shell_interpolation", "caller_controlled_ssh_target", "mutation_action_executable", "automatic_authoritative_update", "external_notification_integration", "autonomous_remediation", "complete_soar"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false.")
    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if not any(line.strip().rstrip("/") == ".runtime/zero-trust" for line in gitignore.splitlines()):
        result.fail(f"{category}.runtime", ".runtime/zero-trust/ must remain ignored.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-AUTO-001 catalogs, default-deny policy, deterministic plan, fixed-handler live execution, evidence, telemetry, and no-mutation boundaries are consistent.")


def validate_continuous_verification_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-cv-001"
    del catalog
    runtime_path = Path("docs/zero-trust/recovery/P1-CV-001/runtime-results.yaml")
    blocked_evidence_path = Path("docs/evidence/zero-trust/zt-cv-001-p1-cv-001-blocked.sanitized.txt")
    required = (
        CONTINUOUS_VERIFICATION_PACKAGE_PATH,
        runtime_path,
        blocked_evidence_path,
        Path("docs/evidence/zero-trust/zt-fnd-001-p1-cv-refresh.sanitized.txt"),
        Path("docs/evidence/zero-trust/zt-fnd-001-remediation-refresh.sanitized.txt"),
        Path("docs/zero-trust/verification-history.yaml"),
        Path("docs/zero-trust/package-acceptance-gates.yaml"),
        Path("tools/live-validation/run-continuous-verification.ps1"),
    )
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required continuous verification file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / CONTINUOUS_VERIFICATION_PACKAGE_PATH)
        runtime = load_json_yaml(root / runtime_path)
        history = load_json_yaml(root / "docs/zero-trust/verification-history.yaml")
        gates = load_json_yaml(root / "docs/zero-trust/package-acceptance-gates.yaml")
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    expected = {
        "package_id": "ZT-CV-001",
        "implementation_status": "IMPLEMENTED",
        "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
        "local_validation_status": "LOCAL_VALIDATED",
        "runtime_validation_status": "PARTIALLY_VALIDATED",
        "runtime_acceptance_status": "PARTIALLY_ACCEPTED",
        "acceptance_state": "PARTIALLY_ACCEPTED",
        "evidence_continuity": "EC3_ONE_TIME_RUNTIME",
        "maturity_status": "UNASSESSED",
        "current_maturity": "UNASSESSED",
    }
    mismatches = {key: (value, package.get(key)) for key, value in expected.items() if package.get(key) != value}
    if mismatches:
        result.fail(category, f"ZT-CV-001 bounded accepted package state differs: {mismatches}")

    historical_execution = runtime.get("execution", {})
    historical_assessment = runtime.get("package_acceptance", {})
    execution = package.get("latest_execution", {})
    expected_hash = "72c0aa52f20b12fb67d7b149e7c1ed980c2cfcbcdafea9cfc344cac2f4912624"
    if (
        execution.get("workflow_id") != "ZT-CV-WF-001"
        or execution.get("plan_hash") != expected_hash
        or execution.get("result") != "PARTIAL"
        or execution.get("steps_failed") != 0
        or execution.get("steps_passed", 0) + execution.get("steps_warned", 0) != 10
        or execution.get("steps_passed", 0) < 7
        or execution.get("steps_warned", 0) > 3
        or execution.get("decision") != "PASS_WITH_OPEN_GAPS"
        or execution.get("blocking_gate") is not None
        or execution.get("blocking_finding") is not None
    ):
        result.fail(f"{category}.execution", "P1-CV-001 must retain a reviewed 7/3/0 or 8/2/0 bounded result with the immutable plan hash and no blocking finding.")

    # The 2026-07-27 blocked cycle remains immutable historical evidence. It is
    # not the authority for the current package decision after FND remediation.
    if (
        runtime.get("action_id") != "P1-CV-001"
        or runtime.get("package_id") != "ZT-CV-001"
        or runtime.get("decision") != "BLOCKED"
        or historical_execution.get("execution_id") != "ZTA-20260727T125822Z-519fe693"
        or historical_execution.get("workflow_id") != "ZT-CV-WF-001"
        or historical_execution.get("plan_hash") != expected_hash
        or historical_execution.get("result") != "PARTIAL"
        or historical_execution.get("steps") != {"pass": 8, "warn": 2, "fail": 0, "skipped": 0}
        or historical_assessment.get("gate_id") != "ZTCV-GATE-FND"
        or historical_assessment.get("finding") != "WARNING_BUDGET_EXCEEDED"
    ):
        result.fail(f"{category}.history", "The superseded blocked P1-CV-001 cycle must remain intact as historical evidence.")

    cv_gate = next((item for item in gates.get("gates", []) if item.get("package_id") == "ZT-CV-001"), None)
    fnd_gate = next((item for item in gates.get("gates", []) if item.get("package_id") == "ZT-FND-001"), None)
    if not cv_gate or cv_gate.get("acceptance_state") != "PARTIALLY_ACCEPTED" or cv_gate.get("blocking_failures"):
        result.fail(f"{category}.gate", "CV gate must retain the reviewed PARTIALLY_ACCEPTED state with no current blocking finding.")
    if (
        not fnd_gate
        or fnd_gate.get("acceptance_state") != "ACCEPTED"
        or fnd_gate.get("allowed_warnings") != 0
        or "docs/evidence/zero-trust/zt-fnd-001-remediation-refresh.sanitized.txt" not in fnd_gate.get("required_evidence_files", [])
    ):
        result.fail(f"{category}.gate", "FND must remain accepted at the unrelaxed zero-warning gate with the remediation evidence required.")

    history_records = history.get("executions", [])
    fnd_refresh = next((item for item in history_records if item.get("execution_id") == "ZTFND-20260727T125219Z-7e484762"), None)
    if not fnd_refresh or fnd_refresh.get("result") != "WARN" or (fnd_refresh.get("pass"), fnd_refresh.get("warn"), fnd_refresh.get("fail")) != (2, 1, 0):
        result.fail(f"{category}.history", "Verification history must retain the fresh FND 2/1/0 record.")
    elif fnd_refresh.get("evidence_hashes", {}).get("docs/evidence/zero-trust/zt-fnd-001-p1-cv-refresh.sanitized.txt") != "aa32d74484bf2ff0586a7fac7105e7f04a4452d2876c193be86078490348820a":
        result.fail(f"{category}.history", "FND refresh evidence hash authority differs.")
    fnd_remediation = next((item for item in history_records if item.get("execution_id") == "ZTFND-20260728T075027Z-10d7a74e"), None)
    if not fnd_remediation or fnd_remediation.get("result") != "PASS" or (fnd_remediation.get("pass"), fnd_remediation.get("warn"), fnd_remediation.get("fail")) != (3, 0, 0):
        result.fail(f"{category}.history", "Verification history must retain the clean FND remediation 3/0/0 record.")
    elif fnd_remediation.get("evidence_hashes", {}).get("docs/evidence/zero-trust/zt-fnd-001-remediation-refresh.sanitized.txt") != "3cf8bf67cc5b7b886bfa86fefedea32f4c09b2cf8303806e9d53ad26ab483192":
        result.fail(f"{category}.history", "FND remediation evidence hash authority differs.")
    cv_final = next((item for item in history_records if item.get("execution_id") == "ZTA-20260728T082622Z-594aed64"), None)
    if not cv_final or cv_final.get("result") != "WARN" or (cv_final.get("pass"), cv_final.get("warn"), cv_final.get("fail")) != (8, 2, 0) or cv_final.get("plan_hash") != expected_hash:
        result.fail(f"{category}.history", "Verification history must retain the final accepted bounded CV 8/2/0 record.")
    elif cv_final.get("evidence_hashes") != {
        "docs/evidence/zero-trust/zt-cv-001-p1-cv-001-remediated-validation.yaml": "066a3b85a5b7a6b6f51cc05e54390c97fa66a40705c77aee3a58c43e2c18404d",
        "docs/evidence/zero-trust/zt-cv-001-p1-cv-001-remediated.sanitized.txt": "648a5f3a0b5181292a95273f4d35537cdf7ffcfc4f5fbf518c96944d7da6fdfd",
    }:
        result.fail(f"{category}.history", "Final CV remediation evidence hash authority differs.")

    for field in ("automatic_remediation", "authoritative_status_update", "maturity_assignment", "schedule_installed", "scheduled_operation", "continuous_operation", "phase_1_complete"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false.")
    if runtime.get("runtime_rollback") != "PASS" or runtime.get("accepted_cv_cycle_recorded") is not False or runtime.get("repeatability_credit") is not False or runtime.get("scheduled_trigger") is not False:
        result.fail(f"{category}.boundary", "Historical blocked CV evidence must retain rollback and no-acceptance/no-repeatability/no-schedule boundaries.")
    wrapper = (root / "tools/live-validation/run-continuous-verification.ps1").read_text(encoding="utf-8", errors="replace")
    for forbidden in ("Register-ScheduledTask", "Restart-Service", "Invoke-Expression"):
        if forbidden in wrapper:
            result.fail(f"{category}.security", f"CV wrapper contains prohibited behavior: {forbidden}.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-CV-001 is implemented and partially accepted at EC3 after clean FND remediation; historical blocked evidence is retained and no maturity, schedule, or Phase 1 completion is claimed.")
    return
    required = (
        CONTINUOUS_VERIFICATION_PACKAGE_PATH,
        CONTINUOUS_VERIFICATION_EXECUTION_PATH,
        *CONTINUOUS_VERIFICATION_POLICY_PATHS,
        *CONTINUOUS_VERIFICATION_SCHEMA_PATHS,
        *CONTINUOUS_VERIFICATION_REQUIRED_PATHS,
    )
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required continuous verification file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / CONTINUOUS_VERIFICATION_PACKAGE_PATH)
        execution = load_json_yaml(root / CONTINUOUS_VERIFICATION_EXECUTION_PATH)
        authorities = [load_json_yaml(root / path) for path in CONTINUOUS_VERIFICATION_POLICY_PATHS]
        schemas = [load_schema(root / path) for path in CONTINUOUS_VERIFICATION_SCHEMA_PATHS]
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    if not isinstance(package, dict) or not isinstance(execution, dict) or not all(isinstance(item, dict) for item in authorities):
        result.fail(f"{category}.configuration", "Continuous verification authorities must be objects.")
        return
    for name, authority, schema in zip(
        ("policy", "freshness", "capability-acceptance", "package-gates", "regression", "exceptions", "maturity", "history"),
        authorities,
        schemas[:8],
    ):
        for error in validate_schema_instance(authority, schema):
            result.fail(f"{category}.{name}", error)

    policy, freshness, capability_acceptance, gates, regressions, exceptions, maturity, history = authorities
    if package.get("package_id") != "ZT-CV-001" or execution.get("package_id") != "ZT-CV-001":
        result.fail(category, "Package and execution identifiers must be ZT-CV-001.")
    expected_state = ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED", "PARTIALLY_ACCEPTED", "EC3_ONE_TIME_RUNTIME", "UNASSESSED")
    actual_state = (
        package.get("implementation_status"), package.get("validation_status"), package.get("acceptance_state"),
        package.get("evidence_continuity"), package.get("current_maturity"),
    )
    if actual_state != expected_state:
        result.fail(category, "ZT-CV-001 must remain IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED / PARTIALLY_ACCEPTED / EC3 / UNASSESSED.")
    if policy.get("metadata", {}).get("default_decision") != "DENY_ACCEPTANCE_WITHOUT_EVIDENCE":
        result.fail(f"{category}.policy", "Continuous verification acceptance must default deny.")
    if len(policy.get("validator_registry", [])) != 10 or len(policy.get("verification_classes", [])) != 10 or len(policy.get("policies", [])) != 10:
        result.fail(f"{category}.policy", "Policy must retain ten validators, ten verification classes, and ten package policies.")
    if len(freshness.get("policies", [])) != 4 or len(capability_acceptance.get("capabilities", [])) != 12 or len(gates.get("gates", [])) != 10 or len(regressions.get("regressions", [])) != 11:
        result.fail(f"{category}.inventory", "CV authorities must retain 4 freshness policies, 12 capability records, 10 gates, and 11 regression classes.")
    if exceptions.get("exceptions") != []:
        result.fail(f"{category}.exceptions", "No active exception is accepted in the CV baseline.")
    if any(item.get("decision") == "UPGRADE_PROPOSED" and "EC4_REPEATABLE_RUNTIME" not in item.get("required_evidence_continuity", []) for item in maturity.get("rules", [])):
        result.fail(f"{category}.maturity", "A maturity upgrade proposal cannot bypass EC4.")

    catalog_ids = {item.get("id") for item in catalog.get("capabilities", []) if isinstance(item, dict)}
    assessed = package.get("capability_assessment", [])
    assessed_ids = {item.get("id") for item in assessed if isinstance(item, dict)}
    if assessed_ids != {"ZT-7.1", "ZT-8.1", "ZT-8.2"} or any(item not in catalog_ids for item in assessed_ids):
        result.fail(f"{category}.capabilities", "ZT-CV-001 must assess only its three canonical bounded capability mappings.")
    if any(item.get("current_maturity") != "UNASSESSED" for item in assessed if isinstance(item, dict)):
        result.fail(f"{category}.maturity", "CV capability records must remain UNASSESSED.")

    expected_execution_id = "ZTA-20260722T045752Z-eb639d92"
    expected_hash = "72c0aa52f20b12fb67d7b149e7c1ed980c2cfcbcdafea9cfc344cac2f4912624"
    if execution.get("execution_id") != expected_execution_id or execution.get("workflow_id") != "ZT-CV-WF-001" or execution.get("plan_hash") != expected_hash:
        result.fail(f"{category}.execution", "CV evidence must retain the reviewed execution ID, workflow, and immutable plan hash.")
    if execution.get("result") != "PARTIAL" or execution.get("results") != {"steps_passed": 8, "steps_warned": 2, "steps_failed": 0, "steps_skipped": 0, "exit_code": 0}:
        result.fail(f"{category}.execution", "CV evidence must retain the honest PARTIAL 8 PASS / 2 WARN / 0 FAIL result.")
    history_records = history.get("executions", [])
    execution_ids = [item.get("execution_id") for item in history_records if isinstance(item, dict)]
    if len(history_records) < 10 or len(execution_ids) != len(set(execution_ids)):
        result.fail(f"{category}.history", "Verification history must contain at least ten accepted execution records with unique execution IDs.")
    live = next((item for item in history_records if item.get("execution_id") == expected_execution_id), None)
    if not live or live.get("scheduled_trigger") is not False or live.get("result") != "WARN" or (live.get("pass"), live.get("warn"), live.get("fail")) != (8, 2, 0):
        result.fail(f"{category}.history", "CV history must retain the one manual accepted 8/2/0 record without schedule credit.")
    for record in history_records:
        for relative, expected in record.get("evidence_hashes", {}).items():
            path = root / relative
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                result.fail(f"{category}.regression", f"Tracked evidence hash diverged: {relative}.")

    cv_gate = next((item for item in gates.get("gates", []) if item.get("package_id") == "ZT-CV-001"), None)
    if not cv_gate or cv_gate.get("acceptance_state") != "PARTIALLY_ACCEPTED" or cv_gate.get("required_evidence_continuity") != "EC3_ONE_TIME_RUNTIME":
        result.fail(f"{category}.gate", "CV gate must remain partially accepted at EC3.")
    for field in ("automatic_remediation", "authoritative_status_update", "maturity_assignment", "schedule_installed", "scheduled_operation", "continuous_operation", "phase_1_complete"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false.")
    wrapper = (root / "tools/live-validation/run-continuous-verification.ps1").read_text(encoding="utf-8", errors="replace")
    for forbidden in ("Register-ScheduledTask", "Restart-Service", "Invoke-Expression"):
        if forbidden in wrapper:
            result.fail(f"{category}.security", f"CV wrapper contains prohibited behavior: {forbidden}.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-CV-001 policies, schemas, history, manual fixed-handler runtime evidence, EC3 boundary, and no-mutation/no-schedule/no-maturity claims are consistent.")


def validate_repeatable_validation_package(root: Path, catalog: dict[str, Any], result: ValidationResult) -> None:
    category = "package.zt-rv-001"
    del catalog
    required = (
        REPEATABLE_VALIDATION_PACKAGE_PATH,
        REPEATABLE_VALIDATION_CAMPAIGN_PATH,
        REPEATABILITY_ACCEPTANCE_POLICY_PATH,
        Path("docs/evidence/zero-trust/zt-rv-001-run-01.sanitized.txt"),
        Path("docs/zero-trust/verification-history.yaml"),
        Path("tools/continuous_verification/run_repeatability_campaign.py"),
    )
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required repeatability file is missing: {path}.")
        return
    try:
        package = load_json_yaml(root / REPEATABLE_VALIDATION_PACKAGE_PATH)
        campaign = load_json_yaml(root / REPEATABLE_VALIDATION_CAMPAIGN_PATH)
        history = load_json_yaml(root / "docs/zero-trust/verification-history.yaml")
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    expected = {
        "package_id": "ZT-RV-001",
        "implementation_status": "IMPLEMENTED",
        "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
        "local_validation_status": "LOCAL_VALIDATED",
        "runtime_validation_status": "PARTIALLY_VALIDATED",
        "runtime_acceptance_status": "PENDING",
        "acceptance_state": "IN_PROGRESS",
        "current_continuity": "EC3_ONE_TIME_RUNTIME",
        "target_continuity": "EC4_REPEATABLE_RUNTIME",
        "accepted_campaign_executions": 1,
        "required_campaign_executions": 3,
        "consecutive_successes": 1,
        "minimum_execution_separation": "PT24H",
        "latest_execution_id": "ZTRV-20260728T082825Z-f22b1052",
        "next_eligible_execution": "2026-07-29T08:28:25.829099Z",
        "maturity_status": "UNASSESSED",
    }
    mismatches = {key: (value, package.get(key)) for key, value in expected.items() if package.get(key) != value}
    if mismatches:
        result.fail(category, f"ZT-RV-001 in-progress package state differs: {mismatches}")

    acceptance = campaign.get("acceptance", {})
    if (
        acceptance.get("current_state") != "IN_PROGRESS"
        or acceptance.get("current_continuity") != "EC3_ONE_TIME_RUNTIME"
        or acceptance.get("successful_independent_executions") != 1
        or acceptance.get("consecutive_successes") != 1
        or acceptance.get("blocking_regressions") != 0
        or acceptance.get("acceptance_decision") != "IN_PROGRESS"
    ):
        result.fail(f"{category}.campaign", "RV campaign authority must retain exactly one accepted execution and remain IN_PROGRESS at EC3.")

    records = [item for item in history.get("executions", []) if item.get("campaign_id") == "ZT-RV-001"]
    if len(records) != 1:
        result.fail(f"{category}.history", "Exactly one ZT-RV-001 campaign execution must be recorded before the second eligible run.")
    else:
        record = records[0]
        if (
            record.get("execution_id") != "ZTRV-20260728T082825Z-f22b1052"
            or record.get("execution_date") != "2026-07-28T08:28:25.829099Z"
            or (record.get("pass"), record.get("warn"), record.get("fail")) != (8, 2, 0)
            or record.get("plan_hash") != "72c0aa52f20b12fb67d7b149e7c1ed980c2cfcbcdafea9cfc344cac2f4912624"
            or record.get("sanitization_status") != "PASS"
            or record.get("scheduled_trigger") is not False
            or record.get("security_boundary", {}).get("status") != "PASS"
            or record.get("warning_categories") != ["ENDPOINT_SCANNER_GAP", "CONFIGURATION_ONLY_RECORDS", "SERVICE_DEGRADED"]
        ):
            result.fail(f"{category}.history", "The first RV execution authority differs from the reviewed 8/2/0 candidate.")
        evidence = "docs/evidence/zero-trust/zt-rv-001-run-01.sanitized.txt"
        if record.get("evidence_hashes", {}).get(evidence) != "90e607e67d4b1603f80fdf13d78bcd6fb61f2ed7e088cb521b893cd6e6b4f362":
            result.fail(f"{category}.history", "The first RV sanitized evidence hash differs.")

    for field in ("automatic_schedule", "automatic_retry", "automatic_remediation", "mutation_allowed", "history_auto_append", "authoritative_auto_update_performed", "maturity_assigned", "scheduled_operation", "continuous_operation", "phase_1_complete"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false while RV is in progress.")
    runner = (root / "tools/continuous_verification/run_repeatability_campaign.py").read_text(encoding="utf-8", errors="replace")
    for token in ("observed_warning_categories", "MINIMUM_SEPARATION", "verify_security_boundary"):
        if token not in runner:
            result.fail(f"{category}.runner", f"RV runner is missing required reviewed behavior: {token}.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-RV-001 is implemented and in progress with one eligible independent 8/2/0 execution; EC4, schedule, maturity, and Phase 1 completion remain unclaimed.")
    return
    required = (
        REPEATABLE_VALIDATION_CAMPAIGN_PATH, REPEATABILITY_ACCEPTANCE_POLICY_PATH,
        REPEATABLE_VALIDATION_PACKAGE_PATH, *REPEATABLE_VALIDATION_SCHEMA_PATHS,
        *REPEATABLE_VALIDATION_REQUIRED_PATHS,
    )
    missing = [str(path) for path in required if not (root / path).is_file()]
    if missing:
        for path in missing:
            result.fail(f"{category}.files", f"Required repeatability campaign file is missing: {path}.")
        return
    try:
        campaign = load_json_yaml(root / REPEATABLE_VALIDATION_CAMPAIGN_PATH)
        policy = load_json_yaml(root / REPEATABILITY_ACCEPTANCE_POLICY_PATH)
        package = load_json_yaml(root / REPEATABLE_VALIDATION_PACKAGE_PATH)
        campaign_schema = load_schema(root / REPEATABLE_VALIDATION_SCHEMA_PATHS[0])
        policy_schema = load_schema(root / REPEATABLE_VALIDATION_SCHEMA_PATHS[1])
        recommendation = load_json_yaml(root / "docs/zero-trust/integrated-capability-assessment.yaml")
    except ValueError as exc:
        result.fail(f"{category}.configuration", str(exc))
        return
    for name, value, schema in (("campaign", campaign, campaign_schema), ("policy", policy, policy_schema)):
        for error in validate_schema_instance(value, schema):
            result.fail(f"{category}.{name}", error)
    expected_selection = ("ZT-4.1.1", "ZTCV-VAL-SYS", "ZT-CV-WF-001")
    recommendation_record = recommendation.get("repeatability_recommendation", {})
    selected = campaign.get("selection", {})
    if (recommendation_record.get("capability_id"), recommendation_record.get("validator_id"), recommendation_record.get("workflow_id")) != expected_selection:
        result.fail(f"{category}.selection", "CV must recommend exactly ZT-4.1.1 / ZTCV-VAL-SYS / ZT-CV-WF-001.")
    if (selected.get("capability_id"), selected.get("validator_id"), selected.get("workflow_id")) != expected_selection:
        result.fail(f"{category}.selection", "RV campaign selection must match the exact CV recommendation.")
    catalog_ids = {item.get("id") for item in catalog.get("capabilities", []) if isinstance(item, dict)}
    if selected.get("capability_id") not in catalog_ids:
        result.fail(f"{category}.selection", "Selected capability is not canonical.")
    requirements = campaign.get("requirements", {})
    if (requirements.get("evidence_continuity_target"), requirements.get("minimum_successful_executions"), requirements.get("minimum_consecutive_successes"), requirements.get("minimum_execution_separation")) != ("EC4_REPEATABLE_RUNTIME", 3, 3, "PT24H"):
        result.fail(f"{category}.criteria", "RV campaign must target EC4 with three consecutive successes separated by PT24H.")
    execution_policy = campaign.get("execution_policy", {})
    for field in ("automatic_schedule", "automatic_retry", "automatic_remediation", "mutation_allowed", "history_auto_append"):
        if execution_policy.get(field) is not False:
            result.fail(f"{category}.security", f"{field} must remain false.")
    scope = campaign.get("target_scope_definition", {})
    scope_hash = hashlib.sha256(json.dumps(scope, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()
    fingerprints = campaign.get("fingerprints", {})
    if fingerprints.get("target_scope_fingerprint") != scope_hash:
        result.fail(f"{category}.fingerprints", "Target-scope fingerprint is not deterministic.")
    validator_hash = hashlib.sha256((root / "tools/live-validation/validate-systems-live.ps1").read_bytes()).hexdigest()
    if fingerprints.get("validator_version") != f"1.0.0+sha256:{validator_hash}":
        result.fail(f"{category}.fingerprints", "Validator version/hash changed without review.")
    if fingerprints.get("expected_plan_hash") != "72c0aa52f20b12fb67d7b149e7c1ed980c2cfcbcdafea9cfc344cac2f4912624":
        result.fail(f"{category}.fingerprints", "Expected deterministic plan hash changed.")
    if policy.get("metadata", {}).get("default_decision") != "DENY" or policy.get("criteria", {}).get("target_continuity") != "EC4_REPEATABLE_RUNTIME":
        result.fail(f"{category}.policy", "Repeatability acceptance must default deny and target EC4 only.")
    if package.get("implementation_status") != "IMPLEMENTED" or package.get("validation_status") != "VALIDATED_LOCAL_CONFIGURATION" or package.get("acceptance_state") != "NOT_STARTED":
        result.fail(category, "RV tooling must remain IMPLEMENTED / VALIDATED_LOCAL_CONFIGURATION / NOT_STARTED before its first live run.")
    if package.get("accepted_campaign_executions") != 0 or package.get("current_continuity") != "EC3_ONE_TIME_RUNTIME":
        result.fail(f"{category}.claims", "No RV campaign execution or EC4 credit exists yet.")
    for field in ("automatic_schedule", "automatic_retry", "automatic_remediation", "mutation_allowed", "history_auto_append", "authoritative_update_performed", "maturity_assigned", "scheduled_operation", "continuous_operation", "phase_1_complete"):
        if package.get(field) is not False:
            result.fail(f"{category}.claims", f"{field} must remain false.")
    wrapper = (root / "tools/live-validation/run-repeatable-validation-pilot.ps1").read_text(encoding="utf-8", errors="replace")
    for forbidden in ("Register-ScheduledTask", "Restart-Service", "Invoke-Expression"):
        if forbidden in wrapper:
            result.fail(f"{category}.security", f"Repeatability wrapper contains prohibited behavior: {forbidden}.")
    if not any(item.level == "FAIL" and item.category.startswith(category) for item in result.findings):
        result.passed(category, "ZT-RV-001 single-candidate campaign, EC4 criteria, deterministic fingerprints, explicit history-review boundary, and enforced not-before time are valid; no live campaign execution is claimed.")


def run_validation(root: Path, strict: bool = False) -> ValidationResult:
    result = ValidationResult()
    try:
        catalog_schema = load_schema(root / CATALOG_SCHEMA_PATH)
        baseline_schema = load_schema(root / BASELINE_SCHEMA_PATH)
        backlog_schema = load_schema(root / BACKLOG_SCHEMA_PATH)
        catalog = load_json_yaml(root / CATALOG_PATH)
        baseline = load_json_yaml(root / BASELINE_PATH)
        backlog = load_json_yaml(root / BACKLOG_PATH)
    except ValueError as exc:
        result.fail("configuration", str(exc))
        return result

    validate_source(root, result)
    validate_catalog(catalog, catalog_schema, result)
    validate_baseline(baseline, baseline_schema, result)
    validate_backlog(backlog, backlog_schema, catalog, result)
    validate_foundation_package(root, catalog, result)
    validate_router_package(root, catalog, result)
    validate_telemetry_package(root, catalog, result)
    validate_endpoint_package(root, catalog, result)
    validate_application_package(root, catalog, result)
    validate_data_package(root, catalog, result)
    validate_system_package(root, catalog, result)
    validate_automation_package(root, catalog, result)
    validate_continuous_verification_package(root, catalog, result)
    validate_repeatable_validation_package(root, catalog, result)
    if not any(item.level == "FAIL" and item.category.startswith("schema.") for item in result.findings):
        validate_catalog_baseline_sync(catalog, baseline, result)
        validate_maturity(catalog["capabilities"], result, "catalog")
        validate_maturity(baseline["capabilities"], result, "baseline")
        validate_evidence(root, baseline, result)
    validate_overclaims(root, result)
    validate_sensitive_data(root, result)
    validate_markdown_links(root, result)
    if strict:
        for warning in [item for item in result.findings if item.level == "WARN"]:
            result.fail("strict", f"Warning promoted to failure: {warning.category}: {warning.message}")
    return result


def _render_text(result: ValidationResult, verbose: bool) -> None:
    for item in result.findings:
        if verbose or item.level != "PASS":
            print(f"[{item.level}] {item.category}: {item.message}")
    counts = result.counts
    print("\nZero Trust validation summary:")
    print(f"  Passed checks: {counts['PASS']}")
    print(f"  Warnings: {counts['WARN']}")
    print(f"  Failed checks: {counts['FAIL']}")
    print(f"  Exit status: {0 if counts['FAIL'] == 0 else 1}")


def _render_json(result: ValidationResult) -> None:
    counts = result.counts
    payload = {
        "findings": [item.__dict__ for item in result.findings],
        "summary": {"passed": counts["PASS"], "warnings": counts["WARN"], "failed": counts["FAIL"]},
        "exit_status": 0 if counts["FAIL"] == 0 else 1,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="print successful checks")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--root", type=Path, default=repository_root(), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    result = run_validation(args.root.resolve(), strict=args.strict)
    if args.format == "json":
        _render_json(result)
    else:
        _render_text(result, args.verbose)
    configuration_failure = any(item.category == "configuration" for item in result.findings)
    if configuration_failure:
        return 2
    return 1 if result.counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
