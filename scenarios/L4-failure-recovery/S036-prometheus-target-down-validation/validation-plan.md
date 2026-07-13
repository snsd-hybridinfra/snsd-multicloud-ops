# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Complete | files/summary |
| V002 | Runbook workflow and modes | Complete | runbook |
| V003 | Alert rule placeholder | Correct/S036 | alert example |
| V004 | Criteria matrix | Eleven phases | criteria |
| V005 | Response matrix | Complete | matrix |
| V006 | Pre-failure target UP evidence | health up/up=1 | pre samples |
| V007 | Manual target-down injection | Manual-only | injection |
| V008 | Target DOWN and up=0 evidence | Detected | down samples |
| V009 | Alert firing evidence | Firing | down alerts |
| V010 | Manual recovery evidence | Manual-only | recovery |
| V011 | Post-recovery target UP evidence | health up/up=1 | post samples |
| V012 | Alert cleared evidence | Resolved/inactive | post alerts |
| V013 | Manual command boundary | Stop/start manual | commands |
| V014 | Recovery timing | Numeric or WARN | injection |
| V015 | Recovered-state failure indicators | None | post samples |
| V016 | Endpoint and secret safety | Safe | log/summary |
| V017 | Execution safety boundary | No mutation | validator |
| V018 | LivePrometheus read-only state | Reachable/expected or NOT_RUN | log/summary |
