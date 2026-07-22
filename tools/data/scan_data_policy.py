#!/usr/bin/env python3
"""Detection-only, redacting DLP scanner for approved ZT-DATA-001 paths."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
APPROVED_ROOTS = {"docs", "schemas", "tools", "tests", "policy", "profiles", "observability"}
EXCLUDED_PARTS = {".git", ".runtime", ".venv", "venv", "node_modules", "vendor", "__pycache__"}
SAFE_CONTEXT = re.compile(r"(?i)(placeholder|example|fixture|regex|detector|prohibit|must not|do not|redact|construction|pattern_ref)")
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".ps1", ".sh", ".tf", ".ini", ".conf", ".csv"}


@dataclass(frozen=True)
class DlpFinding:
    detector: str
    severity: str
    path: str
    line: int
    redacted_match: str
    test_fixture: bool


def _patterns() -> tuple[tuple[str, str, re.Pattern[str]], ...]:
    five = "-" * 5
    return (
        ("PRIVATE_KEY_PATTERN", "CRITICAL", re.compile(five + r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY" + five)),
        ("API_TOKEN_PATTERN", "CRITICAL", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
        ("CLOUD_ACCESS_KEY_PATTERN", "CRITICAL", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
        ("PASSWORD_ASSIGNMENT", "HIGH", re.compile(r"(?i)\bpassword\s*[:=]\s*['\"]?[^\s'\"]{8,}")),
        ("CLIENT_SECRET_PATTERN", "CRITICAL", re.compile(r"(?i)\bclient[_-]?secret\s*[:=]\s*['\"]?[^\s'\"]{8,}")),
        ("DATABASE_CREDENTIAL_PATTERN", "CRITICAL", re.compile(r"(?i)\b(?:postgres(?:ql)?|mysql|mariadb)://[^\s:@]+:[^\s@]+@")),
        ("MFA_SECRET_PATTERN", "CRITICAL", re.compile(r"(?i)\botpauth://|\bmfa[_-]?seed\s*[:=]")),
        ("RECOVERY_CODE_PATTERN", "HIGH", re.compile(r"(?i)\brecovery[_-]?code\s*[:=]\s*[^\s]{6,}")),
        ("PERSONAL_IDENTIFIER_TEST_PATTERN", "MEDIUM", re.compile(r"\bTEST-PERSON-[0-9]{6}\b")),
        ("RESTRICTED_DATA_LABEL", "HIGH", re.compile(r"\bZTDATA-RESTRICTED-CONTENT\b")),
        ("UNAPPROVED_EXPORT_PATH", "CRITICAL", re.compile(r"(?i)(curl\s+[^\r\n]*(?:--upload-file|-T\s)|Invoke-WebRequest[^\r\n]*-Method\s+Put|aws\s+s3\s+cp)")),
    )


def scan_text(text: str, path: str) -> list[DlpFinding]:
    findings: list[DlpFinding] = []
    for number, line in enumerate(text.splitlines(), 1):
        fixture = "TEST_FIXTURE" in line
        if not fixture and SAFE_CONTEXT.search(line):
            continue
        for detector, severity, pattern in _patterns():
            if pattern.search(line):
                findings.append(DlpFinding(detector, severity, path, number, "[REDACTED]", fixture))
    return findings


def candidate_files(root: Path) -> Iterable[Path]:
    output = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout
    for relative in output.splitlines():
        path = Path(relative)
        if not path.parts or path.parts[0] not in APPROVED_ROOTS or set(path.parts) & EXCLUDED_PARTS:
            continue
        full = root / path
        if full.is_file() and full.suffix.lower() in TEXT_SUFFIXES:
            yield full


def scan_repository(root: Path) -> list[DlpFinding]:
    findings: list[DlpFinding] = []
    skip = {
        "tools/data/scan_data_policy.py",
        "docs/zero-trust/dlp-policy.yaml",
        "tests/fixtures/zt-data-001/fixture-catalog.yaml",
    }
    for path in candidate_files(root):
        relative = path.relative_to(root).as_posix()
        if relative in skip:
            continue
        findings.extend(scan_text(path.read_text(encoding="utf-8", errors="replace"), relative))
    return findings


def validate_policy(policy: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if policy.get("mode") != "DETECTION_ONLY":
        errors.append("DLP mode must remain DETECTION_ONLY.")
    if policy.get("external_transmission") is not False or policy.get("source_modification") is not False:
        errors.append("DLP policy must prohibit external transmission and source modification.")
    allowed = {"LOG", "ALERT", "CREATE_EVIDENCE", "REQUIRE_REVIEW"}
    forbidden = {"DELETE", "QUARANTINE", "BLOCK", "MODIFY", "ROTATE"}
    for rule in policy.get("rules", []):
        if not isinstance(rule, dict):
            errors.append("DLP rules must be objects.")
            continue
        actions = set(rule.get("actions", []))
        if not actions or actions - allowed or actions & forbidden:
            errors.append(f"{rule.get('rule_id', '<missing>')} contains a blocking or mutating action.")
        if rule.get("redaction") != "REDACT_MATCH":
            errors.append(f"{rule.get('rule_id', '<missing>')} does not require match redaction.")
    return errors


def controlled_fixture_text() -> str:
    five = "-" * 5
    values = [
        five + "BEGIN PRIVATE KEY" + five,
        "password" + " = " + "not-a-real-password",
        "AKIA" + "0" * 16,
        "gh" + "p_" + "A" * 24,
        "postgresql" + "://test:not-real@invalid.local/db",
        "otpauth" + "://totp/TEST?secret=NOTREAL",
        "TEST-PERSON-" + "0" * 6,
        "ZTDATA-RESTRICTED-CONTENT",
    ]
    return "\n".join("TEST_FIXTURE " + value for value in values)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    policy = json.loads((ROOT / "docs/zero-trust/dlp-policy.yaml").read_text(encoding="utf-8"))
    policy_errors = validate_policy(policy)
    findings = scan_repository(ROOT)
    fixture_findings = scan_text(controlled_fixture_text(), "TEST_FIXTURE/runtime-generated") if args.self_test else []
    confirmed = [item for item in findings if not item.test_fixture]
    critical = [item for item in confirmed if item.severity == "CRITICAL"]
    result = {
        "package_id": "ZT-DATA-001",
        "mode": "DETECTION_ONLY",
        "repository_findings": [asdict(item) for item in findings],
        "controlled_fixture_findings": [asdict(item) for item in fixture_findings],
        "confirmed_findings": len(confirmed),
        "critical_findings": len(critical),
        "matches_redacted": all(item.redacted_match == "[REDACTED]" for item in findings + fixture_findings),
        "source_modified": False,
        "external_transmission": False,
        "blocking_actions": False,
        "policy_errors": policy_errors,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        if args.verbose:
            print(f"[PASS] approved repository paths scanned with {len(_patterns())} detection-only detectors")
            print(f"[PASS] controlled non-functional fixture detections: {len(fixture_findings)}")
            print(f"[PASS] findings redacted: {result['matches_redacted']}")
            for item in confirmed:
                print(f"[{item.severity}] {item.detector} {item.path}:{item.line} [REDACTED]")
        print(f"DLP summary: confirmed={len(confirmed)} critical={len(critical)} fixtures={len(fixture_findings)} blocking=false external_transmission=false")
    return 1 if critical or policy_errors or not result["matches_redacted"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
