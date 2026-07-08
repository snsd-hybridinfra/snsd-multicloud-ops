# Scope

## Included

- AWS Kubernetes/k3s service node readiness validation plan.
- Azure Kubernetes/k3s service node readiness validation plan.
- OpenStack Kubernetes/k3s service node readiness validation plan.
- Control Plane `kubectl` access validation plan.
- Node role and label validation plan.
- Node condition validation plan.
- Node resource capacity validation plan.
- Node version consistency validation plan.
- Node reachability from Bastion or Control Plane validation plan.
- Node readiness evidence collection plan.

## Excluded

- Real Kubernetes manifest implementation.
- Real kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Workload deployment validation, which is handled in S022.
- Ingress routing validation, which is handled in S023.
- Kubernetes RBAC validation, which is handled in S018.
- Kubernetes manifest policy validation, which is handled in S044.
- EKS and AKS production-grade managed Kubernetes operations, which are excluded from v1 scope.

## Placeholder Rules

Use placeholders such as `<aws-k8s-node>`, `<azure-k8s-node>`, `<openstack-k8s-node>`, `<kubeconfig-path>`, and `<cluster-context>`.
