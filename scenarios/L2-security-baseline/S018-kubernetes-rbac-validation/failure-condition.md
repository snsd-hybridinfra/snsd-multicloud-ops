# Failure Condition

S018 fails if the Kubernetes RBAC model allows unsafe or undocumented access patterns.

## Failure Conditions

- Required namespaces are missing from the planned RBAC model.
- Required ServiceAccounts are missing or shared across unrelated workloads.
- Required Roles are missing, cluster-scoped when namespace scope is expected, or grant excessive permissions.
- Required RoleBindings are missing or bind unintended subjects.
- `kubectl auth can-i` allows actions that should be denied.
- Application workloads or read-only validation accounts receive unnecessary cluster-admin access.
- Secret read permission is unrestricted or granted without explicit justification.
- Workload access crosses namespace boundaries without explicit approval.
- RBAC evidence cannot be captured or reviewed.
- Evidence contains kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder RBAC model exists.
- Future `kubectl auth can-i` output is unavailable.
- Required evidence files are missing.
