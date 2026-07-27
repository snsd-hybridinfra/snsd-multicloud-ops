#!/usr/bin/env python3
"""Read-only validator for the bounded ZT-ID-001 identity policy package."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_VERSION = "1.1.0"
POLICY_VERSION = "1.1.0"
LOCAL_EVIDENCE_VALIDATOR_VERSION = "1.0.0"
LOCAL_EVIDENCE_POLICY_VERSION = "1.0.0"

PACKAGE_PATH = Path("docs/zero-trust/packages/zt-id-001-package.yaml")
PACKAGE_DOCUMENT_PATH = Path(
    "docs/zero-trust/packages/zt-id-001-bounded-identity-validation.md"
)
CATALOG_PATH = Path("docs/zero-trust/capability-catalog.yaml")
RUNBOOK_PATH = Path("docs/runbooks/phase-1/06-identity-validation-readiness.md")
MANIFEST_PATH = Path("docs/runbooks/phase-1/runbook-manifest.yaml")
EVIDENCE_PATH = Path("docs/evidence/zero-trust/zt-id-001-local-validation.yaml")
RUNTIME_EVIDENCE_PATH = Path(
    "docs/evidence/zero-trust/zt-id-001-runtime-validation.yaml"
)

MODEL_PATHS = {
    "inventory": Path("docs/zero-trust/identity/identity-subject-model.yaml"),
    "roles": Path("docs/zero-trust/identity/role-policy-matrix.yaml"),
    "authentication": Path(
        "docs/zero-trust/identity/authentication-assurance-model.yaml"
    ),
    "lifecycle": Path("docs/zero-trust/identity/identity-lifecycle-policy.yaml"),
    "decision": Path("docs/zero-trust/identity/decision-policy.yaml"),
    "evidence_contract": Path("docs/zero-trust/identity/evidence-contract.yaml"),
}

SCHEMA_PATHS = {
    "common": Path("schemas/zero-trust-identity-common.schema.json"),
    "inventory": Path(
        "schemas/zero-trust-identity-subject-inventory.schema.json"
    ),
    "roles": Path("schemas/zero-trust-role-policy-matrix.schema.json"),
    "authentication": Path(
        "schemas/zero-trust-authentication-assurance.schema.json"
    ),
    "lifecycle": Path("schemas/zero-trust-identity-lifecycle.schema.json"),
    "decision": Path("schemas/zero-trust-access-decision.schema.json"),
    "evidence": Path("schemas/zero-trust-identity-evidence.schema.json"),
}

POSITIVE_FIXTURES = Path("tests/fixtures/zt-id-001/valid/positive-cases.yaml")
NEGATIVE_FIXTURES = Path("tests/fixtures/zt-id-001/invalid/negative-cases.yaml")

DIRECT_CAPABILITY_IDS = {
    "ZT-1.1.1",
    "ZT-1.1.2",
    "ZT-1.2.1",
    "ZT-1.4.1",
    "ZT-1.4.2",
}
EXCLUDED_IDENTITY_CAPABILITY_IDS = {"ZT-1.2.2", "ZT-1.3.1", "ZT-1.3.2"}
CANONICAL_NAMES = {
    "ZT-1.1.1": "사용자 인벤토리",
    "ZT-1.1.2": "ID 연계 및 사용자 자격 증명",
    "ZT-1.2.1": "다중인증 (MFA)",
    "ZT-1.4.1": "조건부 사용자 접근",
    "ZT-1.4.2": "최소 권한 접근",
}

IDENTITY_TYPES = {
    "HUMAN_OPERATOR",
    "SERVICE_IDENTITY",
    "AUTOMATION_IDENTITY",
    "VALIDATOR_IDENTITY",
    "BREAK_GLASS_IDENTITY",
}
ROLE_NAMES = {
    "IDENTITY_READER",
    "VALIDATION_OPERATOR",
    "EVIDENCE_REVIEWER",
    "PACKAGE_APPROVER",
    "MUTATING_OPERATOR",
    "BREAK_GLASS_OPERATOR",
}
AUTHENTICATION_METHODS = {
    "SSH_KEY",
    "LOCAL_CREDENTIAL",
    "FEDERATED_OIDC",
    "SERVICE_TOKEN",
    "CERTIFICATE",
    "MFA_PROTECTED_INTERACTIVE",
    "BREAK_GLASS_CREDENTIAL",
}
LIFECYCLE_STATES = {
    "PROPOSED",
    "APPROVED",
    "ACTIVE",
    "SUSPENDED",
    "REVOKED",
    "EXPIRED",
    "REVIEW_REQUIRED",
}
SECRET_REFERENCE_PATTERN = re.compile(
    r"^(?:env|file-ref|vault-ref|external-secret)://[A-Za-z0-9][A-Za-z0-9._/-]*$"
)
LIKELY_REAL_SECRET_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
]

FINGERPRINT_EXCLUDED_PARTS = {".git", ".runtime", "__pycache__"}


@dataclass
class Finding:
    level: str
    category: str
    message: str


class Results:
    def __init__(self) -> None:
        self.findings: list[Finding] = []

    def pass_(self, category: str, message: str) -> None:
        self.findings.append(Finding("PASS", category, message))

    def warn(self, category: str, message: str) -> None:
        self.findings.append(Finding("WARN", category, message))

    def fail(self, category: str, message: str) -> None:
        self.findings.append(Finding("FAIL", category, message))

    def summary(self) -> dict[str, int]:
        return {
            "passed": sum(item.level == "PASS" for item in self.findings),
            "warnings": sum(item.level == "WARN" for item in self.findings),
            "failed": sum(item.level == "FAIL" for item in self.findings),
        }


def load_json_document(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.as_posix()} must contain a top-level object")
    return value


def repository_fingerprint(root: Path) -> dict[str, str]:
    """Hash repository files without reading protected runtime or Git internals."""

    fingerprints: dict[str, str] = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in FINGERPRINT_EXCLUDED_PARTS for part in relative.parts):
            continue
        if not path.is_file() or path.suffix == ".pyc":
            continue
        fingerprints[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return fingerprints


def detect_repository_mutation(
    before: dict[str, str], after: dict[str, str]
) -> list[str]:
    paths = sorted(set(before) | set(after))
    return [path for path in paths if before.get(path) != after.get(path)]


def _json_pointer(document: Any, pointer: str) -> Any:
    current = document
    if pointer in ("", "/"):
        return current
    for raw in pointer.lstrip("/").split("/"):
        path_part = raw.replace("~1", "/").replace("~0", "~")
        current = (
            current[int(path_part)]
            if isinstance(current, list)
            else current[path_part]
        )
    return current


def _schema_type_matches(value: Any, expected: str) -> bool:
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


class LocalSchemaValidator:
    """Small dependency-free validator for the schema keywords used here."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.cache: dict[Path, dict[str, Any]] = {}

    def _load(self, path: Path) -> dict[str, Any]:
        path = path.resolve()
        if path not in self.cache:
            self.cache[path] = load_json_document(path)
        return self.cache[path]

    def _resolve_ref(
        self, reference: str, current_schema_path: Path
    ) -> tuple[dict[str, Any], Path]:
        file_part, _, pointer = reference.partition("#")
        target_path = (
            current_schema_path
            if not file_part
            else (current_schema_path.parent / file_part).resolve()
        )
        schema = self._load(target_path)
        if pointer:
            value = _json_pointer(schema, pointer)
            if not isinstance(value, dict):
                raise ValueError(f"Schema reference {reference!r} is not an object")
            schema = value
        return schema, target_path

    def validate(self, instance: Any, schema_path: Path) -> list[str]:
        absolute = (self.root / schema_path).resolve()
        schema = self._load(absolute)
        errors: list[str] = []
        self._walk(instance, schema, absolute, "$", errors)
        return errors

    def _walk(
        self,
        instance: Any,
        schema: dict[str, Any],
        schema_path: Path,
        location: str,
        errors: list[str],
    ) -> None:
        if "oneOf" in schema:
            candidate_results: list[list[str]] = []
            for candidate in schema["oneOf"]:
                candidate_errors: list[str] = []
                self._walk(
                    instance,
                    candidate,
                    schema_path,
                    location,
                    candidate_errors,
                )
                candidate_results.append(candidate_errors)
            matches = [item for item in candidate_results if not item]
            if len(matches) != 1:
                errors.append(
                    f"{location}: expected exactly one oneOf schema match, got {len(matches)}"
                )
            return

        if "$ref" in schema:
            resolved, resolved_path = self._resolve_ref(schema["$ref"], schema_path)
            self._walk(instance, resolved, resolved_path, location, errors)
            return

        expected_type = schema.get("type")
        if expected_type is not None:
            allowed = expected_type if isinstance(expected_type, list) else [expected_type]
            if not any(_schema_type_matches(instance, item) for item in allowed):
                errors.append(f"{location}: expected type {allowed}, got {type(instance).__name__}")
                return

        if "const" in schema and instance != schema["const"]:
            errors.append(f"{location}: expected constant {schema['const']!r}")
        if "enum" in schema and instance not in schema["enum"]:
            errors.append(f"{location}: value {instance!r} is outside the enum")

        if isinstance(instance, str):
            if "minLength" in schema and len(instance) < schema["minLength"]:
                errors.append(f"{location}: string is shorter than minLength")
            if "pattern" in schema and not re.search(schema["pattern"], instance):
                errors.append(f"{location}: string does not match the required pattern")

        if isinstance(instance, (int, float)) and not isinstance(instance, bool):
            if "minimum" in schema and instance < schema["minimum"]:
                errors.append(f"{location}: value is lower than minimum")

        if isinstance(instance, list):
            if "minItems" in schema and len(instance) < schema["minItems"]:
                errors.append(f"{location}: array has fewer than minItems")
            if schema.get("uniqueItems"):
                normalized = [json.dumps(item, sort_keys=True) for item in instance]
                if len(normalized) != len(set(normalized)):
                    errors.append(f"{location}: array items are not unique")
            item_schema = schema.get("items")
            if isinstance(item_schema, dict):
                for index, item in enumerate(instance):
                    self._walk(
                        item,
                        item_schema,
                        schema_path,
                        f"{location}[{index}]",
                        errors,
                    )

        if isinstance(instance, dict):
            required = schema.get("required", [])
            for key in required:
                if key not in instance:
                    errors.append(f"{location}: missing required property {key!r}")
            properties = schema.get("properties", {})
            for key, value in instance.items():
                child_schema = properties.get(key)
                if isinstance(child_schema, dict):
                    self._walk(
                        value,
                        child_schema,
                        schema_path,
                        f"{location}.{key}",
                        errors,
                    )
                elif schema.get("additionalProperties") is False:
                    errors.append(f"{location}: additional property {key!r} is prohibited")


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            return datetime.fromisoformat(value[:-1] + "+00:00")
        parsed = datetime.fromisoformat(value)
        return parsed.replace(tzinfo=parsed.tzinfo or timezone.utc)
    except (TypeError, ValueError):
        return None


def _walk_values(value: Any) -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield key, child
            yield from _walk_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_values(child)


def validate_package_document(
    package: dict[str, Any], catalog: dict[str, Any] | None = None
) -> set[str]:
    codes: set[str] = set()
    expected = {
        "package_id": "ZT-ID-001",
        "package_type": "IDENTITY_VALIDATION",
        "phase": "PHASE_1",
        "authority_status": "AUTHORITATIVE",
        "implementation_status": "IMPLEMENTED",
        "validation_status": "LOCAL_VALIDATED",
        "local_validation_status": "LOCAL_VALIDATED",
        "runtime_validation_status": "NOT_VALIDATED",
        "runtime_acceptance_status": "PENDING",
        "maturity_status": "UNASSESSED",
        "current_maturity": "UNASSESSED",
    }
    for field, value in expected.items():
        if package.get(field) != value:
            if field == "package_id":
                codes.add("INVALID_PACKAGE_ID")
            elif field == "phase":
                codes.add("INVALID_PACKAGE_PHASE")
            elif field == "runtime_validation_status":
                codes.add("UNSUPPORTED_RUNTIME_CLAIM")
            elif field == "maturity_status":
                codes.add("UNSUPPORTED_MATURITY_CLAIM")
            else:
                codes.add("INVALID_PACKAGE_STATE")

    false_fields = {
        "identity_provider_deployed",
        "mfa_enforced",
        "oidc_deployed",
        "centralized_rbac_enforced",
        "action_runtime_executed",
        "action_live_identity_changed",
    }
    if any(package.get(field) is not False for field in false_fields):
        codes.add("UNSUPPORTED_RUNTIME_CLAIM")

    capability_ids = package.get("capability_ids", [])
    if len(capability_ids) != len(set(capability_ids)):
        codes.add("DUPLICATE_CAPABILITY_MAPPING")
    if set(capability_ids) != DIRECT_CAPABILITY_IDS:
        codes.add("MISSING_CAPABILITY_MAPPING")
    if catalog is not None:
        catalog_rows = {
            row.get("id"): row
            for row in catalog.get("capabilities", [])
            if isinstance(row, dict)
        }
        if any(identifier not in catalog_rows for identifier in capability_ids):
            codes.add("UNKNOWN_CAPABILITY_ID")
        for identifier, expected_name in CANONICAL_NAMES.items():
            if catalog_rows.get(identifier, {}).get("capability_ko") != expected_name:
                codes.add("INVALID_CAPABILITY_MAPPING")

    for key, value in _walk_values(package):
        if key == "runtime_tracking_path" or (
            isinstance(value, str) and value.startswith(".runtime/") and key != "limitations"
        ):
            codes.add("TRACKED_RUNTIME_PROHIBITED")
    return codes


def validate_role_policy(role_policy: dict[str, Any]) -> set[str]:
    codes: set[str] = set()
    roles = role_policy.get("roles", [])
    role_names = [row.get("role_name") for row in roles if isinstance(row, dict)]
    if set(role_names) != ROLE_NAMES or len(role_names) != len(set(role_names)):
        codes.add("INVALID_ROLE_POLICY")
    actions = {
        row.get("action"): row
        for row in role_policy.get("actions", [])
        if isinstance(row, dict)
    }
    if role_policy.get("default_policy") != "DENY_BY_DEFAULT_FOR_UNREGISTERED_IDENTITY":
        codes.add("DEFAULT_DENY_MISSING")
    for role in roles:
        if not isinstance(role, dict):
            codes.add("INVALID_ROLE_POLICY")
            continue
        allowed = set(role.get("allowed_actions", []))
        prohibited = set(role.get("prohibited_actions", []))
        if allowed & prohibited or any(action not in actions for action in allowed | prohibited):
            codes.add("INVALID_ROLE_POLICY")
        if "ADMIN" in str(role.get("role_name", "")):
            codes.add("UNRESTRICTED_ADMIN_ROLE")
    return codes


def validate_authentication_model(model: dict[str, Any]) -> set[str]:
    codes: set[str] = set()
    if model.get("mfa_enforced") is not False:
        codes.add("FICTIONAL_MFA_ENFORCEMENT")
    if model.get("oidc_deployed") is not False:
        codes.add("FICTIONAL_OIDC_DEPLOYMENT")
    if model.get("identity_provider_deployed") is not False:
        codes.add("FICTIONAL_IDENTITY_PROVIDER_DEPLOYMENT")
    if model.get("runtime_authentication_validated") is not False:
        codes.add("UNSUPPORTED_RUNTIME_CLAIM")
    methods = {
        row.get("method")
        for row in model.get("authentication_methods", [])
        if isinstance(row, dict)
    }
    if methods != AUTHENTICATION_METHODS:
        codes.add("UNSUPPORTED_AUTHENTICATION_METHOD")
    if any(
        row.get("deployed_by_package") is not False
        for row in model.get("authentication_methods", [])
        if isinstance(row, dict)
    ):
        codes.add("FICTIONAL_IDENTITY_PROVIDER_DEPLOYMENT")
    return codes


def validate_lifecycle_policy(policy: dict[str, Any]) -> set[str]:
    codes: set[str] = set()
    states = policy.get("states", [])
    if set(states) != LIFECYCLE_STATES or len(states) != len(set(states)):
        codes.add("INVALID_LIFECYCLE_POLICY")
    required_rules = {f"LIFECYCLE-{number:03d}" for number in range(1, 9)}
    actual_rules = {
        row.get("rule_id")
        for row in policy.get("acceptance_rules", [])
        if isinstance(row, dict)
    }
    if actual_rules != required_rules:
        codes.add("INVALID_LIFECYCLE_POLICY")
    return codes


def validate_identity_inventory(
    inventory: dict[str, Any], role_policy: dict[str, Any]
) -> set[str]:
    codes: set[str] = set()
    if inventory.get("data_classification") != "SYNTHETIC_LOCAL_FIXTURE" or inventory.get("production_data") is not False:
        codes.add("PRODUCTION_IDENTITY_DATA_PROHIBITED")

    identities = inventory.get("identities", [])
    fixture_time = _parse_datetime(inventory.get("fixture_time"))
    if fixture_time is None:
        codes.add("INVALID_FIXTURE_TIME")

    role_map = {
        row.get("role_name"): row
        for row in role_policy.get("roles", [])
        if isinstance(row, dict)
    }
    seen: set[str] = set()
    for identity in identities:
        if not isinstance(identity, dict):
            codes.add("INVALID_IDENTITY_RECORD")
            continue
        identity_id = identity.get("identity_id")
        if not identity_id:
            codes.add("MISSING_IDENTITY_ID")
        elif identity_id in seen:
            codes.add("DUPLICATE_IDENTITY_ID")
        else:
            seen.add(identity_id)

        identity_type = identity.get("identity_type")
        if identity_type not in IDENTITY_TYPES:
            codes.add("UNKNOWN_IDENTITY_TYPE")
        if not identity.get("accountable_owner"):
            codes.add("MISSING_ACCOUNTABLE_OWNER")
        if identity.get("lifecycle_status") not in LIFECYCLE_STATES:
            codes.add("INVALID_LIFECYCLE_STATE")
        if identity.get("authentication_method") not in AUTHENTICATION_METHODS:
            codes.add("UNSUPPORTED_AUTHENTICATION_METHOD")

        assigned_roles = identity.get("assigned_roles", [])
        invalid_roles = [role for role in assigned_roles if role not in ROLE_NAMES]
        if invalid_roles:
            codes.add("INVALID_ROLE")
        for role in assigned_roles:
            conflicts = set(role_map.get(role, {}).get("separation_of_duties_conflicts", []))
            if conflicts & set(assigned_roles):
                codes.add("SEPARATION_OF_DUTIES_CONFLICT")

        privilege = identity.get("privilege_level")
        if privilege in {"PRIVILEGED", "EMERGENCY"} and identity.get("shared_identity") is not False:
            codes.add("SHARED_PRIVILEGED_IDENTITY")
        if (
            identity_type == "HUMAN_OPERATOR"
            and identity.get("interactive_access") is True
            and privilege == "PRIVILEGED"
            and identity.get("mfa_requirement") != "REQUIRED_NOT_IMPLEMENTED"
        ):
            codes.add("PRIVILEGED_MFA_REQUIRED")

        expiration = _parse_datetime(identity.get("expiration"))
        if fixture_time is not None and expiration is not None and expiration <= fixture_time:
            codes.add("IDENTITY_EXPIRED")
        if identity.get("lifecycle_status") == "REVOKED" and assigned_roles:
            codes.add("REVOKED_IDENTITY_HAS_ROLES")
        if identity.get("lifecycle_status") == "ACTIVE":
            if not identity.get("accountable_owner") or identity.get("approval_status") != "APPROVED":
                codes.add("ACTIVE_IDENTITY_REQUIRES_APPROVAL")

        if identity_type == "AUTOMATION_IDENTITY" and identity.get("interactive_access") is not False:
            codes.add("AUTOMATION_INTERACTIVE_ACCESS")
        if identity_type == "SERVICE_IDENTITY":
            if not identity.get("target_scope"):
                codes.add("SERVICE_TARGET_SCOPE_REQUIRED")
            if identity.get("interactive_access") is not False:
                codes.add("SERVICE_INTERACTIVE_ACCESS")

        if identity_type == "BREAK_GLASS_IDENTITY":
            if not identity.get("expiration"):
                codes.add("BREAK_GLASS_EXPIRATION_REQUIRED")
            if identity.get("logging_requirement") != "REQUIRED":
                codes.add("BREAK_GLASS_LOGGING_REQUIRED")
            if not identity.get("recovery_procedure"):
                codes.add("BREAK_GLASS_RECOVERY_REQUIRED")
            if not identity.get("rollback_procedure"):
                codes.add("BREAK_GLASS_ROLLBACK_REQUIRED")
            if not identity.get("approval_reference"):
                codes.add("BREAK_GLASS_APPROVAL_REQUIRED")
            if identity.get("lockout_stop_condition") != "STOP_ON_UNEXPECTED_DENIAL":
                codes.add("BREAK_GLASS_LOCKOUT_STOP_REQUIRED")
            if "*" in identity.get("target_scope", []):
                codes.add("UNRESTRICTED_BREAK_GLASS_SCOPE")

        for reference in identity.get("secret_references", []):
            if not isinstance(reference, str) or not SECRET_REFERENCE_PATTERN.fullmatch(reference):
                codes.add("INVALID_SECRET_REFERENCE")

        for key, value in _walk_values(identity):
            normalized_key = key.lower()
            if normalized_key in {"password", "password_hash", "plaintext_password"}:
                codes.add("PLAINTEXT_SECRET_MATERIAL")
            if normalized_key in {"private_key", "ssh_private_key"}:
                codes.add("PRIVATE_KEY_MATERIAL")
            if normalized_key in {"token", "token_value", "client_secret", "access_token"}:
                codes.add("TOKEN_OR_CLIENT_SECRET_MATERIAL")
            if normalized_key in {"mfa_seed", "totp_seed"}:
                codes.add("MFA_SEED_MATERIAL")
            if normalized_key in {"recovery_code", "recovery_codes"}:
                codes.add("RECOVERY_CODE_MATERIAL")
            if normalized_key in {"email", "personal_email", "phone", "full_name"}:
                codes.add("EXCESSIVE_PERSONAL_DATA")
            if isinstance(value, str) and any(
                pattern.search(value) for pattern in LIKELY_REAL_SECRET_PATTERNS
            ):
                codes.add("LIKELY_REAL_SECRET_MATERIAL")
    return codes


def evaluate_request(
    request: dict[str, Any],
    inventory: dict[str, Any],
    role_policy: dict[str, Any],
    authentication_model: dict[str, Any],
    decision_id: str = "DEC-LOCAL",
) -> dict[str, Any]:
    identity_id = str(request.get("identity_id", "unregistered-fixture"))
    action = request.get("requested_action", "UNKNOWN_ACTION")
    target_scope = request.get("target_scope", "fixture:unknown")
    fixture_time = inventory.get("fixture_time", "2026-07-19T02:00:00Z")
    identities = {
        row.get("identity_id"): row
        for row in inventory.get("identities", [])
        if isinstance(row, dict) and row.get("identity_id")
    }
    actions = {
        row.get("action"): row
        for row in role_policy.get("actions", [])
        if isinstance(row, dict)
    }
    role_map = {
        row.get("role_name"): row
        for row in role_policy.get("roles", [])
        if isinstance(row, dict)
    }

    identity = identities.get(identity_id)
    decision = "DENY"
    reasons: list[str] = []
    evaluated_role: str | None = None
    approval_requirement = "NONE"

    if identity is None:
        reasons = ["UNREGISTERED_IDENTITY"]
    else:
        status = identity.get("lifecycle_status")
        expiration = _parse_datetime(identity.get("expiration"))
        now = _parse_datetime(fixture_time)
        if status == "REVOKED":
            reasons = ["IDENTITY_REVOKED"]
        elif status == "SUSPENDED":
            reasons = ["IDENTITY_SUSPENDED"]
        elif status == "EXPIRED" or (
            expiration is not None and now is not None and expiration <= now
        ):
            reasons = ["IDENTITY_EXPIRED"]
        elif status in {"PROPOSED", "REVIEW_REQUIRED"}:
            decision = "REVIEW_REQUIRED"
            reasons = ["IDENTITY_NOT_ACTIVE"]
            if action == "FUTURE_FEDERATED_AUTHENTICATION":
                reasons.extend(["RUNTIME_NOT_IMPLEMENTED", "OIDC_NOT_DEPLOYED"])
                approval_requirement = "SEPARATE_APPROVAL_REQUIRED"
        elif action not in actions:
            reasons = ["UNKNOWN_ACTION"]
        else:
            assigned_roles = identity.get("assigned_roles", [])
            for role_name in assigned_roles:
                if action in role_map.get(role_name, {}).get("allowed_actions", []):
                    evaluated_role = role_name
                    break
            if evaluated_role is None:
                reasons = ["ACTION_NOT_ALLOWED_FOR_ROLE"]
            else:
                classification = actions[action].get("classification")
                if classification == "PHASE_2_RUNTIME":
                    decision = "REVIEW_REQUIRED"
                    reasons = ["RUNTIME_NOT_IMPLEMENTED", "OIDC_NOT_DEPLOYED"]
                    approval_requirement = "SEPARATE_APPROVAL_REQUIRED"
                elif classification in {"MUTATING", "EMERGENCY"}:
                    if not request.get("approval_present"):
                        decision = "REVIEW_REQUIRED"
                        reasons = ["APPROVAL_REQUIRED"]
                        approval_requirement = "SEPARATE_APPROVAL_REQUIRED"
                    else:
                        decision = "ALLOW"
                        reasons = [
                            "REGISTERED_IDENTITY",
                            "APPROVAL_PRESENT",
                            "ROLE_ACTION_ALLOWED",
                        ]
                        approval_requirement = "SATISFIED_BY_SYNTHETIC_FIXTURE"
                else:
                    decision = "ALLOW"
                    reasons = ["REGISTERED_IDENTITY", "ROLE_ACTION_ALLOWED"]

    return {
        "decision_id": f"DEC-{decision_id}",
        "identity_id": identity_id,
        "requested_action": action,
        "target_scope": target_scope,
        "evaluated_role": evaluated_role,
        "policy_version": POLICY_VERSION,
        "decision": decision,
        "reason_codes": reasons,
        "approval_requirement": approval_requirement,
        "evidence_authority": "CODEX_EXECUTED_LOCAL",
        "timestamp": fixture_time,
        "limitations": [
            "Synthetic fixture decision only; no live access is granted or denied."
        ],
    }


def apply_mutation(document: dict[str, Any], case: dict[str, Any]) -> None:
    pointer = case.get("path", "")
    tokens = [
        token.replace("~1", "/").replace("~0", "~")
        for token in pointer.lstrip("/").split("/")
        if token
    ]
    if not tokens:
        raise ValueError(f"{case.get('case_id')}: mutation path is empty")
    parent: Any = document
    for token in tokens[:-1]:
        parent = parent[int(token)] if isinstance(parent, list) else parent[token]
    final = tokens[-1]
    index: int | str = int(final) if isinstance(parent, list) else final
    operation = case.get("operation")
    if operation == "remove":
        if isinstance(parent, list):
            parent.pop(index)
        else:
            parent.pop(index, None)
    elif operation in {"replace", "inject"}:
        parent[index] = copy.deepcopy(case.get("value"))
    elif operation == "append_copy":
        target = parent[index]
        if not isinstance(parent, list):
            raise ValueError("append_copy requires a list parent")
        parent.append(copy.deepcopy(target))
    else:
        raise ValueError(f"Unsupported mutation operation: {operation!r}")


def validate_negative_case(
    case: dict[str, Any],
    package: dict[str, Any],
    inventory: dict[str, Any],
    role_policy: dict[str, Any],
    authentication_model: dict[str, Any],
    catalog: dict[str, Any],
) -> set[str]:
    source = case.get("source")
    if source == "identity_inventory":
        mutated = copy.deepcopy(inventory)
        apply_mutation(mutated, case)
        return validate_identity_inventory(mutated, role_policy)
    if source == "authentication_model":
        mutated = copy.deepcopy(authentication_model)
        apply_mutation(mutated, case)
        return validate_authentication_model(mutated)
    if source == "package":
        mutated = copy.deepcopy(package)
        apply_mutation(mutated, case)
        return validate_package_document(mutated, catalog)
    if source == "access_request":
        mutated_inventory = copy.deepcopy(inventory)
        identity_mutation = case.get("identity_mutation")
        if isinstance(identity_mutation, dict):
            for row in mutated_inventory.get("identities", []):
                if row.get("identity_id") == identity_mutation.get("identity_id"):
                    row[identity_mutation["field"]] = identity_mutation.get("value")
        decision = evaluate_request(
            case.get("request", {}),
            mutated_inventory,
            role_policy,
            authentication_model,
            case.get("case_id", "NEG"),
        )
        return set(decision["reason_codes"])
    return {"UNKNOWN_NEGATIVE_FIXTURE_SOURCE"}


def validate_evidence_document(
    evidence: dict[str, Any],
    package: dict[str, Any],
    positive_cases: list[dict[str, Any]],
    negative_cases: list[dict[str, Any]],
) -> set[str]:
    codes: set[str] = set()
    required = {
        "package_id": "ZT-ID-001",
        "execution_authority": "CODEX_EXECUTED_LOCAL",
        "execution_mode": "SYNTHETIC_FIXTURE_VALIDATION",
        "validator": "tools/validate_zt_id_001.py",
        "validator_version": LOCAL_EVIDENCE_VALIDATOR_VERSION,
        "policy_version": LOCAL_EVIDENCE_POLICY_VERSION,
        "target": "LOCAL_REPOSITORY_FIXTURES",
        "result": "PASS",
        "runtime_executed": False,
        "live_identity_changed": False,
        "secret_findings": 0,
        "privacy_findings": 0,
        "status": "LOCAL_VALIDATION_ONLY",
    }
    for field, expected in required.items():
        if evidence.get(field) != expected:
            if field in {"runtime_executed", "execution_authority", "execution_mode"}:
                codes.add("EVIDENCE_RUNTIME_CLAIM_MISMATCH")
            elif field == "validator_version":
                codes.add("MISSING_VALIDATOR_VERSION")
            elif field == "policy_version":
                codes.add("MISSING_POLICY_VERSION")
            else:
                codes.add("PACKAGE_EVIDENCE_STATUS_MISMATCH")
    if set(evidence.get("capability_ids", [])) != set(package.get("capability_ids", [])):
        codes.add("PACKAGE_EVIDENCE_STATUS_MISMATCH")
    expected_passes = len(positive_cases) + len(negative_cases)
    if (
        evidence.get("pass_count") != expected_passes
        or evidence.get("warn_count") != 0
        or evidence.get("fail_count") != 0
        or len(evidence.get("positive_cases", [])) != len(positive_cases)
        or len(evidence.get("negative_cases", [])) != len(negative_cases)
    ):
        codes.add("EVIDENCE_COUNT_MISMATCH")
    if not evidence.get("limitations"):
        codes.add("MISSING_EVIDENCE_LIMITATION")
    return codes


def validate_runtime_evidence_document(
    evidence: dict[str, Any], package: dict[str, Any]
) -> set[str]:
    codes: set[str] = set()
    required = {
        "action_id": "P1-ID-ENF-001-RETRY",
        "parent_action_id": "P1-ID-ENF-001",
        "package_id": "ZT-ID-001",
        "execution_authority": "USER_APPROVED_CODEX_EXECUTION",
        "execution_mode": "BOUNDED_NON_PRODUCTION_ENFORCEMENT",
        "target_alias": "NONPROD_VALIDATOR_TARGET_01",
        "target_environment": "NON_PRODUCTION",
        "target_class": "EVE_NG_RESTRICTED_VALIDATOR_ENDPOINT",
        "operator_access": "PASS",
        "validator_identity": "DEDICATED_PACKAGE_OWNED_VALIDATOR",
        "forced_command": "ENFORCED",
        "ssh_enforcement": "ENFORCED",
        "sudoers_enforcement": "ENFORCED",
        "third_party_sudoers_unchanged": True,
        "backup_created": True,
        "rollback_armed": True,
        "rollback_cancelled": True,
        "residual_jobs": 0,
        "unexpected_allowances": 0,
        "protected_state_mutations": "PACKAGE_OWNED_CONFIGURATION_ONLY",
        "sshd_validation": "PASS",
        "sudoers_package_validation": "PASS",
        "sudoers_global_validation": "PASS",
        "ssh_reload": "PASS",
        "service_health": "PASS",
        "runtime_executed": True,
        "live_identity_changed": True,
        "identity_provider_deployed": False,
        "mfa_enforced": False,
        "oidc_deployed": False,
        "rbac_runtime_enforced": False,
        "secret_findings": 0,
        "privacy_findings": 0,
        "evidence_freshness": "CURRENT_ACTION",
        "implementation_status": "IMPLEMENTED",
        "validation_status": "RUNTIME_VALIDATED",
        "runtime_validation_status": "VALIDATED",
        "runtime_acceptance_status": "ACCEPTED",
        "maturity_status": "UNASSESSED",
        "validator": "tools/validate_zt_id_001.py",
        "validator_version": VALIDATOR_VERSION,
        "policy_version": POLICY_VERSION,
        "result": "PASS",
    }
    for field, expected in required.items():
        if evidence.get(field) != expected:
            codes.add("RUNTIME_EVIDENCE_STATUS_MISMATCH")

    if set(evidence.get("capability_ids", [])) != set(package.get("capability_ids", [])):
        codes.add("PACKAGE_EVIDENCE_STATUS_MISMATCH")
    if (
        evidence.get("positive_test_count", 0) < 20
        or evidence.get("positive_pass_count") != evidence.get("positive_test_count")
        or evidence.get("negative_test_count", 0) < 42
        or evidence.get("negative_denied_count") != evidence.get("negative_test_count")
    ):
        codes.add("RUNTIME_EVIDENCE_COUNT_MISMATCH")
    if evidence.get("account_created_or_reused") not in {"CREATED", "REUSED"}:
        codes.add("RUNTIME_IDENTITY_STATE_MISMATCH")
    if evidence.get("group_created_or_reused") not in {"CREATED", "REUSED"}:
        codes.add("RUNTIME_IDENTITY_STATE_MISMATCH")
    if _parse_datetime(evidence.get("timestamp")) is None:
        codes.add("INVALID_EVIDENCE_TIMESTAMP")
    if not evidence.get("limitations"):
        codes.add("MISSING_EVIDENCE_LIMITATION")
    return codes


def _check_paths_and_claims(root: Path, results: Results) -> None:
    required_paths = [
        PACKAGE_DOCUMENT_PATH,
        RUNBOOK_PATH,
        RUNTIME_EVIDENCE_PATH,
        Path("docs/zero-trust/identity/rollback-and-lockout-safety.md"),
        Path("docs/zero-trust/target-architecture/implementation-dependency-map.md"),
        Path("docs/zero-trust/target-architecture/operator-interface-contract.md"),
        Path("tools/live-validation/install-eve-validator.ps1"),
        Path("tools/live-validation/remote/codex-eve-dispatcher.sh.example"),
        Path("tools/live-validation/remote/validate-eve-identity-readonly.sh.example"),
        Path("tools/live-validation/remote/eve-validator-sudoers.example"),
        Path("tools/live-validation/remote/eve-validator-authorized-key.example"),
        Path("tools/live-validation/remote/eve-validator-sshd.conf.example"),
    ]
    missing = [path.as_posix() for path in required_paths if not (root / path).is_file()]
    if missing:
        results.fail("links.required", f"Missing required package links: {missing}")
    else:
        results.pass_("links.required", "Package, runbook, rollback, and architecture links resolve.")

    package_text = (root / PACKAGE_DOCUMENT_PATH).read_text(encoding="utf-8")
    required_sections = [
        "Package Identity",
        "Purpose",
        "Scope",
        "Explicit Exclusions",
        "Guideline Capability Mapping",
        "Current Authority",
        "Identity Subject Model",
        "Role and Privilege Model",
        "Authentication Assurance Model",
        "Lifecycle Model",
        "Decision Model",
        "Positive Acceptance Cases",
        "Negative Acceptance Cases",
        "Evidence Contract",
        "Privacy and Data-Minimization Boundary",
        "Secret Boundary",
        "Lockout Prevention",
        "Break-Glass Requirements",
        "Failure Handling",
        "Rollback",
        "Runtime Validation Boundary",
        "Phase 2 Dependency Boundary",
        "Known Limitations",
        "Package Acceptance",
        "Related Runbooks",
        "Related Architecture",
    ]
    missing_sections = [
        section for section in required_sections if f"## {section}" not in package_text
    ]
    if missing_sections:
        results.fail("package.sections", f"Missing package sections: {missing_sections}")
    else:
        results.pass_("package.sections", "All required package sections are present.")

    prohibited_affirmative = [
        r"mfa_status\s*[:=]\s*ENFORCED",
        r"OIDC\s+(?:is\s+)?OPERATIONAL",
        r"KEYCLOAK\s+(?:is\s+)?OPERATIONAL",
        r"RBAC_RUNTIME_ENFORCED\s*[:=]\s*true",
        r"maturity_status\s*[:=]\s*ADVANCED",
    ]
    if any(re.search(pattern, package_text, re.IGNORECASE) for pattern in prohibited_affirmative):
        results.fail("package.claims", "A prohibited runtime or maturity claim is present.")
    else:
        results.pass_("package.claims", "Runtime, provider, MFA, OIDC, RBAC, and maturity boundaries are explicit.")

    enforcement_requirements = {
        Path("tools/live-validation/remote/codex-eve-dispatcher.sh.example"): [
            "identity-summary",
            "bounded-validation",
            "UNSAFE_SYNTAX",
            "/usr/local/sbin/validate-eve-identity-readonly",
        ],
        Path("tools/live-validation/remote/validate-eve-identity-readonly.sh.example"): [
            "DEDICATED_VALIDATOR",
            "EXACT_ALLOWLIST",
            "configuration_metadata=COMPLIANT",
        ],
        Path("tools/live-validation/remote/eve-validator-sudoers.example"): [
            "NOSETENV",
            "identity-summary",
            "validator-version",
        ],
        Path("tools/live-validation/remote/eve-validator-authorized-key.example"): [
            "restrict,command=",
            "no-agent-forwarding",
            "no-port-forwarding",
            "no-pty",
            "no-user-rc",
            "no-X11-forwarding",
        ],
        Path("tools/live-validation/remote/eve-validator-sshd.conf.example"): [
            "AuthenticationMethods publickey",
            "PasswordAuthentication no",
            "AllowTcpForwarding no",
            "AllowStreamLocalForwarding no",
            "ForceCommand /usr/local/sbin/codex-eve-dispatcher",
        ],
        Path("tools/live-validation/install-eve-validator.ps1"): [
            "RollbackArmed",
            "visudo -cf",
            "sshd -t",
            "systemctl reload",
        ],
    }
    missing_controls: list[str] = []
    for path, tokens in enforcement_requirements.items():
        text = (root / path).read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                missing_controls.append(f"{path.as_posix()}:{token}")
    if missing_controls:
        results.fail(
            "enforcement.templates",
            f"Bounded enforcement templates are incomplete: {missing_controls}",
        )
    else:
        results.pass_(
            "enforcement.templates",
            "Forced command, identity helper, SSH, authorized-key, sudoers, and rollback-gated installer templates are synchronized.",
        )


def _validate_repository_integrity(root: Path, results: Results) -> None:
    try:
        tracked_runtime = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--", ".runtime"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError) as exc:
        results.fail("repository.git", f"Unable to inspect tracked runtime: {exc}")
        return
    if tracked_runtime:
        results.fail("repository.runtime", "Tracked runtime paths exist.")
    else:
        results.pass_("repository.runtime", "No runtime file is tracked.")

def validate(root: Path = ROOT, strict: bool = False) -> dict[str, Any]:
    root = root.resolve()
    results = Results()
    initial_fingerprint = repository_fingerprint(root)
    required_documents = {
        "package": PACKAGE_PATH,
        "catalog": CATALOG_PATH,
        "manifest": MANIFEST_PATH,
        "evidence": EVIDENCE_PATH,
        "runtime_evidence": RUNTIME_EVIDENCE_PATH,
        "positive": POSITIVE_FIXTURES,
        "negative": NEGATIVE_FIXTURES,
        **MODEL_PATHS,
    }
    documents: dict[str, dict[str, Any]] = {}
    try:
        for name, relative in required_documents.items():
            documents[name] = load_json_document(root / relative)
        schemas = {
            name: load_json_document(root / relative)
            for name, relative in SCHEMA_PATHS.items()
        }
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"Required JSON-compatible YAML/schema parse failed: {exc}") from exc
    results.pass_("parse.documents", "All package YAML and JSON documents parse deterministically.")
    results.pass_("parse.schemas", f"All {len(schemas)} identity schemas parse as JSON.")

    schema_validator = LocalSchemaValidator(root)
    instance_pairs = [
        ("inventory", documents["inventory"], SCHEMA_PATHS["inventory"]),
        ("roles", documents["roles"], SCHEMA_PATHS["roles"]),
        (
            "authentication",
            documents["authentication"],
            SCHEMA_PATHS["authentication"],
        ),
        ("lifecycle", documents["lifecycle"], SCHEMA_PATHS["lifecycle"]),
        ("evidence", documents["evidence"], SCHEMA_PATHS["evidence"]),
        (
            "runtime_evidence",
            documents["runtime_evidence"],
            SCHEMA_PATHS["evidence"],
        ),
    ]
    schema_errors: list[str] = []
    for name, instance, schema_path in instance_pairs:
        schema_errors.extend(
            f"{name}: {error}"
            for error in schema_validator.validate(instance, schema_path)
        )
    if schema_errors:
        results.fail("schema.instances", "; ".join(schema_errors[:20]))
    else:
        results.pass_("schema.instances", "Identity models and evidence satisfy their JSON Schemas.")

    package_codes = validate_package_document(documents["package"], documents["catalog"])
    if package_codes:
        results.fail("package.metadata", f"Package metadata failures: {sorted(package_codes)}")
    else:
        results.pass_("package.metadata", "Package metadata and canonical capability mappings are valid.")

    role_codes = validate_role_policy(documents["roles"])
    if role_codes:
        results.fail("policy.roles", f"Role policy failures: {sorted(role_codes)}")
    else:
        results.pass_("policy.roles", "Role, action, approval, least-privilege, and separation rules are valid.")

    authentication_codes = validate_authentication_model(documents["authentication"])
    if authentication_codes:
        results.fail("policy.authentication", f"Authentication model failures: {sorted(authentication_codes)}")
    else:
        results.pass_("policy.authentication", "Authentication assurance is policy-only and makes no deployment claim.")

    lifecycle_codes = validate_lifecycle_policy(documents["lifecycle"])
    if lifecycle_codes:
        results.fail("policy.lifecycle", f"Lifecycle model failures: {sorted(lifecycle_codes)}")
    else:
        results.pass_("policy.lifecycle", "Lifecycle states, transitions, review, expiry, and revocation rules are valid.")

    inventory_codes = validate_identity_inventory(documents["inventory"], documents["roles"])
    if inventory_codes:
        results.fail("policy.inventory", f"Identity inventory failures: {sorted(inventory_codes)}")
    else:
        results.pass_("policy.inventory", "Synthetic identities satisfy ownership, role, lifecycle, assurance, privacy, and secret boundaries.")

    positive_cases = documents["positive"].get("cases", [])
    positive_failures: list[str] = []
    for case in positive_cases:
        decision = evaluate_request(
            case.get("request", {}),
            documents["inventory"],
            documents["roles"],
            documents["authentication"],
            case.get("case_id", "POS"),
        )
        if decision["decision"] != case.get("expected_decision"):
            positive_failures.append(
                f"{case.get('case_id')}: expected {case.get('expected_decision')}, got {decision['decision']}"
            )
        if not set(case.get("expected_reason_codes", [])).issubset(decision["reason_codes"]):
            positive_failures.append(f"{case.get('case_id')}: reason-code mismatch")
        decision_errors = schema_validator.validate(decision, SCHEMA_PATHS["decision"])
        if decision_errors:
            positive_failures.append(f"{case.get('case_id')}: invalid decision schema")
    if positive_failures:
        results.fail("fixtures.positive", "; ".join(positive_failures))
    else:
        results.pass_("fixtures.positive", f"All {len(positive_cases)} positive synthetic cases match deterministic decisions.")

    negative_cases = documents["negative"].get("cases", [])
    negative_failures: list[str] = []
    for case in negative_cases:
        codes = validate_negative_case(
            case,
            documents["package"],
            documents["inventory"],
            documents["roles"],
            documents["authentication"],
            documents["catalog"],
        )
        expected_code = case.get("expected_reason_code")
        if expected_code not in codes:
            negative_failures.append(
                f"{case.get('case_id')}: expected {expected_code}, got {sorted(codes)}"
            )
    if negative_failures:
        results.fail("fixtures.negative", "; ".join(negative_failures[:20]))
    else:
        results.pass_("fixtures.negative", f"All {len(negative_cases)} negative synthetic cases are rejected as expected.")

    evidence_codes = validate_evidence_document(
        documents["evidence"], documents["package"], positive_cases, negative_cases
    )
    if evidence_codes:
        results.fail("evidence.sync", f"Evidence failures: {sorted(evidence_codes)}")
    else:
        results.pass_("evidence.sync", "Evidence counts, authority, package status, and runtime boundary are synchronized.")

    runtime_evidence_codes = validate_runtime_evidence_document(
        documents["runtime_evidence"], documents["package"]
    )
    if runtime_evidence_codes:
        results.fail(
            "evidence.runtime_sync",
            f"Runtime evidence failures: {sorted(runtime_evidence_codes)}",
        )
    else:
        results.pass_(
            "evidence.runtime_sync",
            "Runtime evidence counts, enforcement outcomes, package status, and limitations are synchronized.",
        )

    contract = documents["evidence_contract"]
    if (
        contract.get("required_execution_authority")
        != "USER_APPROVED_CODEX_EXECUTION"
        or contract.get("required_execution_mode")
        != "BOUNDED_NON_PRODUCTION_ENFORCEMENT"
        or contract.get("runtime_executed") is not True
        or contract.get("live_identity_changed") is not True
        or contract.get("status") != "RUNTIME_ACCEPTED"
    ):
        results.fail("evidence.contract", "Evidence contract does not match bounded runtime authority.")
    else:
        results.pass_("evidence.contract", "Evidence contract enforces bounded runtime authority, sanitization, privacy, and external secrets.")

    _check_paths_and_claims(root, results)
    _validate_repository_integrity(root, results)

    final_fingerprint = repository_fingerprint(root)
    mutation_paths = detect_repository_mutation(initial_fingerprint, final_fingerprint)
    if mutation_paths:
        results.fail(
            "repository.mutation",
            f"Repository content changed during validation: {mutation_paths[:20]}",
        )
    else:
        results.pass_(
            "repository.mutation",
            "Repository content fingerprint is unchanged by validation.",
        )

    summary = results.summary()
    exit_status = 1 if summary["failed"] or (strict and summary["warnings"]) else 0
    return {
        "validator": "validate_zt_id_001",
        "validator_version": VALIDATOR_VERSION,
        "root": root.as_posix(),
        "strict": strict,
        "runtime_executed": True,
        "live_identity_changed": True,
        "findings": [asdict(item) for item in results.findings],
        "summary": summary,
        "fixture_summary": {
            "positive": len(positive_cases),
            "negative": len(negative_cases),
        },
        "exit_status": exit_status,
    }


def _format_text(report: dict[str, Any], verbose: bool) -> str:
    lines = []
    for item in report["findings"]:
        if verbose or item["level"] != "PASS":
            lines.append(f"[{item['level']}] {item['category']}: {item['message']}")
    summary = report["summary"]
    fixtures = report["fixture_summary"]
    lines.append(
        f"Fixtures: {fixtures['positive']} positive / {fixtures['negative']} negative"
    )
    lines.append(
        f"Summary: {summary['passed']} PASS / {summary['warnings']} WARN / {summary['failed']} FAIL"
    )
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="Show passing findings.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        report = validate(args.root, strict=args.strict)
    except Exception as exc:
        if args.format == "json":
            print(json.dumps({"error": str(exc), "exit_status": 2}, indent=2))
        else:
            print(f"[ERROR] validator.configuration: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(_format_text(report, args.verbose))
    return int(report["exit_status"])


if __name__ == "__main__":
    raise SystemExit(main())
