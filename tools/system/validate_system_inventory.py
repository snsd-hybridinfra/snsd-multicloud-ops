#!/usr/bin/env python3
"""Read-only cross-record system inventory validator for ZT-SYS-001."""

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

def validate(inventory: dict[str, Any], baselines: dict[str, Any], authority: dict[str, Any], credentials: dict[str, Any], exposures: dict[str, Any], recovery: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    systems = inventory.get("systems", [])
    if not systems:
        return [Finding("FAIL", "inventory.present", "System inventory is empty.")]
    system_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    if len(system_ids) != len(set(system_ids)):
        findings.append(Finding("FAIL", "inventory.duplicate", "System IDs must be unique."))
    system_set = set(system_ids)
    profiles = baselines.get("profiles", [])
    profile_ids = [item.get("profile_id") for item in profiles if isinstance(item, dict)]
    profile_set = set(profile_ids)
    if len(profile_ids) != len(set(profile_ids)):
        findings.append(Finding("FAIL", "baseline.duplicate", "Baseline profile IDs must be unique."))
    for system in systems:
        system_id = system.get("id", "<missing>")
        if system.get("lifecycle_state") in {"ACTIVE", "DEGRADED", "MAINTENANCE"} and (not system.get("owner") or not system.get("custodian")):
            findings.append(Finding("FAIL", "ownership.missing", f"Active system {system_id} lacks an owner or custodian."))
        if system.get("current_state") == "UNKNOWN" and system.get("lifecycle_state") == "ACTIVE":
            findings.append(Finding("FAIL", "inventory.unknown-active", f"Active system {system_id} has unknown current state."))
        if system.get("baseline_profile") not in profile_set:
            findings.append(Finding("FAIL", "baseline.reference", f"{system_id} references missing baseline profile {system.get('baseline_profile')}."))
        if not system.get("privileged_access_model"):
            findings.append(Finding("FAIL", "privileged.model", f"{system_id} lacks a privileged-access model."))
        if system.get("evidence_level") == "RUNTIME" and system.get("evidence_authority") not in {"CODEX_EXECUTED_LIVE_RUNTIME", "USER_EXECUTED_RUNTIME"}:
            findings.append(Finding("FAIL", "evidence.authority", f"{system_id} runtime evidence has invalid authority."))
    for profile in profiles:
        if profile.get("destructive_test_prohibition") is not True:
            findings.append(Finding("FAIL", "baseline.destructive", f"{profile.get('profile_id')} must prohibit destructive tests."))

    configurations = authority.get("configurations", [])
    config_ids = [item.get("configuration_id") for item in configurations if isinstance(item, dict)]
    if len(config_ids) != len(set(config_ids)):
        findings.append(Finding("FAIL", "authority.duplicate", "Configuration authority IDs must be unique."))
    for item in configurations:
        config_id = item.get("configuration_id", "<missing>")
        if item.get("system_id") not in system_set:
            findings.append(Finding("FAIL", "authority.system", f"{config_id} references an unknown system."))
        checksum = item.get("approved_sha256")
        if item.get("sensitive") is True and checksum is not None:
            findings.append(Finding("FAIL", "authority.secret-hash", f"{config_id} records a checksum for sensitive configuration."))
        if checksum is not None and (not isinstance(checksum, str) or len(checksum) != 64):
            findings.append(Finding("FAIL", "authority.checksum", f"{config_id} has an invalid SHA-256 value."))

    forbidden_keys = {"value", "password", "token", "private_key", "secret_value", "mfa_seed", "recovery_code"}
    for item in credentials.get("references", []):
        reference_id = item.get("reference_id", "<missing>")
        if item.get("system_id") not in system_set:
            findings.append(Finding("FAIL", "credential.system", f"{reference_id} references an unknown system."))
        if forbidden_keys & set(item):
            findings.append(Finding("FAIL", "credential.value", f"{reference_id} contains a prohibited credential-value field."))
    for item in exposures.get("exposures", []):
        if item.get("system_id") not in system_set:
            findings.append(Finding("FAIL", "exposure.system", f"{item.get('exposure_id')} references an unknown system."))
        if item.get("bind_scope") == "EXTERNAL" and item.get("port_category") == "ADMINISTRATIVE" and item.get("authentication") in {"NONE", "UNKNOWN", None}:
            findings.append(Finding("FAIL", "exposure.unauthenticated", f"{item.get('exposure_id')} exposes unauthenticated administration."))
    for item in recovery.get("systems", []):
        if item.get("system_id") not in system_set:
            findings.append(Finding("FAIL", "recovery.system", f"Recovery record references unknown system {item.get('system_id')}."))
        if item.get("readiness") == "RESTORE_VALIDATED" and not item.get("last_recovery_evidence"):
            findings.append(Finding("FAIL", "recovery.evidence", f"{item.get('system_id')} claims restore validation without evidence."))
    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "system", f"{len(systems)} systems, {len(profiles)} profiles, {len(configurations)} configuration authorities, and bounded references are consistent."))
    return findings

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=ROOT / "docs/zero-trust/system-inventory.yaml")
    parser.add_argument("--baselines", type=Path, default=ROOT / "docs/zero-trust/system-baseline-policy.yaml")
    parser.add_argument("--authority", type=Path, default=ROOT / "docs/zero-trust/system-configuration-authority.yaml")
    parser.add_argument("--credentials", type=Path, default=ROOT / "docs/zero-trust/system-credential-reference-inventory.yaml")
    parser.add_argument("--exposures", type=Path, default=ROOT / "docs/zero-trust/system-service-exposure.yaml")
    parser.add_argument("--recovery", type=Path, default=ROOT / "docs/zero-trust/system-recovery-readiness.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    try:
        findings = validate(load(args.inventory), load(args.baselines), load(args.authority), load(args.credentials), load(args.exposures), load(args.recovery))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        findings = [Finding("FAIL", "load", str(exc))]
    counts = {level: sum(item.level == level for item in findings) for level in ("PASS", "WARN", "FAIL")}
    if args.format == "json": print(json.dumps({"findings": [asdict(item) for item in findings], "summary": counts}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS": print(f"[{item.level}] {item.check}: {item.message}")
        print(f"Summary: {counts['PASS']} PASS / {counts['WARN']} WARN / {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0

if __name__ == "__main__": raise SystemExit(main())
