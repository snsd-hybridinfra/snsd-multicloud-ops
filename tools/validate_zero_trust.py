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
SCENARIO_ID_RE = re.compile(r"\bS(\d{3})\b")
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
    schema: dict[str, Any],
    root_schema: dict[str, Any] | None = None,
    path: str = "$",
) -> list[str]:
    """Validate the JSON Schema subset used by the repository schemas."""
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
        if "items" in schema:
            for index, item in enumerate(value):
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
    scenario_errors: list[str] = []
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
        if SCENARIO_ID_RE.search(item["future_scenario_boundary"]):
            scenario_errors.append(f"{capability_id}: future scenario boundary assigns or embeds a scenario ID")
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
    if scenario_errors:
        for error in scenario_errors:
            result.fail("backlog.scenarios", error)
    elif re.search(r"\bS(?:0(?:5[1-9]|[6-9]\d)|1(?:[0-4]\d|50))\b", json.dumps(backlog, ensure_ascii=False)):
        result.fail("backlog.scenarios", "Backlog contains an unauthorized future scenario ID.")
    else:
        result.passed("backlog.scenarios", "Backlog assigns no future scenario ID and leaves scenario creation approval-gated.")

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


def _scenario_directories(root: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in (root / "scenarios").glob("L*/S???-*"):
        if path.is_dir():
            scenario_id = path.name[:4]
            if scenario_id in result:
                result[scenario_id] = Path("<duplicate>")
            else:
                result[scenario_id] = path
    return result


def validate_scenarios(root: Path, result: ValidationResult) -> None:
    scenarios = _scenario_directories(root)
    expected = {f"S{number:03d}" for number in range(1, 51)}
    if set(scenarios) == expected and all(path != Path("<duplicate>") for path in scenarios.values()):
        result.passed("scenario.lock", "Exactly the locked S001-S050 scenario directories exist.")
    else:
        result.fail("scenario.lock", f"Scenario set differs; missing={sorted(expected-set(scenarios))}, extra={sorted(set(scenarios)-expected)}.")

    zero_trust_dir = root / "docs/zero-trust"
    bad_refs: list[str] = []
    for path in sorted(zero_trust_dir.glob("*")):
        if path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in SCENARIO_ID_RE.finditer(line):
                number = int(match.group(1))
                if 1 <= number <= 50:
                    if f"S{number:03d}" not in scenarios:
                        bad_refs.append(f"{path.relative_to(root)}:{line_number}: missing {match.group(0)}")
                elif 51 <= number <= 150:
                    allowed = path.name == "implementation-roadmap.md" and re.search(r"(?i)future|roadmap|planned|not created|not approved", line)
                    if not allowed:
                        bad_refs.append(f"{path.relative_to(root)}:{line_number}: unauthorized {match.group(0)}")
                else:
                    bad_refs.append(f"{path.relative_to(root)}:{line_number}: invalid {match.group(0)}")
    matrix_path = zero_trust_dir / "scenario-capability-matrix.md"
    rows = _markdown_table(matrix_path)
    seen: list[str] = []
    for row in rows:
        scenario_id = row.get("Scenario", "")
        seen.append(scenario_id)
        actual = scenarios.get(scenario_id)
        expected_name = actual.name[5:] if actual and actual != Path("<duplicate>") else None
        if expected_name and row.get("Name") != expected_name:
            bad_refs.append(f"{matrix_path.relative_to(root)}: {scenario_id} name does not match {expected_name}")
    if len(rows) != 50 or len(set(seen)) != 50:
        bad_refs.append("scenario-capability-matrix.md must contain exactly one row for each S001-S050")
    if bad_refs:
        for error in bad_refs:
            result.fail("scenario.references", error)
    else:
        result.passed("scenario.references", "Scenario references, names, roadmap ranges, and matrix rows are valid.")


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
    live_authorities = {"CODEX_EXECUTED_LIVE_RUNTIME", "USER_EXECUTED_RUNTIME"}
    if execution is None:
        if status in {"VALIDATED", "PARTIALLY_VALIDATED"} or authority in live_authorities:
            result.fail(category, "A router live-validation claim requires a machine-readable execution record.")
    else:
        if execution.get("execution_authority") not in live_authorities:
            result.fail(category, "Router execution authority must identify actual live runtime execution.")
        if execution.get("execution_authority") == "CODEX_EXECUTED_LIVE_RUNTIME" and not execution.get("commands"):
            result.fail(category, "Codex router runtime authority requires recorded commands.")
        if status in {"VALIDATED", "PARTIALLY_VALIDATED"}:
            results = execution.get("results")
            if not isinstance(results, dict) or results.get("exit_code") != 0 or results.get("fail") != 0:
                result.fail(category, "A live router validation status requires exit code 0 and zero failed checks.")
            boundary = execution.get("security_boundary")
            required = ("interactive_shell_blocked", "arbitrary_command_blocked", "configuration_command_blocked", "arbitrary_ping_blocked")
            if not isinstance(boundary, dict) or any(boundary.get(field) is not True for field in required):
                result.fail(category, "Router live validation requires all forced-command boundary tests.")
        if status == "VALIDATED" and execution.get("validation", {}).get("access_control") != "PASS":
            result.fail(category, "VALIDATED router package requires a passing persistent access-control result.")

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
        if package.get("validation_status") in {"VALIDATED", "PARTIALLY_VALIDATED"} and (results.get("exit_code") != 0 or results.get("fail") != 0):
            result.fail("package.zt-vis-001", "Telemetry live-validation status requires exit code 0 and zero failed checks.")
        if package.get("validation_status") == "VALIDATED" and results.get("unavailable_sources", 0) != 0:
            result.fail("package.zt-vis-001", "VALIDATED telemetry package cannot have unavailable mandatory sources.")

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
    if not any(item.level == "FAIL" and item.category.startswith("package.zt-vis-001") for item in result.findings):
        result.passed("package.zt-vis-001", "ZT-VIS-001 inventory, schemas, deterministic rules, runtime record, and non-blocking boundary are consistent.")


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
    if not any(item.level == "FAIL" and item.category.startswith("schema.") for item in result.findings):
        validate_catalog_baseline_sync(catalog, baseline, result)
        validate_maturity(catalog["capabilities"], result, "catalog")
        validate_maturity(baseline["capabilities"], result, "baseline")
        validate_evidence(root, baseline, result)
    validate_scenarios(root, result)
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
