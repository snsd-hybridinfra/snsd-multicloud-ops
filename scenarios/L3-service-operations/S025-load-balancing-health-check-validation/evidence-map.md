# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Kubernetes Service endpoint health validation plan | `commands.md`; `configs/backend-endpoint-health-summary.md`; `validation.md` | command plan, backend health summary, validation record | yes |
| Ingress backend endpoint health validation plan | `commands.md`; `configs/load-balancing-health-check-summary.md`; `validation.md` | command plan, health check summary, validation record | yes |
| Nginx upstream health validation plan | `commands.md`; `configs/load-balancing-health-check-summary.md`; `validation.md` | command plan, health check summary, validation record | yes |
| AWS service entrypoint health check plan | `commands.md`; `configs/load-balancing-health-check-summary.md`; `validation.md` | command plan, health check summary, validation record | yes |
| Azure service entrypoint health check plan | `commands.md`; `configs/load-balancing-health-check-summary.md`; `validation.md` | command plan, health check summary, validation record | yes |
| OpenStack service entrypoint health check plan | `commands.md`; `configs/load-balancing-health-check-summary.md`; `validation.md` | command plan, health check summary, validation record | yes |
| HTTP /health endpoint response validation plan | `commands.md`; `logs/load-balancing-health-check-validation.log`; `screenshots/load-balancing-health-check-test.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Backend unavailable detection plan | `commands.md`; `logs/load-balancing-health-check-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Traffic continuity validation plan with one backend unavailable | `commands.md`; `logs/load-balancing-health-check-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Health check log capture plan | `commands.md`; `logs/load-balancing-health-check-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failure condition for all backends unhealthy, health endpoint missing, HTTP 5xx, route timeout, stale endpoint, or no health evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real load balancing health check output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
