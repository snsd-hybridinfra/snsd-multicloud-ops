# Validation

Scenario: S045-cost-guardrail-validation
Level: L5-governance-intelligent-ops
Capability: Cost Guardrail Validation

| Field | Value |
| --- | --- |
| Result | PARTIAL |
| Reviewer | TBD |
| Date | TBD |
| Follow-up | Collect sanitized cost guardrail evidence after execution approval. |

No real billing output has been collected yet. This file defines the validation skeleton and TODO evidence expectations.

## Validation Checks

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Cost input artifact validation plan | Cost input is identified or marked missing. | TODO | PARTIAL | `commands.md`, `configs/cost-guardrail-summary.md` |
| V002 | Resource inventory review validation plan | Placeholder resource inventory is reviewable. | TODO | PARTIAL | `commands.md`, `configs/cost-risk-resource-mapping.md` |
| V003 | Required cost owner tag validation plan | Cost owner tag or label is present. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V004 | Required environment tag validation plan | Environment tag or label is present. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V005 | Approved resource type validation plan | Resource type is approved or violation is recorded. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V006 | Resource count threshold validation plan | Resource count is within placeholder threshold or risk is recorded. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V007 | Compute size threshold validation plan | Compute size is within placeholder threshold or risk is recorded. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V008 | Public IP justification validation plan | Public IP usage is justified or risk is recorded without real IP values. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V009 | Unattached volume placeholder validation plan | Volume attachment state is reviewed and risk is recorded if unattached. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V010 | Load balancer or reverse proxy cost justification validation plan | Load balancer or reverse proxy resource is justified or risk is recorded. | TODO | PARTIAL | `configs/cost-risk-resource-mapping.md` |
| V011 | Cleanup candidate documentation validation plan | Cleanup candidate is documented and left to S046. | TODO | PARTIAL | `configs/cost-guardrail-summary.md` |
| V012 | Cost guardrail judgment state validation plan | Result is classified as `COST_OK`, `COST_WARNING`, `COST_RISK`, `COST_UNKNOWN`, or `COST_OUT_OF_SCOPE`. | TODO | PARTIAL | `configs/cost-guardrail-judgment-model.md` |
| V013 | Failure condition review | Missing cost owner, missing environment tag, excessive count, unjustified public IP, unused volume, unapproved type, unsupported FinOps claim, or missing evidence produces `FAIL` or `BLOCKED`. | TODO | PARTIAL | `validation.md`, `logs/cost-guardrail-validation.log`, `screenshots/cost-guardrail-review-result.png`, `screenshots/cost-risk-example.png` |

## Evidence Completeness

- Commands or review actions are planned: PARTIAL
- Validation outputs captured: NOT_READY
- Cost guardrail summary: NOT_READY
- Cost guardrail judgment model: NOT_READY
- Cost risk resource mapping: NOT_READY
- Cost guardrail validation log: NOT_READY
- Cost guardrail screenshots captured: NOT_READY

## Cost Guardrail Judgment States

- `COST_OK`: Resource cost risk is acceptable.
- `COST_WARNING`: Resource may cause unnecessary cost and requires review.
- `COST_RISK`: Resource violates defined cost guardrail.
- `COST_UNKNOWN`: Required cost or ownership evidence is missing.
- `COST_OUT_OF_SCOPE`: Cost validation belongs to a provider billing platform or future FinOps process.

## Boundary Notes

This scenario validates cost guardrails through placeholder resource review and evidence capture only. It does not claim real billing integration, automated budget enforcement, production-grade FinOps, AWS Budgets, Azure Cost Management, third-party FinOps tooling, automated cost remediation, real Terraform execution, or new tooling.
