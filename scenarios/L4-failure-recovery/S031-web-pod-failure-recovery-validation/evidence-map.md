# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-failure Web Deployment status validation plan | `commands.md`; `logs/web-pod-failure-recovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Pre-failure Web Pod Ready status validation plan | `commands.md`; `screenshots/web-pod-before-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Pre-failure Service endpoint validation plan | `commands.md`; `configs/web-pod-failure-recovery-summary.md`; `validation.md` | command plan, recovery summary, validation record | yes |
| Web Pod delete failure injection plan | `commands.md`; `logs/web-pod-failure-recovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replacement Pod creation validation plan | `commands.md`; `logs/web-pod-failure-recovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Web Pod Ready recovery validation plan | `commands.md`; `screenshots/web-pod-after-recovery.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Service endpoint recovery validation plan | `commands.md`; `configs/web-pod-failure-recovery-summary.md`; `validation.md` | command plan, recovery summary, validation record | yes |
| HTTP health endpoint recovery validation plan | `commands.md`; `logs/web-pod-failure-recovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Recovery time measurement plan | `commands.md`; `configs/web-pod-recovery-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Post-recovery workload status validation plan | `commands.md`; `logs/web-pod-failure-recovery-validation.log`; `screenshots/web-pod-after-recovery.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Failure condition for no replacement Pod, Pod stuck in Pending or CrashLoopBackOff, Service endpoint missing, HTTP recovery failure, or recovery threshold exceeded | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Kubernetes command output or failure injection evidence has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
