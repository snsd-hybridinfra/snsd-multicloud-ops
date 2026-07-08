# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing Kubernetes RBAC objects.

## Rollback Steps

1. Stop validation if evidence includes kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies excessive permissions, cluster-admin misuse, unrestricted Secret access, or namespace boundary violations, record the finding as `FAIL`.
5. Do not modify Kubernetes manifests or live RBAC objects from this scenario. Any future corrective Kubernetes change must be handled by an explicitly approved implementation task.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should tighten the proposed namespace, ServiceAccount, Role, RoleBinding, Secret, and `kubectl auth can-i` model to least privilege, then repeat evidence collection with sanitized outputs.
