#!/usr/bin/env python3
"""Read-only application/workload inventory validator for ZT-APP-001."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    message: str


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def validate(app_data: dict[str, Any], workload_data: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    apps = app_data.get("applications", [])
    workloads = workload_data.get("workloads", [])
    if not isinstance(apps, list) or not apps:
        findings.append(Finding("FAIL", "applications.present", "Application inventory is empty."))
        return findings
    if not isinstance(workloads, list) or not workloads:
        findings.append(Finding("FAIL", "workloads.present", "Workload inventory is empty."))
        return findings
    app_ids = [item.get("id") for item in apps if isinstance(item, dict)]
    workload_ids = [item.get("id") for item in workloads if isinstance(item, dict)]
    if len(app_ids) != len(set(app_ids)):
        findings.append(Finding("FAIL", "applications.duplicate", "Application IDs must be unique."))
    if len(workload_ids) != len(set(workload_ids)):
        findings.append(Finding("FAIL", "workloads.duplicate", "Workload IDs must be unique."))
    app_set = set(app_ids)
    workload_set = set(workload_ids)
    referenced: set[str] = set()
    for app in apps:
        app_id = app.get("id", "<missing>")
        if not app.get("owner"):
            findings.append(Finding("FAIL", "applications.owner", f"{app_id} has no owner."))
        if app.get("criticality") == "UNKNOWN":
            findings.append(Finding("WARN", "applications.criticality", f"{app_id} has unknown criticality."))
        declared = set(app.get("workload_ids", []))
        referenced |= declared
        missing = declared - workload_set
        if missing:
            findings.append(Finding("FAIL", "applications.workloads", f"{app_id} references missing workloads: {sorted(missing)}"))
        if not declared:
            findings.append(Finding("FAIL", "applications.workloads", f"{app_id} has no workload."))
        if app.get("criticality") in {"HIGH", "CRITICAL"} and app.get("recovery_status") in {"UNKNOWN", "NOT_AVAILABLE", None}:
            findings.append(Finding("FAIL", "applications.rollback", f"{app_id} lacks required recovery status."))
    for workload in workloads:
        workload_id = workload.get("id", "<missing>")
        app_id = workload.get("application_id")
        if app_id not in app_set:
            findings.append(Finding("FAIL", "workloads.orphan", f"{workload_id} references unknown application {app_id}."))
        if not workload.get("owner"):
            findings.append(Finding("FAIL", "workloads.owner", f"{workload_id} has no owner."))
        if workload.get("inventory_state") == "CURRENT_RUNNING":
            if workload.get("health_check") in {"", "UNKNOWN", "NOT_VALIDATED", None}:
                findings.append(Finding("FAIL", "workloads.health", f"Running workload {workload_id} has no validated health boundary."))
            if workload.get("evidence_level") != "RUNTIME":
                findings.append(Finding("FAIL", "workloads.evidence", f"Running workload {workload_id} lacks runtime evidence."))
    undeclared = workload_set - referenced
    if undeclared:
        findings.append(Finding("FAIL", "workloads.relationship", f"Workloads are not declared by their applications: {sorted(undeclared)}"))
    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "inventory", f"{len(apps)} applications and {len(workloads)} workloads have valid ownership and relationships."))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applications", type=Path, default=ROOT / "docs/zero-trust/application-inventory.yaml")
    parser.add_argument("--workloads", type=Path, default=ROOT / "docs/zero-trust/workload-inventory.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    try:
        findings = validate(load(args.applications), load(args.workloads))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        findings = [Finding("FAIL", "load", str(exc))]
    counts = {level: sum(item.level == level for item in findings) for level in ("PASS", "WARN", "FAIL")}
    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in findings], "summary": counts}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS":
                print(f"[{item.level}] {item.check}: {item.message}")
        print(f"Summary: {counts['PASS']} PASS / {counts['WARN']} WARN / {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
