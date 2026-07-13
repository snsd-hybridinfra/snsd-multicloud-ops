# Prerequisites

PowerShell and repository samples are sufficient; OPA, Conftest, Terraform, cloud credentials/state, and network access are not required.

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S043 scenario and evidence directories exist.
- Policy names, resources, CIDRs, tags, regions, and results use placeholders only.
- The repository naming rules are available for naming convention review.
- Security rule scenarios S014, S015, and S016 exist as policy input references.
- Cost guardrail validation is understood as a reference only and remains in S045.
- No real policy engine output, Terraform output, cloud account value, tfstate, kubeconfig, credential, secret, private key, subscription ID, tenant ID, or account-specific value is present.

## Related Scenario Boundaries

- S041 handles Terraform drift detection.
- S042 handles Terraform drift remediation.
- S044 handles Kubernetes manifest policy validation.
- S045 handles cost guardrail validation.
- S037 handles security rule misconfiguration response.
