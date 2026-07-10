# Rollback Plan

This skeleton does not execute policy enforcement or infrastructure changes, so rollback is documentation-focused.

1. Stop validation if real credentials, tfstate, cloud account values, account identifiers, public IPs, or account-specific data appear.
2. Remove unsafe evidence and replace it with sanitized placeholders.
3. Mark unsupported policy claims as `POLICY_INCONCLUSIVE` or out of scope.
4. Record any policy input gaps in `validation.md`.
5. Keep cost guardrail, Kubernetes manifest policy, Terraform drift, and security response findings in their assigned scenarios.
6. Do not add a policy engine unless the repository scope is changed through an ADR.

No cloud cleanup, Terraform rollback, or policy engine rollback is performed by this scenario skeleton.
