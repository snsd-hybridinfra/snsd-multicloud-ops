# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Complete | files/summary |
| V002 | Runbook workflow and modes | Complete | runbook |
| V003 | Criteria matrix | Eleven phases | criteria |
| V004 | Manual command boundary | Stop/start manual | commands |
| V005 | Metrics and response matrix | Symbolic/complete | metrics/matrix |
| V006 | Pre-failure LB and backend health | All healthy | pre samples |
| V007 | Manual failure injection | Manual-only | injection |
| V008 | LB down and client impact | Detected | down/impact |
| V009 | Backend isolation during LB failure | Both healthy | direct backend |
| V010 | Manual recovery event | Manual-only | recovery |
| V011 | Post-recovery LB and client health | Restored | post samples |
| V012 | Manual bypass and rollback | Documented | bypass sample |
| V013 | Recovery timing | Numeric or WARN | injection |
| V014 | Recovered-state failure indicators | None | post samples |
| V015 | Endpoint and secret safety | Safe | log/summary |
| V016 | Execution safety boundary | No mutation | validator |
| V017 | LiveHttp read-only state | Healthy or NOT_RUN | log/summary |
