# Failure Condition

## Failure Conditions

- Scenario directory count is not 50.
- Evidence directory count is not 50.
- A scenario does not have a matching evidence directory.
- An evidence directory is missing `commands.md` or `validation.md`.
- An evidence directory is missing `logs/.gitkeep`, `screenshots/.gitkeep`, or `configs/.gitkeep`.
- Evidence status matrix is missing a scenario or contains an invalid status.
- Evidence includes real credentials, private keys, public IPs, tfstate, kubeconfig files, or account-specific values.
- Repository validation script fails.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `configs/evidence-structure-summary.md`, `configs/scenario-evidence-mapping-summary.md`, or `logs/evidence-structure-validation.log`.

## Follow-Up Requirement

Create a follow-up task to repair evidence structure, update tracking matrices, remove sensitive files, or correct repository validation script findings.
