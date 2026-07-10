# Scope

## Included

- Terraform working directory validation plan.
- Terraform backend placeholder validation plan.
- Terraform provider placeholder validation plan.
- Terraform plan-based drift detection model.
- AWS resource drift placeholder.
- Azure resource drift placeholder.
- OpenStack resource drift placeholder.
- Security rule drift placeholder.
- Tag or label drift placeholder.
- Manual change detection placeholder.
- Drift evidence collection plan.

## Target Drift Categories

- AWS Security Group rule drift.
- Azure NSG rule drift.
- OpenStack Security Group rule drift.
- Compute instance metadata/tag drift.
- Network route or subnet drift placeholder.

Kubernetes manifest drift is excluded from this scenario and handled separately in S044.

## Drift Detection Model

- `NO_DRIFT`: Terraform desired state matches observed infrastructure state.
- `DRIFT_DETECTED`: Terraform plan identifies unmanaged or changed resource state.
- `INCONCLUSIVE`: required plan output or baseline evidence is missing.
- `OUT_OF_SCOPE`: drift belongs to Kubernetes manifest, cost, or policy validation scenarios.

## Important Boundary

- Do not claim automated remediation.
- Do not claim production-grade IaC governance.
- Do not claim Terraform Cloud, Spacelift, Atlantis, or GitOps integration.
- Do not introduce new tools.
- This scenario detects drift through controlled Terraform plan output and evidence review only.

## Excluded

- Real Terraform modules or provider implementation.
- Real Terraform execution against cloud accounts.
- Real backend bucket names, access keys, secrets, credentials, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Terraform drift remediation, which is handled in S042.
- Policy as Code validation, which is handled in S043.
- Kubernetes manifest policy validation, which is handled in S044.
- Security rule misconfiguration response, which is handled in S037.
- Cost Guardrail validation, which is handled in S045.
- Terraform Cloud, Spacelift, Atlantis, GitOps, or automated remediation claims.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
