# Commands

Scenario: S028-prometheus-target-discovery-validation
Level: L3-service-operations
Capability: Prometheus Target Discovery Validation
Target: `<prometheus-endpoint>`
Execution timestamp: TODO

Record sanitized output only. Do not include credentials, secrets, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Prometheus service status validation plan | Plan service status review for Prometheus. | Confirm Prometheus service status can be reviewed. | TODO: record sanitized output after approved execution. |
| V002 | Prometheus configuration syntax validation plan | Plan syntax or config validation review. | Confirm Prometheus configuration can be validated. | TODO: record sanitized output after approved execution. |
| V003 | Prometheus /targets access validation plan | Plan access to `<prometheus-endpoint>` `/targets`. | Confirm targets page can be reviewed. | TODO: record sanitized output after approved execution. |
| V004 | Node Exporter target UP validation plan | Review `<node-exporter-target>` state. | Confirm Node Exporter target discovery is planned. | TODO: record sanitized output after approved execution. |
| V005 | kube-state-metrics target UP validation plan | Review `<kube-state-metrics-target>` state. | Confirm kube-state-metrics target discovery is planned. | TODO: record sanitized output after approved execution. |
| V006 | DB Exporter target UP validation plan | Review `<db-exporter-target>` state. | Confirm DB Exporter target discovery is planned. | TODO: record sanitized output after approved execution. |
| V007 | Blackbox Exporter target discovery validation plan | Review `<blackbox-exporter-target>` placeholder discovery. | Confirm Blackbox target mapping is planned. | TODO: record sanitized output after approved execution. |
| V008 | AWS target placeholder validation plan | Review AWS service zone target placeholder. | Confirm AWS target mapping is documented. | TODO: record sanitized output after approved execution. |
| V009 | Azure target placeholder validation plan | Review Azure service zone target placeholder. | Confirm Azure target mapping is documented. | TODO: record sanitized output after approved execution. |
| V010 | OpenStack target placeholder validation plan | Review OpenStack service zone target placeholder. | Confirm OpenStack target mapping is documented. | TODO: record sanitized output after approved execution. |
| V011 | On-Prem target placeholder validation plan | Review On-Prem Internal Server Zone target placeholder. | Confirm On-Prem target mapping is documented. | TODO: record sanitized output after approved execution. |
| V012 | Target label consistency validation plan | Review planned job names and labels across target categories. | Confirm labels and job names are consistent. | TODO: record sanitized output after approved execution. |
| V013 | Failure condition for missing target, DOWN target, invalid scrape config, duplicate target label, wrong job name, or missing evidence | Review validation findings against failure criteria. | Confirm target discovery failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/prometheus-target-discovery-summary.md`
- `configs/prometheus-scrape-target-mapping.md`
- `logs/prometheus-target-discovery-validation.log`
- `screenshots/prometheus-targets-page.png`
