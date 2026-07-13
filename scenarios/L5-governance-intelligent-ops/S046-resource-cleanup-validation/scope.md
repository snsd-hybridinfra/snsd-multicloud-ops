# Scope

Implemented scope is limited to sanitized local sample evidence, policy/rule review, and manifest mapping. Resource discovery, deletion, `terraform destroy`, cloud CLI/API access, and Kubernetes deletion remain excluded.

## Included

- Cleanup candidate identification plan.
- Terraform-managed resource cleanup placeholder.
- AWS resource cleanup placeholder.
- Azure resource cleanup placeholder.
- OpenStack resource cleanup placeholder.
- Kubernetes resource cleanup placeholder.
- Unused public IP cleanup placeholder.
- Unattached volume cleanup placeholder.
- Temporary test resource cleanup placeholder.
- Cleanup approval decision point documentation.
- Post-cleanup inventory validation plan.
- Cleanup evidence collection plan.

## Target Cleanup Categories

- Unused compute instance placeholder.
- Temporary test instance placeholder.
- Unattached volume placeholder.
- Unused public IP placeholder.
- Unused security group or NSG rule placeholder.
- Unused Kubernetes namespace placeholder.
- Unused Kubernetes workload placeholder.
- Unused Nginx reverse proxy config placeholder.
- Stale monitoring target placeholder.
- Temporary evidence artifact placeholder.

## Required Cleanup Checks

- Resource ownership is identified.
- Environment tag or label is present.
- Resource usage state is reviewed.
- Dependency impact is reviewed.
- Cleanup candidate is documented.
- Cleanup approval decision is documented.
- Cleanup command or runbook placeholder is documented.
- Post-cleanup inventory check is documented.
- Cleanup evidence is recorded.
- Rollback or recreation note is documented where applicable.

## Cleanup Judgment Model

- `CLEANUP_NOT_REQUIRED`: Resource is valid and should remain.
- `CLEANUP_CANDIDATE`: Resource appears unused and requires review.
- `CLEANUP_APPROVED`: Resource is approved for cleanup.
- `CLEANUP_COMPLETED`: Cleanup action is executed or documented as placeholder.
- `CLEANUP_BLOCKED`: Cleanup is unsafe or requires further investigation.
- `CLEANUP_INCONCLUSIVE`: Required ownership or usage evidence is missing.

## Excluded

- Real resource deletion.
- Real Terraform destroy against cloud accounts.
- Automated cleanup.
- Automated Terraform destroy.
- Production-grade lifecycle management.
- FinOps automation.
- New tools or technologies.
- Real account IDs, billing account IDs, subscription IDs, tenant IDs, access keys, secrets, private keys, tfstate, kubeconfig, public IPs, or account-specific values.
- Cost guardrail validation, handled in S045.
- Terraform drift detection, handled in S041.
- Terraform drift remediation, handled in S042.
- Final evidence report generation, handled in S050.
