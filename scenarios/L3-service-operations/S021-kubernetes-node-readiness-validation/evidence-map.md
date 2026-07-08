# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| kubectl client availability validation plan | `commands.md`; `logs/kubernetes-node-readiness-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Kubernetes context availability validation plan | `commands.md`; `configs/kubernetes-node-readiness-summary.md`; `validation.md` | command plan, readiness summary, validation record | yes |
| kubectl get nodes validation plan | `commands.md`; `logs/kubernetes-node-readiness-validation.log`; `screenshots/kubernetes-node-status.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| AWS Kubernetes/k3s node Ready status validation plan | `commands.md`; `configs/kubernetes-node-readiness-summary.md`; `validation.md` | command plan, readiness summary, validation record | yes |
| Azure Kubernetes/k3s node Ready status validation plan | `commands.md`; `configs/kubernetes-node-readiness-summary.md`; `validation.md` | command plan, readiness summary, validation record | yes |
| OpenStack Kubernetes/k3s node Ready status validation plan | `commands.md`; `configs/kubernetes-node-readiness-summary.md`; `validation.md` | command plan, readiness summary, validation record | yes |
| Node role and label validation plan | `commands.md`; `configs/kubernetes-node-role-label-summary.md`; `validation.md` | command plan, role and label summary, validation record | yes |
| Node condition validation plan | `commands.md`; `logs/kubernetes-node-readiness-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Node resource capacity validation plan | `commands.md`; `configs/kubernetes-node-readiness-summary.md`; `validation.md` | command plan, readiness summary, validation record | yes |
| Node version consistency validation plan | `commands.md`; `configs/kubernetes-node-readiness-summary.md`; `validation.md` | command plan, readiness summary, validation record | yes |
| Failure condition for missing node, NotReady node, unreachable cluster, invalid context, or inconsistent node role | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Kubernetes node readiness output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
