#!/usr/bin/env python3
"""Validate retirement of the numbered scenario framework without mutating the repository."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import validate_zero_trust as core

ROOT = Path(__file__).resolve().parents[1]
FLOW_PATH = Path("docs/zero-trust/package-flow.yaml")
FLOW_SCHEMA = Path("schemas/zero-trust-package-flow.schema.json")
ACTION_ROOT = Path("docs/zero-trust/recovery/ZT-SCN-RETIRE-001")
MIGRATION_DOC = Path("docs/zero-trust/governance/scenario-framework-retirement.md")

EXPECTED_SEQUENCE = [
    "ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001",
    "ZT-CV-001", "ZT-RV-001", "ZT-SCH-001", "P1-ACC-001",
]
EXPECTED_PACKAGE_STATES = {
    "ZT-FND-001": ("IMPLEMENTED", "RUNTIME_VALIDATED"),
    "ZT-NET-001": ("IMPLEMENTED", "RUNTIME_VALIDATED"),
    "ZT-VIS-001": ("IMPLEMENTED", "RUNTIME_VALIDATED"),
    "ZT-ID-001": ("IMPLEMENTED", "RUNTIME_VALIDATED"),
    "ZT-CV-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
    "ZT-RV-001": ("IMPLEMENTED", "RUNTIME_VALIDATED"),
    "ZT-SCH-001": ("IMPLEMENTED", "LOCAL_VALIDATED"),
    "ZT-ARC-001": ("DESIGN_ONLY", "LOCAL_VALIDATED"),
}
RETIRED_PATHS = [
    Path("scenarios"),
    Path("evidence/L1-foundation"), Path("evidence/L2-security-baseline"),
    Path("evidence/L3-service-operations"), Path("evidence/L4-failure-recovery"),
    Path("evidence/L5-governance-intelligent-ops"),
    Path("tools/validate-all-scenarios.ps1"),
    Path("tools/validate-scenario-quality.ps1"),
    Path("tools/generate-final-evidence-report.ps1"),
]
NUMBERED_ID = re.compile(r"\bS(?:00[1-9]|0[1-4][0-9]|050|051)\b")
NUMBERED_PATH = re.compile(r"(?:^|[\\/])S(?:00[1-9]|0[1-4][0-9]|050)(?:[-\\/]|$)")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".ps1", ".txt", ".example", ".tf", ".j2"}
RETIRED_AGGREGATE_TOOL = re.compile(r"(?i)(?:scenario.*aggregate|aggregate.*scenario)")


@dataclass
class Finding:
    level: str
    category: str
    message: str


@dataclass
class Result:
    findings: list[Finding] = field(default_factory=list)

    def passed(self, category: str, message: str) -> None:
        self.findings.append(Finding("PASS", category, message))

    def fail(self, category: str, message: str) -> None:
        self.findings.append(Finding("FAIL", category, message))

    @property
    def failed(self) -> int:
        return sum(item.level == "FAIL" for item in self.findings)


def tracked_paths(root: Path) -> list[Path]:
    process = subprocess.run(
        ["git", "ls-files"], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or "git ls-files failed")
    return [Path(line) for line in process.stdout.splitlines() if line.strip()]


def validate_flow(root: Path, result: Result) -> None:
    try:
        flow = core.load_json_yaml(root / FLOW_PATH)
        schema = core.load_schema(root / FLOW_SCHEMA)
    except ValueError as exc:
        result.fail("flow.parse", str(exc))
        return
    errors = core.validate_schema_instance(flow, schema)
    if errors:
        for error in errors:
            result.fail("flow.schema", error)
    else:
        result.passed("flow.schema", "Package flow conforms to its schema.")
    sequence = flow.get("phase_1_sequence")
    package_ids = [item.get("package_id") for item in flow.get("packages", [])]
    if sequence == EXPECTED_SEQUENCE and package_ids == EXPECTED_SEQUENCE[:-1] and len(package_ids) == len(set(package_ids)):
        result.passed("flow.sequence", "Canonical Phase 1 package flow is ordered and unique.")
    else:
        result.fail("flow.sequence", f"Unexpected flow: sequence={sequence}, packages={package_ids}")
    for index, row in enumerate(flow.get("packages", [])):
        expected = None if index == 0 else package_ids[index - 1]
        if row.get("predecessor") != expected:
            result.fail("flow.predecessor", f"{row.get('package_id')}: expected predecessor {expected!r}")
    acceptance = flow.get("phase_1_acceptance", {})
    expected_acceptance = {
        "implementation_status": "PARTIAL", "validation_status": "PARTIALLY_VALIDATED",
        "completion_status": "NOT_COMPLETE", "scope_boundary": "ZT-SCH-001",
        "requires_all_predecessors_accepted": True,
    }
    if acceptance == expected_acceptance:
        result.passed("flow.acceptance", "Phase 1 remains NOT_COMPLETE at the scheduled-validation boundary.")
    else:
        result.fail("flow.acceptance", "Phase 1 acceptance state is overclaimed or inconsistent.")


def validate_package_truth(root: Path, result: Result) -> None:
    errors: list[str] = []
    for package_id, (implementation, validation) in EXPECTED_PACKAGE_STATES.items():
        path = root / "docs/zero-trust/packages" / f"{package_id.lower()}-package.yaml"
        if not path.is_file():
            errors.append(f"missing {path.relative_to(root)}")
            continue
        try:
            record = core.load_json_yaml(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if record.get("implementation_status") != implementation or record.get("validation_status") != validation:
            errors.append(
                f"{package_id}: expected {implementation}/{validation}, "
                f"found {record.get('implementation_status')}/{record.get('validation_status')}"
            )
        if package_id == "ZT-ARC-001":
            if record.get("runtime_validation_status") != "NOT_VALIDATED" or record.get("maturity_status") != "UNASSESSED":
                errors.append(f"{package_id}: runtime or maturity boundary changed")
        if package_id == "ZT-ID-001":
            if (
                record.get("runtime_validation_status") != "VALIDATED"
                or record.get("runtime_acceptance_status") != "ACCEPTED"
                or record.get("runtime_scope") != "BOUNDED_NON_PRODUCTION_TARGET"
                or record.get("maturity_status") != "UNASSESSED"
            ):
                errors.append("ZT-ID-001: bounded runtime acceptance or maturity boundary changed")
            evidence_path = root / "docs/evidence/zero-trust/zt-id-001-runtime-validation.yaml"
            try:
                evidence = core.load_json_yaml(evidence_path)
            except ValueError as exc:
                errors.append(str(exc))
            else:
                if (
                    evidence.get("result") != "PASS"
                    or evidence.get("runtime_validation_status") != "VALIDATED"
                    or evidence.get("runtime_acceptance_status") != "ACCEPTED"
                    or evidence.get("maturity_status") != "UNASSESSED"
                ):
                    errors.append("ZT-ID-001: accepted state lacks matching sanitized runtime evidence")
        if package_id == "ZT-RV-001":
            if (
                record.get("runtime_validation_status") != "VALIDATED"
                or record.get("runtime_acceptance_status") != "ACCEPTED"
                or record.get("acceptance_state") != "REPEATABILITY_ACCEPTED"
                or record.get("current_continuity") != "EC4_REPEATABLE_RUNTIME"
                or record.get("accepted_campaign_executions") != 3
                or record.get("consecutive_successes") != 3
                or record.get("scheduled_operation") is not False
                or record.get("maturity_status") != "UNASSESSED"
            ):
                errors.append("ZT-RV-001: bounded EC4 acceptance, schedule, or maturity boundary changed")
        if package_id == "ZT-NET-001":
            if (
                record.get("runtime_validation_status") != "VALIDATED"
                or record.get("runtime_acceptance_status") != "ACCEPTED"
                or record.get("runtime_scope") != "BOUNDED_DIRECTIONAL_INTERZONE_ACL"
                or record.get("segmentation_classification") != "BOUNDED_INTERZONE_ACL_VALIDATED"
                or record.get("maturity_status") != "UNASSESSED"
            ):
                errors.append("ZT-NET-001: bounded runtime acceptance or maturity boundary changed")
            evidence_path = root / "docs/evidence/zero-trust/zt-net-001-validation.yaml"
            try:
                evidence = core.load_json_yaml(evidence_path)
            except ValueError as exc:
                errors.append(str(exc))
            else:
                results = evidence.get("results", {})
                persistent = evidence.get("persistent_acl", {})
                if (
                    results != {"exit_code": 0, "pass": 39, "warn": 0, "fail": 0}
                    or evidence.get("validation", {}).get("access_control") != "PASS"
                    or persistent.get("startup_configuration") != "PASS"
                    or persistent.get("automatic_rollback_exercised") is not True
                ):
                    errors.append("ZT-NET-001: accepted state lacks matching sanitized runtime evidence")
        if package_id == "ZT-VIS-001":
            if (
                record.get("runtime_validation_status") != "VALIDATED"
                or record.get("runtime_acceptance_status") != "ACCEPTED"
                or record.get("runtime_scope") != "BOUNDED_SINGLE_NODE_SANITIZED_LOCAL_TELEMETRY"
                or record.get("maturity_status") != "UNASSESSED"
            ):
                errors.append("ZT-VIS-001: bounded runtime acceptance or maturity boundary changed")
            evidence_path = root / "docs/evidence/zero-trust/zt-vis-001-validation.yaml"
            try:
                evidence = core.load_json_yaml(evidence_path)
            except ValueError as exc:
                errors.append(str(exc))
            else:
                revalidation = evidence.get("runtime_revalidation", {})
                event_validation = revalidation.get("event_validation", {})
                rollback = revalidation.get("rollback", {})
                if (
                    evidence.get("results", {}).get("fail") != 0
                    or evidence.get("persistent_storage", {}).get("post_restart_same_event_query") != "PASS"
                    or revalidation.get("decision") != "ACCEPTED_BOUNDED_LOCAL_VISIBILITY"
                    or event_validation.get("source_attribution") != "PASS_4_OF_4"
                    or event_validation.get("event_freshness") != "PASS_WITHIN_900_SECONDS"
                    or rollback.get("runtime_power_state_rollback") != "PASS_ORIGINAL_STOPPED_STATE_RESTORED"
                    or revalidation.get("central_visibility_claimed") is not False
                    or revalidation.get("maturity_assessed") is not False
                ):
                    errors.append("ZT-VIS-001: accepted state lacks matching sanitized runtime evidence")
    if errors:
        for error in errors:
            result.fail("package.truth", error)
    else:
        result.passed("package.truth", "Canonical package states preserve evidence-backed implementation and validation truth.")


def validate_retired_paths(root: Path, result: Result) -> None:
    present = [str(path) for path in RETIRED_PATHS if (root / path).exists()]
    tools_root = root / "tools"
    if tools_root.is_dir():
        present.extend(
            str(path.relative_to(root))
            for path in tools_root.rglob("*")
            if path.is_file() and RETIRED_AGGREGATE_TOOL.search(path.name)
        )
    if present:
        result.fail("retirement.paths", "Retired paths remain: " + ", ".join(present))
    else:
        result.passed("retirement.paths", "Numbered definitions, evidence roots, and aggregate tools are absent.")


def validate_references(root: Path, paths: list[Path], result: Result) -> None:
    allowed = {MIGRATION_DOC.as_posix()}
    stale: list[str] = []
    for relative in paths:
        relative_posix = relative.as_posix()
        path = root / relative
        if not path.is_file() or relative_posix in allowed or relative_posix.startswith(ACTION_ROOT.as_posix() + "/"):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and "." in path.name:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            if NUMBERED_ID.search(line) or NUMBERED_PATH.search(line):
                stale.append(f"{relative_posix}:{line_number}")
                if len(stale) >= 100:
                    break
    if stale:
        result.fail("retirement.references", "Active numbered references remain: " + ", ".join(stale))
    else:
        result.passed("retirement.references", "No active numbered scenario reference remains outside migration records.")


def validate_repository_safety(root: Path, paths: list[Path], result: Result) -> None:
    runtime = [path.as_posix() for path in paths if path.as_posix().startswith(".runtime/")]
    if runtime:
        result.fail("safety.runtime", "Tracked runtime paths: " + ", ".join(runtime))
    else:
        result.passed("safety.runtime", "No runtime file is tracked.")
    evidence = list((root / "docs/evidence/zero-trust").rglob("*"))
    if any(path.is_file() for path in evidence):
        result.passed("safety.evidence", "Package evidence remains present.")
    else:
        result.fail("safety.evidence", "Package evidence is missing.")
    core_result = core.ValidationResult()
    core.validate_sensitive_data(root, core_result)
    failures = [item.message for item in core_result.findings if item.level == "FAIL"]
    if failures:
        for message in failures:
            result.fail("safety.secrets", message)
    else:
        result.passed("safety.secrets", "No secret material is tracked or exposed by the retirement.")


def run(root: Path = ROOT) -> Result:
    result = Result()
    try:
        paths = tracked_paths(root)
    except RuntimeError as exc:
        result.fail("git", str(exc))
        return result
    validate_flow(root, result)
    validate_package_truth(root, result)
    validate_retired_paths(root, result)
    validate_references(root, paths, result)
    validate_repository_safety(root, paths, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--strict", action="store_true", help="Reserved; all findings are already strict.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    result = run(args.root.resolve())
    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in result.findings], "failed": result.failed}, indent=2))
    else:
        for item in result.findings:
            if args.verbose or item.level == "FAIL":
                print(f"[{item.level}] {item.category}: {item.message}")
        print(f"Scenario-retirement summary: passed={sum(i.level == 'PASS' for i in result.findings)}, failed={result.failed}")
    return 1 if result.failed else 0


if __name__ == "__main__":
    sys.exit(main())
