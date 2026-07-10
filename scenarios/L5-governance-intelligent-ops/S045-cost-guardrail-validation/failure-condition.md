# Failure Condition

S045 fails or is blocked if any of the following occur:

- Cost input artifact is missing.
- Required cost owner tag or label is missing.
- Required environment tag or label is missing.
- Resource count exceeds placeholder threshold without classification.
- Compute size exceeds placeholder threshold without classification.
- Public IP usage is unjustified.
- Unattached volume is identified but not recorded.
- Load balancer or reverse proxy usage is unjustified.
- Resource type is unapproved.
- Cleanup candidate is not documented.
- Cost judgment state is ambiguous or missing.
- Evidence is missing or cannot be mapped to validation checks.
- The scenario claims real billing integration, automated budget enforcement, production-grade FinOps, AWS Budgets, Azure Cost Management, third-party FinOps tooling, or automated remediation.
- Real credentials, secrets, access keys, private keys, kubeconfig content, billing account IDs, subscription IDs, tenant IDs, account IDs, public IPs, tfstate, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the cost result as `COST_RISK`, `COST_UNKNOWN`, or `COST_OUT_OF_SCOPE` as appropriate.
