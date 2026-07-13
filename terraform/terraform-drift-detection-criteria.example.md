# Terraform Drift Detection Criteria — Non-Production Example

| Drift Type | Evidence Source | Drift Signal | Expected Judgment | Severity | Required Follow-up | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| Resource deleted outside Terraform | Sanitized plan | create action for declared resource | DRIFT_DETECTED | High | Review and remediate | S042 | `<evidence-path>` |
| Resource created outside Terraform | Sanitized inventory/plan | unmanaged resource placeholder | DRIFT_DETECTED | Medium | Investigate/codify | S042 | `<evidence-path>` |
| Security rule changed outside Terraform | Sanitized plan | broad ingress update | CRITICAL_DRIFT | Critical | Escalate | S042 | `<evidence-path>` |
| Instance size changed outside Terraform | Sanitized plan | update action | DRIFT_DETECTED | Medium | Review cost and state | S042 | `<evidence-path>` |
| Tag/label drift | Sanitized plan | tag-only update | DRIFT_DETECTED | Low/Medium | Policy review | S042 | `<evidence-path>` |
| Network route drift | Sanitized plan | route create/update/delete | DRIFT_DETECTED | High | Connectivity review | S042 | `<evidence-path>` |
| Public exposure drift | Sanitized plan | unrestricted source placeholder | CRITICAL_DRIFT | Critical | Immediate escalation | S042 | `<evidence-path>` |
| Provider configuration drift placeholder | Review note | provider mismatch placeholder | REVIEW_REQUIRED | Medium | Manual review | S042 | `<evidence-path>` |
| State/backend mismatch placeholder | Review note | state unavailable/mismatch | EVIDENCE_INCOMPLETE | High | Stop and investigate | S042 | `<evidence-path>` |
| No drift detected | No-op plan | no changes | NO_DRIFT | None | Record evidence | S041 | `<evidence-path>` |

A no-op plan means no drift. Update/change is a drift candidate; delete/create replacement is high impact. Missing evidence is incomplete. Remediation belongs to S042.
