# Terraform Drift Remediation Criteria — Non-Production Example

| Remediation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Drift detection reference | retired-numbered-case sample | retired-numbered-case ID/status present | Missing reference | EVIDENCE_INCOMPLETE | retired-numbered-case | `<evidence-path>` |
| Drift classification review | Classification sample | Severity reviewed | Severity absent | MANUAL_REVIEW_REQUIRED | retired-numbered-case | `<evidence-path>` |
| Remediation option selection | Decision sample | Approved option selected | Invalid option | REMEDIATION_REJECTED | retired-numbered-case | `<evidence-path>` |
| Approval placeholder | Approval sample | Medium/High/Critical approval exists | Approval absent | REMEDIATION_REJECTED | retired-numbered-case | `<evidence-path>` |
| Risk assessment placeholder | Decision sample | Risk documented | Risk absent | MANUAL_REVIEW_REQUIRED | retired-numbered-case | `<evidence-path>` |
| Remediation plan evidence | Plan sample | Plan documented; no automatic execution | Execution implied | REMEDIATION_REJECTED | retired-numbered-case | `<evidence-path>` |
| Rollback plan evidence | Rollback sample | Rollback precedes remediation | Missing rollback | REMEDIATION_REJECTED | retired-numbered-case | `<evidence-path>` |
| Post-remediation plan evidence | No-drift sample | Sanitized exit 0 | Missing sample | EVIDENCE_INCOMPLETE | retired-numbered-case | `<evidence-path>` |
| Post-remediation no-drift validation | No-drift sample | NO_DRIFT or accepted drift | Drift remains | MANUAL_REVIEW_REQUIRED | retired-numbered-case | `<evidence-path>` |
| Final remediation judgment | Final summary | Allowed judgment | Invalid result | REMEDIATION_REJECTED | retired-numbered-case | `<evidence-path>` |

Allowed final judgments are `REMEDIATION_READY`, `REMEDIATION_VALIDATED`, `MANUAL_REVIEW_REQUIRED`, `REMEDIATION_REJECTED`, and `EVIDENCE_INCOMPLETE`. No real cloud change is performed.
