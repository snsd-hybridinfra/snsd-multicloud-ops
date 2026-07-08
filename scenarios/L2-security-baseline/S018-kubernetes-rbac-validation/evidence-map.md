# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Namespace existence validation plan | `commands.md`; `configs/kubernetes-rbac-summary.md`; `validation.md` | command plan, RBAC summary, validation record | yes |
| ServiceAccount existence validation plan | `commands.md`; `configs/kubernetes-rbac-summary.md`; `validation.md` | command plan, RBAC summary, validation record | yes |
| Role existence validation plan | `commands.md`; `configs/kubernetes-rbac-policy.md`; `validation.md` | command plan, RBAC policy, validation record | yes |
| RoleBinding existence validation plan | `commands.md`; `configs/kubernetes-rbac-policy.md`; `validation.md` | command plan, RBAC policy, validation record | yes |
| kubectl auth can-i allowed action validation plan | `commands.md`; `logs/kubernetes-rbac-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| kubectl auth can-i denied action validation plan | `commands.md`; `logs/kubernetes-rbac-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| No unnecessary cluster-admin binding validation plan | `commands.md`; `configs/kubernetes-rbac-policy.md`; `validation.md` | command plan, RBAC policy, validation record | yes |
| Secret read permission restriction validation plan | `commands.md`; `configs/kubernetes-rbac-policy.md`; `validation.md` | command plan, RBAC policy, validation record | yes |
| Workload namespace boundary validation plan | `commands.md`; `logs/kubernetes-rbac-validation.log`; `screenshots/kubernetes-rbac-validation.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Failure condition for missing RBAC objects, excessive permissions, cluster-admin misuse, unrestricted secret access, or namespace boundary violation | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Kubernetes RBAC output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
