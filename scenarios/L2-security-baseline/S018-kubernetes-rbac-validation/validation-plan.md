# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | RBAC baseline | Baseline exists. | generated log and summary |
| V002 | RBAC rule matrix | Matrix exists. | generated log and summary |
| V003 | RBAC manifest directory | Directory exists. | generated log and summary |
| V004 | Required manifest examples | All required files exist. | generated log and summary |
| V005 | Policy statements and subjects | Required controls and four subjects exist. | generated log and summary |
| V006 | Namespace-scoped RBAC structure | Kinds, markers, and namespace are correct. | generated log and summary |
| V007 | Cluster-wide privilege denial | No ClusterRoleBinding or cluster-admin. | generated log and summary |
| V008 | Wildcard permission denial | No wildcard permission. | generated log and summary |
| V009 | Application account restrictions | Dedicated account; no secrets access. | generated log and summary |
| V010 | Default ServiceAccount denial | No default application account use or approval. | generated log and summary |
| V011 | Monitoring read-only role | Only get, list, watch. | generated log and summary |
| V012 | Kubernetes credential files | No kubeconfig, token, certificate, or key file. | generated log and summary |
| V013 | Manifest sensitive-content safety | No Secret, token data, endpoint, or address. | generated log and summary |
| V014 | Execution safety boundary | No kubectl, Helm, API, or network command. | generated log and summary |

Every check maps by ID to `logs/kubernetes-rbac-validation.log` and `configs/kubernetes-rbac-summary.md`.
