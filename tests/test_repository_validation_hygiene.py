import subprocess
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
POWERSHELL_TEST_ROOT = REPOSITORY_ROOT / "tests" / "powershell"


def run_powershell_test(name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(POWERSHELL_TEST_ROOT / name),
        ],
        cwd=REPOSITORY_ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


class RepositoryValidationHygieneTests(unittest.TestCase):
    def test_s021_strict_mode_fixture_regressions(self) -> None:
        result = run_powershell_test("test-s021-node-status-parser.ps1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("passed=9 failed=0", result.stdout)

    def test_repository_state_guard_regressions(self) -> None:
        result = run_powershell_test("test-repository-validation-safety.ps1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("passed=8 failed=0", result.stdout)

    def test_validate_all_defaults_to_isolated_read_only_mode(self) -> None:
        source = (REPOSITORY_ROOT / "tools" / "validate-all-scenarios.ps1").read_text(encoding="utf-8")
        self.assertIn("[switch] $GenerateReports", source)
        self.assertIn('validationMode = "ReadOnlyIsolated"', source)
        self.assertIn("Report generation: SKIPPED (read-only isolated mode).", source)
        self.assertIn("Scenario results: PASS=", source)
        self.assertIn("Get-RepositoryStateSnapshot", source)
        self.assertIn("Compare-RepositoryStateSnapshot", source)
        self.assertIn('"validate-zero-trust.ps1"', source)
        self.assertLess(source.index("if ($GenerateReports) {", source.index("$validatorPassCount")), source.index("Set-Content -LiteralPath $logPath"))

    def test_s021_uses_normalized_parser_without_weakening_strict_mode(self) -> None:
        source = (REPOSITORY_ROOT / "tools" / "validate-kubernetes-node-readiness.ps1").read_text(encoding="utf-8")
        self.assertIn("Set-StrictMode -Version Latest", source)
        self.assertIn("NodeReadinessParser.psm1", source)
        self.assertIn("ConvertFrom-NodeStatusEvidence", source)
        self.assertNotIn("function Get-NodeStatusEvidence", source)


if __name__ == "__main__":
    unittest.main()
