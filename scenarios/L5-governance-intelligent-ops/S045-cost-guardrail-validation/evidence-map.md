# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Cost input artifact validation plan | `commands.md`; `configs/cost-guardrail-summary.md`; `validation.md` | review plan, guardrail summary, validation record | yes |
| Resource inventory review validation plan | `commands.md`; `configs/cost-risk-resource-mapping.md`; `validation.md` | review plan, resource mapping, validation record | yes |
| Required cost owner tag validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Required environment tag validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Approved resource type validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Resource count threshold validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Compute size threshold validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Public IP justification validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Unattached volume placeholder validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Load balancer or reverse proxy cost justification validation plan | `configs/cost-risk-resource-mapping.md`; `validation.md` | resource mapping, validation record | yes |
| Cleanup candidate documentation validation plan | `configs/cost-guardrail-summary.md`; `validation.md` | guardrail summary, validation record | yes |
| Cost guardrail judgment state validation plan | `configs/cost-guardrail-judgment-model.md`; `validation.md` | judgment model, validation record | yes |
| Failure condition for missing cost owner, missing environment tag, excessive resource count, unjustified public IP, unused volume, unapproved resource type, unsupported FinOps claim, or missing evidence | `validation.md`; `logs/cost-guardrail-validation.log`; `screenshots/cost-guardrail-review-result.png`; `screenshots/cost-risk-example.png` | failure criteria, validation log, screenshot reference | yes |

No real billing output has been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
