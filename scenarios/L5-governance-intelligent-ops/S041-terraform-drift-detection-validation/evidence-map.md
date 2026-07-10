# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Terraform working directory validation plan | `commands.md`; `configs/terraform-drift-detection-summary.md`; `validation.md` | command plan, drift summary, validation record | yes |
| Terraform init placeholder validation plan | `commands.md`; `logs/terraform-drift-detection-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Terraform validate placeholder validation plan | `commands.md`; `logs/terraform-drift-detection-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Terraform plan drift detection validation plan | `commands.md`; `screenshots/terraform-plan-no-drift.png`; `screenshots/terraform-plan-drift-detected.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| AWS drift placeholder validation plan | `commands.md`; `configs/terraform-drift-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| Azure drift placeholder validation plan | `commands.md`; `configs/terraform-drift-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| OpenStack drift placeholder validation plan | `commands.md`; `configs/terraform-drift-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| Security rule drift detection reference plan | `commands.md`; `configs/terraform-drift-detection-summary.md`; `validation.md` | command plan, drift summary, validation record | yes |
| Tag or label drift detection plan | `commands.md`; `configs/terraform-drift-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| Drift judgment state validation plan | `commands.md`; `configs/terraform-drift-judgment-model.md`; `validation.md` | command plan, judgment model, validation record | yes |
| Drift evidence capture plan | `commands.md`; `logs/terraform-drift-detection-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failure condition for missing Terraform baseline, missing plan output, undetected manual change, ambiguous drift result, use of real credentials, generated tfstate committed to repository, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Terraform output, plan output, provider output, or tfstate has been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
