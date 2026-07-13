# Prerequisites

The implemented validator requires only PowerShell and the repository files listed in the evidence manifest. No credential, provider CLI, kubeconfig, state, or live network access is required.

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S046 scenario and evidence directories exist.
- Provider, resource, ID, region, zone, environment, ownership, and cleanup values use placeholders only.
- S041, S042, S045, and S050 boundaries are understood.
- No real deletion output, Terraform destroy output, billing account ID, cloud account value, tfstate, kubeconfig, credential, secret, private key, subscription ID, tenant ID, public IP, or account-specific value is present.

## Related Scenario Boundaries

- S041 handles Terraform drift detection.
- S042 handles Terraform drift remediation.
- S045 handles cost guardrail validation.
- S050 handles final evidence report generation.
