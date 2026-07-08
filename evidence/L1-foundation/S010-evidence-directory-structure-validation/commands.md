# Commands

Scenario: S010-evidence-directory-structure-validation
Level: L1-foundation
Capability: Evidence Directory Structure Validation
Target: `<repository-root>`
Execution timestamp: TODO

Record sanitized output only. Do not include real public IPs, credentials, private keys, tfstate, kubeconfig content, account IDs, subscription IDs, tenant IDs, project IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Scenario directory count validation plan | Count `S###-*` directories under `scenarios/`. | Confirm 50 scenario directories exist. | TODO: record sanitized output after approved execution. |
| V002 | Evidence directory count validation plan | Count `S###-*` directories under `evidence/`. | Confirm 50 evidence directories exist. | TODO: record sanitized output after approved execution. |
| V003 | Scenario-to-evidence path matching validation plan | Compare `scenarios/<level>/<scenario>/` to `evidence/<level>/<scenario>/`. | Confirm every scenario has matching evidence path. | TODO: record sanitized output after approved execution. |
| V004 | Required evidence file validation plan | Check each evidence directory for `commands.md` and `validation.md`. | Confirm required evidence files exist. | TODO: record sanitized output after approved execution. |
| V005 | Required evidence subdirectory validation plan | Check each evidence directory for `logs/.gitkeep`, `screenshots/.gitkeep`, and `configs/.gitkeep`. | Confirm required subdirectories and placeholders exist. | TODO: record sanitized output after approved execution. |
| V006 | Evidence filename convention validation plan | Review evidence artifact names for kebab-case where applicable. | Confirm evidence naming is consistent. | TODO: record sanitized result after review. |
| V007 | Sensitive file exclusion validation plan | Review evidence paths for secrets, keys, tfstate, kubeconfig, and account-specific files. | Confirm sensitive files are absent. | TODO: record sanitized result after review. |
| V008 | Evidence status matrix consistency validation plan | Compare evidence directories to `docs/evidence-status-matrix.md`. | Confirm all 50 scenarios are represented with valid statuses. | TODO: record sanitized result after review. |
| V009 | Repository validation script execution plan | `powershell -ExecutionPolicy Bypass -File tools/validate-repo-structure.ps1` | Confirm repository structure validation passes. | TODO: record sanitized output after approved execution. |
| V010 | Missing evidence directory, missing required file, inconsistent path, or sensitive file exposure failure condition | Review failed structure validation findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/evidence-structure-summary.md`
- `configs/scenario-evidence-mapping-summary.md`
- `logs/evidence-structure-validation.log`
- `screenshots/evidence-directory-tree.png`
