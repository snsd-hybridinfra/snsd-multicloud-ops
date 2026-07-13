# Validation Result

- Actual Result: StaticEvidence validation completed; generated summary is authoritative.
- Status: PASS when critical failures equal zero; placeholder-only exception expiry may be WARN.

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Artifacts | Complete | summary | PASS |
| V002 | Runbook | Complete | runbook | PASS |
| V003 | Criteria | Ten types | criteria | PASS |
| V004 | Decision matrix | Nine cases | matrix | PASS |
| V005 | Policy | Complete | policy | PASS |
| V006 | Command scope | Out of scope | commands | PASS |
| V007 | Pre state | Restricted | pre sample | PASS |
| V008 | Misconfiguration | Manual | event | PASS |
| V009 | Detection | Complete | detection | PASS |
| V010 | Impact | Classified | impact | PASS |
| V011 | Rollback | Manual | rollback | PASS |
| V012 | Post state | Safe | post sample | PASS |
| V013 | Summary | Safe/no real change | validation | PASS |
| V014 | Expiry maturity | Review | event | WARN |
| V015 | Identifier safety | Safe | summary | PASS |
| V016 | Execution safety | No execution | validator | PASS |
