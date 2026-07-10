# Validation

Scenario: S032-api-service-failure-validation
Level: L4-failure-recovery
Capability: API Service Failure Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Kubernetes command output or API failure evidence has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Pre-failure API Deployment status validation plan | API Deployment exists and desired replicas are available before failure. | TODO | NOT_RUN | `commands.md`; `logs/api-service-failure-validation.log` |
| V002 | Pre-failure API Pod Ready status validation plan | Target API Pod is Running and Ready before failure. | TODO | NOT_RUN | `commands.md`; `screenshots/api-service-before-failure.png` |
| V003 | Pre-failure API Service endpoint validation plan | API Service has at least one ready endpoint before failure. | TODO | NOT_RUN | `commands.md`; `configs/api-service-failure-summary.md` |
| V004 | API failure injection plan | Failure injection is scoped to API workload only. | TODO | NOT_RUN | `commands.md`; `logs/api-service-failure-validation.log` |
| V005 | API route failure response validation plan | API route failure or degradation is visible. | TODO | NOT_RUN | `commands.md`; `screenshots/api-service-during-failure.png` |
| V006 | API health endpoint failure validation plan | API health endpoint shows failed or degraded status. | TODO | NOT_RUN | `commands.md`; `logs/api-service-failure-validation.log` |
| V007 | Ingress API path failure validation plan | Ingress API path failure is documented without reimplementing Ingress routing. | TODO | NOT_RUN | `commands.md`; `configs/api-service-failure-summary.md` |
| V008 | Blackbox API probe failure reference plan | Blackbox API probe failure reference is documented. | TODO | NOT_RUN | `commands.md`; `configs/api-service-failure-summary.md` |
| V009 | API workload restoration validation plan | API workload restoration path is documented. | TODO | NOT_RUN | `commands.md`; `logs/api-service-failure-validation.log` |
| V010 | API health recovery validation plan | API health endpoint returns expected healthy status after recovery. | TODO | NOT_RUN | `commands.md`; `screenshots/api-service-after-recovery.png` |
| V011 | Recovery time measurement plan | Detection and recovery timing is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/api-service-recovery-threshold.md` |
| V012 | Failure condition for API failure not detected, unexpected success during failure, API Pod stuck in CrashLoopBackOff, missing Service endpoint, HTTP 5xx persistence, or recovery threshold exceeded | API failure or recovery issues produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- API service failure summary is captured: NOT_READY
- API service recovery threshold summary is captured: NOT_READY
- API service failure validation log is captured: NOT_READY
- Before, during, and after screenshots are captured: NOT_READY

## Provisional Failure and Recovery Thresholds

- DETECTED: API failure visible within `< 60 seconds`.
- WARNING: recovery within `60-180 seconds`.
- CRITICAL: recovery failed or exceeds `180 seconds`.

## Notes

This scenario validates API service failure behavior only. Workload deployment is handled in S022, Ingress routing in S023, Nginx Reverse Proxy forwarding in S024, load balancing health checks in S025, Blackbox endpoint probing in S030, and Web Pod failure recovery in S031.
