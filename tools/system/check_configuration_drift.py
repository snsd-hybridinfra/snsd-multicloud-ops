#!/usr/bin/env python3
"""Read-only metadata/checksum drift validator for approved ZT-SYS-001 controls."""

from __future__ import annotations

import argparse
import hashlib
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

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate(authority: dict[str, Any], integrity: dict[str, Any], evidence: dict[str, Any], root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    configs = {item.get("configuration_id"): item for item in authority.get("configurations", []) if isinstance(item, dict)}
    records = {item.get("configuration_id"): item for item in evidence.get("records", []) if isinstance(item, dict)}
    matched = 0
    for control in integrity.get("controls", []):
        control_id = control.get("control_id", "<missing>")
        config_id = control.get("configuration_id")
        config = configs.get(config_id)
        if config is None:
            findings.append(Finding("FAIL", "authority.reference", f"{control_id} references unknown configuration {config_id}.")); continue
        if config.get("sensitive") is True and config.get("approved_sha256") is not None:
            findings.append(Finding("FAIL", "secret.hash", f"{config_id} must not store a secret-bearing checksum."))
        expected = config.get("approved_sha256")
        source = config.get("authoritative_source", "")
        if expected:
            path = root / source
            if not path.is_file():
                findings.append(Finding("FAIL", "source.missing", f"{config_id} authoritative source is missing.")); continue
            actual = sha256(path)
            if actual != expected:
                findings.append(Finding("FAIL", "drift.checksum", f"{config_id} approved checksum differs from current source.")); continue
            record = records.get(config_id)
            if not record or record.get("state") != "MATCHED" or record.get("syntax_result") != "PASS" or record.get("owner_match") is not True or record.get("mode_match") is not True:
                findings.append(Finding("FAIL", "drift.evidence", f"{config_id} lacks matched metadata and syntax evidence.")); continue
            if record.get("actual_sha256") != actual:
                findings.append(Finding("FAIL", "drift.evidence", f"{config_id} evidence checksum is stale or mismatched.")); continue
            matched += 1
        else:
            state = records.get(config_id, {}).get("state", control.get("expected_integrity_state"))
            if state in {"CONFIGURATION_ONLY", "NOT_ASSESSED", "UNKNOWN"}:
                findings.append(Finding("WARN", "drift.unassessed", f"{config_id} remains {state}; no secret-bearing content comparison is claimed."))
            elif state == "DRIFT_DETECTED":
                findings.append(Finding("FAIL", "drift.detected", f"{config_id} has required configuration drift."))
    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "drift", f"{matched} safe repository configuration baselines match; sensitive/host-local records remain metadata-only."))
    return findings

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=ROOT / "docs/zero-trust/system-inventory.yaml")
    parser.add_argument("--authority", type=Path, default=ROOT / "docs/zero-trust/system-configuration-authority.yaml")
    parser.add_argument("--integrity", type=Path, default=ROOT / "docs/zero-trust/system-integrity-policy.yaml")
    parser.add_argument("--evidence-root", type=Path, default=ROOT / "docs/evidence/zero-trust/zt-sys-001-integrity-validation.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    try:
        load(args.inventory)
        findings = validate(load(args.authority), load(args.integrity), load(args.evidence_root), ROOT)
    except (OSError, ValueError, json.JSONDecodeError) as exc: findings = [Finding("FAIL", "load", str(exc))]
    if args.strict:
        findings += [Finding("FAIL", "strict", f"Warning promoted: {item.check}: {item.message}") for item in list(findings) if item.level == "WARN"]
    counts = {level: sum(item.level == level for item in findings) for level in ("PASS", "WARN", "FAIL")}
    if args.format == "json": print(json.dumps({"findings": [asdict(item) for item in findings], "summary": counts}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS": print(f"[{item.level}] {item.check}: {item.message}")
        print(f"Summary: {counts['PASS']} PASS / {counts['WARN']} WARN / {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0

if __name__ == "__main__": raise SystemExit(main())
