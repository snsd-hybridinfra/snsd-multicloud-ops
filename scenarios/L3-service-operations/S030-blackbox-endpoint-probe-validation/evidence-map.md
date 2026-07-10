# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Blackbox Exporter service status validation plan | `commands.md`; `logs/blackbox-endpoint-probe-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Blackbox probe module existence validation plan | `commands.md`; `configs/blackbox-endpoint-probe-summary.md`; `validation.md` | command plan, probe summary, validation record | yes |
| Web endpoint probe success validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `logs/blackbox-endpoint-probe-validation.log`; `validation.md` | command plan, target mapping, validation log, validation record | yes |
| API endpoint probe success validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `logs/blackbox-endpoint-probe-validation.log`; `validation.md` | command plan, target mapping, validation log, validation record | yes |
| Ingress endpoint probe success validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `screenshots/blackbox-probe-result.png`; `validation.md` | command plan, target mapping, screenshot reference, validation record | yes |
| Reverse Proxy endpoint probe success validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `screenshots/blackbox-probe-result.png`; `validation.md` | command plan, target mapping, screenshot reference, validation record | yes |
| AWS endpoint placeholder probe validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| Azure endpoint placeholder probe validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| OpenStack endpoint placeholder probe validation plan | `commands.md`; `configs/blackbox-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| HTTP status code validation plan | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `validation.md` | command plan, query mapping, validation record | yes |
| Probe duration and latency validation plan | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `logs/blackbox-endpoint-probe-validation.log`; `validation.md` | command plan, query mapping, validation log, validation record | yes |
| Prometheus `probe_success` query validation plan | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `screenshots/prometheus-blackbox-query-result.png`; `validation.md` | command plan, query mapping, screenshot reference, validation record | yes |
| Prometheus `probe_http_status_code` query validation plan | `commands.md`; `configs/blackbox-prometheus-query-mapping.md`; `screenshots/prometheus-blackbox-query-result.png`; `validation.md` | command plan, query mapping, screenshot reference, validation record | yes |
| Failure condition for failed probe, HTTP 5xx, route timeout, DNS resolution failure, unexpected status code, excessive latency, or missing probe evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Blackbox Exporter or Prometheus query output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
