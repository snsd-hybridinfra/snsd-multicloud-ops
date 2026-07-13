# Load Balancer Failure Summary

- Scenario: S035-load-balancer-failure-validation
- Generated: 2026-07-13T13:46:16+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Pre-failure health result: **PASS**
- Manual fault result: **PASS**
- Failure/impact result: **PASS**
- Backend isolation result: **PASS**
- Recovery result: **PASS**
- Bypass/rollback result: **PASS**
- Secret-safety result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required artifacts | PASS | Five baselines and ten samples are required. |
| V002 | Runbook workflow and modes | PASS | Placeholders, manual boundaries, and modes are required. |
| V003 | Criteria matrix | PASS | All eleven phases are required. |
| V004 | Manual command boundary | PASS | Stop/start must be manual-only. |
| V005 | Metrics and response matrix | PASS | Symbolic metrics and failure isolation response are required. |
| V006 | Pre-failure LB and backend health | PASS | LB and two backends must be healthy. |
| V007 | Manual failure injection | PASS | Failure event must be manual-only. |
| V008 | LB down and client impact | PASS | Entrypoint and client failure evidence are required. |
| V009 | Backend isolation during LB failure | PASS | Both direct backends must remain healthy. |
| V010 | Manual recovery event | PASS | Recovery must be manual-only. |
| V011 | Post-recovery LB and client health | PASS | LB and client path must be restored. |
| V012 | Manual bypass and rollback | PASS | Both steps must be documented without real routing data. |
| V013 | Recovery timing | WARN | Unmeasured time leaves threshold compliance unproven. |
| V014 | Recovered-state failure indicators | PASS | No failure signal may remain after recovery. |
| V015 | Endpoint and secret safety | PASS | No real URL/domain/address, credential, cookie, key, or secret may exist. |
| V016 | Execution safety boundary | PASS | Validator must not change services, traffic, DNS, routing, or infrastructure. |
