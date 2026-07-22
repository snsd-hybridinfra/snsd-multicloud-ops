#!/usr/bin/env python3
"""Validate backup claims and optionally run one isolated synthetic restore test."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
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


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(inventory: dict[str, Any], evidence: dict[str, Any], root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    records = inventory.get("backups", [])
    if not records:
        return [Finding("FAIL", "backup.present", "Backup inventory is empty.")]
    evidence_id = evidence.get("backup_id")
    for record in records:
        backup_id = record.get("backup_id", "<missing>")
        status = record.get("validation_status")
        backup_evidence = record.get("last_backup_evidence")
        restore_evidence = record.get("last_restore_evidence")
        if status in {"BACKUP_CREATED", "INTEGRITY_VALIDATED", "RESTORE_PARTIALLY_VALIDATED", "RESTORE_VALIDATED"}:
            if not backup_evidence or (not (root / backup_evidence).is_file() and backup_id != evidence_id):
                findings.append(Finding("FAIL", "backup.evidence", f"{backup_id} lacks an existing backup evidence file."))
        if status == "RESTORE_VALIDATED":
            if not restore_evidence or (not (root / restore_evidence).is_file() and backup_id != evidence_id):
                findings.append(Finding("FAIL", "restore.evidence", f"{backup_id} claims restore validation without existing evidence."))
            if backup_id != evidence_id:
                findings.append(Finding("FAIL", "restore.record", f"{backup_id} has no matching assurance record."))
            hashes = [evidence.get(name) for name in ("source_sha256", "backup_sha256", "restore_sha256")]
            if any(not isinstance(value, str) or len(value) != 64 for value in hashes):
                findings.append(Finding("FAIL", "restore.hash", f"{backup_id} evidence lacks three SHA-256 values."))
            elif len(set(hashes)) != 1:
                findings.append(Finding("FAIL", "restore.hash", f"{backup_id} source, backup, and restore hashes differ."))
            if evidence.get("source_overwritten") is not False or evidence.get("isolated_restore") is not True:
                findings.append(Finding("FAIL", "restore.isolation", f"{backup_id} does not prove isolated, non-overwriting restoration."))
    if not any(item.level == "FAIL" for item in findings):
        unknown = sum(item.get("validation_status") == "UNKNOWN" for item in records)
        if unknown:
            findings.append(Finding("WARN", "backup.unknown", f"{unknown} active platform backup records remain UNKNOWN."))
        findings.append(Finding("PASS", "backup", f"{len(records)} backup records preserve creation/restore separation; the synthetic pilot has matching hashes."))
    return findings


def execute_controlled_fixture(output_root: Path) -> dict[str, Any]:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    run_root = output_root / stamp
    source_dir = run_root / "source"
    backup_dir = run_root / "backup"
    restore_dir = run_root / "restore"
    source_dir.mkdir(parents=True, exist_ok=False)
    backup_dir.mkdir()
    restore_dir.mkdir()
    source = source_dir / "synthetic-dataset.json"
    backup = backup_dir / "synthetic-dataset.backup"
    restored = restore_dir / "synthetic-dataset.restored.json"
    payload = {
        "fixture_authority": "TEST_FIXTURE",
        "dataset_id": "ZTDATA-SYNTHETIC-BACKUP-SOURCE",
        "classification": "INTERNAL",
        "contains_real_data": False,
        "records": [{"record_id": "SYNTHETIC-001", "value": "NON_SENSITIVE_TEST_VALUE"}],
    }
    source.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")
    source_before = digest(source)
    shutil.copy2(source, backup)
    backup_hash = digest(backup)
    shutil.copy2(backup, restored)
    restore_hash = digest(restored)
    source_after = digest(source)
    result = {
        "package_id": "ZT-DATA-001",
        "backup_id": "ZTBACKUP-SYNTHETIC-PILOT",
        "execution_timestamp": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "dataset_classification": "INTERNAL_TEST_FIXTURE",
        "source_sha256": source_before,
        "backup_sha256": backup_hash,
        "restore_sha256": restore_hash,
        "source_unchanged_sha256": source_after,
        "hash_match": len({source_before, backup_hash, restore_hash, source_after}) == 1,
        "isolated_restore": restored.parent != source.parent,
        "source_overwritten": False,
        "encryption_status": "NOT_ENCRYPTED",
        "external_transmission": False,
        "source_contains_real_data": False,
        "cleanup_performed": False,
        "cleanup_boundary": "OPERATOR_REVIEWED_RUNTIME_CLEANUP",
        "runtime_root": ".runtime/zero-trust/data/backup-test/<run-id>",
    }
    (run_root / "backup-assurance.raw.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if not result["hash_match"] or not result["isolated_restore"]:
        raise RuntimeError("Controlled backup/restore hash or isolation validation failed.")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=ROOT / "docs/zero-trust/backup-inventory.yaml")
    parser.add_argument("--evidence", type=Path, default=ROOT / "docs/evidence/zero-trust/zt-data-001-backup-assurance.yaml")
    parser.add_argument("--execute-controlled-fixture", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / ".runtime/zero-trust/data/backup-test")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    try:
        executed = execute_controlled_fixture(args.output) if args.execute_controlled_fixture else None
        evidence = executed if executed is not None else load(args.evidence)
        findings = validate(load(args.inventory), evidence, ROOT)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        findings = [Finding("FAIL", "execution", str(exc))]
        executed = None
    counts = {level: sum(item.level == level for item in findings) for level in ("PASS", "WARN", "FAIL")}
    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in findings], "summary": counts, "execution": executed}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS":
                print(f"[{item.level}] {item.check}: {item.message}")
        if executed is not None:
            print(f"[PASS] controlled synthetic source/backup/restore hashes match: {executed['hash_match']}")
            print("[PASS] isolated restore completed without overwriting source; no external transmission occurred")
        print(f"Summary: {counts['PASS']} PASS / {counts['WARN']} WARN / {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
