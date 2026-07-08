# Validation

Scenario: S022-kubernetes-workload-deployment-validation
Level: L3-service-operations
Capability: Kubernetes/k3s Workload Deployment Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Kubernetes workload deployment output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Namespace existence validation plan | Target namespace is identifiable. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V002 | Web Deployment existence validation plan | Web Deployment is identifiable in `<namespace>`. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V003 | API Deployment existence validation plan | API Deployment is identifiable in `<namespace>`. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V004 | Deployment rollout status validation plan | Deployment rollouts complete successfully. | TODO | NOT_RUN | `commands.md`; `logs/kubernetes-workload-deployment-validation.log` |
| V005 | Pod Running and Ready status validation plan | Pods are Running and Ready. | TODO | NOT_RUN | `commands.md`; `logs/kubernetes-workload-deployment-validation.log`; `screenshots/kubernetes-workload-status.png` |
| V006 | Replica availability validation plan | Available replicas match desired replicas. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V007 | Kubernetes Service existence validation plan | Required Service objects are identifiable. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V008 | ConfigMap reference validation plan | Required ConfigMap references are present. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V009 | Secret template reference validation plan | Secret references exist without storing real Secret values. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-workload-summary.md` |
| V010 | Resource requests and limits validation plan | Workloads define resource requests and limits. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-resource-policy-summary.md` |
| V011 | Image tag not latest validation plan | Container images do not use `latest`. | TODO | NOT_RUN | `commands.md`; `configs/kubernetes-resource-policy-summary.md` |
| V012 | Failure condition for missing namespace, failed rollout, CrashLoopBackOff, ImagePullBackOff, missing service, missing config reference, or missing resource limits | Workload deployment failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Kubernetes workload summary is captured: NOT_READY
- Kubernetes resource policy summary is captured: NOT_READY
- Kubernetes workload deployment validation log is captured: NOT_READY
- Kubernetes workload status screenshot is captured: NOT_READY

## Notes

This scenario validates Kubernetes/k3s workload deployment only. Node readiness validation is handled in S021, ingress routing in S023, Kubernetes RBAC in S018, and Kubernetes manifest policy validation in S044.
