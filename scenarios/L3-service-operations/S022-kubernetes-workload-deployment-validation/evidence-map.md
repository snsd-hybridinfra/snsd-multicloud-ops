# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Namespace existence validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| Web Deployment existence validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| API Deployment existence validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| Deployment rollout status validation plan | `commands.md`; `logs/kubernetes-workload-deployment-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Pod Running and Ready status validation plan | `commands.md`; `logs/kubernetes-workload-deployment-validation.log`; `screenshots/kubernetes-workload-status.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Replica availability validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| Kubernetes Service existence validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| ConfigMap reference validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| Secret template reference validation plan | `commands.md`; `configs/kubernetes-workload-summary.md`; `validation.md` | command plan, workload summary, validation record | yes |
| Resource requests and limits validation plan | `commands.md`; `configs/kubernetes-resource-policy-summary.md`; `validation.md` | command plan, resource policy summary, validation record | yes |
| Image tag not latest validation plan | `commands.md`; `configs/kubernetes-resource-policy-summary.md`; `validation.md` | command plan, resource policy summary, validation record | yes |
| Failure condition for missing namespace, failed rollout, CrashLoopBackOff, ImagePullBackOff, missing service, missing config reference, or missing resource limits | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Kubernetes workload deployment output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
