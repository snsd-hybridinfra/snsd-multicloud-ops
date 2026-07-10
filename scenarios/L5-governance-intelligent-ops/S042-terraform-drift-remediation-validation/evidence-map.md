# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Prior drift detection evidence reference validation plan | `commands.md`; `validation.md`; `configs/terraform-drift-remediation-summary.md` | command plan, validation record, remediation summary | yes |
| Terraform plan review validation plan | `commands.md`; `logs/terraform-drift-remediation-validation.log`; `screenshots/terraform-plan-before-remediation.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Remediation decision point validation plan | `configs/terraform-remediation-decision-model.md`; `validation.md` | decision model, validation record | yes |
| Terraform apply placeholder validation plan | `commands.md`; `logs/terraform-drift-remediation-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| AWS drift remediation placeholder validation plan | `configs/terraform-remediation-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Azure drift remediation placeholder validation plan | `configs/terraform-remediation-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| OpenStack drift remediation placeholder validation plan | `configs/terraform-remediation-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Security rule drift remediation reference validation plan | `configs/terraform-drift-remediation-summary.md`; `validation.md` | remediation summary, validation record | yes |
| Tag or label drift remediation validation plan | `configs/terraform-remediation-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Post-remediation Terraform plan validation plan | `commands.md`; `screenshots/terraform-plan-after-remediation.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Remediation judgment state validation plan | `configs/terraform-remediation-decision-model.md`; `screenshots/terraform-remediation-judgment.png`; `validation.md` | decision model, screenshot reference, validation record | yes |
| Remediation evidence capture plan | `commands.md`; `validation.md`; `logs/terraform-drift-remediation-validation.log` | command plan, validation record, validation log | yes |
| Failure condition for missing drift evidence, unsafe remediation decision, unreviewed plan, failed apply, drift remaining after remediation, generated tfstate committed to repository, use of real credentials, or missing evidence | `validation.md` | failure criteria and status record | yes |

No real Terraform output, apply output, provider output, or tfstate has been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
