"""Regression tests for the Phase 1 runbook baseline validator."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "tools" / "validate_phase1_runbook_baseline.py"
SPEC = importlib.util.spec_from_file_location("phase1_runbook_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class Phase1RunbookBaselineTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temp = tempfile.TemporaryDirectory()
        self.root = Path(self._temp.name)
        shutil.copytree(REPO_ROOT / "docs" / "runbooks", self.root / "docs" / "runbooks")
        (self.root / "runbooks").mkdir()

    def tearDown(self) -> None:
        self._temp.cleanup()

    def _path(self, runbook_id: str) -> Path:
        return self.root / VALIDATOR.REQUIRED_RUNBOOKS[runbook_id]

    def _manifest(self) -> dict:
        return json.loads((self.root / VALIDATOR.MANIFEST_PATH).read_text(encoding="utf-8"))

    def _write_manifest(self, manifest: dict) -> None:
        (self.root / VALIDATOR.MANIFEST_PATH).write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    def _metadata(self, runbook_id: str) -> dict:
        text = self._path(runbook_id).read_text(encoding="utf-8")
        match = re.search(r"```json runbook-metadata\s*\n(.*?)\n```", text, re.DOTALL)
        assert match
        return json.loads(match.group(1))

    def _write_metadata(self, runbook_id: str, metadata: dict) -> None:
        path = self._path(runbook_id)
        text = path.read_text(encoding="utf-8")
        replacement = "```json runbook-metadata\n" + json.dumps(metadata, indent=2) + "\n```"
        text = re.sub(
            r"```json runbook-metadata\s*\n.*?\n```",
            lambda _: replacement,
            text,
            count=1,
            flags=re.DOTALL,
        )
        path.write_text(text, encoding="utf-8")

    def _sync_manifest_metadata(self, runbook_id: str, metadata: dict) -> None:
        manifest = self._manifest()
        entry = next(item for item in manifest["runbooks"] if item["runbook_id"] == runbook_id)
        for key in VALIDATOR.REQUIRED_METADATA:
            entry[key] = metadata[key]
        self._write_manifest(manifest)

    def _append(self, runbook_id: str, value: str) -> None:
        path = self._path(runbook_id)
        path.write_text(path.read_text(encoding="utf-8") + "\n" + value + "\n", encoding="utf-8")

    def _remove_section(self, runbook_id: str, section: str) -> None:
        path = self._path(runbook_id)
        text = path.read_text(encoding="utf-8")
        text = text.replace(f"## {section}\n", f"### Removed {section}\n", 1)
        path.write_text(text, encoding="utf-8")

    def _report(self) -> dict:
        return VALIDATOR.validate(self.root)

    def _assert_failure(self, category: str) -> None:
        report = self._report()
        self.assertEqual(1, report["exit_status"], report)
        self.assertTrue(
            any(item["level"] == "FAIL" and item["category"] == category for item in report["findings"]),
            report,
        )

    @staticmethod
    def _command_block(command: str, status: str, approval: bool, executable: bool | None = None) -> str:
        value = {
            "command": command,
            "command_status": status,
            "execution_owner": "CODEX_OR_AUTOMATION",
            "approval_required": approval,
            "runtime_target": "TEST_FIXTURE",
            "expected_effect": "Controlled negative fixture.",
            "evidence_output": "None.",
            "rollback_reference": "Fixture cleanup.",
        }
        if executable is not None:
            value["executable"] = executable
        return "```json command-metadata\n" + json.dumps(value, indent=2) + "\n```"

    def test_missing_required_runbook(self) -> None:
        self._path("RB-P1-007").unlink()
        self._assert_failure("runbooks.required")

    def test_duplicate_runbook_id(self) -> None:
        metadata = self._metadata("RB-P1-007")
        metadata["runbook_id"] = "RB-P1-006"
        self._write_metadata("RB-P1-007", metadata)
        self._assert_failure("runbooks.ids")

    def test_missing_purpose(self) -> None:
        self._remove_section("RB-P1-001", "Purpose")
        self._assert_failure("runbooks.sections")

    def test_missing_stop_conditions(self) -> None:
        self._remove_section("RB-P1-001", "Stop Conditions")
        self._assert_failure("runbooks.sections")

    def test_missing_failure_handling(self) -> None:
        self._remove_section("RB-P1-001", "Failure Handling")
        self._assert_failure("runbooks.sections")

    def test_missing_rollback(self) -> None:
        self._remove_section("RB-P1-001", "Rollback")
        self._assert_failure("runbooks.sections")

    def test_missing_evidence(self) -> None:
        self._remove_section("RB-P1-001", "Evidence")
        self._assert_failure("runbooks.sections")

    def test_invalid_procedure_status(self) -> None:
        runbook_id = "RB-P1-001"
        metadata = self._metadata(runbook_id)
        metadata["procedure_status"] = "OPERATIONAL"
        self._write_metadata(runbook_id, metadata)
        self._sync_manifest_metadata(runbook_id, metadata)
        self._assert_failure("runbooks.status")

    def test_invalid_validation_status(self) -> None:
        runbook_id = "RB-P1-001"
        metadata = self._metadata(runbook_id)
        metadata["validation_status"] = "COMPLETE"
        self._write_metadata(runbook_id, metadata)
        self._sync_manifest_metadata(runbook_id, metadata)
        self._assert_failure("runbooks.status")

    def test_runtime_claim_with_not_validated_status(self) -> None:
        runbook_id = "RB-P1-004"
        metadata = self._metadata(runbook_id)
        metadata["validation_status"] = "NOT_VALIDATED"
        self._write_metadata(runbook_id, metadata)
        self._sync_manifest_metadata(runbook_id, metadata)
        self._assert_failure("runbooks.status-coherence")

    def test_package_overclaim(self) -> None:
        self._append("RB-P1-004", "ZT-NET-001 is fully validated.")
        self._assert_failure("runbooks.claims")

    def test_identity_implemented_claim(self) -> None:
        self._append("RB-P1-006", "ZT-ID-001 is IMPLEMENTED.")
        self._assert_failure("runbooks.claims")

    def test_scheduler_operational_claim(self) -> None:
        self._append("RB-P1-007", "ZT-SCH-001 is OPERATIONAL.")
        self._assert_failure("runbooks.claims")

    def test_visibility_two_evidence_claim(self) -> None:
        self._append("RB-P1-005", "ZT-VIS-002 provides runtime evidence.")
        self._assert_failure("runbooks.claims")

    def test_mutating_command_without_approval(self) -> None:
        self._append(
            "RB-P1-002",
            self._command_block("Set-Content result.txt changed", "AVAILABLE_READ_ONLY", False),
        )
        self._assert_failure("runbooks.commands")

    def test_live_command_classified_read_only(self) -> None:
        self._append(
            "RB-P1-004",
            self._command_block("ssh fixed-validator validate", "AVAILABLE_READ_ONLY", False),
        )
        self._assert_failure("runbooks.commands")

    def test_planned_command_presented_as_executable(self) -> None:
        self._append(
            "RB-P1-007",
            self._command_block("future-validator run", "PLANNED_NOT_IMPLEMENTED", True, True),
        )
        self._assert_failure("runbooks.commands")

    def test_fictional_pass_result(self) -> None:
        self._append("RB-P1-006", "Execution result: PASS")
        self._assert_failure("runbooks.claims")

    def test_advanced_maturity_claim(self) -> None:
        self._append("RB-P1-006", "Current maturity: ADVANCED")
        self._assert_failure("runbooks.claims")

    def test_optimal_maturity_claim(self) -> None:
        self._append("RB-P1-006", "Current maturity: OPTIMAL")
        self._assert_failure("runbooks.claims")

    def test_optimal_ready_implementation_claim(self) -> None:
        self._append("RB-P1-006", "Current implementation is OPTIMAL_READY")
        self._assert_failure("runbooks.claims")

    def test_secret_pattern(self) -> None:
        secret_fixture = "api_" + "key" + " = " + '"' + "realisticSecretValue123" + '"'
        self._append("RB-P1-003", secret_fixture)
        self._assert_failure("runbooks.sensitive-data")

    def test_real_env_file(self) -> None:
        (self.root / ".env").write_text("fixture=true\n", encoding="utf-8")
        self._assert_failure("runbooks.sensitive-data")

    def test_s051_reference(self) -> None:
        self._append("RB-P1-007", "Future scenario: S051")
        self._assert_failure("runbooks.scenario-lock")

    def test_missing_manifest_entry(self) -> None:
        manifest = self._manifest()
        manifest["runbooks"] = manifest["runbooks"][:-1]
        self._write_manifest(manifest)
        self._assert_failure("manifest.runbooks")

    def test_index_mismatch(self) -> None:
        path = self.root / VALIDATOR.INDEX_PATH
        text = path.read_text(encoding="utf-8")
        text = "\n".join(line for line in text.splitlines() if "RB-P1-007" not in line) + "\n"
        path.write_text(text, encoding="utf-8")
        self._assert_failure("index.sync")

    def test_legacy_reference_marked_authoritative(self) -> None:
        manifest = self._manifest()
        manifest["legacy_references"][0]["authoritative"] = True
        manifest["legacy_references"][0]["authority_status"] = "AUTHORITATIVE"
        self._write_manifest(manifest)
        self._assert_failure("manifest.legacy")

    def test_validator_does_not_mutate_fixture(self) -> None:
        def snapshot() -> dict[str, str]:
            return {
                path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(item for item in self.root.rglob("*") if item.is_file())
            }

        before = snapshot()
        report = self._report()
        after = snapshot()
        self.assertEqual(0, report["exit_status"], report)
        self.assertEqual(before, after)

    def test_valid_baseline(self) -> None:
        report = self._report()
        self.assertEqual(0, report["exit_status"], report)
        self.assertEqual(0, report["summary"]["failed"])
        self.assertEqual(0, report["summary"]["warnings"])


if __name__ == "__main__":
    unittest.main()
