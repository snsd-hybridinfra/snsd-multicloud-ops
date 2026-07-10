# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Web service HTTP response post-recovery validation plan | `commands.md`; `screenshots/service-health-after-recovery-web-api.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| API service HTTP response post-recovery validation plan | `commands.md`; `screenshots/service-health-after-recovery-web-api.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Ingress route post-recovery validation plan | `commands.md`; `logs/service-health-after-recovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Nginx Reverse Proxy post-recovery validation plan | `commands.md`; `logs/service-health-after-recovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Load balancing health endpoint post-recovery validation plan | `commands.md`; `configs/post-recovery-checklist.md`; `validation.md` | command plan, checklist, validation record | yes |
| MariaDB Primary availability reference validation plan | `commands.md`; `configs/service-health-after-recovery-summary.md`; `validation.md` | command plan, health summary, validation record | yes |
| MariaDB Replica state reference validation plan | `commands.md`; `configs/service-health-after-recovery-summary.md`; `validation.md` | command plan, health summary, validation record | yes |
| Prometheus target UP post-recovery validation plan | `commands.md`; `screenshots/service-health-after-recovery-monitoring.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Grafana dashboard visibility post-recovery validation plan | `commands.md`; `screenshots/service-health-after-recovery-monitoring.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Blackbox `probe_success` post-recovery validation plan | `commands.md`; `configs/post-recovery-checklist.md`; `validation.md` | command plan, checklist, validation record | yes |
| Final service recovery judgment validation plan | `commands.md`; `configs/post-recovery-judgment-model.md`; `screenshots/service-health-after-recovery-final-judgment.png`; `validation.md` | command plan, judgment model, screenshot reference, validation record | yes |
| Failure condition for Web/API unavailable, DB dependency unavailable, monitoring visibility missing, Blackbox probe failed, inconsistent recovery evidence, degraded state not documented, or missing final judgment | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real post-recovery service output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
