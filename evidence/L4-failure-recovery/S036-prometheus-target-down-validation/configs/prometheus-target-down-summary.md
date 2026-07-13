# Prometheus Target Down Summary

- Scenario: S036-prometheus-target-down-validation
- Generated: 2026-07-13T13:46:16+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Alert rule placeholder result: **PASS**
- Pre-failure UP result: **PASS**
- Manual target-down result: **PASS**
- Target DOWN/up=0 result: **PASS**
- Alert firing result: **PASS**
- Manual recovery result: **PASS**
- Post-recovery UP result: **PASS**
- Alert cleared result: **PASS**
- Secret-safety result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required artifacts | PASS | Five baselines and ten samples are required. |
| V002 | Runbook workflow and modes | PASS | Workflow placeholders and modes are required. |
| V003 | Alert rule placeholder | PASS | Target-down expression, duration, and S036 label are required. |
| V004 | Criteria matrix | PASS | All eleven phases are required. |
| V005 | Response matrix | PASS | Required target/up/alert signals are required. |
| V006 | Pre-failure target UP evidence | PASS | Target health up and up value 1 are required. |
| V007 | Manual target-down injection | PASS | Stop event must be manual-only. |
| V008 | Target DOWN and up=0 evidence | PASS | Down health, scrape error, and up value 0 are required. |
| V009 | Alert firing evidence | PASS | Target-down alert must be firing. |
| V010 | Manual recovery evidence | PASS | Start event must be manual-only. |
| V011 | Post-recovery target UP evidence | PASS | Target health up and up value 1 are required. |
| V012 | Alert cleared evidence | PASS | Alert must be inactive/resolved/cleared. |
| V013 | Manual command boundary | PASS | Exporter stop/start must be manual-only. |
| V014 | Recovery timing | WARN | Unmeasured time leaves threshold compliance unproven. |
| V015 | Recovered-state failure indicators | PASS | No down/up=0/firing signal may remain. |
| V016 | Endpoint and secret safety | PASS | No real URL/domain/address, credential, webhook, key, or secret may exist. |
| V017 | Execution safety boundary | PASS | No exporter/Prometheus start, stop, reload, rule change, or other mutation is allowed. |
