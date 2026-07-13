# API Service Failure Criteria

| Failure Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Pre-failure API deployment state | Deployment | Exists and available | Missing/unavailable | Baseline | S032 | pre-failure evidence |
| Pre-failure API pod readiness | Pods | Running and Ready 1/1 | Not ready | Baseline | S032 | pre-failure pod sample |
| Pre-failure Service endpoint availability | Endpoints | Placeholder endpoint is non-empty | `<none>` | Baseline | S032 | pre-failure endpoint sample |
| Pre-failure API HTTP health response | HTTP | 200 or documented healthy status | 5xx/timeout/refused | Baseline | S032 | pre-failure HTTP sample |
| Manual failure injection event | Operator record | Explicit manual marker | Automated/ambiguous | Controlled fault | S032 | injection sample |
| API failure detection | Workload/HTTP | Failure signal recorded | No failure evidence | Detected | S032 | detection sample |
| Endpoint loss or degraded endpoint state | Endpoints | Empty/degraded during fault | Not assessed | Detected | S032 | detection sample |
| HTTP failure response | HTTP | 5xx, timeout, or connection refused | Healthy-only evidence | Detected | S032 | detection sample |
| Recovery action placeholder | Runbook | Manual recovery documented | Undocumented mutation | Recovering | S032 | runbook |
| Post-recovery pod readiness | Pods | Replacement Running and Ready 1/1 | Unhealthy | Recovered | S032 | post pod sample |
| Post-recovery Service endpoint availability | Endpoints | Non-empty placeholder | `<none>` | Recovered | S032 | post endpoint sample |
| Post-recovery API HTTP health response | HTTP | 200 or documented healthy status | 5xx/timeout/refused | Recovered | S032 | post HTTP sample |
| Recovery time threshold | Timing | Within `<recovery-time-threshold-seconds>` | Threshold breached/missing | Review | S032 | summary |
