# Prerequisites

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S041 drift detection evidence model exists and can be referenced.
- The S042 scenario and evidence directories exist.
- Terraform command examples are treated as planned placeholders only.
- Placeholder resource identifiers are used for all AWS, Azure, and OpenStack examples.
- No real provider credentials, backend configuration, tfstate, subscription IDs, tenant IDs, account IDs, private keys, kubeconfig files, or account-specific values are present.

## Related Scenario Boundaries

- S041 handles Terraform drift detection.
- S043 handles Policy as Code validation.
- S044 handles Kubernetes manifest policy validation.
- S037 handles security rule misconfiguration response.
- S045 handles cost guardrail validation.
