# Evidence Model

Evidence proves that a scenario was executed and validated. It must be reproducible, reviewable, and mapped to validation criteria.

Screenshots alone are not enough. Every evidence item must be linked to a scenario and explain what it proves.

## Evidence Directory Rule

Each scenario must have a matching evidence directory using the same level and scenario directory name.

Example:

```text
scenarios/L1-foundation/S001-control-plane-toolchain-validation/
evidence/L1-foundation/S001-control-plane-toolchain-validation/
```

## Required Evidence Files

Every evidence directory must include:

- `commands.md`
- `validation.md`
- `logs/.gitkeep`
- `screenshots/.gitkeep`
- `configs/.gitkeep`

## Evidence File Purpose

`commands.md` records:

- commands executed
- execution timestamp
- target host or environment
- expected purpose of each command

`validation.md` records:

- validation criteria
- expected result
- actual result
- `PASS`, `FAIL`, `PARTIAL`, `BLOCKED`, or `NOT_RUN` status
- evidence reference

`logs/` stores applicable text logs, including:

- tool execution logs
- Terraform logs
- Ansible logs
- Kubernetes command output
- Prometheus or Grafana related logs where applicable

`screenshots/` stores applicable screenshots, including:

- console screenshots
- Grafana dashboard screenshots
- Prometheus target screenshots
- cloud resource screenshots where applicable

`configs/` stores sanitized configuration snapshots only. Do not include secrets, credentials, private keys, or account-specific sensitive data.

## Evidence Naming Rule

Use clear kebab-case filenames.

Examples:

- `terraform-plan-output.md`
- `ansible-playbook-result.md`
- `kubectl-get-pods.md`
- `prometheus-targets.md`
- `grafana-dashboard-screenshot.png`
- `db-replication-status.md`
- `security-policy-validation.md`

## Evidence Status Model

- `PASS`: validation criteria were met.
- `FAIL`: validation criteria were not met.
- `PARTIAL`: some criteria were met, but gaps remain.
- `BLOCKED`: validation could not proceed due to a dependency or access issue.
- `NOT_RUN`: validation has not been executed.

## Validation Table Template

Use this table in `validation.md`:

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|

## Evidence Quality Rule

Evidence must be:

- specific
- timestamped when possible
- sanitized
- scenario-mapped
- repeatable
- minimal but sufficient

## Prohibited Evidence

Do not commit:

- real credentials
- private keys
- cloud account IDs
- subscription IDs
- tenant IDs
- real public IPs unless intentionally sanitized
- Terraform state files
- kubeconfig files
- `.env` files
- binary archives
- unexplained screenshots

## Evidence Review Checklist

- [ ] Does the evidence map to a scenario?
- [ ] Does the evidence map to validation criteria?
- [ ] Is the result clearly `PASS` or `FAIL` when execution is complete?
- [ ] Are commands recorded?
- [ ] Are sensitive values removed?
- [ ] Are screenshots explained?
- [ ] Can another reviewer understand the result?
