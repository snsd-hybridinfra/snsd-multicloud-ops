#!/usr/bin/env python3
"""Normalize an approved sanitized endpoint summary without touching endpoints."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_SOURCE_AUTHORITIES = {"CODEX_EXECUTED_LIVE_RUNTIME", "SYNTHETIC_FIXTURE"}
ALLOWED_AGENT_STATES = {"NOT_INSTALLED", "EXISTING_HEALTHY", "EXISTING_UNHEALTHY", "UNKNOWN"}
REQUIRED_INPUTS = {
    "asset_id",
    "collection_time",
    "source_authority",
    "os_family",
    "os_release",
    "kernel",
    "package_count",
    "container_runtime",
    "compose_runtime",
    "running_container_count",
    "security_updates_available",
    "reboot_required",
    "package_manager_error",
    "endpoint_agent_state",
}


def _as_bool(value: Any, field: str) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes"}:
        return True
    if text in {"false", "0", "no"}:
        return False
    raise ValueError(f"{field} must be a boolean")


def _as_nonnegative_int(value: Any, field: str) -> int:
    try:
        result = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be an integer") from exc
    if result < 0:
        raise ValueError(f"{field} must not be negative")
    return result


def normalize_record(raw: dict[str, Any]) -> dict[str, Any]:
    missing = sorted(REQUIRED_INPUTS - raw.keys())
    if missing:
        raise ValueError(f"missing required sanitized inputs: {', '.join(missing)}")
    unexpected = sorted(set(raw) - REQUIRED_INPUTS)
    if unexpected:
        raise ValueError(f"unexpected input fields: {', '.join(unexpected)}")

    authority = str(raw["source_authority"])
    if authority not in ALLOWED_SOURCE_AUTHORITIES:
        raise ValueError("source_authority is not approved")
    asset_id = str(raw["asset_id"])
    if not asset_id.startswith("ZTD-ASSET-"):
        raise ValueError("asset_id must use the stable ZTD-ASSET alias namespace")

    package_error = _as_bool(raw["package_manager_error"], "package_manager_error")
    reboot_required = _as_bool(raw["reboot_required"], "reboot_required")
    security_updates = _as_nonnegative_int(raw["security_updates_available"], "security_updates_available")
    if package_error:
        patch_classification = "PACKAGE_MANAGER_ERROR"
    elif reboot_required:
        patch_classification = "REBOOT_REQUIRED"
    elif security_updates:
        patch_classification = "SECURITY_UPDATES_AVAILABLE"
    else:
        patch_classification = "CURRENT"

    agent_state = str(raw["endpoint_agent_state"])
    if agent_state not in ALLOWED_AGENT_STATES:
        raise ValueError("endpoint_agent_state is invalid")

    return {
        "schema_version": "1.0.0",
        "package_id": "ZT-DEV-001",
        "asset_id": asset_id,
        "collection_time": str(raw["collection_time"]),
        "source_authority": authority,
        "operating_system": {
            "family": str(raw["os_family"]),
            "release": str(raw["os_release"]),
            "kernel": str(raw["kernel"]),
        },
        "software": {
            "package_count": _as_nonnegative_int(raw["package_count"], "package_count"),
            "container_runtime": str(raw["container_runtime"]),
            "compose_runtime": str(raw["compose_runtime"]),
            "running_container_count": _as_nonnegative_int(raw["running_container_count"], "running_container_count"),
        },
        "patch_state": {
            "classification": patch_classification,
            "security_updates_available": security_updates,
            "reboot_required": reboot_required,
            "automatic_patching_performed": False,
        },
        "vulnerability": {
            "assessment_method": "NATIVE_SECURITY_UPDATE_PROXY",
            "classification": "ASSESSMENT_LIMITED" if not package_error else "NOT_ASSESSED",
            "finding_count": security_updates if not package_error else None,
            "exploit_executed": False,
        },
        "endpoint_agent": {
            "state": agent_state,
            "installed_by_package": False,
        },
        "incomplete_data": [
            "No dedicated vulnerability scanner result is included.",
            "Package names and personal or hardware identifiers are intentionally excluded.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--format", choices=("json", "yaml"), default="json")
    args = parser.parse_args(argv)

    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("input must be a JSON object")
        record = normalize_record(raw)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    # JSON is a valid YAML 1.2 serialization and keeps this tool dependency-free.
    rendered = json.dumps(record, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
