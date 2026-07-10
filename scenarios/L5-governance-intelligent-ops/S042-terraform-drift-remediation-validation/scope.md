# Scope

## Included

- Drift detection result review plan.
- Terraform remediation decision point documentation.
- Terraform plan review before remediation.
- Terraform apply placeholder validation plan.
- AWS Security Group drift remediation placeholder.
- Azure NSG drift remediation placeholder.
- OpenStack Security Group drift remediation placeholder.
- Security rule drift remediation reference.
- Tag or label drift remediation placeholder.
- Post-remediation Terraform plan validation plan.
- Remediation evidence collection plan.

## Target Remediation Categories

- AWS Security Group rule drift.
- Azure NSG rule drift.
- OpenStack Security Group rule drift.
- Compute instance metadata or tag drift.
- Network route or subnet drift placeholder.
- Terraform-managed resource configuration drift.

## Remediation Decision Model

- `REMEDIATION_READY`: Drift is understood and Terraform remediation is safe to proceed.
- `REMEDIATION_APPLIED`: Terraform remediation action is executed or documented as placeholder.
- `REMEDIATION_BLOCKED`: Drift requires manual investigation or is unsafe to remediate.
- `REMEDIATION_FAILED`: Drift remains after remediation attempt.
- `OUT_OF_SCOPE`: Drift belongs to Kubernetes manifest, cost, security incident, or policy validation scenarios.

## Excluded

- Real Terraform module implementation.
- Real Terraform execution against AWS, Azure, OpenStack, or any cloud account.
- Real backend bucket names, tfstate, credentials, secrets, private keys, kubeconfig, subscription IDs, tenant IDs, account IDs, public IPs, or account-specific values.
- Automated remediation claims.
- Terraform Cloud, Spacelift, Atlantis, GitOps, or other new tool integrations.
- Policy as Code validation, handled in S043.
- Kubernetes manifest policy validation, handled in S044.
- Security misconfiguration response, handled in S037.
- Cost guardrail validation, handled in S045.
