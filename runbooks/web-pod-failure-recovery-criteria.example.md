# Web Pod Failure Recovery Criteria Example

NON-PRODUCTION EXAMPLE.

| Recovery Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Pre-failure deployment state | Deployment status | Desired replicas remain `<replica-count>` | Desired replicas change | READY | S022 | `<evidence-path>` |
| Pre-failure pod readiness | Pod list | At least one Running and Ready Pod | No Ready Pod | READY | S022 | `<evidence-path>` |
| Fault injection event | Manual event note | Explicit manual disposable-lab event | Automated/production deletion | CONTROLLED | S031 | `<evidence-path>` |
| Failed pod termination | Pod list/event | Original Pod terminates or disappears | Original remains active without explanation | RECOVERING | S031 | `<evidence-path>` |
| Replacement pod creation | Pod list | `<replacement-pod-name>` appears | No replacement | FAILED | S031 | `<evidence-path>` |
| Replacement pod Ready state | Pod list | Replacement Running and Ready | Pending/failed/not Ready | RECOVERED | S031 | `<evidence-path>` |
| Deployment replica consistency | Deployment status | Desired and available replicas equal `<replica-count>` | Counts differ | RECOVERED | S031 | `<evidence-path>` |
| Rollout status | Rollout status | Successfully rolled out | Rollout fails/times out | RECOVERED | S031 | `<evidence-path>` |
| Service endpoint continuity | Endpoint list | At least one placeholder endpoint | Empty or `<none>` | CONTINUOUS | S040 | `<evidence-path>` |
| Recovery time threshold | Sanitized timing note | Within `<recovery-time-threshold-seconds>` | Missing/over threshold | REVIEW | S031 | `<evidence-path>` |
