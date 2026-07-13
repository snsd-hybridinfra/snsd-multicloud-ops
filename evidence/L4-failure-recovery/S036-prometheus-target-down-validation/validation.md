# Validation Result

- Actual Result: Static validation completed; generated summary is authoritative.
- Status: PASS when critical failures equal zero; timing may be WARN.

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Artifacts | Complete | summary | PASS |
| V002 | Workflow | Complete | runbook | PASS |
| V003 | Alert rule | Correct | alert | PASS |
| V004 | Criteria | Complete | criteria | PASS |
| V005 | Response matrix | Complete | matrix | PASS |
| V006 | Pre UP | up/up=1 | pre samples | PASS |
| V007 | Fault | Manual | injection | PASS |
| V008 | DOWN | down/up=0 | down samples | PASS |
| V009 | Alert | Firing | down alerts | PASS |
| V010 | Recovery | Manual | recovery | PASS |
| V011 | Post UP | up/up=1 | post samples | PASS |
| V012 | Alert cleared | Resolved | post alerts | PASS |
| V013 | Command boundary | Manual-only | commands | PASS |
| V014 | Timing | Review | injection | WARN |
| V015 | Post indicators | None | post samples | PASS |
| V016 | Sensitive safety | Safe | summary | PASS |
| V017 | Execution safety | No mutation | validator | PASS |
| V018 | LivePrometheus | Explicit/read-only | generated log | NOT_RUN |
