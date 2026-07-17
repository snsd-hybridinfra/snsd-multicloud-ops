#!/usr/bin/env python3
"""Read-only synchronization checks for Zero Trust YAML and Markdown views."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from generate_zero_trust_reports import run as run_report_check
from validate_zero_trust import (
    BASELINE_PATH,
    CATALOG_PATH,
    _markdown_table,
    calculate_summary,
    load_json_yaml,
    repository_root,
)


def _capability_set(value: str) -> set[str]:
    return set(re.findall(r"ZT-(?:[1-6]\.\d+\.\d+|[78]\.\d+)", value))


def _scenario_set(value: str) -> set[str]:
    return set(re.findall(r"S\d{3}", value))


def run_sync(root: Path) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    passes: list[str] = []
    try:
        catalog = load_json_yaml(root / CATALOG_PATH)
        baseline = load_json_yaml(root / BASELINE_PATH)
    except ValueError as exc:
        return [], [str(exc)]
    catalog_by_id = {item["id"]: item for item in catalog["capabilities"]}
    baseline_by_id = {item["id"]: item for item in baseline["capabilities"]}
    catalog_ids = set(catalog_by_id)

    taxonomy_text = (root / "docs/zero-trust/capability-taxonomy.md").read_text(encoding="utf-8")
    taxonomy_ids = _capability_set(taxonomy_text)
    if taxonomy_ids == catalog_ids:
        passes.append("Capability taxonomy contains exactly the catalog capability IDs.")
    else:
        failures.append(f"Capability taxonomy IDs differ: missing={sorted(catalog_ids-taxonomy_ids)}, extra={sorted(taxonomy_ids-catalog_ids)}")

    control_rows = _markdown_table(root / "docs/zero-trust/control-coverage-matrix.md")
    control_by_id = {row.get("Capability", ""): row for row in control_rows}
    if set(control_by_id) != catalog_ids or len(control_rows) != 52:
        failures.append("Control coverage matrix must contain one row for every catalog capability.")
    else:
        mismatches: list[str] = []
        fields = {
            "Korean name": "capability_ko",
            "Pillar": "pillar",
            "Function": "function",
            "Implementation": "implementation_status",
            "Validation": "validation_status",
            "Evidence": "evidence_level",
        }
        for capability_id, item in catalog_by_id.items():
            row = control_by_id[capability_id]
            for markdown_key, catalog_key in fields.items():
                if row.get(markdown_key) != item[catalog_key]:
                    mismatches.append(f"{capability_id}:{markdown_key}")
            if set(part.strip() for part in row.get("Authority", "").split(";") if part.strip()) != set(item["evidence_authority"]):
                mismatches.append(f"{capability_id}:Authority")
        if mismatches:
            failures.append("Control coverage matrix differs from catalog: " + ", ".join(mismatches))
        else:
            passes.append("Control coverage matrix fields match the catalog.")

    scenario_rows = _markdown_table(root / "docs/zero-trust/scenario-capability-matrix.md")
    evidence_rows = _markdown_table(root / "docs/zero-trust/evidence-coverage-matrix.md")
    scenario_by_id = {row.get("Scenario", ""): row for row in scenario_rows}
    evidence_by_id = {row.get("Scenario", ""): row for row in evidence_rows}
    expected_scenarios = {f"S{number:03d}" for number in range(1, 51)}
    if set(scenario_by_id) != expected_scenarios or set(evidence_by_id) != expected_scenarios:
        failures.append("Scenario and evidence coverage matrices must each contain S001-S050 exactly once.")
    else:
        mapping_errors: list[str] = []
        inverse: dict[str, set[str]] = defaultdict(set)
        for scenario_id in sorted(expected_scenarios):
            scenario_caps = _capability_set(scenario_by_id[scenario_id].get("Capability IDs", ""))
            evidence_caps = _capability_set(evidence_by_id[scenario_id].get("Capability IDs", ""))
            if scenario_caps != evidence_caps:
                mapping_errors.append(f"{scenario_id}:capabilities")
            if scenario_by_id[scenario_id].get("Evidence") != evidence_by_id[scenario_id].get("Quality"):
                mapping_errors.append(f"{scenario_id}:evidence-level")
            for capability_id in scenario_caps:
                inverse[capability_id].add(scenario_id)
        for capability_id, row in control_by_id.items():
            if _scenario_set(row.get("Mapped scenarios", "")) != inverse.get(capability_id, set()):
                mapping_errors.append(f"{capability_id}:mapped-scenarios")
        if mapping_errors:
            failures.append("Scenario mapping views differ: " + ", ".join(mapping_errors))
        else:
            passes.append("Scenario, evidence, and control mapping views agree.")

    machine_errors: list[str] = []
    if set(baseline_by_id) != catalog_ids:
        machine_errors.append("capability ID set")
    for capability_id in sorted(catalog_ids & set(baseline_by_id)):
        catalog_item = catalog_by_id[capability_id]
        baseline_item = baseline_by_id[capability_id]
        comparisons = [
            ("implementation_status", "implementation_status"),
            ("validation_status", "validation_status"),
            ("evidence_level", "evidence_level"),
            ("current_maturity", "current_maturity"),
            ("assessment_confidence", "confidence"),
            ("evidence_authority", "evidence_authority"),
        ]
        for left, right in comparisons:
            if catalog_item[left] != baseline_item[right]:
                machine_errors.append(f"{capability_id}:{left}")
    if baseline["summary"] != calculate_summary(baseline["capabilities"]):
        machine_errors.append("summary counts")
    if machine_errors:
        failures.append("Catalog/baseline machine-readable data differ: " + ", ".join(machine_errors))
    else:
        passes.append("Catalog, baseline records, and baseline summary counts agree.")

    report_ok, report_message = run_report_check(root, write=False)
    if report_ok:
        passes.append(report_message.removeprefix("[PASS] "))
    else:
        failures.append(report_message.removeprefix("[FAIL] "))
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
