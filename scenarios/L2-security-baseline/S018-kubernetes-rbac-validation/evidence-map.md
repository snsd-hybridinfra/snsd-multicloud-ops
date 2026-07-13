# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | RBAC baseline | `logs/kubernetes-rbac-validation.log`; `configs/kubernetes-rbac-summary.md` | yes |
| V002 | RBAC rule matrix | same generated evidence | yes |
| V003 | RBAC manifest directory | same generated evidence | yes |
| V004 | Required manifest examples | same generated evidence | yes |
| V005 | Policy statements and subjects | same generated evidence | yes |
| V006 | Namespace-scoped RBAC structure | same generated evidence | yes |
| V007 | Cluster-wide privilege denial | same generated evidence | yes |
| V008 | Wildcard permission denial | same generated evidence | yes |
| V009 | Application account restrictions | same generated evidence | yes |
| V010 | Default ServiceAccount denial | same generated evidence | yes |
| V011 | Monitoring read-only role | same generated evidence | yes |
| V012 | Kubernetes credential files | same generated evidence | yes |
| V013 | Manifest sensitive-content safety | same generated evidence | yes |
| V014 | Execution safety boundary | same generated evidence | yes |

`commands.md` documents execution and `validation.md` records final results. The generated log is ignored; the sanitized summary is tracked.
