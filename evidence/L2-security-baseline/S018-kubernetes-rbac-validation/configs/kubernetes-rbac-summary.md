# Kubernetes RBAC Summary

- Scenario: S018-kubernetes-rbac-validation
- Generated: 2026-07-13T11:00:52+09:00
- Overall result: **PASS**
- Scope: local policy, matrix, manifest examples, and safety checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | RBAC baseline | PASS | Baseline document exists. |
| V002 | RBAC rule matrix | PASS | Rule matrix exists. |
| V003 | RBAC manifest directory | PASS | Manifest example directory exists. |
| V004 | Required manifest examples | PASS | All required example files exist. |
| V005 | Policy statements and subjects | PASS | Required least-privilege statements and four subject placeholders exist. |
| V006 | Namespace-scoped RBAC structure | PASS | Dedicated accounts, namespaced Roles/RoleBindings, example markers, and namespace scope are correct. |
| V007 | Cluster-wide privilege denial | PASS | No ClusterRoleBinding or cluster-admin binding exists. |
| V008 | Wildcard permission denial | PASS | No wildcard apiGroup, resource, or verb exists. |
| V009 | Application account restrictions | PASS | Application binding uses its dedicated account and receives no secrets access. |
| V010 | Default ServiceAccount denial | PASS | Default ServiceAccount is not used or approved for application workloads. |
| V011 | Monitoring read-only role | PASS | Monitoring Role uses get, list, and watch only. |
| V012 | Kubernetes credential files | PASS | No kubeconfig, service-account token, certificate, or private-key file exists. |
| V013 | Manifest sensitive-content safety | PASS | No Secret resource, token, certificate data, endpoint URL, or numeric address exists. |
| V014 | Execution safety boundary | PASS | The validator contains no kubectl, Helm, API, or network execution command. |

## Safety Boundary

This validation read repository files only. It did not run kubectl, read kubeconfig, connect to a cluster, query an API server, apply manifests, or access credentials.
