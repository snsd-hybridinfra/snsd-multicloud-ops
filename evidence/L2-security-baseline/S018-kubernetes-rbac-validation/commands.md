# Commands

Scenario: S018-kubernetes-rbac-validation
Level: L2-security-baseline
Capability: Kubernetes RBAC Least Privilege Validation
Target: `<namespace>`
Execution timestamp: TODO

Record sanitized output only. Do not include kubeconfig files, Kubernetes Secrets, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Namespace existence validation plan | Plan read-only lookup for `<namespace>`. | Confirm required namespaces are identifiable. | TODO: record sanitized output after approved execution. |
| V002 | ServiceAccount existence validation plan | Plan read-only lookup for `<service-account>` in `<namespace>`. | Confirm required ServiceAccounts are identifiable. | TODO: record sanitized output after approved execution. |
| V003 | Role existence validation plan | Plan read-only lookup for `<role-name>` in `<namespace>`. | Confirm required Roles are identifiable and namespace-scoped. | TODO: record sanitized output after approved execution. |
| V004 | RoleBinding existence validation plan | Plan read-only lookup for `<rolebinding-name>` in `<namespace>`. | Confirm RoleBindings map intended subjects to intended Roles. | TODO: record sanitized output after approved execution. |
| V005 | kubectl auth can-i allowed action validation plan | Plan `kubectl auth can-i <verb> <target-resource> --as system:serviceaccount:<namespace>:<service-account> -n <namespace>`. | Confirm required actions are allowed for intended subjects. | TODO: record sanitized output after approved execution. |
| V006 | kubectl auth can-i denied action validation plan | Plan `kubectl auth can-i <denied-verb> <target-resource> --as system:serviceaccount:<namespace>:<service-account> -n <namespace>`. | Confirm unnecessary actions are denied. | TODO: record sanitized output after approved execution. |
| V007 | No unnecessary cluster-admin binding validation plan | Review planned ClusterRoleBinding or equivalent bindings for cluster-admin usage. | Confirm cluster-admin is not assigned unnecessarily. | TODO: record sanitized output after approved execution. |
| V008 | Secret read permission restriction validation plan | Review whether `<service-account>` can read Secret resources. | Confirm Secret read access is restricted. | TODO: record sanitized output after approved execution. |
| V009 | Workload namespace boundary validation plan | Review planned cross-namespace access attempts for `<service-account>`. | Confirm workload access stays inside intended namespace boundaries. | TODO: record sanitized output after approved execution. |
| V010 | Failure condition for missing RBAC objects, excessive permissions, cluster-admin misuse, unrestricted secret access, or namespace boundary violation | Review validation findings against failure criteria. | Confirm unsafe RBAC patterns result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/kubernetes-rbac-summary.md`
- `configs/kubernetes-rbac-policy.md`
- `logs/kubernetes-rbac-validation.log`
- `screenshots/kubernetes-rbac-validation.png`
