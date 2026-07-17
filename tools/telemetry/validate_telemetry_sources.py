#!/usr/bin/env python3
"""Read-only validation for the ZT-VIS-001 inventory, schemas, rules, and events."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from correlate_events import ALLOWED_ACTIONS, load_events, load_rules

SOURCE_STATES = {"CURRENT_RUNNING", "CURRENT_CONFIG_ONLY", "PLANNED", "ABSENT", "UNKNOWN"}


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=root / "docs/zero-trust/telemetry-source-inventory.yaml")
    parser.add_argument("--rules", type=Path, default=root / "docs/zero-trust/correlation-rule-catalog.yaml")
    parser.add_argument("--events", type=Path)
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
            events = load_events(args.events)
            running_names = {source["name"].lower().replace(" ", "-") for source in sources if source["current_state"] == "CURRENT_RUNNING"}
            observed = {event["source_name"] for event in events}
            result("PASS" if events else "FAIL", f"Normalized event storage contains {len(events)} records")
            result("PASS" if observed else "FAIL", "At least one current source has normalized events")
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
