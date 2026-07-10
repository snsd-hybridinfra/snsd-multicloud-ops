# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Prometheus service status validation plan | Plan service status review for Prometheus. | Prometheus service status can be reviewed. | `commands.md`, `logs/prometheus-target-discovery-validation.log`, `validation.md` |
| V002 | Prometheus configuration syntax validation plan | Plan configuration syntax or config check review. | Prometheus configuration can be validated before target checks. | `commands.md`, `configs/prometheus-target-discovery-summary.md`, `validation.md` |
| V003 | Prometheus /targets access validation plan | Plan access to `<prometheus-endpoint>` `/targets`. | `/targets` page can be reviewed and captured. | `commands.md`, `logs/prometheus-target-discovery-validation.log`, `screenshots/prometheus-targets-page.png`, `validation.md` |
| V004 | Node Exporter target UP validation plan | Review `<node-exporter-target>` state. | Node Exporter targets are discoverable and planned as UP. | `commands.md`, `configs/prometheus-scrape-target-mapping.md`, `validation.md` |
| V005 | kube-state-metrics target UP validation plan | Review `<kube-state-metrics-target>` state. | kube-state-metrics target is discoverable and planned as UP. | `commands.md`, `configs/prometheus-scrape-target-mapping.md`, `validation.md` |
| V006 | DB Exporter target UP validation plan | Review `<db-exporter-target>` state. | DB Exporter target is discoverable and planned as UP. | `commands.md`, `configs/prometheus-scrape-target-mapping.md`, `validation.md` |
| V007 | Blackbox Exporter target discovery validation plan | Review `<blackbox-exporter-target>` discovery placeholder. | Blackbox target mapping is discoverable as a placeholder. | `commands.md`, `configs/prometheus-scrape-target-mapping.md`, `validation.md` |
| V008 | AWS target placeholder validation plan | Review AWS service zone target placeholder. | AWS service targets are mapped with placeholder labels. | `commands.md`, `configs/prometheus-target-discovery-summary.md`, `validation.md` |
| V009 | Azure target placeholder validation plan | Review Azure service zone target placeholder. | Azure service targets are mapped with placeholder labels. | `commands.md`, `configs/prometheus-target-discovery-summary.md`, `validation.md` |
| V010 | OpenStack target placeholder validation plan | Review OpenStack service zone target placeholder. | OpenStack service targets are mapped with placeholder labels. | `commands.md`, `configs/prometheus-target-discovery-summary.md`, `validation.md` |
| V011 | On-Prem target placeholder validation plan | Review On-Prem Internal Server Zone target placeholder. | On-Prem targets are mapped with placeholder labels. | `commands.md`, `configs/prometheus-target-discovery-summary.md`, `validation.md` |
| V012 | Target label consistency validation plan | Review job names and labels across target categories. | Target labels and job names are consistent and non-duplicative. | `commands.md`, `configs/prometheus-scrape-target-mapping.md`, `validation.md` |
| V013 | Failure condition for missing target, DOWN target, invalid scrape config, duplicate target label, wrong job name, or missing evidence | Evaluate findings against explicit failure conditions. | Target discovery failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates target discovery only; Grafana dashboards are handled in S029 and blackbox endpoint probes in S030.
