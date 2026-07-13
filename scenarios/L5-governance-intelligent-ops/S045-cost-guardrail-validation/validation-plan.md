# Validation Plan

Implemented checks: `V001` artifacts, `V002` commands, `V003` rules, `V004` inputs, `V005` load, `V006` pass, `V007` fail, `V008` exception, `V009` impact, `V010` cleanup, `V011` summary, `V012` manifest/mappings, `V013` policy, `V014` artifact safety, `V015` sensitive/execution safety, and `V016` maturity.

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Cost input artifact validation plan | Review cost input placeholders. | Cost input is identified or marked missing. | `commands.md`, `configs/cost-guardrail-summary.md`, `validation.md` |
| V002 | Resource inventory review validation plan | Review placeholder inventory of resources. | Resource inventory is reviewable. | `commands.md`, `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V003 | Required cost owner tag validation plan | Review `<cost-owner>` placeholder. | Cost owner tag or label is present. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V004 | Required environment tag validation plan | Review `<environment>` placeholder. | Environment tag or label is present. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V005 | Approved resource type validation plan | Review `<resource-type>` placeholder. | Resource type is approved or violation is recorded. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V006 | Resource count threshold validation plan | Compare count placeholder to `<cost-threshold>`. | Resource count is within threshold or risk is recorded. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V007 | Compute size threshold validation plan | Review compute size placeholder. | Compute size is within threshold or risk is recorded. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V008 | Public IP justification validation plan | Review public IP usage placeholder. | Public IP usage is justified or risk is recorded. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V009 | Unattached volume placeholder validation plan | Review volume attachment placeholder. | Unattached volume is documented as risk or cleanup candidate. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V010 | Load balancer or reverse proxy cost justification validation plan | Review load balancer or reverse proxy placeholder. | Resource is justified or risk is recorded. | `configs/cost-risk-resource-mapping.md`, `validation.md` |
| V011 | Cleanup candidate documentation validation plan | Record cleanup candidate decision point. | Cleanup candidate is documented and left to S046. | `configs/cost-guardrail-summary.md`, `validation.md` |
| V012 | Cost guardrail judgment state validation plan | Apply cost judgment states. | Result is classified as `COST_OK`, `COST_WARNING`, `COST_RISK`, `COST_UNKNOWN`, or `COST_OUT_OF_SCOPE`. | `configs/cost-guardrail-judgment-model.md`, `validation.md` |
| V013 | Failure condition for missing cost owner, missing environment tag, excessive resource count, unjustified public IP, unused volume, unapproved resource type, unsupported FinOps claim, or missing evidence | Evaluate findings against explicit failure conditions. | Cost guardrail issues produce `FAIL` or `BLOCKED` status. | `validation.md`, `logs/cost-guardrail-validation.log`, `screenshots/cost-guardrail-review-result.png`, `screenshots/cost-risk-example.png` |

Every validation item must map to evidence. This scenario validates cost guardrails through placeholder review only.
