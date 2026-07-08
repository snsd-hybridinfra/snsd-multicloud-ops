# Architecture

## Relevant Components

- Control Plane: records validation commands and evidence.
- Kubernetes/k3s API: target for future read-only RBAC validation checks.
- Namespaces: separate workload, platform, and validation boundaries.
- ServiceAccounts: represent workload identities and read-only validation identities.
- Roles and RoleBindings: namespace-scoped permission grants.
- Secrets: restricted resources that require explicit access denial or limited access validation.

## Access Model

- `<namespace>` represents the workload or validation namespace under review.
- `<service-account>` must be bound only to required namespace-scoped permissions.
- `<role-name>` must describe the minimum resource verbs needed for the workload or validation function.
- `<rolebinding-name>` must bind only the intended ServiceAccount to the intended Role.
- Cluster-admin binding must not be used for application workloads or read-only validation accounts.
- Secret read access must be denied unless explicitly required and documented.
- Workload access must remain inside the intended namespace boundary.

## Boundary Notes

This scenario validates Kubernetes RBAC design only. Workload deployment validation and manifest policy validation are handled by separate scenarios.
