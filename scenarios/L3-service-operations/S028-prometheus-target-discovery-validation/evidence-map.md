# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Prometheus service status validation plan | `commands.md`; `logs/prometheus-target-discovery-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Prometheus configuration syntax validation plan | `commands.md`; `configs/prometheus-target-discovery-summary.md`; `validation.md` | command plan, discovery summary, validation record | yes |
| Prometheus /targets access validation plan | `commands.md`; `logs/prometheus-target-discovery-validation.log`; `screenshots/prometheus-targets-page.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Node Exporter target UP validation plan | `commands.md`; `configs/prometheus-scrape-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| kube-state-metrics target UP validation plan | `commands.md`; `configs/prometheus-scrape-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| DB Exporter target UP validation plan | `commands.md`; `configs/prometheus-scrape-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| Blackbox Exporter target discovery validation plan | `commands.md`; `configs/prometheus-scrape-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| AWS target placeholder validation plan | `commands.md`; `configs/prometheus-target-discovery-summary.md`; `validation.md` | command plan, discovery summary, validation record | yes |
| Azure target placeholder validation plan | `commands.md`; `configs/prometheus-target-discovery-summary.md`; `validation.md` | command plan, discovery summary, validation record | yes |
| OpenStack target placeholder validation plan | `commands.md`; `configs/prometheus-target-discovery-summary.md`; `validation.md` | command plan, discovery summary, validation record | yes |
| On-Prem target placeholder validation plan | `commands.md`; `configs/prometheus-target-discovery-summary.md`; `validation.md` | command plan, discovery summary, validation record | yes |
| Target label consistency validation plan | `commands.md`; `configs/prometheus-scrape-target-mapping.md`; `validation.md` | command plan, target mapping, validation record | yes |
| Failure condition for missing target, DOWN target, invalid scrape config, duplicate target label, wrong job name, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Prometheus target discovery output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
