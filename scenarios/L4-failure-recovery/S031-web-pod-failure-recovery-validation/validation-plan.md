# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-failure Web Deployment status validation plan | Plan `kubectl get deployment <web-deployment> -n <namespace>`. | Web Deployment exists and desired replicas are available before failure. | `commands.md`, `logs/web-pod-failure-recovery-validation.log`, `validation.md` |
| V002 | Pre-failure Web Pod Ready status validation plan | Plan `kubectl get pods -n <namespace>` filtered for `<web-pod>`. | Target Web Pod is Running and Ready before failure. | `commands.md`, `screenshots/web-pod-before-failure.png`, `validation.md` |
| V003 | Pre-failure Service endpoint validation plan | Plan endpoint review for `<web-service>`. | Web Service has at least one ready endpoint before failure. | `commands.md`, `configs/web-pod-failure-recovery-summary.md`, `validation.md` |
| V004 | Web Pod delete failure injection plan | Plan `kubectl delete pod <web-pod> -n <namespace>`. | Only one Web Pod is targeted for controlled failure injection. | `commands.md`, `logs/web-pod-failure-recovery-validation.log`, `validation.md` |
| V005 | Replacement Pod creation validation plan | Observe Deployment/ReplicaSet replacement behavior. | A replacement Web Pod is created. | `commands.md`, `logs/web-pod-failure-recovery-validation.log`, `validation.md` |
| V006 | Web Pod Ready recovery validation plan | Review replacement Pod readiness. | Replacement Web Pod reaches Ready state. | `commands.md`, `screenshots/web-pod-after-recovery.png`, `validation.md` |
| V007 | Service endpoint recovery validation plan | Review `<web-service>` endpoint after replacement. | Web Service endpoint is restored or remains available. | `commands.md`, `configs/web-pod-failure-recovery-summary.md`, `validation.md` |
| V008 | HTTP health endpoint recovery validation plan | Plan HTTP health check against `<health-endpoint>`. | Health endpoint returns expected healthy status after recovery. | `commands.md`, `logs/web-pod-failure-recovery-validation.log`, `validation.md` |
| V009 | Recovery time measurement plan | Measure time from delete action to restored Ready/healthy state. | Recovery time is recorded and compared with thresholds. | `commands.md`, `configs/web-pod-recovery-threshold.md`, `validation.md` |
| V010 | Post-recovery workload status validation plan | Capture Deployment, Pod, and Service status after recovery. | Workload returns to expected replica and endpoint state. | `commands.md`, `logs/web-pod-failure-recovery-validation.log`, `screenshots/web-pod-after-recovery.png`, `validation.md` |
| V011 | Failure condition for no replacement Pod, Pod stuck in Pending or CrashLoopBackOff, Service endpoint missing, HTTP recovery failure, or recovery threshold exceeded | Evaluate findings against explicit failure conditions. | Recovery failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates Web Pod recovery only; workload deployment is handled in S022, Ingress routing in S023, load balancing health checks in S025, Blackbox probing in S030, and API service failure in S032.
