# Validation

Scenario: S010-evidence-directory-structure-validation
Level: L1-foundation
Capability: Evidence Directory Structure Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real validation command output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Scenario directory count validation plan | 50 scenario directories are present. | TODO | NOT_RUN | `commands.md`; `logs/evidence-structure-validation.log` |
| V002 | Evidence directory count validation plan | 50 evidence directories are present. | TODO | NOT_RUN | `commands.md`; `logs/evidence-structure-validation.log` |
| V003 | Scenario-to-evidence path matching validation plan | Every scenario has a matching evidence directory. | TODO | NOT_RUN | `configs/scenario-evidence-mapping-summary.md` |
| V004 | Required evidence file validation plan | Required evidence files exist for every scenario. | TODO | NOT_RUN | `configs/evidence-structure-summary.md` |
| V005 | Required evidence subdirectory validation plan | Required evidence subdirectories and placeholders exist. | TODO | NOT_RUN | `configs/evidence-structure-summary.md` |
| V006 | Evidence filename convention validation plan | Evidence filenames use clear kebab-case names where applicable. | TODO | NOT_RUN | `configs/evidence-structure-summary.md` |
| V007 | Sensitive file exclusion validation plan | Credentials, private keys, public IPs, tfstate, kubeconfig, and account-specific files are absent. | TODO | NOT_RUN | `commands.md`; `logs/evidence-structure-validation.log` |
| V008 | Evidence status matrix consistency validation plan | All 50 scenarios are represented with valid evidence status values. | TODO | NOT_RUN | `configs/scenario-evidence-mapping-summary.md` |
| V009 | Repository validation script execution plan | Repository structure validation returns pass status. | TODO | NOT_RUN | `commands.md`; `logs/evidence-structure-validation.log` |
| V010 | Missing evidence directory, missing required file, inconsistent path, or sensitive file exposure failure condition | Structural or sensitive-file failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Evidence structure summary is captured: NOT_READY
- Scenario/evidence mapping summary is captured: NOT_READY
- Evidence structure validation log is captured: NOT_READY
- Evidence directory tree screenshot is captured: NOT_READY

## Notes

This scenario validates evidence structure and policy only. It does not collect live system evidence or implement infrastructure logic.
