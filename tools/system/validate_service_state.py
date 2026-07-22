#!/usr/bin/env python3
"""Validate approved ZT-SYS-001 service-state evidence without restart or remote execution."""

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
    if not isinstance(value, dict): raise ValueError(f"{path} must contain an object")
    return value

def validate(policy: dict[str, Any], evidence: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if policy.get("automatic_restart") is not False or evidence.get("restart_performed") is not False:
        findings.append(Finding("FAIL", "service.restart", "Automatic or executed service restart is prohibited."))
    records = {item.get("service_id"): item for item in evidence.get("services", []) if isinstance(item, dict)}
    for service in policy.get("services", []):
        service_id = service.get("service_id", "<missing>")
        record = records.get(service_id)
        if record is None:
            findings.append(Finding("FAIL", "service.evidence", f"{service_id} lacks current approved state evidence.")); continue
        expected = service.get("expected_state")
        current = record.get("current_state")
        if expected == "RUNNING" and current == "STOPPED":
            findings.append(Finding("FAIL", "service.state", f"Required service {service_id} is stopped."))
        elif expected == "RUNNING" and current == "DEGRADED":
            findings.append(Finding("WARN", "service.degraded", f"{service_id} is available but degraded; remediation requires approval."))
        elif expected == "AVAILABLE_ON_DEMAND" and current not in {"AVAILABLE", "RUNNING"}:
            findings.append(Finding("FAIL", "service.state", f"On-demand service {service_id} is unavailable."))
        if not record.get("evidence"):
            findings.append(Finding("FAIL", "service.evidence", f"{service_id} has no sanitized evidence reference."))
        if record.get("restart_performed") is not False:
            findings.append(Finding("FAIL", "service.restart", f"{service_id} evidence indicates a restart."))
    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "service", f"{len(records)} approved service records are available; degraded state remains explicit and no restart occurred."))
    return findings

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=ROOT / "docs/zero-trust/system-service-policy.yaml")
    parser.add_argument("--evidence", type=Path, default=ROOT / "docs/evidence/zero-trust/zt-sys-001-service-state.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    try: findings = validate(load(args.policy), load(args.evidence))
    except (OSError, ValueError, json.JSONDecodeError) as exc: findings = [Finding("FAIL", "load", str(exc))]
    counts = {level: sum(item.level == level for item in findings) for level in ("PASS", "WARN", "FAIL")}
    if args.format == "json": print(json.dumps({"findings": [asdict(item) for item in findings], "summary": counts}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS": print(f"[{item.level}] {item.check}: {item.message}")
        print(f"Summary: {counts['PASS']} PASS / {counts['WARN']} WARN / {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0

if __name__ == "__main__": raise SystemExit(main())
