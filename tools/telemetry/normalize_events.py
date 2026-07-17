#!/usr/bin/env python3
"""Normalize approved sanitized validator summaries into telemetry JSON Lines."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ALLOWED_ADAPTERS = {
    "validator-summary",
    "repository-validator-summary",
    "openstack-service-summary",
    "eve-host-summary",
    "router-validation-summary",
    "docker-health-summary",
}
LEVEL_RE = re.compile(r"^\[(PASS|WARN|FAIL)\]\s+(.+?)\s*$")
SENSITIVE_RE = re.compile(
    r"(?i)(?:-----BEGIN .*PRIVATE KEY-----|authorization\s*:|cookie\s*:|"
    r"password\s*[=:]|token\s*[=:]|(?:\d{1,3}\.){3}\d{1,3}|"
    r"(?:[0-9a-f]{2}:){5}[0-9a-f]{2}|[0-9a-f]{8}-[0-9a-f-]{27,})"
)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def category(source_type: str, message: str) -> str:
    lowered = message.lower()
    if source_type == "repository-validator-summary":
        return "REPOSITORY_VALIDATION"
    if any(word in lowered for word in ("interface", "route", "vlan", "nat", "network", "floating ip", "provider path")):
        return "NETWORK_POLICY" if any(word in lowered for word in ("acl", "policy", "segmentation")) else "NETWORK_STATE"
    if any(word in lowered for word in ("service", "container", "api", "endpoint")):
        return "SERVICE_HEALTH"
    if any(word in lowered for word in ("evidence", "sanitiz")):
        return "EVIDENCE_GENERATION"
    return "VALIDATOR_EXECUTION"


def validate_event(record: dict) -> list[str]:
    errors: list[str] = []
    event = record.get("event")
    required = {
        "schema_version", "event_id", "timestamp", "received_timestamp",
        "source_type", "source_name", "environment", "event_category",
        "event_type", "severity", "action", "outcome", "actor", "target",
        "network", "process", "authentication", "authorization", "policy",
        "validation", "correlation", "evidence", "sensitivity",
        "sanitization", "raw_reference",
    }
    if not isinstance(event, dict):
        return ["event object is missing"]
    missing = sorted(required - set(event))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if event.get("source_type") not in ALLOWED_ADAPTERS:
        errors.append("unsupported source adapter")
    if event.get("outcome") not in {"PASS", "WARN", "FAIL", "UNKNOWN"}:
        errors.append("invalid outcome")
    if event.get("severity") not in {"INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        errors.append("invalid severity")
    if SENSITIVE_RE.search(json.dumps(record, ensure_ascii=False)):
        errors.append("sensitive or unsanitized value detected")
    return errors


def normalize(path: Path, source_type: str, source_name: str, raw_reference: str) -> list[dict]:
    if source_type not in ALLOWED_ADAPTERS:
        raise ValueError("unsupported source adapter")
    if not re.fullmatch(r"[a-z0-9-]+", source_name):
        raise ValueError("source name must be a bounded slug")
    text = path.read_text(encoding="utf-8", errors="replace")
    if SENSITIVE_RE.search(text):
        raise ValueError("input is not sanitized")
    received = utc_now()
    records: list[dict] = []
    for index, line in enumerate(text.splitlines(), 1):
        match = LEVEL_RE.match(line)
        if not match:
            continue
        outcome, message = match.groups()
        severity = "HIGH" if outcome == "FAIL" else "MEDIUM" if outcome == "WARN" else "INFO"
        digest = hashlib.sha256(f"{source_name}|{index}|{message}|{received}".encode()).hexdigest()[:24]
        record = {
            "event": {
                "schema_version": "1.0",
                "event_id": f"evt-{digest}",
                "timestamp": received,
                "received_timestamp": received,
                "source_type": source_type,
                "source_name": source_name,
                "environment": "NON_PRODUCTION_LAB",
                "event_category": category(source_type, message),
                "event_type": "CHECK_RESULT",
                "severity": severity,
                "action": "VALIDATE",
                "outcome": outcome,
                "actor": None,
                "target": {"type": source_name},
                "network": None,
                "process": None,
                "authentication": None,
                "authorization": None,
                "policy": None,
                "validation": {"check": message, "result": outcome},
                "correlation": None,
                "evidence": {"authority": "CODEX_EXECUTED_LIVE_RUNTIME"},
                "sensitivity": "SANITIZED",
                "sanitization": {"status": "APPLIED"},
                "raw_reference": raw_reference,
            }
        }
        errors = validate_event(record)
        if errors:
            raise ValueError(f"normalized event {index} invalid: {'; '.join(errors)}")
        records.append(record)
    if not records:
        raise ValueError("input contains no PASS/WARN/FAIL records")
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--source-type", required=True, choices=sorted(ALLOWED_ADAPTERS))
    parser.add_argument("--source-name", required=True)
    parser.add_argument("--raw-reference", default="<ignored-runtime-reference>")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--append", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    try:
        records = normalize(args.input, args.source_type, args.source_name, args.raw_reference)
        if not args.check:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            mode = "a" if args.append else "w"
            with args.output.open(mode, encoding="utf-8", newline="\n") as handle:
                for record in records:
                    handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
        if args.verbose:
            print(f"[PASS] normalized {len(records)} events from {args.source_name}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[FAIL] normalization failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
