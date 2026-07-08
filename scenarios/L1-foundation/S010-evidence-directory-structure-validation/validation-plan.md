# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Scenario directory count validation plan | Count `S###-*` directories under `scenarios/`. | 50 scenario directories are present. | `commands.md`, `logs/evidence-structure-validation.log`, `validation.md` |
| V002 | Evidence directory count validation plan | Count `S###-*` directories under `evidence/`. | 50 evidence directories are present. | `commands.md`, `logs/evidence-structure-validation.log`, `validation.md` |
| V003 | Scenario-to-evidence path matching validation plan | Compare scenario paths to matching evidence paths. | Every scenario has a matching evidence directory. | `configs/scenario-evidence-mapping-summary.md`, `validation.md` |
| V004 | Required evidence file validation plan | Check `commands.md` and `validation.md` in each evidence directory. | Required evidence files exist for every scenario. | `configs/evidence-structure-summary.md`, `validation.md` |
| V005 | Required evidence subdirectory validation plan | Check `logs/.gitkeep`, `screenshots/.gitkeep`, and `configs/.gitkeep`. | Required evidence subdirectories and placeholders exist. | `configs/evidence-structure-summary.md`, `validation.md` |
| V006 | Evidence filename convention validation plan | Review evidence artifact naming convention. | Evidence filenames use clear kebab-case names where applicable. | `configs/evidence-structure-summary.md`, `validation.md` |
| V007 | Sensitive file exclusion validation plan | Review evidence paths for prohibited file types or sensitive names. | Credentials, private keys, public IPs, tfstate, kubeconfig, and account-specific files are absent. | `commands.md`, `logs/evidence-structure-validation.log`, `validation.md` |
| V008 | Evidence status matrix consistency validation plan | Compare evidence directories to `docs/evidence-status-matrix.md`. | All 50 scenarios are represented with valid evidence status values. | `configs/scenario-evidence-mapping-summary.md`, `validation.md` |
| V009 | Repository validation script execution plan | Run `tools/validate-repo-structure.ps1`. | Repository structure validation returns pass status. | `commands.md`, `logs/evidence-structure-validation.log`, `validation.md` |
| V010 | Missing evidence directory, missing required file, inconsistent path, or sensitive file exposure failure condition | Define explicit failure criteria. | Structural or sensitive-file failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. S010 validates structure and policy only; it does not collect live system evidence.
