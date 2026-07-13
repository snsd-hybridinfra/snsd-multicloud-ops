# Scope

Implemented boundary: static placeholders only; no Terraform, billing/cloud API, invoice/export ingestion, budget mutation, optimization, deletion, external cost runtime, credentials, or real financial/account data.

## Included

- AWS cost risk placeholder validation.
- Azure cost risk placeholder validation.
- OpenStack resource usage placeholder validation.
- Terraform resource count review plan.
- Unused resource identification placeholder.
- Oversized resource identification placeholder.
- Required tag or label for cost ownership placeholder.
- Required environment tag or label placeholder.
- Resource cleanup decision point documentation.
- Cost risk judgment model.
- Cost guardrail evidence collection plan.

## Target Cost Risk Categories

- Unused compute instance placeholder.
- Oversized compute instance placeholder.
- Unattached volume placeholder.
- Unused public IP placeholder.
- Unused load balancer or reverse proxy placeholder.
- Excessive node count placeholder.
- Missing cost owner tag placeholder.
- Unapproved resource type placeholder.
- Resource outside approved environment placeholder.

## Required Cost Guardrail Checks

- Resource has cost owner tag or label.
- Resource has environment tag or label.
- Resource type is approved for the scenario.
- Resource count is within placeholder threshold.
- Compute size is within placeholder threshold.
- Public IP usage is justified.
- Volume attachment state is reviewed.
- Load balancer or reverse proxy resource is justified.
- Cleanup candidate is documented.
- Cost risk judgment is recorded.

## Cost Guardrail Judgment Model

- `COST_OK`: Resource cost risk is acceptable.
- `COST_WARNING`: Resource may cause unnecessary cost and requires review.
- `COST_RISK`: Resource violates defined cost guardrail.
- `COST_UNKNOWN`: Required cost or ownership evidence is missing.
- `COST_OUT_OF_SCOPE`: Cost validation belongs to a provider billing platform or future FinOps process.

## Excluded

- Real cloud billing integration.
- Real Terraform execution against cloud accounts.
- Automated budget enforcement.
- Production-grade FinOps.
- AWS Budgets, Azure Cost Management, third-party FinOps tooling, or automated cost remediation.
- New tools or technologies.
- Real account IDs, billing account IDs, subscription IDs, tenant IDs, access keys, secrets, private keys, tfstate, kubeconfig, public IPs, or account-specific values.
- Terraform drift detection, handled in S041.
- Terraform drift remediation, handled in S042.
- Policy as Code validation, handled in S043.
- Resource cleanup validation, handled in S046.
- Final evidence report generation, handled in S050.
