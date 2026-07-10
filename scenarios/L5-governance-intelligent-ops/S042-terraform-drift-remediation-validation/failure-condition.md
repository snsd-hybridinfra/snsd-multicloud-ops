# Failure Condition

S042 fails or is blocked if any of the following occur:

- Prior drift detection evidence is missing.
- Remediation proceeds without reviewed Terraform plan evidence.
- Remediation decision is unsafe, ambiguous, or undocumented.
- Terraform apply is claimed without approved and sanitized evidence.
- Drift remains after remediation and is not classified.
- Generated tfstate or backend metadata is committed to the repository.
- Real credentials, secrets, access keys, private keys, kubeconfig content, subscription IDs, tenant IDs, account IDs, backend bucket names, public IPs, or account-specific values are present.
- Evidence is missing or cannot be mapped to validation checks.
- The scenario claims automated remediation, production-grade IaC governance, Terraform Cloud, Spacelift, Atlantis, GitOps, or any unapproved tool integration.

If a failure is found, stop the scenario, preserve sanitized notes, and mark the result as `REMEDIATION_BLOCKED` or `REMEDIATION_FAILED`.
