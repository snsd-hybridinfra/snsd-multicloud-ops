#!/usr/bin/env python3
"""Read-only synchronization checks for capability and package authorities."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from generate_zero_trust_reports import run as run_report_check
from validate_zero_trust import (
    BACKLOG_PATH,
    BASELINE_PATH,
    CATALOG_PATH,
    calculate_summary,
    load_json_yaml,
    repository_root,
)

FLOW_PATH = Path("docs/zero-trust/package-flow.yaml")
PACKAGE_ROOT = Path("docs/zero-trust/packages")
PROJECT_AUTHORITIES = {
    "roadmap": Path("docs/zero-trust/final-roadmap.yaml"),
    "execution_plan": Path("docs/zero-trust/final-execution-plan.yaml"),
    "maturity_target": Path("docs/zero-trust/maturity-target.yaml"),
    "package_status": Path("docs/zero-trust/package-status.yaml"),
    "acceptance_cases": Path("docs/zero-trust/package-acceptance-cases.yaml"),
}
EXPECTED_FLOW = [
    "ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001",
    "ZT-CV-001", "ZT-RV-001", "P1-ACC-001",
]


def run_sync(root: Path) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    failures: list[str] = []
    try:
        catalog = load_json_yaml(root / CATALOG_PATH)
        baseline = load_json_yaml(root / BASELINE_PATH)
        backlog = load_json_yaml(root / BACKLOG_PATH)
        flow = load_json_yaml(root / FLOW_PATH)
        project = {name: load_json_yaml(root / path) for name, path in PROJECT_AUTHORITIES.items()}
    except ValueError as exc:
        return [], [str(exc)]

    catalog_by_id = {item["id"]: item for item in catalog.get("capabilities", [])}
    baseline_by_id = {item["id"]: item for item in baseline.get("capabilities", [])}
    backlog_by_id = {item["id"]: item for item in backlog.get("capabilities", [])}
    canonical_ids = set(catalog_by_id)
    if len(canonical_ids) == 52 and canonical_ids == set(baseline_by_id) == set(backlog_by_id):
        passes.append("Catalog, baseline, and backlog contain the same 52 unique capability IDs.")
    else:
        failures.append("Capability IDs are not synchronized across catalog, baseline, and backlog.")

    comparable = (
        ("implementation_status", "implementation_status"),
        ("validation_status", "validation_status"),
        ("evidence_level", "evidence_level"),
        ("current_maturity", "current_maturity"),
    )
    mismatches: list[str] = []
    for capability_id in canonical_ids & set(baseline_by_id) & set(backlog_by_id):
        catalog_item = catalog_by_id[capability_id]
        baseline_item = baseline_by_id[capability_id]
        backlog_item = backlog_by_id[capability_id]
        for left, right in comparable:
            if catalog_item[left] != baseline_item[right] or catalog_item[left] != backlog_item[right]:
                mismatches.append(f"{capability_id}:{left}")
    if mismatches:
        failures.append("Capability status authorities differ: " + ", ".join(mismatches))
    else:
        passes.append("Capability implementation, validation, evidence, and maturity states agree.")

    if baseline.get("summary") == calculate_summary(baseline.get("capabilities", [])):
        passes.append("Baseline summary counts match capability records.")
    else:
        failures.append("Baseline summary counts do not match capability records.")

    sequence = flow.get("phase_1_sequence", [])
    package_rows = flow.get("packages", [])
    package_ids = [item.get("package_id") for item in package_rows]
    if sequence == EXPECTED_FLOW and package_ids == EXPECTED_FLOW[:-1] and len(package_ids) == len(set(package_ids)):
        passes.append("Phase 1 package flow and package IDs are canonical and unique.")
    else:
        failures.append(f"Invalid Phase 1 package flow: sequence={sequence}, packages={package_ids}")

    deferred = flow.get("deferred_final_work", {})
    expected_deferred = {
        "package_id": "ZT-SCH-001", "action_id": "P1-SCH-001",
        "planning_status": "DEFERRED_FINAL", "schedule_state": "DISABLED",
        "execution_phase": "PHASE_5", "predecessor_action": "P5-DEMO-001",
        "successor_action": "P5-ACC-001", "runtime_validation_status": "NOT_VALIDATED",
        "runtime_acceptance_status": "PENDING",
    }
    if deferred == expected_deferred:
        passes.append("ZT-SCH-001 is preserved as the disabled deferred final project gate.")
    else:
        failures.append("Deferred final scheduled-validation authority differs.")

    predecessor_errors: list[str] = []
    for index, row in enumerate(package_rows):
        expected = None if index == 0 else package_ids[index - 1]
        if row.get("predecessor") != expected:
            predecessor_errors.append(f"{row.get('package_id')}->{row.get('predecessor')}")
        package_id = row.get("package_id", "")
        package_path = root / PACKAGE_ROOT / f"{package_id.lower()}-package.yaml"
        if not package_path.is_file():
            predecessor_errors.append(f"missing:{package_path.relative_to(root)}")
    if predecessor_errors:
        failures.append("Package predecessor/file synchronization failed: " + ", ".join(predecessor_errors))
    else:
        passes.append("Package predecessor links and package authority files are synchronized.")

    acceptance = flow.get("phase_1_acceptance", {})
    expected_acceptance = {
        "implementation_status": "PARTIAL",
        "validation_status": "PARTIALLY_VALIDATED",
        "completion_status": "COMPLETED_WITH_GAPS",
        "scope_boundary": "ZT-RV-001",
        "requires_all_predecessors_accepted": True,
        "decision_status": "ACCEPTED_WITH_GAPS",
        "blocking_reason": None,
        "accepted_exception": "P1-RV-FRESHNESS-001",
        "deferred_final_risk": "STALE_RV_EVIDENCE",
        "decision_record": "docs/zero-trust/recovery/P1-ACC-001/acceptance-decision-with-gaps.yaml",
    }
    if acceptance == expected_acceptance:
        passes.append("Phase 1 is completed with gaps under the scoped RV freshness exception; stale evidence remains a deferred final-gate risk at the ZT-RV-001 boundary.")
    else:
        failures.append("Phase 1 acceptance state differs from the conservative authority.")

    roadmap_ids = [action_id for phase in project["roadmap"].get("phases", []) for action_id in phase.get("actions", [])]
    execution_ids = [item.get("action_id") for item in project["execution_plan"].get("actions", [])]
    if roadmap_ids == execution_ids and len(execution_ids) == len(set(execution_ids)):
        passes.append("Roadmap and execution-plan action IDs are ordered, unique, and synchronized.")
    else:
        failures.append("Roadmap and execution-plan action IDs differ or contain duplicates.")

    if (
        project["maturity_target"].get("actual_project_target") == "L3_ADVANCED"
        and project["maturity_target"].get("future_roadmap_target") == "L4_OPTIMAL"
        and project["maturity_target"].get("l3_completion_decision") == "NOT_YET_ASSESSED"
    ):
        passes.append("L3 is a target without a completion decision and L4 remains future roadmap scope.")
    else:
        failures.append("Maturity target authority overclaims L3 or does not preserve the L4 roadmap boundary.")

    status_ids = {item.get("package_id") for item in project["package_status"].get("packages", [])}
    case_ids = {item.get("package_id") for item in project["acceptance_cases"].get("packages", [])}
    expected_status_ids = set(package_ids) | {"ZT-ARC-001", "ZT-SCH-001", "ZT-DEV-001", "ZT-APP-001", "ZT-DATA-001", "ZT-SYS-001", "ZT-AUTO-001", "ZT-VIS-002"}
    if case_ids == expected_status_ids - {"ZT-ARC-001"} and status_ids == expected_status_ids:
        passes.append("Package status and all technical-package acceptance-case coverage are synchronized.")
    else:
        failures.append("Package status and acceptance-case package coverage is not synchronized.")

    report_ok, report_message = run_report_check(root, write=False)
    (passes if report_ok else failures).append(report_message.removeprefix("[PASS] ").removeprefix("[FAIL] "))
    return passes, failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=repository_root(), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    passes, failures = run_sync(args.root.resolve())
    for message in passes:
        print(f"[PASS] {message}")
    for message in failures:
        print(f"[FAIL] {message}")
    print(f"Synchronization summary: passed={len(passes)}, failed={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
