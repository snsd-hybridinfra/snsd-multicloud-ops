# Scope

## Included

- Web workload deployment validation plan.
- API workload deployment validation plan.
- Namespace placement validation plan.
- Deployment status validation plan.
- Replica availability validation plan.
- Pod readiness validation plan.
- Service object validation plan.
- ConfigMap placeholder validation plan.
- Secret template placeholder validation plan.
- Resource requests and limits validation plan.
- Image tag policy validation plan.

## Excluded

- Real Kubernetes manifest implementation.
- Real kubeconfig files, Kubernetes Secrets, private registry credentials, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Kubernetes node readiness validation, which is handled in S021.
- Ingress routing validation, which is handled in S023.
- Kubernetes RBAC validation, which is handled in S018.
- Kubernetes manifest policy validation, which is handled in S044.
- Service mesh, Istio, Argo CD, and full GitOps, which are excluded from v1 scope.

## Placeholder Rules

Use placeholders such as `<namespace>`, `<web-deployment>`, `<api-deployment>`, `<web-service>`, `<api-service>`, and `<container-image>`.
