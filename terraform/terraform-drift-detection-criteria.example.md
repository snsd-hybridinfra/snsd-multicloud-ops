# Terraform Drift Detection Criteria — Non-Production Example

| Drift Type | Evidence Source | Drift Signal | Expected Judgment | Severity | Required Follow-up | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| Resource deleted outside Terraform | Sanitized plan | create action for declared resource | DRIFT_DETECTED | High | Review and remediate | retired-numbered-case | `<evidence-path>` |
| Resource created outside Terraform | Sanitized inventory/plan | unmanaged resource placeholder | DRIFT_DETECTED | Medium | Investigate/codify | retired-numbered-case | `<evidence-path>` |
| Security rule changed outside Terraform | Sanitized plan | broad ingress update | CRITICAL_DRIFT | Critical | Escalate | retired-numbered-case | `<evidence-path>` |
| Instance size changed outside Terraform | Sanitized plan | update action | DRIFT_DETECTED | Medium | Review cost and state | retired-numbered-case | `<evidence-path>` |
| Tag/label drift | Sanitized plan | tag-only update | DRIFT_DETECTED | Low/Medium | Policy review | retired-numbered-case | `<evidence-path>` |
| Network route drift | Sanitized plan | route create/update/delete | DRIFT_DETECTED | High | Connectivity review | retired-numbered-case | `<evidence-path>` |
| Public exposure drift | Sanitized plan | unrestricted source placeholder | CRITICAL_DRIFT | Critical | Immediate escalation | retired-numbered-case | `<evidence-path>` |
| Provider configuration drift placeholder | Review note | provider mismatch placeholder | REVIEW_REQUIRED | Medium | Manual review | retired-numbered-case | `<evidence-path>` |
| State/backend mismatch placeholder | Review note | state unavailable/mismatch | EVIDENCE_INCOMPLETE | High | Stop and investigate | retired-numbered-case | `<evidence-path>` |
| No drift detected | No-op plan | no changes | NO_DRIFT | None | Record evidence | retired-numbered-case | `<evidence-path>` |

A no-op plan means no drift. Update/change is a drift candidate; delete/create replacement is high impact. Missing evidence is incomplete. Remediation belongs to retired-numbered-case.
