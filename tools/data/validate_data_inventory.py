#!/usr/bin/env python3
"""Read-only cross-record validator for the bounded ZT-DATA-001 package."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CLASSIFICATIONS = {"PUBLIC", "INTERNAL", "SENSITIVE", "RESTRICTED", "SECRET_MATERIAL_REFERENCE"}
WILDCARDS = {"*", "ANY", "ALL", "EVERYONE"}


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


def validate(
    inventory: dict[str, Any],
    classifications: dict[str, Any],
    access: dict[str, Any],
    flows: dict[str, Any],
    encryption: dict[str, Any],
    backups: dict[str, Any],
    root: Path | None = None,
) -> list[Finding]:
    findings: list[Finding] = []
    assets = inventory.get("data_assets", [])
    if not isinstance(assets, list) or not assets:
        return [Finding("FAIL", "inventory.present", "Data inventory is empty.")]
    asset_ids = [item.get("id") for item in assets if isinstance(item, dict)]
    if len(asset_ids) != len(set(asset_ids)):
        findings.append(Finding("FAIL", "inventory.duplicate", "Data asset IDs must be unique."))
    asset_map = {item.get("id"): item for item in assets if isinstance(item, dict)}

    defined_classes = {item.get("id") for item in classifications.get("classifications", []) if isinstance(item, dict)}
    if defined_classes != CLASSIFICATIONS:
        findings.append(Finding("FAIL", "classification.model", "The five bounded classifications must be defined exactly."))

    policies = access.get("policies", [])
    policy_ids = [item.get("policy_id") for item in policies if isinstance(item, dict)]
    policy_map = {item.get("policy_id"): item for item in policies if isinstance(item, dict)}
    if len(policy_ids) != len(set(policy_ids)):
        findings.append(Finding("FAIL", "access.duplicate", "Data access policy IDs must be unique."))
    roles = set(access.get("roles", []))
    for policy in policies:
        policy_id = policy.get("policy_id", "<missing>")
        if policy.get("required_role") not in roles:
            findings.append(Finding("FAIL", "access.role", f"{policy_id} references an undefined role."))
        if not policy.get("audit_requirement"):
            findings.append(Finding("FAIL", "access.audit", f"{policy_id} has no audit requirement."))
        if policy.get("data_classification") in {"SENSITIVE", "RESTRICTED"}:
            values = {str(policy.get("required_role", "")).upper(), *(str(item).upper() for item in policy.get("allowed_actions", []))}
            if values & WILDCARDS:
                findings.append(Finding("FAIL", "access.wildcard", f"{policy_id} grants wildcard access to protected data."))
        for asset_id in policy.get("data_asset_ids", []):
            if asset_id not in asset_map:
                findings.append(Finding("FAIL", "access.asset", f"{policy_id} references unknown asset {asset_id}."))

    for asset in assets:
        asset_id = asset.get("id", "<missing>")
        classification = asset.get("classification")
        if classification not in CLASSIFICATIONS:
            findings.append(Finding("FAIL", "classification.invalid", f"{asset_id} has invalid or absent classification {classification}."))
        if asset.get("lifecycle_state") == "ACTIVE" and classification in {None, "", "UNCLASSIFIED"}:
            findings.append(Finding("FAIL", "classification.unclassified", f"Active asset {asset_id} is unclassified."))
        if classification in {"SENSITIVE", "RESTRICTED", "SECRET_MATERIAL_REFERENCE"} and not asset.get("owner"):
            findings.append(Finding("FAIL", "ownership.missing", f"Protected asset {asset_id} has no owner."))
        policy_id = asset.get("access_model")
        if classification == "RESTRICTED" and policy_id not in policy_map:
            findings.append(Finding("FAIL", "access.restricted", f"Restricted asset {asset_id} lacks a defined access policy."))
        if policy_id not in policy_map:
            findings.append(Finding("FAIL", "access.reference", f"{asset_id} references unknown access policy {policy_id}."))

    flow_ids: list[str] = []
    for flow in flows.get("flows", []):
        flow_id = flow.get("flow_id", "<missing>")
        flow_ids.append(flow_id)
        source_id = flow.get("source_data_asset_id")
        destination_id = flow.get("destination_data_asset_id")
        if source_id not in asset_map:
            findings.append(Finding("FAIL", "flow.source", f"{flow_id} references unknown source asset {source_id}."))
            continue
        if destination_id is not None and destination_id not in asset_map:
            findings.append(Finding("FAIL", "flow.destination", f"{flow_id} references unknown destination asset {destination_id}."))
        source_class = asset_map[source_id].get("classification")
        if source_class == "RESTRICTED" and flow.get("trust_boundary_crossing") is True and not str(flow.get("encryption", "")).startswith("ENCRYPTED"):
            findings.append(Finding("FAIL", "flow.encryption", f"{flow_id} crosses a trust boundary with restricted data without evidenced encryption."))
        if source_class == "RESTRICTED" and not flow.get("logging"):
            findings.append(Finding("FAIL", "flow.logging", f"{flow_id} carries restricted data without audit metadata."))
    if len(flow_ids) != len(set(flow_ids)):
        findings.append(Finding("FAIL", "flow.duplicate", "Data flow IDs must be unique."))

    assessment_ids: list[str] = []
    for item in encryption.get("assessments", []):
        assessment_id = item.get("assessment_id", "<missing>")
        assessment_ids.append(assessment_id)
        if item.get("asset_id") not in asset_map:
            findings.append(Finding("FAIL", "encryption.asset", f"{assessment_id} references an unknown data asset."))
        if item.get("state") == "ENCRYPTED" and not item.get("evidence"):
            findings.append(Finding("FAIL", "encryption.evidence", f"{assessment_id} claims encryption without evidence."))
        if item.get("plane") == "IN_USE" and item.get("state") not in {"NOT_IMPLEMENTED", "REFERENCE_ONLY", "UNKNOWN"}:
            findings.append(Finding("FAIL", "encryption.in-use", f"{assessment_id} makes an unsupported encryption-in-use claim."))
    if len(assessment_ids) != len(set(assessment_ids)):
        findings.append(Finding("FAIL", "encryption.duplicate", "Encryption assessment IDs must be unique."))

    backup_ids: list[str] = []
    for backup in backups.get("backups", []):
        backup_id = backup.get("backup_id", "<missing>")
        backup_ids.append(backup_id)
        if backup.get("source_data_asset_id") not in asset_map:
            findings.append(Finding("FAIL", "backup.asset", f"{backup_id} references an unknown source asset."))
        if backup.get("validation_status") == "RESTORE_VALIDATED":
            evidence = backup.get("last_restore_evidence")
            if not evidence:
                findings.append(Finding("FAIL", "backup.restore", f"{backup_id} claims restore validation without restore evidence."))
            elif root is not None and not (root / evidence).is_file():
                findings.append(Finding("FAIL", "backup.evidence", f"{backup_id} restore evidence does not exist: {evidence}."))
    if len(backup_ids) != len(set(backup_ids)):
        findings.append(Finding("FAIL", "backup.duplicate", "Backup IDs must be unique."))

    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "data", f"{len(assets)} data assets, {len(policies)} access policies, {len(flow_ids)} flows, and {len(backup_ids)} backup records are internally consistent."))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=ROOT / "docs/zero-trust/data-inventory.yaml")
    parser.add_argument("--classifications", type=Path, default=ROOT / "docs/zero-trust/data-classification-policy.yaml")
    parser.add_argument("--access", type=Path, default=ROOT / "docs/zero-trust/data-access-policy.yaml")
    parser.add_argument("--flows", type=Path, default=ROOT / "docs/zero-trust/data-flow-map.yaml")
    parser.add_argument("--encryption", type=Path, default=ROOT / "docs/zero-trust/data-encryption-assessment.yaml")
    parser.add_argument("--backups", type=Path, default=ROOT / "docs/zero-trust/backup-inventory.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    try:
        findings = validate(load(args.inventory), load(args.classifications), load(args.access), load(args.flows), load(args.encryption), load(args.backups), ROOT)
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
