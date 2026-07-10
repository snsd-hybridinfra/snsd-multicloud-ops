# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Policy input artifact validation plan | `commands.md`; `configs/policy-as-code-summary.md`; `validation.md` | review plan, policy summary, validation record | yes |
| Public SSH exposure policy validation plan | `commands.md`; `configs/policy-control-mapping.md`; `validation.md` | review plan, control mapping, validation record | yes |
| Public DB port exposure policy validation plan | `commands.md`; `configs/policy-control-mapping.md`; `validation.md` | review plan, control mapping, validation record | yes |
| Least privilege security rule policy validation plan | `configs/policy-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Required tag or label policy validation plan | `configs/policy-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Resource naming convention policy validation plan | `configs/policy-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Approved region or zone placeholder policy validation plan | `configs/policy-control-mapping.md`; `validation.md` | control mapping, validation record | yes |
| Terraform configuration policy placeholder validation plan | `commands.md`; `configs/policy-as-code-summary.md`; `validation.md` | review plan, policy summary, validation record | yes |
| Cost guardrail reference validation plan | `configs/policy-as-code-summary.md`; `validation.md` | policy summary, validation record | yes |
| Policy judgment state validation plan | `configs/policy-judgment-model.md`; `validation.md` | judgment model, validation record | yes |
| Policy evidence capture plan | `commands.md`; `logs/policy-as-code-validation.log`; `screenshots/policy-validation-result.png`; `screenshots/policy-violation-example.png`; `validation.md` | review plan, validation log, screenshot reference, validation record | yes |
| Failure condition for missing policy input, public SSH allowed, public DB allowed, missing required tag, naming violation, ambiguous result, unsupported policy claim, or missing evidence | `validation.md` | failure criteria and status record | yes |

No real policy engine output has been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
