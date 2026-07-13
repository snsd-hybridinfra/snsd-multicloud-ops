# Validation Result

- Actual Result: StaticEvidence validation completed; generated summary is authoritative.
- Status: PASS when critical failures equal zero; unmeasured time is WARN.

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Artifacts | Complete | summary | PASS |
| V002 | Boundary | Manual/no promotion | runbook | PASS |
| V003 | Criteria | Complete | criteria | PASS |
| V004 | Ansible | Debug-only | playbook | PASS |
| V005 | Metrics | Symbolic | metrics | PASS |
| V006 | Pre Primary | Healthy | pre primary | PASS |
| V007 | Pre replication | Healthy | pre replica | PASS |
| V008 | Stop | Manual | stop event | PASS |
| V009 | Down | Detected | down sample | PASS |
| V010 | Write impact | Detected | impact | PASS |
| V011 | No promotion | Confirmed | outage replica | PASS |
| V012 | Recovery | Manual | recovery event | PASS |
| V013 | Post state | Healthy | post samples | PASS |
| V014 | Catch-up | Healthy | catch-up | PASS |
| V015 | Timing | Review | stop event | WARN |
| V016 | Post indicators | None | post/catch-up | PASS |
| V017 | Sensitive safety | Safe | summary | PASS |
| V018 | Execution safety | No execution | validator | PASS |
