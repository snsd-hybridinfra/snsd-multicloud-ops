# Rollback Plan

No live resource changes occur; correct only invalid sanitized S044 artifacts and rerun the validator.

This skeleton does not deploy manifests or enforce policy, so rollback is documentation-focused.

1. Stop validation if kubeconfig content, Kubernetes secrets, credentials, private keys, tfstate, cloud account values, account identifiers, or account-specific data appear.
2. Remove unsafe evidence and replace it with sanitized placeholders.
3. Mark unsupported enforcement claims as `MANIFEST_INCONCLUSIVE` or out of scope.
4. Record missing manifest input or failed controls in `validation.md`.
5. Keep RBAC, node readiness, workload deployment, ingress routing, and general Policy as Code findings in their assigned scenarios.
6. Do not add policy engines, admission controllers, or GitOps tooling unless the repository scope is changed through an ADR.

No Kubernetes rollback, manifest delete, or admission controller rollback is performed by this scenario skeleton.
