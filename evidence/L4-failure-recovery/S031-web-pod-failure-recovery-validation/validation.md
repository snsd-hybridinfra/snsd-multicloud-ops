# Validation

Scenario: S031-web-pod-failure-recovery-validation
Level: L4-failure-recovery
Capability: Web Pod Failure Recovery Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Kubernetes command output or failure injection evidence has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Pre-failure Web Deployment status validation plan | Web Deployment exists and desired replicas are available before failure. | TODO | NOT_RUN | `commands.md`; `logs/web-pod-failure-recovery-validation.log` |
| V002 | Pre-failure Web Pod Ready status validation plan | Target Web Pod is Running and Ready before failure. | TODO | NOT_RUN | `commands.md`; `screenshots/web-pod-before-failure.png` |
| V003 | Pre-failure Service endpoint validation plan | Web Service has at least one ready endpoint before failure. | TODO | NOT_RUN | `commands.md`; `configs/web-pod-failure-recovery-summary.md` |
| V004 | Web Pod delete failure injection plan | Only one Web Pod is targeted for controlled failure injection. | TODO | NOT_RUN | `commands.md`; `logs/web-pod-failure-recovery-validation.log` |
| V005 | Replacement Pod creation validation plan | A replacement Web Pod is created. | TODO | NOT_RUN | `commands.md`; `logs/web-pod-failure-recovery-validation.log` |
| V006 | Web Pod Ready recovery validation plan | Replacement Web Pod reaches Ready state. | TODO | NOT_RUN | `commands.md`; `screenshots/web-pod-after-recovery.png` |
| V007 | Service endpoint recovery validation plan | Web Service endpoint is restored or remains available. | TODO | NOT_RUN | `commands.md`; `configs/web-pod-failure-recovery-summary.md` |
| V008 | HTTP health endpoint recovery validation plan | Health endpoint returns expected healthy status after recovery. | TODO | NOT_RUN | `commands.md`; `logs/web-pod-failure-recovery-validation.log` |
| V009 | Recovery time measurement plan | Recovery time is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/web-pod-recovery-threshold.md` |
| V010 | Post-recovery workload status validation plan | Workload returns to expected replica and endpoint state. | TODO | NOT_RUN | `commands.md`; `logs/web-pod-failure-recovery-validation.log`; `screenshots/web-pod-after-recovery.png` |
| V011 | Failure condition for no replacement Pod, Pod stuck in Pending or CrashLoopBackOff, Service endpoint missing, HTTP recovery failure, or recovery threshold exceeded | Recovery failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Web Pod failure recovery summary is captured: NOT_READY
- Web Pod recovery threshold summary is captured: NOT_READY
- Web Pod failure recovery validation log is captured: NOT_READY
- Before and after screenshots are captured: NOT_READY

## Provisional Recovery Thresholds

- NORMAL: recovery within `< 60 seconds`.
- WARNING: recovery within `60-180 seconds`.
- CRITICAL: recovery failed or exceeds `180 seconds`.

## Notes

This scenario validates Web Pod failure recovery only. Workload deployment is handled in S022, Ingress routing in S023, load balancing health checks in S025, Blackbox endpoint probing in S030, and API service failure in S032.
