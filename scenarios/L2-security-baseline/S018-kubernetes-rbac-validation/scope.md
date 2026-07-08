# Scope

## Included

- Namespace separation model validation plan.
- ServiceAccount separation model validation plan.
- Role and RoleBinding validation plan.
- Least privilege access for application workloads.
- Read-only validation account placeholder.
- Denial of unnecessary cluster-admin access.
- `kubectl auth can-i` allowed action validation plan.
- `kubectl auth can-i` denied action validation plan.
- Kubernetes Secret access restriction plan.
- Workload namespace access boundary validation plan.
- RBAC evidence collection plan.

## Excluded

- Real Kubernetes manifest implementation.
- Real kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Kubernetes workload deployment validation, which is handled in S022.
- Kubernetes manifest policy validation, which is handled in S044.
- Service mesh, Istio, Argo CD, and full GitOps, which are excluded from v1 scope.

## Placeholder Rules

Use placeholders such as `<namespace>`, `<service-account>`, `<role-name>`, `<rolebinding-name>`, and `<target-resource>`.
