# S018-kubernetes-rbac-validation

| Field | Value |
|---|---|
| Scenario ID | S018 |
| Scenario Name | Kubernetes RBAC Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Related Components | RBAC policy, rule matrix, namespace-scoped example manifests, local validator |
| Validation Type | Safe local repository validation |
| Evidence Directory | `evidence/L2-security-baseline/S018-kubernetes-rbac-validation/` |
| Status | NOT_STARTED |

## Objective Summary

Validate namespace-scoped Kubernetes RBAC least privilege without connecting to a cluster, running kubectl, applying manifests, or storing cluster credentials.

## Scope Summary

S018 inspects repository policy, a rule matrix, and non-production RBAC examples only. It validates dedicated ServiceAccounts, limited Roles, RoleBindings, and prohibited cluster-wide or secret permissions.

## Validation Summary

Fourteen checks validate files, policy subjects, resource kinds, namespace scope, cluster-wide privilege denial, wildcard denial, application and monitoring controls, credential-file absence, sensitive content, and execution safety.

## Evidence Output Summary

The validator writes an ignored execution log and a tracked sanitized Markdown summary under the S018 evidence directory.
