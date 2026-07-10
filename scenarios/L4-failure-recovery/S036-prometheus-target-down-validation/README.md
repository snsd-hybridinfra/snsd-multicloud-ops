# S036-prometheus-target-down-validation

| Field | Value |
|---|---|
| Scenario ID | S036 |
| Scenario Name | Prometheus Target DOWN Validation |
| Level | L4 Failure and Recovery Validation |
| Category | Failure Recovery |
| Primary Domain | Prometheus target state detection |
| Related Components | Prometheus, `/targets` page, `up` query, Node Exporter, DB Exporter, Blackbox Exporter, kube-state-metrics, cloud and on-prem target placeholders |
| Validation Type | Failure Recovery Validation |
| Evidence Directory | evidence/L4-failure-recovery/S036-prometheus-target-down-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate Prometheus target DOWN detection behavior for the SNSD Multi-Cloud Ops observability layer.

## Scope Summary

This scenario validates Prometheus target DOWN detection only. It covers pre-failure Prometheus service and target UP state, placeholder exporter or endpoint outage injection, `/targets` DOWN evidence, query-based `up{job="<target-job>"}` evidence, target failure timestamp capture, exporter restoration, post-recovery target UP state, and detection/recovery timing.

## Validation Summary

Validation checks confirm that a target starts UP, a single target failure is planned, Prometheus detects the target as DOWN through target state and query evidence, the target returns to UP after restoration, timing is measured, and failures such as missing detection, invalid scrape config, missing labels, persistent DOWN state, recovery threshold breach, or missing evidence are captured.

## Evidence Output Summary

Evidence must be recorded under `evidence/L4-failure-recovery/S036-prometheus-target-down-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
