#!/usr/bin/env python3
"""Read-only validator for the bounded ZT-DEV-001 endpoint package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY = REPO_ROOT / "docs/zero-trust/device/device-inventory.yaml"
DEFAULT_POLICY = REPO_ROOT / "docs/zero-trust/device/endpoint-compliance-policy.yaml"
DEFAULT_EVIDENCE_ROOT = REPO_ROOT / ".runtime/zero-trust/endpoint/latest"
MAC_PATTERN = re.compile(r"(?i)\b(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b")
SECRET_PATTERN = re.compile(r"(?i)(?:BEGIN [A-Z ]*PRIVATE KEY|(?:password|token|client_secret|totp_seed)\s*[:=])")


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    message: str


def _load_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return parsed.astimezone(timezone.utc)


def validate_package(
    inventory: dict[str, Any],
    policy: dict[str, Any],
    evidence_records: list[dict[str, Any]],
    *,
    now: datetime | None = None,
) -> tuple[list[Finding], dict[str, int]]:
    findings: list[Finding] = []
    counts = {"assessed_assets": 0, "compliant": 0, "partially_compliant": 0, "noncompliant": 0, "unknown": 0}
    now = now or datetime.now(timezone.utc)

    if inventory.get("schema_version") != "1.0.0" or inventory.get("package_id") != "ZT-DEV-001":
        findings.append(Finding("FAIL", "inventory.metadata", "Inventory schema or package identifier is invalid."))
    assets = inventory.get("assets")
    if not isinstance(assets, list) or not assets:
        return findings + [Finding("FAIL", "inventory.assets", "At least one asset is required.")], counts

    profile_ids = {item.get("profile_id") for item in policy.get("profiles", []) if isinstance(item, dict)}
    asset_map: dict[str, dict[str, Any]] = {}
    for asset in assets:
        if not isinstance(asset, dict):
            findings.append(Finding("FAIL", "inventory.asset", "Asset records must be objects."))
            continue
        asset_id = str(asset.get("asset_id", ""))
        if not asset_id:
            findings.append(Finding("FAIL", "inventory.asset-id", "An asset is missing asset_id."))
        elif asset_id in asset_map:
            findings.append(Finding("FAIL", "inventory.duplicate", f"Duplicate asset ID: {asset_id}"))
        else:
            asset_map[asset_id] = asset
        if not asset.get("owner_role"):
            findings.append(Finding("FAIL", "inventory.owner", f"{asset_id or '<missing>'} has no owner role."))
        if asset.get("management_state") not in {"MANAGED", "PARTIALLY_MANAGED", "DECLARED_ONLY", "OUT_OF_SCOPE"}:
            findings.append(Finding("FAIL", "inventory.management", f"{asset_id} has an invalid management state."))
        if asset.get("compliance_profile") not in profile_ids:
            findings.append(Finding("FAIL", "inventory.profile", f"{asset_id} references an unknown compliance profile."))
        if asset.get("privileged") is True and not asset.get("compliance_profile"):
            findings.append(Finding("FAIL", "inventory.privileged", f"Privileged asset {asset_id} has no compliance profile."))

    serialized = json.dumps({"inventory": inventory, "policy": policy}, ensure_ascii=False)
    if MAC_PATTERN.search(serialized):
        findings.append(Finding("FAIL", "privacy.mac", "A full MAC address is present in committed package data."))
    if SECRET_PATTERN.search(serialized):
        findings.append(Finding("FAIL", "security.secret", "Credential or private-key material pattern is present."))
    if policy.get("automatic_remediation") is not False or policy.get("automatic_patching") is not False or policy.get("automatic_reboot") is not False:
        findings.append(Finding("FAIL", "policy.mutation", "Automatic remediation, patching, and reboot must remain disabled."))

    evidence_map: dict[str, dict[str, Any]] = {}
    for record in evidence_records:
        asset_id = str(record.get("asset_id", ""))
        if asset_id not in asset_map:
            counts["unknown"] += 1
            findings.append(Finding("FAIL", "evidence.unknown-asset", f"Evidence references unknown asset {asset_id or '<missing>'}."))
            continue
        if asset_id in evidence_map:
            findings.append(Finding("FAIL", "evidence.duplicate", f"Multiple evidence records exist for {asset_id}."))
            continue
        evidence_map[asset_id] = record

    mandatory = policy.get("mandatory_live_assets", [])
    if not isinstance(mandatory, list) or not mandatory:
        findings.append(Finding("FAIL", "policy.mandatory", "At least one mandatory live asset is required."))
        mandatory = []
    freshness_hours = int(policy.get("freshness_hours", 0))
    for asset_id in mandatory:
        if asset_id not in asset_map:
            findings.append(Finding("FAIL", "policy.mandatory", f"Mandatory asset {asset_id} is not inventoried."))
            continue
        record = evidence_map.get(asset_id)
        if not record:
            counts["noncompliant"] += 1
            findings.append(Finding("FAIL", "evidence.missing", f"Mandatory live evidence is missing for {asset_id}."))
            continue
        counts["assessed_assets"] += 1
        record_failed = False
        try:
            age_hours = (now - _parse_time(str(record.get("collection_time", "")))).total_seconds() / 3600
            if age_hours < -0.25 or age_hours > freshness_hours:
                findings.append(Finding("FAIL", "evidence.freshness", f"Evidence for {asset_id} is outside the {freshness_hours}-hour freshness boundary."))
                record_failed = True
        except (TypeError, ValueError):
            findings.append(Finding("FAIL", "evidence.timestamp", f"Evidence for {asset_id} has an invalid timestamp."))
            record_failed = True

        patch = record.get("patch_state", {})
        vulnerability = record.get("vulnerability", {})
        agent = record.get("endpoint_agent", {})
        if patch.get("automatic_patching_performed") is not False or vulnerability.get("exploit_executed") is not False:
            findings.append(Finding("FAIL", "evidence.mutation", f"{asset_id} evidence indicates a prohibited mutation or exploit."))
            record_failed = True
        if agent.get("installed_by_package") is not False:
            findings.append(Finding("FAIL", "evidence.agent", f"{asset_id} indicates an unauthorized agent installation."))
            record_failed = True
        patch_class = patch.get("classification")
        if patch_class in {"PACKAGE_MANAGER_ERROR", "UNSUPPORTED_OS", "UNKNOWN", None}:
            findings.append(Finding("FAIL", "evidence.patch", f"{asset_id} patch state is {patch_class or 'missing'}."))
            record_failed = True
        elif patch_class in {"SECURITY_UPDATES_AVAILABLE", "REBOOT_REQUIRED"}:
            findings.append(Finding("WARN", "evidence.patch", f"{asset_id} requires operator-reviewed maintenance: {patch_class}."))
        if vulnerability.get("classification") in {"ASSESSMENT_LIMITED", "NOT_ASSESSED"}:
            findings.append(Finding("WARN", "evidence.vulnerability", f"{asset_id} has no dedicated scanner evidence."))

        if record_failed:
            counts["noncompliant"] += 1
        elif patch_class in {"SECURITY_UPDATES_AVAILABLE", "REBOOT_REQUIRED"} or vulnerability.get("classification") == "ASSESSMENT_LIMITED":
            counts["partially_compliant"] += 1
        else:
            counts["compliant"] += 1

    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "package", "Inventory, policy, and mandatory live evidence satisfy the bounded package contract."))
    return findings, counts


def _load_evidence(root: Path) -> list[dict[str, Any]]:
    if not root.exists():
        return []
    records = []
    for path in sorted(root.glob("*.evidence.json")):
        records.append(_load_object(path))
    return records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--evidence-root", type=Path, default=DEFAULT_EVIDENCE_ROOT)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    try:
        inventory = _load_object(args.inventory)
        policy = _load_object(args.policy)
        evidence = _load_evidence(args.evidence_root)
        findings, counts = validate_package(inventory, policy, evidence)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        findings = [Finding("FAIL", "load", str(exc))]
        counts = {"assessed_assets": 0, "compliant": 0, "partially_compliant": 0, "noncompliant": 0, "unknown": 0}

    fail_count = sum(item.level == "FAIL" for item in findings)
    warn_count = sum(item.level == "WARN" for item in findings)
    pass_count = sum(item.level == "PASS" for item in findings)
    exit_status = 1 if fail_count or (args.strict and warn_count) else 0
    report = {
        "package_id": "ZT-DEV-001",
        "results": {**counts, "pass": pass_count, "warn": warn_count, "fail": fail_count, "exit_code": exit_status},
        "findings": [asdict(item) for item in findings],
    }
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS":
                print(f"[{item.level}] {item.check}: {item.message}")
        print(f"Summary: {pass_count} PASS / {warn_count} WARN / {fail_count} FAIL")
        print("Asset results: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
    return exit_status


if __name__ == "__main__":
    raise SystemExit(main())
