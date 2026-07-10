# Expected Result

- Terraform working directory, backend placeholder, and provider placeholder checks are planned.
- Plan-based drift detection model is documented.
- AWS, Azure, OpenStack, security rule, tag/label, and manual change drift placeholders are mapped.
- Drift judgment states are documented as `NO_DRIFT`, `DRIFT_DETECTED`, `INCONCLUSIVE`, and `OUT_OF_SCOPE`.
- Drift detection is separated from remediation, Policy as Code, Kubernetes manifest policy, security misconfiguration response, and cost governance.
- Automated remediation, Terraform Cloud, Atlantis, Spacelift, and GitOps integration claims are explicitly excluded.
- All validation checks map to `commands.md`, `validation.md`, or required future artifacts under `configs/`, `logs/`, and `screenshots/`.
- No credentials, secrets, cloud account values, public IPs, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, or account-specific values are added.
