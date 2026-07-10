# Prerequisites

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S044 scenario and evidence directories exist.
- Manifest names, namespaces, services, ingress objects, images, and policy results use placeholders only.
- S018 exists for Kubernetes RBAC validation and is referenced only.
- S021, S022, and S023 exist for node readiness, workload deployment, and ingress routing boundaries.
- S043 exists for general Policy as Code governance validation.
- No kubeconfig, Kubernetes secret, private registry credential, cloud account value, tfstate, credential, private key, subscription ID, tenant ID, or account-specific value is present.

## Related Scenario Boundaries

- S018 handles Kubernetes RBAC validation.
- S021 handles Kubernetes node readiness validation.
- S022 handles workload deployment validation.
- S023 handles ingress routing validation.
- S043 handles general Policy as Code validation.
