#!/usr/bin/env python3
"""Read-only validation for the Phase 1 package runbook manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path("docs/runbooks/phase-1/runbook-manifest.yaml")
FLOW_PATH = Path("docs/zero-trust/package-flow.yaml")
REQUIRED_RUNBOOKS = {
    f"RB-P1-{number:03d}": f"docs/runbooks/phase-1/{number:02d}-{slug}.md"
    for number, slug in [
        (1, "phase-1-entry-and-preflight"), (2, "repository-safe-validation"),
        (3, "evidence-handling-and-sanitization"), (4, "network-validation-and-gap-management"),
        (5, "visibility-validation-and-gap-management"), (6, "identity-validation-readiness"),
        (7, "repeatable-and-scheduled-validation"),
    ]
}


@dataclass
class Finding:
    level: str
    category: str
    message: str


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top level must be an object")
    return value


def run_validation(root: Path = ROOT, strict: bool = False) -> list[Finding]:
    del strict
    findings: list[Finding] = []
    try:
        manifest = load(root / MANIFEST_PATH)
        flow = load(root / FLOW_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        return [Finding("FAIL", "parse", str(exc))]
    expected_phase = {
        "implementation_status": "PARTIAL", "validation_status": "PARTIALLY_VALIDATED",
        "completion_status": "NOT_COMPLETE", "boundary": "ZT-SCH-001",
    }
    findings.append(Finding(
        "PASS" if manifest.get("phase_state") == expected_phase else "FAIL", "phase",
        "Manifest preserves the Phase 1 boundary." if manifest.get("phase_state") == expected_phase
        else "Manifest overclaims or changes Phase 1 state.",
    ))
    rows = manifest.get("runbooks", [])
    ids = [row.get("runbook_id") for row in rows]
    paths = {row.get("runbook_id"): row.get("path") for row in rows}
    manifest_ok = ids == list(REQUIRED_RUNBOOKS) and paths == REQUIRED_RUNBOOKS and len(ids) == len(set(ids))
    findings.append(Finding("PASS" if manifest_ok else "FAIL", "manifest",
                            "Seven unique package runbooks are registered." if manifest_ok else f"Unexpected registration: {paths}"))
    package_ids = {row.get("package_id") for row in flow.get("packages", [])}
    for row in rows:
        relative = row.get("path", "")
        path = root / relative
        if not path.is_file():
            findings.append(Finding("FAIL", "files", f"Missing {relative}"))
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(r"```json runbook-metadata\s*\n(.*?)\n```", text, re.DOTALL)
        try:
            metadata = json.loads(match.group(1)) if match else {}
        except json.JSONDecodeError as exc:
            findings.append(Finding("FAIL", "metadata", f"{relative}: {exc}"))
            continue
        if metadata.get("runbook_id") != row.get("runbook_id"):
            findings.append(Finding("FAIL", "metadata", f"{relative}: runbook ID mismatch"))
        if metadata.get("validation_status") != row.get("validation_status"):
            findings.append(Finding("FAIL", "metadata", f"{relative}: validation status mismatch"))
        unknown = set(row.get("related_packages", [])) - package_ids
        if unknown:
            findings.append(Finding("FAIL", "packages", f"{relative}: unknown packages {sorted(unknown)}"))
    if not any(item.level == "FAIL" and item.category in {"files", "metadata", "packages"} for item in findings):
        findings.append(Finding("PASS", "runbooks", "Runbook files, metadata, statuses, and package ownership agree."))
    legacy = root / "runbooks"
    findings.append(Finding("FAIL" if legacy.exists() else "PASS", "retirement",
                            "Legacy root runbook authority still exists." if legacy.exists()
                            else "Legacy root runbook authority is absent."))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    findings = run_validation(args.root.resolve(), args.strict)
    failed = sum(item.level == "FAIL" for item in findings)
    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in findings], "failed": failed}, indent=2))
    else:
        for item in findings:
            if args.verbose or item.level == "FAIL":
                print(f"[{item.level}] {item.category}: {item.message}")
        print(f"Phase 1 runbook summary: passed={sum(i.level == 'PASS' for i in findings)}, failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
