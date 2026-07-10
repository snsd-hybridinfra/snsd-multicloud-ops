# Validation

Scenario: S028-prometheus-target-discovery-validation
Level: L3-service-operations
Capability: Prometheus Target Discovery Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Prometheus target discovery output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Prometheus service status validation plan | Prometheus service status can be reviewed. | TODO | NOT_RUN | `commands.md`; `logs/prometheus-target-discovery-validation.log` |
| V002 | Prometheus configuration syntax validation plan | Prometheus configuration can be validated before target checks. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-discovery-summary.md` |
| V003 | Prometheus /targets access validation plan | `/targets` page can be reviewed and captured. | TODO | NOT_RUN | `commands.md`; `logs/prometheus-target-discovery-validation.log`; `screenshots/prometheus-targets-page.png` |
| V004 | Node Exporter target UP validation plan | Node Exporter targets are discoverable and planned as UP. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-scrape-target-mapping.md` |
| V005 | kube-state-metrics target UP validation plan | kube-state-metrics target is discoverable and planned as UP. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-scrape-target-mapping.md` |
| V006 | DB Exporter target UP validation plan | DB Exporter target is discoverable and planned as UP. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-scrape-target-mapping.md` |
| V007 | Blackbox Exporter target discovery validation plan | Blackbox target mapping is discoverable as a placeholder. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-scrape-target-mapping.md` |
| V008 | AWS target placeholder validation plan | AWS service targets are mapped with placeholder labels. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-discovery-summary.md` |
| V009 | Azure target placeholder validation plan | Azure service targets are mapped with placeholder labels. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-discovery-summary.md` |
| V010 | OpenStack target placeholder validation plan | OpenStack service targets are mapped with placeholder labels. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-discovery-summary.md` |
| V011 | On-Prem target placeholder validation plan | On-Prem targets are mapped with placeholder labels. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-discovery-summary.md` |
| V012 | Target label consistency validation plan | Target labels and job names are consistent and non-duplicative. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-scrape-target-mapping.md` |
| V013 | Failure condition for missing target, DOWN target, invalid scrape config, duplicate target label, wrong job name, or missing evidence | Target discovery failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Prometheus target discovery summary is captured: NOT_READY
- Prometheus scrape target mapping is captured: NOT_READY
- Prometheus target discovery validation log is captured: NOT_READY
- Prometheus targets page screenshot is captured: NOT_READY

## Notes

This scenario validates Prometheus target discovery only. Grafana dashboard validation is handled in S029, Blackbox endpoint probe validation in S030, and DB replication lag validation in S027. Prometheus alerting and Alertmanager integration are excluded unless later documented separately.
