#!/usr/bin/env python3
"""Apply deterministic, non-mutating correlation rules to normalized JSONL."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

ALLOWED_ACTIONS = {"LOG", "ALERT", "CREATE_EVIDENCE", "REQUIRE_REVIEW"}


def load_rules(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        raise ValueError("rules array is missing")
    ids = [rule.get("id") for rule in rules]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate correlation rule ID")
    for rule in rules:
        if not isinstance(rule.get("event_selection"), dict):
            raise ValueError(f"{rule.get('id')}: event selection is missing")
        actions = set(rule.get("response_actions", []))
        if not actions or not actions <= ALLOWED_ACTIONS:
            raise ValueError(f"{rule.get('id')}: unsupported response action")
        if not isinstance(rule.get("threshold"), int) or rule["threshold"] < 1:
            raise ValueError(f"{rule.get('id')}: invalid threshold")
    return rules


def load_events(path: Path) -> list[dict]:
    events: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        event = record.get("event")
        if not isinstance(event, dict) or not event.get("event_id"):
            raise ValueError(f"line {number}: invalid normalized event")
        events.append(event)
    if not events:
        raise ValueError("no normalized events")
    return events


def matches(event: dict, selection: dict) -> bool:
    return all(event.get(key) == value for key, value in selection.items())


def correlate(events: list[dict], rules: list[dict]) -> list[dict]:
    findings: list[dict] = []
    for rule in rules:
        selected = [event for event in events if matches(event, rule["event_selection"])]
        groups: dict[tuple, list[dict]] = defaultdict(list)
        keys = rule.get("grouping", [])
        for event in selected:
            groups[tuple(event.get(key) for key in keys)].append(event)
        for group_events in groups.values():
            if len(group_events) < rule["threshold"]:
                continue
            source_ids = [event["event_id"] for event in group_events[: rule["threshold"]]]
            digest = hashlib.sha256((rule["id"] + "|" + "|".join(source_ids)).encode()).hexdigest()[:24]
            findings.append({
                "finding_id": f"fnd-{digest}",
                "rule_id": rule["id"],
                "rule_version": rule["version"],
                "timestamp": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
                "severity": rule["severity"],
                "confidence": "HIGH",
                "source_event_ids": source_ids,
                "response_actions": rule["response_actions"],
                "summary": f"{rule['id']} threshold met by sanitized normalized events",
            })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    try:
        rules = load_rules(args.rules)
        events = load_events(args.input)
        findings = correlate(events, rules)
        if not args.check:
            if args.output is None:
                raise ValueError("--output is required unless --check is used")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("w", encoding="utf-8", newline="\n") as handle:
                for finding in findings:
                    handle.write(json.dumps(finding, sort_keys=True) + "\n")
        if args.verbose:
            print(f"[PASS] loaded {len(rules)} rules and generated {len(findings)} findings")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[FAIL] correlation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
