# Failure Condition

This scenario is considered failed or blocked if:

- Terraform baseline or expected state is missing.
- Terraform plan output is missing.
- Manual change is not detected when expected.
- Drift result is ambiguous or cannot be classified.
- Required provider or backend placeholder evidence is missing.
- Real credentials, secrets, cloud account values, subscription IDs, tenant IDs, private keys, kubeconfig, or account-specific values are introduced.
- Generated `tfstate` or Terraform state-like output is committed to the repository.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Documentation claims automated remediation, production-grade IaC governance, Terraform Cloud, Spacelift, Atlantis, or GitOps integration.
