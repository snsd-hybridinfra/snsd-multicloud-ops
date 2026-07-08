# Execution Plan

1. Confirm the scenario evidence directory exists for S018.
2. Identify placeholder namespace targets as `<namespace>`.
3. Identify placeholder ServiceAccounts as `<service-account>`.
4. Record the planned Role and RoleBinding review method for `<role-name>` and `<rolebinding-name>`.
5. Review planned least privilege permissions for application workloads.
6. Review the read-only validation account placeholder.
7. Record planned `kubectl auth can-i` allowed action checks.
8. Record planned `kubectl auth can-i` denied action checks.
9. Review planned detection for unnecessary cluster-admin bindings.
10. Review planned Secret read permission restrictions.
11. Review workload namespace boundary checks.
12. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not create Kubernetes manifests, apply RBAC objects, create kubeconfig files, or read Kubernetes Secrets. It only defines the review flow and evidence requirements for later approved validation.
