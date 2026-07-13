# Validation Result

- Actual Result: Static validation completed; generated summary is authoritative.
- Status: PASS when critical failures equal zero; timing may be WARN.

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Artifacts | Complete | summary | PASS |
| V002 | Workflow | Complete | runbook | PASS |
| V003 | Criteria | Complete | criteria | PASS |
| V004 | Command boundary | Manual-only | commands | PASS |
| V005 | Metrics/matrix | Complete | metrics/matrix | PASS |
| V006 | Pre health | Healthy | pre samples | PASS |
| V007 | Fault | Manual | injection | PASS |
| V008 | LB/client impact | Detected | down/impact | PASS |
| V009 | Backend isolation | Healthy | direct backend | PASS |
| V010 | Recovery | Manual | recovery | PASS |
| V011 | Post health | Healthy | post samples | PASS |
| V012 | Bypass/rollback | Documented | bypass | PASS |
| V013 | Timing | Review | injection | WARN |
| V014 | Post indicators | None | post samples | PASS |
| V015 | Sensitive safety | Safe | summary | PASS |
| V016 | Execution safety | No mutation | validator | PASS |
| V017 | LiveHttp | Explicit/read-only | generated log | NOT_RUN |
