#!/usr/bin/env python3
"""Read-only Terraform lock, module, runner and plan-gate validator."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "applications/internal-iaas-portal"
RUNNER_ROOT = APP / "services/terraform-runner"
sys.path.insert(0, str(RUNNER_ROOT))

from terraform_runner.executor import ALLOWED_MODULES, module_content_digest  # noqa: E402
from terraform_runner.supply_chain import SupplyChainError, load_supply_chain, validate_module_source  # noqa: E402


LOCK = APP / "terraform/supply-chain-lock.json"
CATALOG = APP / "terraform/catalog.json"
AUTHORITY = ROOT / "docs/platform/terraform-supply-chain.yaml"
DECISION = ROOT / "docs/adr/0022-managed-terraform-supply-chain.md"
EXECUTOR = RUNNER_ROOT / "terraform_runner/executor.py"
POLICY_MODULE = RUNNER_ROOT / "terraform_runner/supply_chain.py"
POLICY_TEST = APP / "tests/security/test_terraform_supply_chain.py"


def validate(root: Path = ROOT) -> list[str]:
    failures: list[str] = []
    paths = (AUTHORITY, DECISION, LOCK, CATALOG, EXECUTOR, POLICY_MODULE, POLICY_TEST)
    for source in paths:
        relative = source.relative_to(ROOT)
        if not (root / relative).is_file():
            failures.append(f"required Terraform supply-chain file missing: {relative}")
    if failures:
        return failures
    try:
        authority = json.loads((root / AUTHORITY.relative_to(ROOT)).read_text(encoding="utf-8"))
        status = authority.get("status", {})
        if status.get("runtime") != "NOT_VALIDATED":
            failures.append("Terraform runtime status was promoted without evidence")
        if authority.get("customization", {}).get("terraform_core_forked") is not False:
            failures.append("Terraform core must remain upstream and unforked")
        lock = load_supply_chain(root / LOCK.relative_to(ROOT), root / CATALOG.relative_to(ROOT))
        if set(lock["modules"]) != set(ALLOWED_MODULES):
            failures.append("runner allow-list differs from supply-chain lock")
        for module_name, policy in lock["modules"].items():
            validate_module_source(
                root / APP.relative_to(ROOT) / "terraform/modules" / module_name,
                module_name,
                policy,
                module_content_digest,
            )
    except (OSError, json.JSONDecodeError, SupplyChainError) as exc:
        failures.append(f"Terraform supply-chain authority failed: {exc}")

    executor = (root / EXECUTOR.relative_to(ROOT)).read_text(encoding="utf-8")
    module_text = (root / POLICY_MODULE.relative_to(ROOT)).read_text(encoding="utf-8")
    combined = executor + module_text
    for token in (
        "TF_CLI_CONFIG_FILE",
        "FILESYSTEM_MIRROR_ONLY",
        '"show", "-json", "tfplan"',
        'plan_command.append("-destroy")',
        "validate_plan_json",
        "sanitized_attestation",
    ):
        if token not in combined:
            failures.append(f"Terraform runner gate missing: {token}")
    if '"destroy", "-input=false"' in executor:
        failures.append("uninspected direct terraform destroy remains in the runner")
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    parser.parse_args(argv)
    failures = validate()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: Terraform catalog/module/tool/provider/plan supply-chain gates are locally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
