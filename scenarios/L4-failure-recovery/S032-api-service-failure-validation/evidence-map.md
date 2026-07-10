# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-failure API Deployment status validation plan | `commands.md`; `logs/api-service-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Pre-failure API Pod Ready status validation plan | `commands.md`; `screenshots/api-service-before-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Pre-failure API Service endpoint validation plan | `commands.md`; `configs/api-service-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| API failure injection plan | `commands.md`; `logs/api-service-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| API route failure response validation plan | `commands.md`; `screenshots/api-service-during-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| API health endpoint failure validation plan | `commands.md`; `logs/api-service-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Ingress API path failure validation plan | `commands.md`; `configs/api-service-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Blackbox API probe failure reference plan | `commands.md`; `configs/api-service-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| API workload restoration validation plan | `commands.md`; `logs/api-service-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| API health recovery validation plan | `commands.md`; `screenshots/api-service-after-recovery.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Recovery time measurement plan | `commands.md`; `configs/api-service-recovery-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Failure condition for API failure not detected, unexpected success during failure, API Pod stuck in CrashLoopBackOff, missing Service endpoint, HTTP 5xx persistence, or recovery threshold exceeded | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Kubernetes command output or API failure evidence has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
