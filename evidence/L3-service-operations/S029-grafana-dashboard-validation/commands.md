# Commands

Scenario: S029-grafana-dashboard-validation
Level: L3-service-operations
Capability: Grafana Dashboard Validation
Target: `<grafana-endpoint>`
Execution timestamp: TODO

Record sanitized output only. Do not include Grafana passwords, credentials, secrets, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Grafana service access validation plan | Plan access check for `<grafana-endpoint>`. | Confirm Grafana service access can be reviewed. | TODO: record sanitized output after approved execution. |
| V002 | Grafana login requirement reference validation plan | Reference S020 login requirement evidence. | Confirm dashboard validation assumes authenticated access. | TODO: record sanitized output after approved execution. |
| V003 | Prometheus datasource existence validation plan | Review placeholder datasource `<prometheus-datasource>`. | Confirm datasource placeholder exists. | TODO: record sanitized output after approved execution. |
| V004 | Prometheus datasource connection validation plan | Review datasource connection status. | Confirm datasource connection is successful. | TODO: record sanitized output after approved execution. |
| V005 | Infrastructure dashboard placeholder validation plan | Review infrastructure dashboard placeholder mapping. | Confirm infrastructure dashboard category is mapped. | TODO: record sanitized output after approved execution. |
| V006 | Kubernetes dashboard placeholder validation plan | Review Kubernetes dashboard placeholder mapping. | Confirm Kubernetes dashboard category is mapped. | TODO: record sanitized output after approved execution. |
| V007 | MariaDB dashboard placeholder validation plan | Review MariaDB dashboard placeholder mapping. | Confirm MariaDB dashboard category is mapped. | TODO: record sanitized output after approved execution. |
| V008 | Blackbox endpoint dashboard placeholder validation plan | Review Blackbox endpoint dashboard placeholder mapping. | Confirm Blackbox dashboard category is mapped. | TODO: record sanitized output after approved execution. |
| V009 | Multi-cloud service status dashboard placeholder validation plan | Review `<service-health-dashboard>` mapping. | Confirm multi-cloud service status dashboard is mapped. | TODO: record sanitized output after approved execution. |
| V010 | Dashboard panel data rendering validation plan | Review `<panel-name>` rendering for selected time range. | Confirm panels render expected data. | TODO: record sanitized output after approved execution. |
| V011 | Dashboard screenshot capture plan | Capture sanitized dashboard and datasource screenshots. | Confirm screenshot evidence is available. | TODO: record sanitized output after approved execution. |
| V012 | Failure condition for missing datasource, datasource query failure, empty dashboard, broken panel, no time-series data, missing dashboard screenshot, or anonymous dashboard exposure | Review validation findings against failure criteria. | Confirm dashboard failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/grafana-dashboard-summary.md`
- `configs/grafana-datasource-mapping.md`
- `configs/grafana-panel-mapping.md`
- `logs/grafana-dashboard-validation.log`
- `screenshots/grafana-dashboard-overview.png`
- `screenshots/grafana-datasource-status.png`
