# Failure Condition

S046 fails or is blocked if any of the following occur:

- Cleanup input artifact is missing.
- Resource ownership is missing.
- Resource usage evidence is missing.
- Environment tag or label is missing.
- Dependency impact is undocumented.
- Cleanup decision is unsafe, ambiguous, or undocumented.
- Cleanup command or runbook placeholder is missing.
- Post-cleanup inventory check is missing.
- Rollback or recreation note is missing where applicable.
- Evidence is missing or cannot be mapped to validation checks.
- Real resource deletion, Terraform destroy, cloud delete, Kubernetes delete, or cleanup execution occurs unintentionally.
- The scenario claims automated cleanup, automated Terraform destroy, production-grade lifecycle management, FinOps automation, or new tooling.
- Real credentials, secrets, access keys, private keys, kubeconfig content, billing account IDs, subscription IDs, tenant IDs, account IDs, public IPs, tfstate, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the cleanup result as `CLEANUP_BLOCKED` or `CLEANUP_INCONCLUSIVE` as appropriate.
