# Kubernetes RBAC Rule Matrix Example

NON-PRODUCTION EXAMPLE: this matrix documents policy placeholders and does not grant cluster permissions.

| Subject Placeholder | Namespace Scope | Role Type | Resource | Verbs | Explicitly Forbidden Permissions | Purpose | Least Privilege Judgment | Evidence Reference |
|---|---|---|---|---|---|---|---|---|
| `<application-service-account>` | `<namespace>` | Role | configmaps and approved workload resources | get, list, watch, create, update, patch | cluster-admin, secrets, wildcard `*`, ClusterRoleBinding | Limited application runtime operations; never default ServiceAccount | PASS | S018-V009 |
| `<monitoring-service-account>` | `<namespace>` | Role | pods, services, endpoints, deployments, replicasets | get, list, watch | write verbs, secrets, wildcard `*`, cluster-admin | Read-only monitoring | PASS | S018-V011 |
| `<deployment-automation-service-account>` | `<namespace>` | Role | approved deployments and configmaps | get, list, watch, create, update, patch | delete without approval, secrets, wildcard `*`, cluster-admin | Limited deployment automation | REVIEW_REQUIRED | S018-V008 |
| `<read-only-operator-service-account>` | `<namespace>` | Role | approved namespace resources | get, list, watch | create, update, patch, delete, secrets, wildcard `*`, cluster-admin | Read-only operations | PASS | S018-V008 |

## Baseline Expectations

- Application workloads do not receive `cluster-admin` and do not use `ClusterRoleBinding`.
- Application workloads do not receive secrets access by default.
- Monitoring permissions remain read-only.
- Wildcard permissions are forbidden.
- The `default` ServiceAccount is not approved for application workloads.

