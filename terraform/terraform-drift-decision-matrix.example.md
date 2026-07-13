# Terraform Drift Decision Matrix — Non-Production Example

| Plan Signal | Example Evidence | Operational Meaning | Severity | Required Action | Remediation Owner Scenario | Final Judgment |
|---|---|---|---|---|---|---|
| No changes | exit code 0 | Desired and observed placeholders match | None | Record | S042 | NO_DRIFT |
| Change outside Terraform detected | update placeholder | Manual change candidate | Medium | Review | S042 | DRIFT_DETECTED |
| Resource must be created | create placeholder | Declared resource absent | High | Review | S042 | DRIFT_DETECTED |
| Resource must be updated | update placeholder | Configuration differs | Medium | Review | S042 | DRIFT_DETECTED |
| Resource must be replaced | replace placeholder | High-impact replacement | High | Approval | S042 | DRIFT_DETECTED |
| Resource must be destroyed | delete placeholder | Unmanaged or removed declaration | High | Approval | S042 | REVIEW_REQUIRED |
| Security rule broadened | source becomes unrestricted placeholder | Exposure increased | Critical | Escalate | S042 | CRITICAL_DRIFT |
| Public exposure detected | public exposure placeholder | Protected surface exposed | Critical | Escalate | S042 | CRITICAL_DRIFT |
| Tag drift only | tag update placeholder | Governance metadata differs | Low | Review | S042 | DRIFT_DETECTED |
| Plan failed | exit code 1 | Plan cannot be judged | High | Investigate | S042 | PLAN_FAILED |
| State unavailable | missing sanitized baseline | Evidence unavailable | High | Stop | S042 | EVIDENCE_INCOMPLETE |

Allowed judgments are `NO_DRIFT`, `DRIFT_DETECTED`, `CRITICAL_DRIFT`, `PLAN_FAILED`, `EVIDENCE_INCOMPLETE`, and `REVIEW_REQUIRED`.
