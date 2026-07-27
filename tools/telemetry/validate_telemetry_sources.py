#!/usr/bin/env python3
"""Read-only validation for the ZT-VIS-001 inventory, schemas, rules, and events."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from correlate_events import ALLOWED_ACTIONS, load_events, load_rules

SOURCE_STATES = {"CURRENT_RUNNING", "CURRENT_CONFIG_ONLY", "PLANNED", "ABSENT", "UNKNOWN"}


def newest_event_age_seconds(events: list[dict], now: dt.datetime | None = None) -> int:
    """Return newest received-event age while rejecting ambiguous or future time."""
    timestamps: list[dt.datetime] = []
    for event in events:
        value = event.get("received_timestamp")
        if not isinstance(value, str):
            raise ValueError("normalized event received_timestamp is missing")
        try:
            parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("normalized event received_timestamp is invalid") from exc
        if parsed.tzinfo is None:
            raise ValueError("normalized event received_timestamp lacks a timezone")
        timestamps.append(parsed.astimezone(dt.timezone.utc))
    if not timestamps:
        raise ValueError("no normalized event timestamps")
    reference = now or dt.datetime.now(dt.timezone.utc)
    if reference.tzinfo is None:
        raise ValueError("freshness reference lacks a timezone")
    age = (reference.astimezone(dt.timezone.utc) - max(timestamps)).total_seconds()
    if age < -30:
        raise ValueError("newest normalized event is more than 30 seconds in the future")
    return max(0, int(age))


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=root / "docs/zero-trust/telemetry-source-inventory.yaml")
    parser.add_argument("--rules", type=Path, default=root / "docs/zero-trust/correlation-rule-catalog.yaml")
    parser.add_argument("--events", type=Path)
    parser.add_argument("--maximum-age-seconds", type=int, default=900)
    args = parser.parse_args()
    passed = warnings = failed = 0

    def result(level: str, message: str) -> None:
        nonlocal passed, warnings, failed
        if level == "PASS": passed += 1
        elif level == "WARN": warnings += 1
        else: failed += 1
        print(f"[{level}] {message}")

    try:
        inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
        sources = inventory.get("sources", [])
        result("PASS" if sources else "FAIL", "Telemetry source inventory is loadable")
        ids = [source.get("id") for source in sources]
        result("PASS" if len(ids) == len(set(ids)) else "FAIL", "Telemetry source IDs are unique")
        result("PASS" if all(source.get("current_state") in SOURCE_STATES for source in sources) else "FAIL", "Source states use the approved model")
        forbidden_paths = ("clouds.yaml", "passwords.yml", "/etc/shadow", "/.ssh/", "kubeconfig")
        serialized = json.dumps(inventory).lower()
        result("PASS" if not any(value in serialized for value in forbidden_paths) else "FAIL", "Credential-bearing collection paths are absent")
        rules = load_rules(args.rules)
        result("PASS", f"{len(rules)} unique deterministic correlation rules are loadable")
        actions = {action for rule in rules for action in rule["response_actions"]}
        result("PASS" if actions <= ALLOWED_ACTIONS else "FAIL", "Correlation actions are non-blocking")
        schemas = (root / "schemas/zero-trust-telemetry-event.schema.json", root / "schemas/zero-trust-correlation-finding.schema.json")
        for schema in schemas:
            json.loads(schema.read_text(encoding="utf-8"))
        result("PASS", "Telemetry and finding schemas are valid JSON")
        if args.events:
            if args.maximum_age_seconds <= 0:
                raise ValueError("maximum event age must be positive")
            events = load_events(args.events)
            observed = {event["source_name"] for event in events}
            result("PASS" if events else "FAIL", f"Normalized event storage contains {len(events)} records")
            result("PASS" if observed else "FAIL", "At least one current source has normalized events")
            age = newest_event_age_seconds(events)
            result(
                "PASS" if age <= args.maximum_age_seconds else "FAIL",
                f"Newest normalized event age is {age} seconds (maximum {args.maximum_age_seconds})",
            )
        else:
            result("WARN", "Live event freshness was not requested")
        retention_ok = all(source.get("retention") for source in sources)
        result("PASS" if retention_ok else "FAIL", "Every source has an explicit retention statement")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result("FAIL", f"Telemetry validation error: {exc}")
    print(f"PASS count: {passed}")
    print(f"WARN count: {warnings}")
    print(f"FAIL count: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
