#!/usr/bin/env python3
"""Read-only validator for the authoritative Phase 1 runbook baseline."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path("docs/runbooks/phase-1/runbook-manifest.yaml")
INDEX_PATH = Path("docs/runbooks/RUNBOOK_INDEX.md")
README_PATH = Path("docs/runbooks/README.md")
TEMPLATE_PATH = Path("docs/runbooks/RUNBOOK_TEMPLATE.md")

REQUIRED_RUNBOOKS = {
    "RB-P1-001": "docs/runbooks/phase-1/01-phase-1-entry-and-preflight.md",
    "RB-P1-002": "docs/runbooks/phase-1/02-repository-safe-validation.md",
    "RB-P1-003": "docs/runbooks/phase-1/03-evidence-handling-and-sanitization.md",
    "RB-P1-004": "docs/runbooks/phase-1/04-network-validation-and-gap-management.md",
    "RB-P1-005": "docs/runbooks/phase-1/05-visibility-validation-and-gap-management.md",
    "RB-P1-006": "docs/runbooks/phase-1/06-identity-validation-readiness.md",
    "RB-P1-007": "docs/runbooks/phase-1/07-repeatable-and-scheduled-validation.md",
}

REQUIRED_SECTIONS = [
    "Purpose",
    "Scope",
    "Related Phase",
    "Related Package or Governance Action",
    "Supported Target Types",
    "Current Procedure Status",
    "Current Validation Status",
    "Evidence Authority",
    "Required Authority",
    "User-Performed Physical or Approval Steps",
    "Codex or Automation-Managed Steps",
    "Prerequisites",
    "Inputs",
    "Secret Inputs",
    "Service Impact",
    "Security Impact",
    "Preflight Checks",
    "Procedure",
    "Expected Output",
    "Validation",
    "Pass Criteria",
    "Stop Conditions",
    "Failure Handling",
    "Rollback",
    "Evidence",
    "Escalation",
    "Known Limitations",
    "Related Architecture",
    "Related Runbooks",
]

REQUIRED_METADATA = {
    "runbook_id",
    "title",
    "phase",
    "related_packages",
    "owner_domain",
    "supported_target_types",
    "procedure_status",
    "validation_status",
    "runtime_required",
    "live_execution_permitted",
    "required_authority",
    "evidence_authority",
    "last_reviewed",
    "limitations",
}

PROCEDURE_STATUSES = {
    "DESIGN_SPECIFICATION",
    "IMPLEMENTED",
    "PARTIALLY_IMPLEMENTED",
    "NOT_IMPLEMENTED",
}
VALIDATION_STATUSES = {
    "NOT_VALIDATED",
    "VALIDATED_LOCAL",
    "PARTIALLY_RUNTIME_VALIDATED",
    "VALIDATED_RUNTIME",
    "BLOCKED",
}
EVIDENCE_AUTHORITIES = {
    "NONE",
    "CODEX_EXECUTED_LOCAL",
    "CODEX_EXECUTED_LIVE_RUNTIME",
    "USER_EXECUTED_LIVE_RUNTIME",
}
COMMAND_STATUSES = {
    "AVAILABLE_READ_ONLY",
    "AVAILABLE_MUTATING_APPROVAL_REQUIRED",
    "PLANNED_NOT_IMPLEMENTED",
    "LIVE_RUNTIME_REQUIRED",
    "PHYSICAL_USER_ACTION",
    "PROHIBITED_IN_CURRENT_PHASE",
}
COMMAND_FIELDS = {
    "command_status",
    "execution_owner",
    "approval_required",
    "runtime_target",
    "expected_effect",
    "evidence_output",
    "rollback_reference",
}

PACKAGE_BOUNDARIES = {
    "ZT-FND-001": ("IMPLEMENTED", "VALIDATED_RUNTIME"),
    "ZT-NET-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
    "ZT-VIS-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
    "ZT-ID-001": ("IMPLEMENTED", "RUNTIME_VALIDATED"),
    "ZT-CV-001": ("NOT_IMPLEMENTED", "NOT_VALIDATED"),
    "ZT-RV-001": ("NOT_IMPLEMENTED", "NOT_VALIDATED"),
    "ZT-SCH-001": ("DESIGN_ONLY", "NOT_VALIDATED"),
    "ZT-VIS-002": ("PREPARATION_TRACES_ONLY", "NOT_VALIDATED"),
    "ZT-ARC-001": ("DESIGN_ONLY", "VALIDATED_LOCAL"),
}


@dataclass
class Finding:
    level: str
    category: str
    message: str


class Results:
    def __init__(self) -> None:
        self.findings: list[Finding] = []

    def pass_(self, category: str, message: str) -> None:
        self.findings.append(Finding("PASS", category, message))

    def warn(self, category: str, message: str) -> None:
        self.findings.append(Finding("WARN", category, message))

    def fail(self, category: str, message: str) -> None:
        self.findings.append(Finding("FAIL", category, message))

    def summary(self) -> dict[str, int]:
        return {
            "passed": sum(item.level == "PASS" for item in self.findings),
            "warnings": sum(item.level == "WARN" for item in self.findings),
            "failed": sum(item.level == "FAIL" for item in self.findings),
        }


def _read(path: Path, results: Results, category: str) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        results.fail(category, f"Cannot read {path.as_posix()}: {exc}")
        return None


def _load_json(path: Path, results: Results, category: str) -> dict[str, Any] | None:
    text = _read(path, results, category)
    if text is None:
        return None
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        results.fail(category, f"JSON-compatible YAML parse failed: {exc}")
        return None
    if not isinstance(value, dict):
        results.fail(category, "Top-level document must be an object.")
        return None
    return value


def _json_blocks(text: str, label: str) -> list[dict[str, Any]]:
    pattern = re.compile(rf"```json\s+{re.escape(label)}\s*\n(.*?)\n```", re.DOTALL)
    values: list[dict[str, Any]] = []
    for match in pattern.finditer(text):
        value = json.loads(match.group(1))
        if not isinstance(value, dict):
            raise ValueError(f"{label} block must be an object")
        values.append(value)
    return values


def _runbook_texts(root: Path, results: Results) -> dict[str, tuple[Path, str, dict[str, Any]]]:
    parsed: dict[str, tuple[Path, str, dict[str, Any]]] = {}
    for expected_id, relative in REQUIRED_RUNBOOKS.items():
        path = root / relative
        text = _read(path, results, "runbooks.required")
        if text is None:
            continue
        try:
            blocks = _json_blocks(text, "runbook-metadata")
        except (json.JSONDecodeError, ValueError) as exc:
            results.fail("runbooks.metadata", f"{relative}: invalid metadata: {exc}")
            continue
        if len(blocks) != 1:
            results.fail("runbooks.metadata", f"{relative}: expected exactly one runbook metadata block.")
            continue
        actual_id = blocks[0].get("runbook_id")
        parsed[expected_id] = (path, text, blocks[0])
        if actual_id != expected_id:
            results.fail("runbooks.ids", f"{relative}: expected {expected_id}, found {actual_id!r}.")
    return parsed


def _validate_manifest(root: Path, results: Results) -> dict[str, Any] | None:
    manifest = _load_json(root / MANIFEST_PATH, results, "manifest.parse")
    if manifest is None:
        return None

    required_top = {
        "manifest_id",
        "manifest_version",
        "phase",
        "authoritative_root",
        "validation_status",
        "evidence_authority",
        "phase_state",
        "runbooks",
        "package_boundaries",
        "legacy_references",
        "future_phase_runbooks",
        "unresolved_gaps",
    }
    missing = sorted(required_top - manifest.keys())
    if missing:
        results.fail("manifest.schema", f"Missing manifest fields: {', '.join(missing)}")
    else:
        results.pass_("manifest.schema", "Manifest contains all required top-level fields.")

    if manifest.get("manifest_id") != "P1-RUN-BASE" or manifest.get("phase") != "PHASE_1":
        results.fail("manifest.identity", "Manifest identity or phase is invalid.")
    else:
        results.pass_("manifest.identity", "Manifest identity and phase are correct.")

    entries = manifest.get("runbooks")
    if not isinstance(entries, list):
        results.fail("manifest.runbooks", "runbooks must be a list.")
        entries = []
    ids = [entry.get("runbook_id") for entry in entries if isinstance(entry, dict)]
    paths = [entry.get("path") for entry in entries if isinstance(entry, dict)]
    if len(entries) != 7 or len(ids) != len(set(ids)) or set(ids) != set(REQUIRED_RUNBOOKS):
        results.fail("manifest.runbooks", "Manifest must contain exactly one entry for each RB-P1-001 through RB-P1-007.")
    elif any(REQUIRED_RUNBOOKS[item_id] != path for item_id, path in zip(ids, paths)):
        results.fail("manifest.runbooks", "A manifest runbook path does not match its required ID.")
    else:
        results.pass_("manifest.runbooks", "Manifest contains the seven required unique ID/path pairs.")

    phase = manifest.get("phase_state", {})
    expected_phase = {
        "implementation_status": "PARTIAL",
        "validation_status": "PARTIALLY_VALIDATED",
        "completion_status": "NOT_COMPLETE",
        "boundary": "ZT-SCH-001",
    }
    if not isinstance(phase, dict) or any(phase.get(key) != value for key, value in expected_phase.items()):
        results.fail("manifest.phase", "Phase 1 state or ZT-SCH-001 boundary was promoted or changed.")
    else:
        results.pass_("manifest.phase", "Phase 1 remains PARTIAL/PARTIALLY_VALIDATED/NOT_COMPLETE.")

    packages = manifest.get("package_boundaries", [])
    package_map = {item.get("package_id"): item for item in packages if isinstance(item, dict)}
    errors = []
    for package_id, (implementation, validation) in PACKAGE_BOUNDARIES.items():
        item = package_map.get(package_id)
        if not item:
            errors.append(f"missing {package_id}")
        elif item.get("implementation_status") != implementation or item.get("validation_status") != validation:
            errors.append(f"changed {package_id}")
    if errors:
        results.fail("manifest.packages", "; ".join(errors))
    else:
        results.pass_("manifest.packages", "All protected Phase 1 and architecture package boundaries are preserved.")

    legacy = manifest.get("legacy_references", [])
    legacy_ok = (
        isinstance(legacy, list)
        and len(legacy) == 1
        and legacy[0].get("path") == "runbooks/"
        and legacy[0].get("authoritative") is False
        and legacy[0].get("authority_status") == "SECONDARY_REFERENCE_ONLY"
    )
    if not legacy_ok:
        results.fail("manifest.legacy", "Root runbooks/ must remain a non-authoritative secondary reference collection.")
    else:
        results.pass_("manifest.legacy", "Legacy scenario runbooks remain secondary references.")

    future = manifest.get("future_phase_runbooks", [])
    expected_future = {f"docs/runbooks/{number:02d}-" for number in range(29)}
    prefixes = {str(item)[:17] for item in future if isinstance(item, str)}
    # Check exact count, uniqueness, existence, and 00-28 numeric coverage below.
    numbers = set()
    for item in future if isinstance(future, list) else []:
        match = re.match(r"docs/runbooks/(\d{2})-.*\.md$", str(item))
        if match:
            numbers.add(int(match.group(1)))
    if (
        not isinstance(future, list)
        or len(future) != 29
        or len(set(future)) != 29
        or numbers != set(range(29))
        or any(not (root / item).is_file() for item in future)
    ):
        results.fail("manifest.future", "Future-phase list must resolve uniquely to numbered 00-28 design specifications.")
    else:
        results.pass_("manifest.future", "The 29 numbered future design specifications are separated from Phase 1.")

    return manifest


def _validate_runbooks(
    root: Path,
    manifest: dict[str, Any] | None,
    parsed: dict[str, tuple[Path, str, dict[str, Any]]],
    results: Results,
) -> None:
    actual_ids: list[str] = []
    manifest_entries = {
        item.get("runbook_id"): item
        for item in (manifest or {}).get("runbooks", [])
        if isinstance(item, dict)
    }

    for expected_id, relative in REQUIRED_RUNBOOKS.items():
        if expected_id not in parsed:
            continue
        _, text, metadata = parsed[expected_id]
        actual_ids.append(str(metadata.get("runbook_id")))

        missing_meta = sorted(REQUIRED_METADATA - metadata.keys())
        if missing_meta:
            results.fail("runbooks.metadata", f"{expected_id}: missing metadata fields: {', '.join(missing_meta)}")
        if metadata.get("procedure_status") not in PROCEDURE_STATUSES:
            results.fail("runbooks.status", f"{expected_id}: invalid procedure status.")
        if metadata.get("validation_status") not in VALIDATION_STATUSES:
            results.fail("runbooks.status", f"{expected_id}: invalid validation status.")
        if metadata.get("evidence_authority") not in EVIDENCE_AUTHORITIES:
            results.fail("runbooks.evidence-authority", f"{expected_id}: invalid evidence authority.")
        if metadata.get("phase") != "PHASE_1":
            results.fail("runbooks.metadata", f"{expected_id}: phase must be PHASE_1.")

        headings = re.findall(r"^## (.+?)\s*$", text, re.MULTILINE)
        if headings != REQUIRED_SECTIONS:
            missing = [item for item in REQUIRED_SECTIONS if item not in headings]
            duplicates = sorted({item for item in headings if headings.count(item) > 1})
            results.fail(
                "runbooks.sections",
                f"{expected_id}: required section order/count mismatch; missing={missing}, duplicates={duplicates}.",
            )

        entry = manifest_entries.get(expected_id)
        if not entry:
            results.fail("runbooks.manifest-sync", f"{expected_id}: missing manifest entry.")
        else:
            for key in REQUIRED_METADATA:
                if entry.get(key) != metadata.get(key):
                    results.fail("runbooks.manifest-sync", f"{expected_id}: metadata differs from manifest for {key}.")

        validation_status = metadata.get("validation_status")
        evidence_authority = metadata.get("evidence_authority")
        if validation_status == "NOT_VALIDATED" and evidence_authority != "NONE":
            results.fail("runbooks.status-coherence", f"{expected_id}: NOT_VALIDATED cannot claim execution evidence authority.")
        if validation_status in {"PARTIALLY_RUNTIME_VALIDATED", "VALIDATED_RUNTIME"} and metadata.get("runtime_required") is not True:
            results.fail("runbooks.status-coherence", f"{expected_id}: runtime validation requires runtime_required=true.")

        try:
            command_blocks = _json_blocks(text, "command-metadata")
        except (json.JSONDecodeError, ValueError) as exc:
            results.fail("runbooks.commands", f"{expected_id}: invalid command metadata: {exc}")
            command_blocks = []
        for block in command_blocks:
            _validate_command_block(expected_id, block, results)

        other_fences = re.findall(r"^```([^\n]*)\n", text, re.MULTILINE)
        if any(
            label.strip() and label.strip() not in {"json runbook-metadata", "json command-metadata"}
            for label in other_fences
        ):
            results.fail("runbooks.commands", f"{expected_id}: unclassified fenced block exists.")

    if len(actual_ids) != len(set(actual_ids)):
        results.fail("runbooks.ids", "Duplicate runbook IDs exist in authoritative Markdown metadata.")
    elif len(parsed) == 7:
        results.pass_("runbooks.ids", "Seven authoritative Markdown runbook IDs are unique.")

    if len(parsed) == 7 and not any(item.category in {"runbooks.metadata", "runbooks.sections"} and item.level == "FAIL" for item in results.findings):
        results.pass_("runbooks.structure", "All seven runbooks contain required metadata and 29 ordered sections.")


def _validate_command_block(runbook_id: str, block: dict[str, Any], results: Results) -> None:
    missing = sorted(COMMAND_FIELDS - block.keys())
    commands: list[str]
    if isinstance(block.get("command"), str):
        commands = [block["command"]]
    elif isinstance(block.get("commands"), list) and all(isinstance(item, str) for item in block["commands"]):
        commands = block["commands"]
    else:
        results.fail("runbooks.commands", f"{runbook_id}: command block needs command or commands.")
        return
    if missing:
        results.fail("runbooks.commands", f"{runbook_id}: command metadata missing {', '.join(missing)}.")
        return

    status = block.get("command_status")
    if status not in COMMAND_STATUSES:
        results.fail("runbooks.commands", f"{runbook_id}: invalid command status {status!r}.")
    if not isinstance(block.get("approval_required"), bool):
        results.fail("runbooks.commands", f"{runbook_id}: approval_required must be boolean.")

    mutating = re.compile(
        r"(?:\bSet-Content\b|\bNew-Item\b|\bRemove-Item\b|\bgit\s+(?:add|commit|push|reset|clean|checkout|restore|stash)\b|--write\b|-GenerateReports\b|collect-telemetry-live)",
        re.IGNORECASE,
    )
    live = re.compile(r"(?:^|\s)(?:ssh|kubectl)\s|live-validation|collect-telemetry-live", re.IGNORECASE)
    for command in commands:
        if mutating.search(command) and not (
            block.get("approval_required") is True
            and status in {"AVAILABLE_MUTATING_APPROVAL_REQUIRED", "PROHIBITED_IN_CURRENT_PHASE"}
        ):
            results.fail("runbooks.commands", f"{runbook_id}: mutating command lacks approval-gated classification.")
        if live.search(command) and status == "AVAILABLE_READ_ONLY":
            results.fail("runbooks.commands", f"{runbook_id}: live command is incorrectly classified as repository read-only.")
    if status in {"AVAILABLE_MUTATING_APPROVAL_REQUIRED", "LIVE_RUNTIME_REQUIRED"} and block.get("approval_required") is not True:
        results.fail("runbooks.commands", f"{runbook_id}: runtime or mutating command requires approval.")
    if status in {"PLANNED_NOT_IMPLEMENTED", "PROHIBITED_IN_CURRENT_PHASE"} and block.get("executable") is True:
        results.fail("runbooks.commands", f"{runbook_id}: planned or prohibited command is presented as executable.")


def _validate_semantics(root: Path, parsed: dict[str, tuple[Path, str, dict[str, Any]]], results: Results) -> None:
    all_text = "\n".join(item[1] for item in parsed.values())
    manifest_text = (root / MANIFEST_PATH).read_text(encoding="utf-8") if (root / MANIFEST_PATH).is_file() else ""
    scoped_text = all_text + "\n" + manifest_text

    requirements = {
        "RB-P1-001": ["READY_WITH_WARNINGS", "REVIEW_REQUIRED", "NOT_READY", "dirty tree", "Never use reset"],
        "RB-P1-002": ["ReadOnlyIsolated", "15 PASS", "5 WARN", "30 FAIL", "zero integration failures", "live S021"],
        "RB-P1-003": list(EVIDENCE_AUTHORITIES) + [".runtime/zero-trust/", "clouds.yaml", "kubeconfig"],
        "RB-P1-004": ["PERMANENT_ACL_ENFORCEMENT_EVIDENCE_MISSING", "PARTIAL_NO_INTERFACE_BINDING", "SEGMENTATION_CONFIGURATION_ONLY"],
        "RB-P1-005": ["CENTRAL_MONITORING_SERVICE_ABSENT", "PERSISTENT_STORAGE_EVIDENCE_MISSING", "PREPARATION_TRACES_ONLY"],
        "RB-P1-006": ["PRESENT", "IMPLEMENTED", "RUNTIME_VALIDATED", "VALIDATED", "ACCEPTED", "BOUNDED_NON_PRODUCTION_TARGET", "runtime acceptance"],
        "RB-P1-007": ["ZT-CV-001", "ZT-RV-001", "ABSENT", "ZT-SCH-001", "no scheduler"],
    }
    for runbook_id, tokens in requirements.items():
        text = parsed.get(runbook_id, (None, "", {}))[1]
        missing = [token for token in tokens if token.lower() not in text.lower()]
        if missing:
            results.fail("runbooks.semantics", f"{runbook_id}: missing required boundary text: {missing}")
    if not any(item.category == "runbooks.semantics" and item.level == "FAIL" for item in results.findings):
        results.pass_("runbooks.semantics", "Package-specific workflow and gap boundaries are explicit.")

    prohibited_claims = [
        (r"ZT-(?:NET|VIS)-001.{0,100}\b(?:fully|completely)\s+(?:validated|implemented)\b", "package overclaim"),
        (r"ZT-ID-001.{0,120}\b(?:FULL_PRODUCTION_VALIDATED|MFA_ENFORCED|OIDC_OPERATIONAL|RBAC_RUNTIME_ENFORCED)\b", "identity runtime overclaim"),
        (r"ZT-SCH-001\s+(?:is\s+)?(?:OPERATIONAL|IMPLEMENTED|VALIDATED)\b", "scheduler operational claim"),
        (r"ZT-VIS-002\s+(?:provides\s+runtime\s+evidence|is\s+(?:deployed|validated))", "protected visibility evidence claim"),
        (r"(?:current|achieved|implemented)[^\n]{0,60}\bADVANCED\b", "ADVANCED maturity claim"),
        (r"(?:current|achieved|implemented)[^\n]{0,60}\bOPTIMAL\b", "OPTIMAL maturity claim"),
        (r"(?:current|achieved|implemented)[^\n]{0,60}\bOPTIMAL_READY\b", "OPTIMAL_READY implementation claim"),
        (r"(?:actual|observed|execution|validation)\s+(?:result|status)\s*[:=]\s*PASS\b", "fictional PASS result"),
    ]
    for pattern, label in prohibited_claims:
        if re.search(pattern, scoped_text, re.IGNORECASE | re.DOTALL):
            results.fail("runbooks.claims", f"Detected {label}.")
    if not any(item.category == "runbooks.claims" and item.level == "FAIL" for item in results.findings):
        results.pass_("runbooks.claims", "No package, maturity, protected-work, or fictional execution overclaim was found.")

    secret_patterns = [
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"\bAKIA[0-9A-Z]{16}\b",
        r"\b(?:password|passwd|client_secret|api_key|access_token)\s*[:=]\s*[\"']?(?!<|NONE\b|EXTERNAL\b)[A-Za-z0-9_./+\-=]{8,}",
        r"C:\\Users\\",
        r"/home/[A-Za-z0-9_.-]+/",
    ]
    for pattern in secret_patterns:
        if re.search(pattern, scoped_text, re.IGNORECASE):
            results.fail("runbooks.sensitive-data", "Likely secret or local absolute path detected in authoritative runbook data.")
            break
    env_files = [path for path in root.rglob(".env") if ".git" not in path.parts]
    if env_files:
        results.fail("runbooks.sensitive-data", "A real .env file exists in the validation root.")
    if "S051" in scoped_text:
        results.fail("runbooks.scenario-lock", "S051 appears in the Phase 1 runbook baseline.")
    else:
        results.pass_("runbooks.scenario-lock", "No S051 reference appears in the Phase 1 baseline.")
    if not any(item.category == "runbooks.sensitive-data" and item.level == "FAIL" for item in results.findings):
        results.pass_("runbooks.sensitive-data", "No likely secret, .env file, or local absolute path was detected.")


def _validate_index_and_links(root: Path, manifest: dict[str, Any] | None, results: Results) -> None:
    index = _read(root / INDEX_PATH, results, "index.read") or ""
    readme = _read(root / README_PATH, results, "index.read") or ""
    entries = (manifest or {}).get("runbooks", [])
    missing = []
    for entry in entries if isinstance(entries, list) else []:
        runbook_id = entry.get("runbook_id")
        relative = entry.get("path", "")
        index_relative = relative.replace("docs/runbooks/", "")
        if runbook_id not in index or index_relative not in index:
            missing.append(str(runbook_id))
    index_ids = set(re.findall(r"RB-P1-\d{3}", index))
    if missing or index_ids != set(REQUIRED_RUNBOOKS):
        results.fail("index.sync", f"Runbook index mismatch; missing={missing}, ids={sorted(index_ids)}")
    else:
        results.pass_("index.sync", "Index and manifest contain the same seven Phase 1 runbooks.")
    if "secondary" not in readme.lower() or "not authoritative" not in readme.lower():
        results.fail("index.authority", "README must describe root runbooks/ as a non-authoritative secondary collection.")
    else:
        results.pass_("index.authority", "README preserves the operational authority hierarchy.")

    link_errors = []
    markdown_paths = [root / INDEX_PATH, root / README_PATH]
    markdown_paths.extend(root / relative for relative in REQUIRED_RUNBOOKS.values())
    for path in markdown_paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            clean = target.split("#", 1)[0]
            if not clean or re.match(r"^[a-z]+://", clean):
                continue
            if not (path.parent / clean).resolve().exists():
                link_errors.append(f"{path.relative_to(root).as_posix()} -> {target}")
    if link_errors:
        results.fail("runbooks.links", "; ".join(link_errors))
    else:
        results.pass_("runbooks.links", "All relative Markdown links resolve.")


def _validate_repository_state(root: Path, results: Results) -> None:
    if not (root / ".git").exists():
        results.pass_("repository.fixture", "No Git metadata in fixture; repository-only checks skipped.")
        return
    try:
        tracked_runtime = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--", ".runtime"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError) as exc:
        results.fail("repository.git", f"Unable to inspect tracked runtime: {exc}")
        return
    if tracked_runtime:
        results.fail("repository.runtime", "Tracked runtime paths exist.")
    else:
        results.pass_("repository.runtime", "No runtime file is tracked.")

    scenario_root = root / "scenarios"
    ids = {
        path.name[:4]
        for path in scenario_root.rglob("S???-*")
        if path.is_dir() and re.match(r"^S\d{3}-", path.name)
    }
    expected = {f"S{number:03d}" for number in range(1, 51)}
    if ids != expected:
        results.fail("repository.scenarios", "Scenario directories are not exactly S001-S050.")
    else:
        results.pass_("repository.scenarios", "Scenario directories remain exactly S001-S050.")


def validate(root: Path = ROOT, strict: bool = False) -> dict[str, Any]:
    root = root.resolve()
    results = Results()
    manifest = _validate_manifest(root, results)
    parsed = _runbook_texts(root, results)
    _validate_runbooks(root, manifest, parsed, results)
    _validate_semantics(root, parsed, results)
    _validate_index_and_links(root, manifest, results)
    _validate_repository_state(root, results)
    summary = results.summary()
    exit_status = 1 if summary["failed"] or (strict and summary["warnings"]) else 0
    return {
        "validator": "validate_phase1_runbook_baseline",
        "root": root.as_posix(),
        "strict": strict,
        "findings": [asdict(item) for item in results.findings],
        "summary": summary,
        "exit_status": exit_status,
    }


def _format_text(report: dict[str, Any], verbose: bool) -> str:
    lines = []
    for item in report["findings"]:
        if verbose or item["level"] != "PASS":
            lines.append(f"[{item['level']}] {item['category']}: {item['message']}")
    summary = report["summary"]
    lines.append(
        f"Summary: {summary['passed']} PASS / {summary['warnings']} WARN / {summary['failed']} FAIL"
    )
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="Show passing findings.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        report = validate(args.root, strict=args.strict)
    except Exception as exc:  # Configuration failure, distinct from content findings.
        if args.format == "json":
            print(json.dumps({"error": str(exc), "exit_status": 2}, indent=2))
        else:
            print(f"[ERROR] validator.configuration: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(_format_text(report, args.verbose))
    return int(report["exit_status"])


if __name__ == "__main__":
    raise SystemExit(main())
