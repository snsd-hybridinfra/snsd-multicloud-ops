# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-failure API Deployment status validation plan | Plan `kubectl get deployment <api-deployment> -n <namespace>`. | API Deployment exists and desired replicas are available before failure. | `commands.md`, `logs/api-service-failure-validation.log`, `validation.md` |
| V002 | Pre-failure API Pod Ready status validation plan | Plan `kubectl get pods -n <namespace>` filtered for `<api-pod>`. | Target API Pod is Running and Ready before failure. | `commands.md`, `screenshots/api-service-before-failure.png`, `validation.md` |
| V003 | Pre-failure API Service endpoint validation plan | Plan endpoint review for `<api-service>`. | API Service has at least one ready endpoint before failure. | `commands.md`, `configs/api-service-failure-summary.md`, `validation.md` |
| V004 | API failure injection plan | Plan a placeholder failure action for `<api-deployment>` or `<api-pod>`. | Failure injection is scoped to API workload only. | `commands.md`, `logs/api-service-failure-validation.log`, `validation.md` |
| V005 | API route failure response validation plan | Plan API route check for `<ingress-host><api-path>` during failure. | API route failure or degradation is visible. | `commands.md`, `screenshots/api-service-during-failure.png`, `validation.md` |
| V006 | API health endpoint failure validation plan | Plan health check against `<api-health-endpoint>` during failure. | API health endpoint shows failed or degraded status. | `commands.md`, `logs/api-service-failure-validation.log`, `validation.md` |
| V007 | Ingress API path failure validation plan | Reference S023 route behavior for `<api-path>`. | Ingress API path failure is documented without reimplementing Ingress routing. | `commands.md`, `configs/api-service-failure-summary.md`, `validation.md` |
| V008 | Blackbox API probe failure reference plan | Reference S030 API probe behavior. | Blackbox API probe failure reference is documented. | `commands.md`, `configs/api-service-failure-summary.md`, `validation.md` |
| V009 | API workload restoration validation plan | Plan rollback or workload restoration action. | API workload restoration path is documented. | `commands.md`, `logs/api-service-failure-validation.log`, `validation.md` |
| V010 | API health recovery validation plan | Plan post-restoration API health check. | API health endpoint returns expected healthy status after recovery. | `commands.md`, `screenshots/api-service-after-recovery.png`, `validation.md` |
| V011 | Recovery time measurement plan | Measure failure detection and recovery duration. | Detection and recovery timing is recorded and compared with thresholds. | `commands.md`, `configs/api-service-recovery-threshold.md`, `validation.md` |
| V012 | Failure condition for API failure not detected, unexpected success during failure, API Pod stuck in CrashLoopBackOff, missing Service endpoint, HTTP 5xx persistence, or recovery threshold exceeded | Evaluate findings against explicit failure conditions. | API failure or recovery issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates API service failure behavior only; workload deployment is handled in S022, Ingress routing in S023, reverse proxy forwarding in S024, load balancing health checks in S025, Blackbox probing in S030, and Web Pod recovery in S031.
