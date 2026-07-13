# Scope

## Included

- Counts and ID coverage for 50 scenario and 50 evidence directories.
- One-to-one relative-path mirroring.
- Required `commands.md` and `validation.md` files.
- Required `logs/`, `screenshots/`, and `configs/` directories.
- Sensitive and account-specific evidence filename checks.
- Evidence status matrix coverage, uniqueness, and readiness-value checks.
- Generated S010 log and summary.

## Excluded

- Technical success, correctness, or completeness of scenario-specific implementations.
- Execution of scenario commands, infrastructure, cloud APIs, Ansible, Kubernetes, or Terraform.
- Secret processing, sanitization, recovery, or archival.
- Final evidence aggregation and reporting, which belongs to S050.
- Repository-wide scenario content QA, which belongs to `tools/validate-scenario-quality.ps1`.

## Assumptions

- Evidence Readiness Status describes artifact readiness, not validation results.
- Existing placeholder files and empty canonical subdirectories are valid before scenario execution.
