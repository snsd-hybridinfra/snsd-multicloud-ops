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
EXPECTED_FLOW = [
    "ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001",
    "ZT-CV-001", "ZT-RV-001", "ZT-SCH-001", "PHASE_1_ACCEPTANCE",
]


def run_sync(root: Path) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    failures: list[str] = []
    try:
        catalog = load_json_yaml(root / CATALOG_PATH)
        baseline = load_json_yaml(root / BASELINE_PATH)
        backlog = load_json_yaml(root / BACKLOG_PATH)
        flow = load_json_yaml(root / FLOW_PATH)
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
        "completion_status": "NOT_COMPLETE",
        "scope_boundary": "ZT-SCH-001",
        "requires_all_predecessors_accepted": True,
    }
    if acceptance == expected_acceptance:
        passes.append("Phase 1 remains partial, partially validated, and not complete at ZT-SCH-001.")
    else:
        failures.append("Phase 1 acceptance state differs from the conservative authority.")

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
