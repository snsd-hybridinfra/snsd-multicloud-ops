# Commands

Scenario: S022-kubernetes-workload-deployment-validation
Level: L3-service-operations
Capability: Kubernetes/k3s Workload Deployment Validation
Target: `<namespace>`
Execution timestamp: TODO

Record sanitized output only. Do not include kubeconfig files, Kubernetes Secrets, private registry credentials, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Namespace existence validation plan | Plan read-only lookup for `<namespace>`. | Confirm target namespace exists. | TODO: record sanitized output after approved execution. |
| V002 | Web Deployment existence validation plan | Plan read-only lookup for `<web-deployment>` in `<namespace>`. | Confirm web workload Deployment exists. | TODO: record sanitized output after approved execution. |
| V003 | API Deployment existence validation plan | Plan read-only lookup for `<api-deployment>` in `<namespace>`. | Confirm API workload Deployment exists. | TODO: record sanitized output after approved execution. |
| V004 | Deployment rollout status validation plan | Plan rollout status checks for `<web-deployment>` and `<api-deployment>`. | Confirm workload rollouts complete. | TODO: record sanitized output after approved execution. |
| V005 | Pod Running and Ready status validation plan | Plan pod status review for workload pods. | Confirm pods are Running and Ready. | TODO: record sanitized output after approved execution. |
| V006 | Replica availability validation plan | Plan replica availability review for Deployments. | Confirm available replicas match desired replicas. | TODO: record sanitized output after approved execution. |
| V007 | Kubernetes Service existence validation plan | Plan read-only lookup for `<web-service>` and `<api-service>`. | Confirm required Service objects exist. | TODO: record sanitized output after approved execution. |
| V008 | ConfigMap reference validation plan | Review workload ConfigMap references. | Confirm required non-secret configuration references exist. | TODO: record sanitized output after approved execution. |
| V009 | Secret template reference validation plan | Review Secret template references by placeholder name only. | Confirm Secret references are present without storing real values. | TODO: record sanitized output after approved execution. |
| V010 | Resource requests and limits validation plan | Review workload resource request and limit settings. | Confirm resource policy is defined. | TODO: record sanitized output after approved execution. |
| V011 | Image tag not latest validation plan | Review `<container-image>` tag values. | Confirm images do not use `latest`. | TODO: record sanitized output after approved execution. |
| V012 | Failure condition for missing namespace, failed rollout, CrashLoopBackOff, ImagePullBackOff, missing service, missing config reference, or missing resource limits | Review validation findings against failure criteria. | Confirm workload failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/kubernetes-workload-summary.md`
- `configs/kubernetes-resource-policy-summary.md`
- `logs/kubernetes-workload-deployment-validation.log`
- `screenshots/kubernetes-workload-status.png`
