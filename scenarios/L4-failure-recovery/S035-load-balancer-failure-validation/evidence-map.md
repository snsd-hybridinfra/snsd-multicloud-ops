# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-failure load balancer endpoint validation plan | `commands.md`; `screenshots/load-balancer-before-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Pre-failure backend health validation plan | `commands.md`; `configs/load-balancer-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Pre-failure Ingress route validation reference plan | `commands.md`; `configs/load-balancer-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Load balancer failure injection plan | `commands.md`; `logs/load-balancer-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Endpoint failure detection validation plan | `commands.md`; `screenshots/load-balancer-during-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Health check failure validation plan | `commands.md`; `logs/load-balancer-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Blackbox probe failure reference validation plan | `commands.md`; `configs/load-balancer-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Backend service health during frontend failure validation plan | `commands.md`; `configs/load-balancer-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Manual recovery decision point validation plan | `commands.md`; `configs/load-balancer-decision-points.md`; `validation.md` | command plan, decision point summary, validation record | yes |
| Load balancer restoration validation plan | `commands.md`; `logs/load-balancer-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Post-recovery HTTP response validation plan | `commands.md`; `screenshots/load-balancer-after-recovery.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Recovery time measurement plan | `commands.md`; `configs/load-balancer-recovery-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Failure condition for load balancer failure not detected, wrong backend diagnosis, all endpoints unavailable, backend health unknown, recovery procedure unclear, recovery threshold exceeded, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real load balancer, Nginx, Ingress, or Blackbox output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
