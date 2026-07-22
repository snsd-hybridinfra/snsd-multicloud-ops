#!/usr/bin/env python3
"""Static secure-deployment and gate validator for the Alloy pilot."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    message: str


def validate(policy: dict, compose_text: str, component_inventory: dict | None) -> list[Finding]:
    findings: list[Finding] = []
    if policy.get("automatic_enforcement") is not False or policy.get("automatic_deployment") is not False or policy.get("automatic_restart") is not False:
        findings.append(Finding("FAIL", "policy.mutation", "Automatic enforcement, deployment, and restart must be false."))
    controls = policy.get("controls", [])
    ids = [item.get("control_id") for item in controls if isinstance(item, dict)]
    if len(ids) != len(set(ids)) or len(ids) < 10:
        findings.append(Finding("FAIL", "policy.controls", "Secure-deployment controls must be unique and cover the bounded control set."))

    start = compose_text.find("  alloy:")
    end = compose_text.find("\n  grafana:", start)
    alloy = compose_text[start:end] if start >= 0 and end > start else ""
    required = ("grafana/alloy:v1.18.0", "read_only: true", "no-new-privileges=true", "cap_drop:", "- ALL", "healthcheck:", "mem_limit:", "cpus:", "127.0.0.1:12345:12345")
    for token in required:
        if token not in alloy:
            findings.append(Finding("FAIL", "pilot.configuration", f"Alloy pilot is missing required control: {token}"))
    if "privileged: true" in alloy or "/var/run/docker.sock" in alloy or "network_mode: host" in alloy:
        findings.append(Finding("FAIL", "pilot.privilege", "Alloy pilot contains a forbidden privilege or host boundary."))
    if 'user: "0:0"' in alloy:
        findings.append(Finding("WARN", "pilot.root", "Alloy runs as container UID 0; compensating controls are present but non-root compatibility remains open."))
    if "@sha256:" not in alloy:
        findings.append(Finding("WARN", "pilot.digest", "Alloy image uses a pinned version tag but no immutable digest."))
    if component_inventory is None:
        findings.append(Finding("FAIL", "sbom.missing", "Software component inventory is missing."))
    elif component_inventory.get("sbom_status") != "PARTIAL" or not component_inventory.get("components"):
        findings.append(Finding("FAIL", "sbom.status", "The current direct-image inventory must remain explicitly PARTIAL."))
    if not any(item.level == "FAIL" for item in findings):
        findings.append(Finding("PASS", "deployment", "All blocking bounded deployment controls pass; documented artifact and root-user gaps remain."))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=ROOT / "docs/zero-trust/secure-deployment-policy.yaml")
    parser.add_argument("--compose", type=Path, default=ROOT / "observability/logging/compose.yaml")
    parser.add_argument("--components", type=Path, default=ROOT / "docs/zero-trust/software-component-inventory.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    try:
        policy = json.loads(args.policy.read_text(encoding="utf-8"))
        compose = args.compose.read_text(encoding="utf-8")
        components = json.loads(args.components.read_text(encoding="utf-8")) if args.components.is_file() else None
        findings = validate(policy, compose, components)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        findings = [Finding("FAIL", "load", str(exc))]
    counts = {level: sum(item.level == level for item in findings) for level in ("PASS", "WARN", "FAIL")}
    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in findings], "summary": counts}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level != "PASS": print(f"[{item.level}] {item.check}: {item.message}")
        print(f"Summary: {counts['PASS']} PASS / {counts['WARN']} WARN / {counts['FAIL']} FAIL")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
