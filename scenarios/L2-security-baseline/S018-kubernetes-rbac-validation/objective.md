# Objective

S018 defines the Kubernetes RBAC least privilege validation model for the SNSD Multi-Cloud Ops Kubernetes/k3s service runtime.

The scenario validates that Kubernetes access is planned around explicit namespaces, ServiceAccounts, Roles, RoleBindings, allowed actions, denied actions, Secret access boundaries, and namespace isolation. It prevents unnecessary cluster-admin access, unrestricted Secret access, excessive permissions, and namespace boundary violations from being accepted as a baseline security state.

This scenario does not implement Kubernetes manifests. It defines how future RBAC objects and `kubectl auth can-i` evidence must be reviewed and validated.

## Operational Capability

- Confirm namespace separation is planned.
- Confirm ServiceAccounts are separated by workload or validation purpose.
- Confirm Roles and RoleBindings grant only required access.
- Confirm a read-only validation account placeholder can be tested.
- Confirm unnecessary cluster-admin access is denied.
- Confirm Secret read access and workload namespace boundaries are restricted.
