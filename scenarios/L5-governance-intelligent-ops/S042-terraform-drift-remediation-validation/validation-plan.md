# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Prior drift detection evidence reference validation plan | Reference S041 evidence placeholders. | Drift evidence exists or remediation is blocked. | `commands.md`, `validation.md`, `configs/terraform-drift-remediation-summary.md` |
| V002 | Terraform plan review validation plan | Review pre-remediation plan placeholder. | Plan is reviewed before remediation decision. | `commands.md`, `logs/terraform-drift-remediation-validation.log`, `screenshots/terraform-plan-before-remediation.png`, `validation.md` |
| V003 | Remediation decision point validation plan | Record approval or block decision. | Remediation decision is explicit and reviewable. | `configs/terraform-remediation-decision-model.md`, `validation.md` |
| V004 | Terraform apply placeholder validation plan | Document apply placeholder without real execution. | Apply remains controlled and placeholder-only. | `commands.md`, `logs/terraform-drift-remediation-validation.log`, `validation.md` |
| V005 | AWS drift remediation placeholder validation plan | Map AWS Security Group remediation placeholder. | AWS remediation target is documented without account values. | `configs/terraform-remediation-target-mapping.md`, `validation.md` |
| V006 | Azure drift remediation placeholder validation plan | Map Azure NSG remediation placeholder. | Azure remediation target is documented without subscription or tenant values. | `configs/terraform-remediation-target-mapping.md`, `validation.md` |
| V007 | OpenStack drift remediation placeholder validation plan | Map OpenStack Security Group remediation placeholder. | OpenStack remediation target is documented without openrc or clouds.yaml content. | `configs/terraform-remediation-target-mapping.md`, `validation.md` |
| V008 | Security rule drift remediation reference validation plan | Reference S037 and S042 boundary. | Security rule drift remediation is documented without incident response claims. | `configs/terraform-drift-remediation-summary.md`, `validation.md` |
| V009 | Tag or label drift remediation validation plan | Compare corrected tag or label placeholders. | Metadata drift remediation is documented. | `configs/terraform-remediation-target-mapping.md`, `validation.md` |
| V010 | Post-remediation Terraform plan validation plan | Review post-remediation plan placeholder. | Drift is absent, remains, or is inconclusive. | `commands.md`, `screenshots/terraform-plan-after-remediation.png`, `validation.md` |
| V011 | Remediation judgment state validation plan | Apply remediation decision model. | Result is classified as `REMEDIATION_READY`, `REMEDIATION_APPLIED`, `REMEDIATION_BLOCKED`, `REMEDIATION_FAILED`, or `OUT_OF_SCOPE`. | `configs/terraform-remediation-decision-model.md`, `screenshots/terraform-remediation-judgment.png`, `validation.md` |
| V012 | Remediation evidence capture plan | Review required command, log, screenshot, and summary evidence. | Evidence is mapped and reviewable. | `commands.md`, `validation.md`, `logs/terraform-drift-remediation-validation.log` |
| V013 | Failure condition for missing drift evidence, unsafe remediation decision, unreviewed plan, failed apply, drift remaining after remediation, generated tfstate committed to repository, use of real credentials, or missing evidence | Evaluate findings against explicit failure conditions. | Remediation issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

Every validation item must map to evidence. This scenario validates drift remediation documentation only.
