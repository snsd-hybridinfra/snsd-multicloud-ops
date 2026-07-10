# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Grafana service access validation plan | Plan access check for `<grafana-endpoint>`. | Grafana service access can be reviewed through an approved path. | `commands.md`, `logs/grafana-dashboard-validation.log`, `validation.md` |
| V002 | Grafana login requirement reference validation plan | Reference S020 login requirement evidence. | Dashboard validation assumes authenticated access only. | `commands.md`, `configs/grafana-dashboard-summary.md`, `validation.md` |
| V003 | Prometheus datasource existence validation plan | Review datasource placeholder `<prometheus-datasource>`. | Prometheus datasource is identifiable by placeholder name. | `commands.md`, `configs/grafana-datasource-mapping.md`, `validation.md` |
| V004 | Prometheus datasource connection validation plan | Plan datasource connection status review. | Prometheus datasource connection is successful. | `commands.md`, `configs/grafana-datasource-mapping.md`, `screenshots/grafana-datasource-status.png`, `validation.md` |
| V005 | Infrastructure dashboard placeholder validation plan | Map On-Prem and infrastructure dashboard placeholders. | Infrastructure dashboard placeholder is documented. | `commands.md`, `configs/grafana-dashboard-summary.md`, `validation.md` |
| V006 | Kubernetes dashboard placeholder validation plan | Map Kubernetes/k3s node and workload dashboard placeholders. | Kubernetes dashboard placeholder is documented. | `commands.md`, `configs/grafana-dashboard-summary.md`, `validation.md` |
| V007 | MariaDB dashboard placeholder validation plan | Map MariaDB replication and availability dashboard placeholders. | MariaDB dashboard placeholder is documented. | `commands.md`, `configs/grafana-dashboard-summary.md`, `validation.md` |
| V008 | Blackbox endpoint dashboard placeholder validation plan | Map Blackbox HTTP endpoint dashboard placeholders. | Blackbox endpoint dashboard placeholder is documented. | `commands.md`, `configs/grafana-dashboard-summary.md`, `validation.md` |
| V009 | Multi-cloud service status dashboard placeholder validation plan | Map AWS, Azure, OpenStack, and service health summary placeholders. | Multi-cloud service status dashboard placeholder is documented. | `commands.md`, `configs/grafana-dashboard-summary.md`, `validation.md` |
| V010 | Dashboard panel data rendering validation plan | Review `<panel-name>` data rendering for selected time range. | Panels render non-empty time-series or status data. | `commands.md`, `configs/grafana-panel-mapping.md`, `logs/grafana-dashboard-validation.log`, `validation.md` |
| V011 | Dashboard screenshot capture plan | Capture sanitized dashboard overview evidence. | Dashboard screenshot evidence is available and sanitized. | `commands.md`, `screenshots/grafana-dashboard-overview.png`, `validation.md` |
| V012 | Failure condition for missing datasource, datasource query failure, empty dashboard, broken panel, no time-series data, missing dashboard screenshot, or anonymous dashboard exposure | Evaluate findings against explicit failure conditions. | Dashboard validation failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates dashboard visibility and datasource rendering only; anonymous access denial is handled in S020, target discovery in S028, and blackbox endpoint probes in S030.
