# API Service Failure Summary

- Scenario: S032-api-service-failure-validation
- Generated: 2026-07-13T13:05:49+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Pre-failure API pod evidence result: **PASS**
- Pre-failure endpoint evidence result: **PASS**
- Pre-failure HTTP evidence result: **PASS**
- Manual fault injection evidence result: **PASS**
- Failure detection evidence result: **PASS**
- Post-recovery API pod evidence result: **PASS**
- Post-recovery endpoint evidence result: **PASS**
- Post-recovery HTTP evidence result: **PASS**
- Rollout status result: **PASS**
- Recovery time threshold documentation result: **PASS**
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required artifacts | PASS | Three baselines and nine samples exist. |
| V002 | Workflow and placeholders | PASS | Controlled workflow, modes, and placeholders are documented. |
| V003 | Manual fault boundary | PASS | Delete and scale-to-zero are manual disposable-lab references only. |
| V004 | Failure criteria matrix | PASS | All required phases exist. |
| V005 | Pre-failure Pod evidence | PASS | Running and Ready 1/1 is required. |
| V006 | Pre-failure endpoint evidence | PASS | A symbolic non-empty endpoint is required. |
| V007 | Pre-failure HTTP evidence | PASS | A healthy status is required. |
| V008 | Manual injection evidence | PASS | The event must be explicitly manual and not validator-executed. |
| V009 | Failure detection evidence | PASS | An expected failure signal is required. |
| V010 | Post-recovery Pod evidence | PASS | A replacement Running/Ready Pod is required. |
| V011 | Post-recovery endpoint evidence | PASS | A non-empty endpoint is required. |
| V012 | Post-recovery HTTP evidence | PASS | A healthy recovered status is required. |
| V013 | Rollout evidence | PASS | Successful rollout is required. |
| V014 | Recovered-state health | PASS | No unhealthy recovered-state indicator may remain. |
| V015 | Recovery timing | WARN | Elapsed time is not measured; threshold compliance is unproven. |
| V016 | Endpoint and secret safety | PASS | No real endpoint/address or sensitive artifact may exist. |
| V017 | Execution safety boundary | PASS | Only five read-only kubectl argument sets may execute. |
