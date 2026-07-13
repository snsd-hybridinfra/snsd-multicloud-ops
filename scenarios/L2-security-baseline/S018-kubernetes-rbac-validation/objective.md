# Objective

## Objective Statement

Validate that Kubernetes RBAC definitions use dedicated identities, namespace-scoped permissions, and least-privilege verbs and resources.

## Success Measures

- Required policy, matrix, and marked non-production manifests exist.
- Dedicated application and monitoring ServiceAccounts are bound through namespace-scoped Roles and RoleBindings.
- No ClusterRoleBinding, cluster-admin binding, wildcard permission, default application account, or application secrets access exists.
- Monitoring uses read-only verbs.
- No kubeconfig, token, certificate, private key, endpoint, Secret resource, or account-specific content is present.
