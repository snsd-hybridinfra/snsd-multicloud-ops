# Terraform Drift Remediation Decision Matrix — Non-Production Example

| Drift Case | Remediation Option | Required Approval | Rollback Requirement | Expected Post-Remediation Evidence | Final Judgment |
|---|---|---|---|---|---|
| Security rule broadened outside Terraform | REVERT_TO_TERRAFORM | Required | Required | NO_DRIFT | REMEDIATION_READY |
| Resource deleted outside Terraform | REVERT_TO_TERRAFORM | Required | Required | NO_DRIFT | REMEDIATION_READY |
| Resource created outside Terraform | INVESTIGATE_ONLY | Required | Required | Review record | MANUAL_REVIEW_REQUIRED |
| Instance size changed outside Terraform | CODIFY_APPROVED_CHANGE | Required | Required | NO_DRIFT | REMEDIATION_READY |
| Tag-only drift | CODIFY_APPROVED_CHANGE | Placeholder | Required | NO_DRIFT | REMEDIATION_READY |
| Network route drift | REVERT_TO_TERRAFORM | Required | Required | NO_DRIFT | REMEDIATION_READY |
| Public exposure drift | REJECT_CHANGE | Required | Required | NO_DRIFT | REMEDIATION_READY |
| State unavailable | INVESTIGATE_ONLY | Required | Not applicable | Restored evidence | EVIDENCE_INCOMPLETE |
| Plan failed | INVESTIGATE_ONLY | Required | Not applicable | Successful sanitized plan | MANUAL_REVIEW_REQUIRED |
| Approved manual change needs codification | CODIFY_APPROVED_CHANGE | Required | Required | NO_DRIFT | REMEDIATION_VALIDATED |

`ACCEPT_DOCUMENTED_EXCEPTION` is allowed only with complete approval, owner, expiry, risk, and rollback evidence. `REMEDIATION_REJECTED` applies when controls are absent.
