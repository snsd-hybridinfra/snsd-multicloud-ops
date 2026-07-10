# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Grafana service access validation plan | `commands.md`; `logs/grafana-dashboard-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Grafana login requirement reference validation plan | `commands.md`; `configs/grafana-dashboard-summary.md`; `validation.md` | command plan, dashboard summary, validation record | yes |
| Prometheus datasource existence validation plan | `commands.md`; `configs/grafana-datasource-mapping.md`; `validation.md` | command plan, datasource mapping, validation record | yes |
| Prometheus datasource connection validation plan | `commands.md`; `configs/grafana-datasource-mapping.md`; `screenshots/grafana-datasource-status.png`; `validation.md` | command plan, datasource mapping, screenshot reference, validation record | yes |
| Infrastructure dashboard placeholder validation plan | `commands.md`; `configs/grafana-dashboard-summary.md`; `validation.md` | command plan, dashboard summary, validation record | yes |
| Kubernetes dashboard placeholder validation plan | `commands.md`; `configs/grafana-dashboard-summary.md`; `validation.md` | command plan, dashboard summary, validation record | yes |
| MariaDB dashboard placeholder validation plan | `commands.md`; `configs/grafana-dashboard-summary.md`; `validation.md` | command plan, dashboard summary, validation record | yes |
| Blackbox endpoint dashboard placeholder validation plan | `commands.md`; `configs/grafana-dashboard-summary.md`; `validation.md` | command plan, dashboard summary, validation record | yes |
| Multi-cloud service status dashboard placeholder validation plan | `commands.md`; `configs/grafana-dashboard-summary.md`; `validation.md` | command plan, dashboard summary, validation record | yes |
| Dashboard panel data rendering validation plan | `commands.md`; `configs/grafana-panel-mapping.md`; `logs/grafana-dashboard-validation.log`; `validation.md` | command plan, panel mapping, validation log, validation record | yes |
| Dashboard screenshot capture plan | `commands.md`; `screenshots/grafana-dashboard-overview.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Failure condition for missing datasource, datasource query failure, empty dashboard, broken panel, no time-series data, missing dashboard screenshot, or anonymous dashboard exposure | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Grafana dashboard output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
