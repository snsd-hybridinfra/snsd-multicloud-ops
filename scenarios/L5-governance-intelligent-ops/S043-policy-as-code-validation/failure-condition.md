# Failure Condition

S043 fails or is blocked if any of the following occur:

- Policy input artifact is missing.
- Public SSH exposure is allowed by the policy model.
- Public DB port exposure is allowed by the policy model.
- Required tag or label is missing and not classified.
- Resource naming violation is not recorded.
- Policy result is ambiguous or unsupported.
- Evidence is missing or cannot be mapped to validation checks.
- Real policy engine output is represented as complete without approved execution.
- The scenario claims CSPM, real-time blocking, automated remediation, OPA, Conftest, Checkov, Sentinel, Terraform Cloud, GitOps, or a new policy engine integration.
- Real credentials, secrets, access keys, private keys, kubeconfig content, subscription IDs, tenant IDs, account IDs, public IPs, tfstate, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the policy result as `POLICY_FAIL`, `POLICY_INCONCLUSIVE`, or `POLICY_NOT_APPLICABLE` as appropriate.
