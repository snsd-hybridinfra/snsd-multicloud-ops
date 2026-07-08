# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Namespace existence validation plan | Plan read-only lookup for `<namespace>`. | Target namespace is identifiable. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V002 | Web Deployment existence validation plan | Plan read-only lookup for `<web-deployment>`. | Web Deployment is identifiable in `<namespace>`. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V003 | API Deployment existence validation plan | Plan read-only lookup for `<api-deployment>`. | API Deployment is identifiable in `<namespace>`. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V004 | Deployment rollout status validation plan | Plan rollout status review for web and API Deployments. | Deployment rollouts complete successfully. | `commands.md`, `logs/kubernetes-workload-deployment-validation.log`, `validation.md` |
| V005 | Pod Running and Ready status validation plan | Plan pod status review for workload pods. | Pods are Running and Ready. | `commands.md`, `logs/kubernetes-workload-deployment-validation.log`, `screenshots/kubernetes-workload-status.png`, `validation.md` |
| V006 | Replica availability validation plan | Plan replica availability review for Deployments. | Available replicas match desired replicas. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V007 | Kubernetes Service existence validation plan | Plan read-only lookup for `<web-service>` and `<api-service>`. | Required Service objects are identifiable. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V008 | ConfigMap reference validation plan | Review workload references to non-secret configuration placeholders. | Required ConfigMap references are present. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V009 | Secret template reference validation plan | Review Secret template references by placeholder name only. | Secret references exist without storing real Secret values. | `commands.md`, `configs/kubernetes-workload-summary.md`, `validation.md` |
| V010 | Resource requests and limits validation plan | Review workload resource request and limit placeholders. | Workloads define resource requests and limits. | `commands.md`, `configs/kubernetes-resource-policy-summary.md`, `validation.md` |
| V011 | Image tag not latest validation plan | Review `<container-image>` tag policy. | Container images do not use `latest`. | `commands.md`, `configs/kubernetes-resource-policy-summary.md`, `validation.md` |
| V012 | Failure condition for missing namespace, failed rollout, CrashLoopBackOff, ImagePullBackOff, missing service, missing config reference, or missing resource limits | Evaluate findings against explicit failure conditions. | Workload deployment failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates workload deployment only; node readiness is handled in S021, ingress routing in S023, RBAC in S018, and manifest policy in S044.
