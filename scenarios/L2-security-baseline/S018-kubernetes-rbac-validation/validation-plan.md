# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Namespace existence validation plan | Document planned read-only lookup for `<namespace>`. | Required namespaces are identifiable by placeholder name. | `commands.md`, `configs/kubernetes-rbac-summary.md`, `validation.md` |
| V002 | ServiceAccount existence validation plan | Document planned read-only lookup for `<service-account>`. | Required ServiceAccounts are identifiable by placeholder name. | `commands.md`, `configs/kubernetes-rbac-summary.md`, `validation.md` |
| V003 | Role existence validation plan | Document planned read-only lookup for `<role-name>`. | Required Roles are identifiable and namespace-scoped. | `commands.md`, `configs/kubernetes-rbac-policy.md`, `validation.md` |
| V004 | RoleBinding existence validation plan | Document planned read-only lookup for `<rolebinding-name>`. | Required RoleBindings bind intended ServiceAccounts to intended Roles. | `commands.md`, `configs/kubernetes-rbac-policy.md`, `validation.md` |
| V005 | kubectl auth can-i allowed action validation plan | Plan `kubectl auth can-i` checks for approved actions. | Required actions are allowed only for intended subjects. | `commands.md`, `logs/kubernetes-rbac-validation.log`, `validation.md` |
| V006 | kubectl auth can-i denied action validation plan | Plan `kubectl auth can-i` checks for denied actions. | Unnecessary actions are denied. | `commands.md`, `logs/kubernetes-rbac-validation.log`, `validation.md` |
| V007 | No unnecessary cluster-admin binding validation plan | Review ClusterRoleBinding or equivalent binding scope. | Application workloads and read-only validation accounts do not use cluster-admin. | `commands.md`, `configs/kubernetes-rbac-policy.md`, `validation.md` |
| V008 | Secret read permission restriction validation plan | Review permissions for Secret read access. | Secret read access is denied unless explicitly required and documented. | `commands.md`, `configs/kubernetes-rbac-policy.md`, `validation.md` |
| V009 | Workload namespace boundary validation plan | Review allowed actions across namespace boundaries. | Workload access is constrained to the intended namespace. | `commands.md`, `logs/kubernetes-rbac-validation.log`, `screenshots/kubernetes-rbac-validation.png`, `validation.md` |
| V010 | Failure condition for missing RBAC objects, excessive permissions, cluster-admin misuse, unrestricted secret access, or namespace boundary violation | Evaluate findings against explicit failure conditions. | Unsafe RBAC patterns produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates Kubernetes RBAC design only; workload deployment is handled in S022 and manifest policy validation is handled in S044.
