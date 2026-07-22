from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_zero_trust as core  # noqa: E402


ARCH_ROOT = Path("docs/zero-trust/target-architecture")
SELECTION_PATH = ARCH_ROOT / "capability-selection.yaml"
TRACEABILITY_PATH = ARCH_ROOT / "capability-traceability-matrix.yaml"
SCOPE_PATH = ARCH_ROOT / "advanced-maturity-scope.yaml"
ACCEPTANCE_PATH = ARCH_ROOT / "advanced-maturity-acceptance-model.yaml"
DEPENDENCY_PATH = ARCH_ROOT / "implementation-dependency-map.yaml"
ONBOARDING_PATH = ARCH_ROOT / "host-onboarding-contract.yaml"
HANDOFF_PATH = ARCH_ROOT / "handoff-acceptance-model.yaml"
OPTIMAL_PATH = ARCH_ROOT / "optimal-expansion-roadmap.yaml"

OFFICIAL_MATURITY = {"TRADITIONAL", "INITIAL", "ADVANCED", "OPTIMAL"}
ASSESSMENT_STATES = {"UNASSESSED", "NOT_APPLICABLE"}
SELECTIONS = {
    "ADVANCED_PRIMARY_TARGET",
    "ADVANCED_SUPPORTING_TARGET",
    "INITIAL_TARGET",
    "DESIGN_ONLY",
    "OPTIMAL_ROADMAP_ONLY",
    "NOT_APPLICABLE",
    "UNASSESSED",
}
RUNBOOK_STATUSES = {
    "DESIGN_SPECIFICATION",
    "IMPLEMENTED_NOT_VALIDATED",
    "VALIDATED_LOCAL",
    "VALIDATED_RUNTIME",
    "NOT_IMPLEMENTED",
}

REQUIRED_ARCHITECTURE_FILES = [
    "README.md",
    "project-objective.md",
    "advanced-maturity-scope.md",
    "advanced-maturity-scope.yaml",
    "capability-selection-method.md",
    "capability-selection.yaml",
    "capability-traceability-matrix.md",
    "capability-traceability-matrix.yaml",
    "iac-cac-pac-reference-architecture.md",
    "target-portability-architecture.md",
    "host-onboarding-contract.md",
    "operator-interface-contract.md",
    "advanced-maturity-acceptance-model.md",
    "advanced-maturity-acceptance-model.yaml",
    "optimal-readiness-architecture.md",
    "optimal-expansion-roadmap.md",
    "phase-roadmap.md",
    "golden-path.md",
    "implementation-dependency-map.md",
    "implementation-dependency-map.yaml",
    "handoff-acceptance-model.md",
    "portfolio-positioning.md",
    "limitations.md",
]

REQUIRED_RUNBOOKS = [f"{number:02d}-{slug}.md" for number, slug in [
    (0, "platform-overview"), (1, "prerequisites"), (2, "target-selection"),
    (3, "openstack-vm-onboarding"), (4, "existing-vm-onboarding"),
    (5, "physical-server-onboarding"), (6, "environment-profile"),
    (7, "secret-preparation"), (8, "preflight-validation"), (9, "iac-plan"),
    (10, "policy-evaluation"), (11, "deployment-approval"),
    (12, "platform-deployment"), (13, "runtime-validation"),
    (14, "platform-status"), (15, "drift-detection"), (16, "reconciliation"),
    (17, "backup"), (18, "restore"), (19, "rollback"), (20, "upgrade"),
    (21, "secret-rotation"), (22, "certificate-rotation"),
    (23, "incident-response"), (24, "target-replacement"), (25, "decommission"),
    (26, "evidence-handling"), (27, "operator-handoff"), (28, "troubleshooting"),
]]

RUNBOOK_HEADINGS = [
    "Purpose", "Scope", "Supported target types", "Current implementation status",
    "Current validation status", "Required authority", "Prerequisites", "Inputs",
    "Secret inputs", "Service impact", "Security impact", "Preflight checks",
    "Procedure", "Expected output", "Validation", "Pass criteria", "Stop conditions",
    "Failure handling", "Rollback", "Evidence", "Escalation", "Known limitations",
    "Related architecture", "Related package",
]

SCHEMA_INSTANCES = [
    ("schemas/zero-trust-advanced-maturity-scope.schema.json", SCOPE_PATH),
    ("schemas/zero-trust-capability-selection.schema.json", SELECTION_PATH),
    ("schemas/zero-trust-capability-traceability.schema.json", TRACEABILITY_PATH),
    ("schemas/zero-trust-advanced-acceptance.schema.json", ACCEPTANCE_PATH),
    ("schemas/zero-trust-host-onboarding-contract.schema.json", ONBOARDING_PATH),
    ("schemas/zero-trust-implementation-dependency-map.schema.json", DEPENDENCY_PATH),
    ("schemas/zero-trust-handoff-acceptance.schema.json", HANDOFF_PATH),
    ("schemas/zero-trust-optimal-roadmap.schema.json", OPTIMAL_PATH),
]


@dataclass
class Finding:
    level: str
    category: str
    message: str


@dataclass
class ValidationResult:
    findings: list[Finding] = field(default_factory=list)

    def passed(self, category: str, message: str) -> None:
        self.findings.append(Finding("PASS", category, message))

    def warn(self, category: str, message: str) -> None:
        self.findings.append(Finding("WARN", category, message))

    def fail(self, category: str, message: str) -> None:
        self.findings.append(Finding("FAIL", category, message))

    @property
    def counts(self) -> Counter[str]:
        return Counter(item.level for item in self.findings)


def load(path: Path) -> Any:
    return core.load_json_yaml(path)


def _has_failures(result: ValidationResult, prefix: str) -> bool:
    return any(item.level == "FAIL" and item.category.startswith(prefix) for item in result.findings)


def validate_required_files(root: Path, result: ValidationResult) -> None:
    missing = [str(ARCH_ROOT / name) for name in REQUIRED_ARCHITECTURE_FILES if not (root / ARCH_ROOT / name).is_file()]
    if missing:
        for path in missing:
            result.fail("files.architecture", f"missing authoritative architecture file: {path}")
    else:
        result.passed("files.architecture", f"All {len(REQUIRED_ARCHITECTURE_FILES)} required target-architecture files exist.")

    required_adrs = list(range(3, 9))
    found = {int(path.name[:4]) for path in (root / "docs/adr").glob("000[3-8]-*.md")}
    missing_adrs = sorted(set(required_adrs) - found)
    if missing_adrs:
        result.fail("files.adr", f"missing ADR numbers: {missing_adrs}")
    else:
        result.passed("files.adr", "All six architecture decisions exist.")


def validate_schema_files(root: Path, result: ValidationResult) -> None:
    pairs = list(SCHEMA_INSTANCES)
    profile_schema = "schemas/zero-trust-target-profile.schema.json"
    for target in ("openstack-vm", "existing-vm", "physical-server"):
        pairs.append((profile_schema, Path(f"profiles/templates/{target}/profile.yaml")))
    for schema_rel, instance_rel in pairs:
        try:
            schema = core.load_schema(root / schema_rel)
            value = load(root / instance_rel)
            errors = core.validate_schema_instance(value, schema)
        except ValueError as exc:
            result.fail("schema", str(exc))
            continue
        if errors:
            for error in errors:
                result.fail("schema", f"{instance_rel}: {error}")
        else:
            result.passed("schema", f"{instance_rel} conforms to {schema_rel}.")


def validate_selection_data(selection: dict[str, Any], catalog: dict[str, Any], result: ValidationResult) -> None:
    items = selection.get("capabilities", [])
    canonical_ids = {item["id"] for item in catalog.get("capabilities", [])}
    ids = [item.get("id") for item in items]
    if len(items) != 52:
        result.fail("selection.coverage", f"expected 52 capabilities, found {len(items)}")
    if len(ids) != len(set(ids)):
        result.fail("selection.coverage", "duplicate capability ID detected")
    if set(ids) != canonical_ids:
        result.fail("selection.coverage", f"canonical coverage differs; missing={sorted(canonical_ids-set(ids))}, extra={sorted(set(ids)-canonical_ids)}")
    if not _has_failures(result, "selection.coverage"):
        result.passed("selection.coverage", "Selection represents every canonical capability exactly once.")

    for item in items:
        capability_id = item.get("id", "<missing>")
        classification = item.get("selection")
        if classification not in SELECTIONS:
            result.fail("selection.classification", f"{capability_id}: invalid selection {classification!r}")
        target = item.get("target_maturity")
        if target == "OPTIMAL_READY" or (target is not None and target not in OFFICIAL_MATURITY | ASSESSMENT_STATES):
            result.fail("selection.maturity", f"{capability_id}: invalid official maturity value {target!r}")
        summaries = item.get("source_maturity_summary", {})
        if set(summaries) != OFFICIAL_MATURITY or any(not summaries.get(level) for level in OFFICIAL_MATURITY):
            result.fail("selection.source", f"{capability_id}: four source maturity summaries are required")
        if classification in {"ADVANCED_PRIMARY_TARGET", "ADVANCED_SUPPORTING_TARGET"}:
            if len(item.get("rationale", "")) < 40:
                result.fail("selection.advanced", f"{capability_id}: Advanced target lacks rationale")
            requirements = " ".join(item.get("evidence_requirements", [])).lower()
            if "runtime" not in requirements:
                result.fail("selection.advanced", f"{capability_id}: Advanced target lacks runtime evidence requirement")
        if classification == "OPTIMAL_ROADMAP_ONLY":
            if item.get("roadmap_status") != "ROADMAP_ONLY":
                result.fail("selection.optimal", f"{capability_id}: Optimal item is not roadmap-only")
            if item.get("current_maturity") != "UNASSESSED":
                result.fail("selection.optimal", f"{capability_id}: Optimal roadmap item promotes current maturity")
    if not _has_failures(result, "selection.classification") and not _has_failures(result, "selection.maturity") and not _has_failures(result, "selection.source") and not _has_failures(result, "selection.advanced") and not _has_failures(result, "selection.optimal"):
        result.passed("selection.rules", "Selection, maturity values, rationales, evidence requirements, and Optimal boundaries are valid.")


def validate_scope_data(scope: dict[str, Any], result: ValidationResult) -> None:
    if "repository_maturity" in scope or scope.get("current_maturity") in {"ADVANCED", "OPTIMAL"}:
        result.fail("scope.maturity", "repository-wide Advanced or Optimal maturity assignment is prohibited")
    designation = scope.get("architecture_designation", {})
    if designation.get("value") != "OPTIMAL_READY" or designation.get("official_maturity_level") is not False:
        result.fail("scope.optimal-ready", "OPTIMAL_READY must be repository-local and non-official")
    responsibilities = scope.get("responsibilities", {})
    sets = {name: set(responsibilities.get(name, [])) for name in ("iac", "cac", "pac")}
    for left, right in (("iac", "cac"), ("iac", "pac"), ("cac", "pac")):
        overlap = sorted(sets[left] & sets[right])
        if overlap:
            result.fail("scope.responsibility", f"{left}/{right} responsibility conflict: {overlap}")
    if scope.get("policy_default") != "DENY_BY_DEFAULT_FOR_UNREGISTERED_CHANGE":
        result.fail("scope.policy", "Policy as Code lacks required deny-by-default behavior")
    validate_adapter_claims(scope.get("provider_adapters", []), result)
    if not any(item.level == "FAIL" and item.category.startswith("scope.") for item in result.findings):
        result.passed("scope", "Maturity, responsibility, default-deny, and adapter boundaries are valid.")


def validate_adapter_claims(adapters: list[dict[str, Any]], result: ValidationResult) -> None:
    by_id = {item.get("id"): item for item in adapters}
    for adapter_id in ("existing-vm", "physical-server"):
        item = by_id.get(adapter_id, {})
        if item.get("provisions_compute") is not False:
            result.fail("scope.adapter", f"{adapter_id} must not be marked IaC-provisioned")
    for adapter_id in ("aws", "azure"):
        item = by_id.get(adapter_id, {})
        if item.get("status") != "ROADMAP_ONLY" or item.get("provisions_compute") is not False:
            result.fail("scope.adapter", f"{adapter_id} implementation claim is unsupported")


def validate_acceptance_data(acceptance: dict[str, Any], selection: dict[str, Any], result: ValidationResult) -> None:
    expected = {item["id"] for item in selection.get("capabilities", []) if item.get("selection") in {"ADVANCED_PRIMARY_TARGET", "ADVANCED_SUPPORTING_TARGET"}}
    rows = acceptance.get("capabilities", [])
    ids = [item.get("id") for item in rows]
    if set(ids) != expected or len(ids) != len(set(ids)):
        result.fail("acceptance.coverage", "Advanced acceptance rows do not match selected Advanced capabilities")
    for item in rows:
        capability_id = item.get("id", "<missing>")
        if not item.get("advanced_stage_requirement"):
            result.fail("acceptance.requirement", f"{capability_id}: missing Advanced-stage requirement")
        if item.get("runtime_evidence_required") is not True:
            result.fail("acceptance.evidence", f"{capability_id}: runtime evidence must be required")
        if item.get("result") == "ADVANCED_VALIDATED":
            result.fail("acceptance.claim", f"{capability_id}: architecture package cannot pre-assign ADVANCED_VALIDATED")
        if not item.get("limitation") or not item.get("assessor_rationale"):
            result.fail("acceptance.rationale", f"{capability_id}: limitation and assessor rationale are required")
    if not _has_failures(result, "acceptance."):
        result.passed("acceptance", "Advanced acceptance coverage and evidence gates are valid; no capability is pre-validated.")


def validate_dependency_data(dependency: dict[str, Any], result: ValidationResult) -> None:
    phases = dependency.get("phases", [])
    if len(phases) != 6:
        result.fail("roadmap.phases", f"expected six phases, found {len(phases)}")
    for phase in phases:
        if not phase.get("entry_criteria") or not phase.get("exit_criteria"):
            result.fail("roadmap.gates", f"{phase.get('id')}: entry and exit criteria are required")
    for package_id, status in dependency.get("package_status", {}).items():
        if package_id == "ZT-ID-001":
            expected_identity_status = {
                "package_state": "PRESENT",
                "phase": "PHASE_1_CURRENT",
                "implementation_status": "IMPLEMENTED",
                "validation_status": "RUNTIME_VALIDATED",
                "runtime_validation_status": "VALIDATED",
                "runtime_acceptance_status": "ACCEPTED",
                "runtime_scope": "BOUNDED_NON_PRODUCTION_TARGET",
                "maturity_status": "UNASSESSED",
                "phase_2_dependency_status": "OPEN",
                "roadmap_status": "BOUNDED_RUNTIME_PACKAGE",
            }
            if status != expected_identity_status:
                result.fail(
                    "roadmap.package-status",
                    "ZT-ID-001 must remain bounded to accepted non-production runtime scope with no centralized, production, or maturity promotion",
                )
            continue
        if package_id == "ZT-DEV-001":
            expected_endpoint_status = {
                "package_state": "PRESENT",
                "phase": "PHASE_1_CURRENT",
                "implementation_status": "IMPLEMENTED",
                "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
                "runtime_scope": "ONE_MANDATORY_NON_PRODUCTION_VM",
                "maturity_status": "UNASSESSED",
                "roadmap_status": "BOUNDED_RUNTIME_PACKAGE",
            }
            if status != expected_endpoint_status:
                result.fail(
                    "roadmap.package-status",
                    "ZT-DEV-001 must remain bounded to partial non-production runtime scope without broad management, enforcement, or maturity promotion",
                )
            continue
        if package_id == "ZT-APP-001":
            expected_application_status = {
                "package_state": "PRESENT",
                "phase": "PHASE_1_CURRENT",
                "implementation_status": "IMPLEMENTED",
                "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
                "runtime_scope": "ONE_EXISTING_NON_CRITICAL_ALLOY_PILOT",
                "maturity_status": "UNASSESSED",
                "roadmap_status": "BOUNDED_RUNTIME_PACKAGE",
            }
            if status != expected_application_status:
                result.fail(
                    "roadmap.package-status",
                    "ZT-APP-001 must remain bounded to partial runtime scope without deployment, provenance, vulnerability, enforcement, or maturity promotion",
                )
            continue
        if package_id == "ZT-DATA-001":
            expected_data_status = {
                "package_state": "PRESENT",
                "phase": "PHASE_1_CURRENT",
                "implementation_status": "IMPLEMENTED",
                "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
                "runtime_scope": "SEVEN_METADATA_ASSETS_AND_ONE_SYNTHETIC_RESTORE",
                "maturity_status": "UNASSESSED",
                "roadmap_status": "BOUNDED_RUNTIME_PACKAGE",
            }
            if status != expected_data_status:
                result.fail(
                    "roadmap.package-status",
                    "ZT-DATA-001 must remain bounded to partial metadata, detection-only DLP, synthetic restore, and unassessed maturity scope",
                )
            continue
        if package_id == "ZT-SYS-001":
            expected_system_status = {
                "package_state": "PRESENT",
                "phase": "PHASE_1_CURRENT",
                "implementation_status": "IMPLEMENTED",
                "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
                "runtime_scope": "SEVEN_SYSTEMS_EXISTING_FIXED_READ_ONLY_VALIDATORS_AND_FIVE_SAFE_CONFIGURATION_HASHES",
                "maturity_status": "UNASSESSED",
                "roadmap_status": "BOUNDED_RUNTIME_PACKAGE",
            }
            if status != expected_system_status:
                result.fail(
                    "roadmap.package-status",
                    "ZT-SYS-001 must remain bounded to partial runtime system scope with CURRENT_DEGRADED OpenStack and without complete PAM, FIM, recovery, or maturity promotion",
                )
            continue
        if package_id == "ZT-AUTO-001":
            expected_automation_status = {
                "package_state": "PRESENT",
                "phase": "PHASE_1_CURRENT",
                "implementation_status": "IMPLEMENTED",
                "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
                "runtime_scope": "SINGLE_WORKSTATION_FIXED_R0_R3_HANDLERS_AND_ONE_PARTIAL_CROSS_DOMAIN_READ_ONLY_EXECUTION",
                "maturity_status": "UNASSESSED",
                "roadmap_status": "BOUNDED_RUNTIME_PACKAGE",
            }
            if status != expected_automation_status:
                result.fail(
                    "roadmap.package-status",
                    "ZT-AUTO-001 must remain bounded to partial fixed-handler R0-R3 runtime scope without mutation, response, repeatability, scheduling, SOAR, or maturity promotion",
                )
            continue
        implementation = status.get("implementation_status")
        if implementation in {"IMPLEMENTED", "COMPLETED", "VALIDATED"}:
            result.fail("roadmap.package-status", f"{package_id}: roadmap package is improperly marked {implementation}")
    phase6 = next((phase for phase in phases if phase.get("id") == "FUTURE_PHASE_6"), None)
    if not phase6 or phase6.get("current_state") != "ROADMAP_ONLY":
        result.fail("roadmap.optimal", "Future Phase 6 must remain roadmap-only")
    if phase6:
        for package_id in phase6.get("packages", []):
            status = dependency.get("package_status", {}).get(package_id, {})
            if status != {"implementation_status": "NOT_STARTED", "validation_status": "UNASSESSED", "roadmap_status": "ROADMAP_ONLY"}:
                result.fail("roadmap.optimal", f"{package_id}: invalid future Optimal status")
    if not _has_failures(result, "roadmap."):
        result.passed("roadmap", "All phases have gates; ZT-ID-001, ZT-DEV-001, ZT-APP-001, ZT-DATA-001, ZT-SYS-001, and ZT-AUTO-001 remain bounded runtime packages and roadmap packages remain unimplemented.")


def validate_package_data(package: dict[str, Any], result: ValidationResult) -> None:
    expected = {
        "package_id": "ZT-ARC-001",
        "package_type": "ARCHITECTURE_GOVERNANCE",
        "phase": "CROSS_PHASE_GOVERNANCE",
        "implementation_status": "DESIGN_ONLY",
        "validation_status": "LOCAL_VALIDATED",
        "runtime_validation_status": "NOT_VALIDATED",
        "maturity_status": "UNASSESSED",
        "current_maturity": "UNASSESSED",
        "target_maturity": "ADVANCED",
        "advanced_claim": False,
        "optimal_claim": False,
        "optimal_ready": True,
        "architecture_designation": "OPTIMAL_READY",
        "architecture_designation_is_official_maturity": False,
        "architecture_authority": "AUTHORITATIVE_AFTER_NORMALIZATION",
        "authority_status": "AUTHORITATIVE",
    }
    mismatches = {
        key: {"expected": expected_value, "actual": package.get(key)}
        for key, expected_value in expected.items()
        if package.get(key) != expected_value
    }
    if mismatches:
        result.fail("package.metadata", f"ZT-ARC-001 authority metadata mismatch: {mismatches}")
    else:
        result.passed("package.metadata", "ZT-ARC-001 is authoritative design governance without runtime or maturity claims.")


def _walk_pairs(value: Any, prefix: str = "") -> list[tuple[str, Any]]:
    pairs: list[tuple[str, Any]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else key
            pairs.append((path, item))
            pairs.extend(_walk_pairs(item, path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            pairs.extend(_walk_pairs(item, f"{prefix}[{index}]"))
    return pairs


def validate_profile_data(profile: dict[str, Any], result: ValidationResult, name: str = "profile") -> None:
    secret_key = re.compile(r"(?i)(?:password|passwd|token|client[_-]?secret|private[_-]?key|mfa[_-]?(?:seed|material)|recovery[_-]?code)")
    private_value = re.compile(r"(?i)(?:id_rsa|id_ed25519|\.pem$|\.key$|private[_-]?key)")
    for path, value in _walk_pairs(profile):
        key = path.split(".")[-1].split("[")[0]
        if secret_key.search(key):
            result.fail("profile.secret", f"{name}: forbidden secret field {path}")
        if isinstance(value, str) and private_value.search(value):
            result.fail("profile.private-key", f"{name}: private-key path or value is forbidden at {path}")
    target = profile.get("metadata", {}).get("target_type")
    provisions = profile.get("provider", {}).get("provisions_compute")
    if target in {"existing-vm", "physical-server"} and provisions is not False:
        result.fail("profile.provisioning", f"{name}: {target} must not be marked provisioned")
    if not any(item.level == "FAIL" and item.message.startswith(f"{name}:") for item in result.findings):
        result.passed("profile", f"{name} contains no secret fields and preserves provisioning semantics.")


def validate_runbook_text(text: str, result: ValidationResult, name: str = "runbook") -> None:
    for heading in RUNBOOK_HEADINGS:
        if re.search(rf"(?m)^## {re.escape(heading)}\s*$", text) is None:
            result.fail("runbook.structure", f"{name}: missing heading {heading}")
    status_match = re.search(r"(?ms)^## Current implementation status\s+`?([A-Z_]+)`?", text)
    if not status_match or status_match.group(1) not in RUNBOOK_STATUSES:
        result.fail("runbook.status", f"{name}: missing or invalid implementation status")
    rollback_match = re.search(r"(?ms)^## Rollback\s+(.+?)(?=^## |\Z)", text)
    if not rollback_match or len(rollback_match.group(1).strip()) < 20 or rollback_match.group(1).strip() == "<required>":
        result.fail("runbook.rollback", f"{name}: rollback is missing or empty")


def validate_runbooks(root: Path, result: ValidationResult) -> None:
    runbook_root = root / "docs/runbooks"
    missing = [name for name in REQUIRED_RUNBOOKS if not (runbook_root / name).is_file()]
    if missing:
        result.fail("runbook.index", f"missing runbooks: {missing}")
    for name in REQUIRED_RUNBOOKS:
        path = runbook_root / name
        if path.is_file():
            validate_runbook_text(path.read_text(encoding="utf-8"), result, name)
    index = runbook_root / "RUNBOOK_INDEX.md"
    if not index.is_file() or any(name not in index.read_text(encoding="utf-8") for name in REQUIRED_RUNBOOKS):
        result.fail("runbook.index", "RUNBOOK_INDEX.md does not list every required runbook")
    if not _has_failures(result, "runbook."):
        result.passed("runbook", f"All {len(REQUIRED_RUNBOOKS)} runbooks have status, rollback, and required structure.")


def validate_policy_contract(text: str, result: ValidationResult) -> None:
    if "DENY_BY_DEFAULT_FOR_UNREGISTERED_CHANGE" not in text or "DENY" not in text:
        result.fail("policy.deny", "Policy as Code contract lacks required deny behavior")
    else:
        result.passed("policy.deny", "Policy as Code contract defines required deny behavior.")


def validate_scenario_text(text: str, result: ValidationResult, name: str = "text") -> None:
    if re.search(r"\bS051\b", text):
        result.fail("scenario.lock", f"{name}: unsupported S051 reference")


def validate_tracked_runtime_paths(paths: list[str], result: ValidationResult) -> None:
    tracked = [path for path in paths if path.replace("\\", "/").startswith(".runtime/")]
    if tracked:
        result.fail("runtime.tracking", f"tracked runtime files found: {tracked}")
    else:
        result.passed("runtime.tracking", "No runtime files are tracked.")


def validate_repository_safety(root: Path, result: ValidationResult) -> None:
    candidates = list((root / ARCH_ROOT).rglob("*.md")) + list((root / ARCH_ROOT).rglob("*.yaml"))
    candidates += list((root / "docs/runbooks").glob("*.md")) + list((root / "profiles").rglob("*.yaml"))
    for path in candidates:
        validate_scenario_text(path.read_text(encoding="utf-8", errors="replace"), result, str(path.relative_to(root)))
    if not _has_failures(result, "scenario.lock"):
        result.passed("scenario.lock", "Architecture, profiles, and runbooks contain no unsupported scenario expansion reference.")

    process = subprocess.run(["git", "ls-files", ".runtime"], cwd=root, capture_output=True, text=True, encoding="utf-8")
    validate_tracked_runtime_paths([line for line in process.stdout.splitlines() if line.strip()], result)

    core_result = core.ValidationResult()
    core.validate_sensitive_data(root, core_result)
    sensitive = [item for item in core_result.findings if item.level == "FAIL"]
    if sensitive:
        for item in sensitive:
            result.fail("secret", item.message)
    else:
        result.passed("secret", "No tracked or unignored architecture secret pattern was detected.")


def validate_mermaid(root: Path, result: ValidationResult) -> None:
    blocks: list[str] = []
    for path in (root / ARCH_ROOT).glob("*.md"):
        text = path.read_text(encoding="utf-8")
        blocks.extend(re.findall(r"```mermaid\s*(.*?)```", text, flags=re.DOTALL))
    if len(blocks) < 10:
        result.fail("diagram.count", f"expected at least 10 Mermaid diagrams, found {len(blocks)}")
    for index, block in enumerate(blocks, 1):
        first = next((line.strip() for line in block.splitlines() if line.strip()), "")
        if not (first.startswith("flowchart ") or first.startswith("sequenceDiagram")):
            result.fail("diagram.syntax", f"diagram {index}: unsupported or missing diagram declaration")
    if not _has_failures(result, "diagram."):
        result.passed("diagram", f"Found {len(blocks)} Mermaid diagrams with recognized declarations.")


def run_validation(root: Path = ROOT, strict: bool = False) -> ValidationResult:
    result = ValidationResult()
    validate_required_files(root, result)
    validate_schema_files(root, result)
    try:
        catalog = load(root / "docs/zero-trust/capability-catalog.yaml")
        selection = load(root / SELECTION_PATH)
        scope = load(root / SCOPE_PATH)
        acceptance = load(root / ACCEPTANCE_PATH)
        dependency = load(root / DEPENDENCY_PATH)
    except ValueError as exc:
        result.fail("configuration", str(exc))
        return result
    validate_selection_data(selection, catalog, result)
    validate_scope_data(scope, result)
    validate_acceptance_data(acceptance, selection, result)
    validate_dependency_data(dependency, result)
    for target in ("openstack-vm", "existing-vm", "physical-server"):
        validate_profile_data(load(root / f"profiles/templates/{target}/profile.yaml"), result, target)
    validate_runbooks(root, result)
    validate_policy_contract((root / ARCH_ROOT / "iac-cac-pac-reference-architecture.md").read_text(encoding="utf-8"), result)
    validate_repository_safety(root, result)
    validate_mermaid(root, result)
    package = load(root / "docs/zero-trust/packages/zt-arc-001-package.yaml")
    validate_package_data(package, result)
    if strict:
        for item in list(result.findings):
            if item.level == "WARN":
                result.fail("strict", f"warning promoted to failure: {item.category}: {item.message}")
    return result


def render_text(result: ValidationResult, verbose: bool) -> None:
    for item in result.findings:
        if verbose or item.level != "PASS":
            print(f"[{item.level}] {item.category}: {item.message}")
    counts = result.counts
    print("\nAdvanced target architecture validation summary:")
    print(f"  Passed checks: {counts['PASS']}")
    print(f"  Warnings: {counts['WARN']}")
    print(f"  Failed checks: {counts['FAIL']}")
    print(f"  Exit status: {0 if counts['FAIL'] == 0 else 1}")


def render_json(result: ValidationResult) -> None:
    counts = result.counts
    print(json.dumps({
        "findings": [item.__dict__ for item in result.findings],
        "summary": {"passed": counts["PASS"], "warnings": counts["WARN"], "failed": counts["FAIL"]},
        "exit_status": 0 if counts["FAIL"] == 0 else 1,
    }, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the authoritative Advanced target architecture.")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = run_validation(ROOT, args.strict)
    if args.format == "json":
        render_json(result)
    else:
        render_text(result, args.verbose)
    return 1 if result.counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
