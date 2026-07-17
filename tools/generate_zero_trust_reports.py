#!/usr/bin/env python3
"""Check or update deterministic Zero Trust summary fragments."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from validate_zero_trust import CATALOG_PATH, BASELINE_PATH, load_json_yaml, repository_root


BEGIN_MARKER = "<!-- BEGIN GENERATED ZERO TRUST SUMMARY -->"
END_MARKER = "<!-- END GENERATED ZERO TRUST SUMMARY -->"
TARGET_PATH = Path("docs/zero-trust/current-baseline-assessment.md")


def _ordered_counts(values: Counter[str], order: list[str]) -> list[tuple[str, int]]:
    return [(name, values.get(name, 0)) for name in order]


def build_summary_fragment(catalog: dict, baseline: dict) -> str:
    records = baseline["capabilities"]
    by_id = {item["id"]: item for item in catalog["capabilities"]}
    validation_counts = Counter(item["validation_status"] for item in records)
    maturity_counts = Counter(item["current_maturity"] for item in records)
    evidence_counts = Counter(item["evidence_level"] for item in records)
    domain_counts = Counter(by_id[item["id"]]["pillar"] for item in records)
    lines = [
        "Generated from `capability-catalog.yaml` and `current-baseline-assessment.yaml`. Do not edit this block manually.",
        "",
        "These dimensions overlap; validation, maturity, and evidence are reported separately.",
        "",
        "| Validation status | Count |",
        "|---|---:|",
    ]
    for name, count in _ordered_counts(
        validation_counts,
        ["VALIDATED", "PARTIALLY_VALIDATED", "IMPLEMENTED", "REFERENCE_ONLY", "PLANNED", "GAP_IDENTIFIED", "NOT_APPLICABLE"],
    ):
        lines.append(f"| {name} | {count} |")
    lines.extend(["", "| Maturity | Count |", "|---|---:|"])
    for name, count in _ordered_counts(
        maturity_counts,
        ["UNASSESSED", "TRADITIONAL", "INITIAL", "ADVANCED", "OPTIMAL", "NOT_APPLICABLE"],
    ):
        lines.append(f"| {name} | {count} |")
    lines.extend(["", "| Evidence level | Count |", "|---|---:|"])
    for name, count in _ordered_counts(evidence_counts, ["NONE", "DESIGN", "CONFIGURATION", "RUNTIME", "CONTINUOUS"]):
        lines.append(f"| {name} | {count} |")
    lines.extend(["", "| Domain | Capabilities |", "|---|---:|"])
    for domain in [
        "identity",
        "device-endpoint",
        "network",
        "system",
        "application-workload",
        "data",
        "visibility-analytics",
        "automation-integration",
    ]:
        lines.append(f"| {domain} | {domain_counts.get(domain, 0)} |")
    return "\n".join(lines)


def expected_document(root: Path) -> tuple[Path, str, str]:
    target = root / TARGET_PATH
    current = target.read_text(encoding="utf-8")
    if current.count(BEGIN_MARKER) != 1 or current.count(END_MARKER) != 1:
        raise ValueError(f"{TARGET_PATH} must contain exactly one reviewed generated-marker pair")
    begin = current.index(BEGIN_MARKER) + len(BEGIN_MARKER)
    end = current.index(END_MARKER)
    if begin > end:
        raise ValueError("generated summary markers are reversed")
    catalog = load_json_yaml(root / CATALOG_PATH)
    baseline = load_json_yaml(root / BASELINE_PATH)
    fragment = build_summary_fragment(catalog, baseline)
    replacement = f"{BEGIN_MARKER}\n{fragment}\n{END_MARKER}"
    expected = current[: current.index(BEGIN_MARKER)] + replacement + current[end + len(END_MARKER) :]
    return target, current, expected


def run(root: Path, write: bool = False) -> tuple[bool, str]:
    try:
        target, current, expected = expected_document(root)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return False, str(exc)
    if current == expected:
        return True, f"[PASS] Generated Zero Trust summary is synchronized: {target.relative_to(root)}"
    if not write:
        return False, f"[FAIL] Generated Zero Trust summary is stale: {target.relative_to(root)}"
    target.write_text(expected, encoding="utf-8", newline="\n")
    return True, f"[PASS] Updated reviewed generated summary block: {target.relative_to(root)}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check the generated fragment (default)")
    mode.add_argument("--write", action="store_true", help="update only the reviewed generated marker block")
    parser.add_argument("--root", type=Path, default=repository_root(), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    passed, message = run(args.root.resolve(), write=args.write)
    print(message)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
