# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Terraform working directory validation plan | Review `<terraform-env>` placeholder directory. | Terraform working directory is identified. | `commands.md`, `configs/terraform-drift-detection-summary.md`, `validation.md` |
| V002 | Terraform init placeholder validation plan | Plan `terraform init` placeholder flow without real backend credentials. | Init flow is documented without creating real backend state. | `commands.md`, `logs/terraform-drift-detection-validation.log`, `validation.md` |
| V003 | Terraform validate placeholder validation plan | Plan `terraform validate` placeholder flow. | Validation flow is documented. | `commands.md`, `logs/terraform-drift-detection-validation.log`, `validation.md` |
| V004 | Terraform plan drift detection validation plan | Plan `terraform plan` evidence review. | Plan output can indicate drift state. | `commands.md`, `screenshots/terraform-plan-no-drift.png`, `screenshots/terraform-plan-drift-detected.png`, `validation.md` |
| V005 | AWS drift placeholder validation plan | Map AWS drift placeholder such as security group rule drift. | AWS drift target is documented. | `commands.md`, `configs/terraform-drift-target-mapping.md`, `validation.md` |
| V006 | Azure drift placeholder validation plan | Map Azure drift placeholder such as NSG rule drift. | Azure drift target is documented. | `commands.md`, `configs/terraform-drift-target-mapping.md`, `validation.md` |
| V007 | OpenStack drift placeholder validation plan | Map OpenStack drift placeholder such as Security Group drift. | OpenStack drift target is documented. | `commands.md`, `configs/terraform-drift-target-mapping.md`, `validation.md` |
| V008 | Security rule drift detection reference plan | Reference S037 boundary for security misconfiguration response. | Security rule drift detection is separated from response/remediation. | `commands.md`, `configs/terraform-drift-detection-summary.md`, `validation.md` |
| V009 | Tag or label drift detection plan | Compare `<expected-state>` and `<actual-state>` placeholders. | Tag or label drift can be classified. | `commands.md`, `configs/terraform-drift-target-mapping.md`, `validation.md` |
| V010 | Drift judgment state validation plan | Apply judgment model to planned result. | Drift is classified as `NO_DRIFT`, `DRIFT_DETECTED`, `INCONCLUSIVE`, or `OUT_OF_SCOPE`. | `commands.md`, `configs/terraform-drift-judgment-model.md`, `validation.md` |
| V011 | Drift evidence capture plan | Review required command, log, screenshot, and summary evidence. | Drift evidence is mapped and reviewable. | `commands.md`, `logs/terraform-drift-detection-validation.log`, `validation.md` |
| V012 | Failure condition for missing Terraform baseline, missing plan output, undetected manual change, ambiguous drift result, use of real credentials, generated tfstate committed to repository, or missing evidence | Evaluate findings against explicit failure conditions. | Drift detection issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates Terraform drift detection only; remediation, policy checks, Kubernetes manifest policy, and cost guardrails are handled separately.
