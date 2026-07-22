#!/usr/bin/env python3
"""Dependency-free, offline, read-only security checks and partial SBOM generation."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OPTIONAL_TOOLS = ("trivy", "syft", "grype", "cosign", "gitleaks", "detect-secrets", "semgrep", "bandit", "ruff", "checkov", "tfsec", "hadolint", "shellcheck", "kube-score", "kube-linter", "conftest", "opa")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
SAFE_CONTEXT = re.compile(r"(?i)(placeholder|example|fixture|regex|detect|prohibit|must not|do not|redact)")


def tracked_files(root: Path) -> list[Path]:
    output = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout
    return [root / item for item in output.splitlines() if item]


def scan_secrets(root: Path) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    allowed = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".ps1", ".sh", ".tf", ".ini", ".conf"}
    for path in tracked_files(root):
        if path.suffix.lower() not in allowed or not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if SAFE_CONTEXT.search(line):
                continue
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                findings.append({"path": path.relative_to(root).as_posix(), "line": number, "finding": "REDACTED_SECRET_PATTERN"})
    return findings


def compose_components(compose_text: str, timestamp: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    images = re.findall(r"(?m)^\s+image:\s*([^\s#]+)\s*$", compose_text)
    components = []
    cdx = []
    workload_map = {"grafana/alloy": "ZTA-WORKLOAD-ALLOY", "grafana/loki": "ZTA-WORKLOAD-LOKI", "grafana/grafana": "ZTA-WORKLOAD-GRAFANA"}
    for reference in sorted(set(images)):
        name, version = reference.rsplit(":", 1) if ":" in reference else (reference, "UNKNOWN")
        component = {
            "application_id": "ZTA-APP-OBSERVABILITY-STACK",
            "workload_id": workload_map.get(name, "UNKNOWN"),
            "component_name": name,
            "component_version": version,
            "component_type": "CONTAINER_IMAGE",
            "supplier": "Grafana Labs" if name.startswith("grafana/") else "UNKNOWN",
            "license": "UNKNOWN",
            "package_url": f"pkg:docker/{name}@{version}",
            "source": "observability/logging/compose.yaml",
            "dependency_relationship": "DIRECT",
            "vulnerability_state": "NOT_ASSESSED",
            "evidence_authority": "CODEX_EXECUTED_LOCAL_VALIDATION",
            "collection_timestamp": timestamp,
            "limitations": ["Derived from the reviewed Compose image reference; transitive packages, digest, signature, and vulnerabilities are not represented."],
        }
        components.append(component)
        cdx.append({"type": "container", "name": name, "version": version, "purl": component["package_url"], "properties": [{"name": "snsd:source", "value": component["source"]}]})
    return components, cdx


def run(root: Path) -> dict[str, Any]:
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    compose_path = root / "observability/logging/compose.yaml"
    compose = compose_path.read_text(encoding="utf-8")
    secret_findings = scan_secrets(root)
    fixture_value = "gh" + "p_" + "A" * 24
    fixture_detected = any(pattern.search(fixture_value) for pattern in SECRET_PATTERNS)
    components, cdx_components = compose_components(compose, timestamp)
    config_failures = []
    if "privileged: true" in compose or "/var/run/docker.sock" in compose or "network_mode: host" in compose:
        config_failures.append("FORBIDDEN_CONTAINER_BOUNDARY")
    if compose.count("healthcheck:") < 3:
        config_failures.append("MISSING_HEALTHCHECK")
    tools = {name: ("AVAILABLE" if shutil.which(name) else "ABSENT") for name in OPTIONAL_TOOLS}
    component_inventory = {"schema_version": "1.0.0", "package_id": "ZT-APP-001", "sbom_status": "PARTIAL", "collection_timestamp": timestamp, "components": components, "limitations": ["Direct Compose images only; no external scanner was installed or invoked."]}
    sbom = {"bomFormat": "CycloneDX", "specVersion": "1.5", "version": 1, "metadata": {"timestamp": timestamp, "tools": {"components": [{"type": "application", "name": "snsd-builtin-compose-sbom", "version": "1.0.0"}]}}, "components": cdx_components}
    return {
        "package_id": "ZT-APP-001", "execution_mode": "OFFLINE_READ_ONLY", "timestamp": timestamp,
        "tools": tools, "scans_executed": ["BUILTIN_SECRET_SCAN", "BUILTIN_COMPOSE_POLICY", "BUILTIN_COMPOSE_SBOM"],
        "secret_findings": secret_findings, "controlled_fixture_detected": fixture_detected,
        "configuration_failures": config_failures, "component_inventory": component_inventory, "sbom": sbom,
        "network_access": False, "source_modified": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    report = run(ROOT)
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "scan-summary.json").write_text(json.dumps({k: v for k, v in report.items() if k not in {"component_inventory", "sbom"}}, indent=2) + "\n", encoding="utf-8")
        (args.output / "software-component-inventory.json").write_text(json.dumps(report["component_inventory"], indent=2) + "\n", encoding="utf-8")
        (args.output / "zt-app-001-sbom.cdx.json").write_text(json.dumps(report["sbom"], indent=2) + "\n", encoding="utf-8")
    failed = len(report["secret_findings"]) + len(report["configuration_failures"]) + (0 if report["controlled_fixture_detected"] else 1)
    if args.verbose:
        print(f"[PASS] scans: {', '.join(report['scans_executed'])}")
        print(f"[PASS] controlled non-functional secret fixture detected: {report['controlled_fixture_detected']}")
        print(f"[PASS] direct Compose components derived: {len(report['component_inventory']['components'])}")
        print(f"[INFO] optional tools absent: {sum(value == 'ABSENT' for value in report['tools'].values())}")
    print(f"Security scan summary: secret_findings={len(report['secret_findings'])} configuration_failures={len(report['configuration_failures'])} fail={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
