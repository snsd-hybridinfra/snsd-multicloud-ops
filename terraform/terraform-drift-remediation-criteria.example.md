# Terraform Drift Remediation Criteria — Non-Production Example

| Remediation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Drift detection reference | S041 sample | S041 ID/status present | Missing reference | EVIDENCE_INCOMPLETE | S041 | `<evidence-path>` |
| Drift classification review | Classification sample | Severity reviewed | Severity absent | MANUAL_REVIEW_REQUIRED | S041 | `<evidence-path>` |
| Remediation option selection | Decision sample | Approved option selected | Invalid option | REMEDIATION_REJECTED | S042 | `<evidence-path>` |
| Approval placeholder | Approval sample | Medium/High/Critical approval exists | Approval absent | REMEDIATION_REJECTED | S042 | `<evidence-path>` |
| Risk assessment placeholder | Decision sample | Risk documented | Risk absent | MANUAL_REVIEW_REQUIRED | S042 | `<evidence-path>` |
| Remediation plan evidence | Plan sample | Plan documented; no automatic execution | Execution implied | REMEDIATION_REJECTED | S042 | `<evidence-path>` |
| Rollback plan evidence | Rollback sample | Rollback precedes remediation | Missing rollback | REMEDIATION_REJECTED | S042 | `<evidence-path>` |
| Post-remediation plan evidence | No-drift sample | Sanitized exit 0 | Missing sample | EVIDENCE_INCOMPLETE | S042 | `<evidence-path>` |
| Post-remediation no-drift validation | No-drift sample | NO_DRIFT or accepted drift | Drift remains | MANUAL_REVIEW_REQUIRED | S042 | `<evidence-path>` |
| Final remediation judgment | Final summary | Allowed judgment | Invalid result | REMEDIATION_REJECTED | S042 | `<evidence-path>` |

Allowed final judgments are `REMEDIATION_READY`, `REMEDIATION_VALIDATED`, `MANUAL_REVIEW_REQUIRED`, `REMEDIATION_REJECTED`, and `EVIDENCE_INCOMPLETE`. No real cloud change is performed.
