# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Complete | files/summary |
| V002 | Runbook boundary | Manual/no promotion | runbook |
| V003 | Criteria matrix | Thirteen phases | criteria |
| V004 | Ansible placeholder safety | Debug only | playbook |
| V005 | Metric placeholders | Symbolic | metrics |
| V006 | Pre-stop Primary state | Active/role | pre primary |
| V007 | Pre-stop replication state | Healthy | pre replica |
| V008 | Manual Primary stop event | Manual-only | stop event |
| V009 | Primary down detection | Detected | down sample |
| V010 | Application write impact | Detected/sanitized | impact sample |
| V011 | Replica no-promotion state | Read-only/unpromoted | outage replica |
| V012 | Manual Primary recovery event | Manual-only | recovery event |
| V013 | Post-recovery Primary and replication | Healthy | post samples |
| V014 | Replication catch-up | Healthy/no error | catch-up |
| V015 | Recovery timing | Numeric or WARN | stop event |
| V016 | Recovered-state failure indicators | None | post/catch-up |
| V017 | Database and payload safety | Safe | log/summary |
| V018 | Execution safety boundary | No execution | validator |
