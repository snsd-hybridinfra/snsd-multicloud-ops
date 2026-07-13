# S036-prometheus-target-down-validation

| Field | Value |
|---|---|
| Scenario ID | S036 |
| Scenario Name | Prometheus Target Down Validation |
| Level | L4 Failure Recovery Validation |
| Category | Failure Recovery |
| Related Components | Prometheus targets API, up metric, exporter, alert rule, recovery state |
| Validation Type | Static with optional explicit read-only LivePrometheus |
| Evidence Directory | evidence/L4-failure-recovery/S036-prometheus-target-down-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate target DOWN/up=0 detection, alert firing, manual recovery, target UP/up=1, and alert clearing without modifying Prometheus or exporters.

## Scope Summary

Static mode parses local samples. LivePrometheus requires an explicit URL and performs read-only API queries; committed output stores no URL or raw response.

## Validation Summary

Eighteen checks cover artifacts, workflow, alert/criteria/response definitions, pre/down/alert/recovery/post evidence, timing, sensitive content, execution safety, and optional live state.

## Evidence Output Summary

Committed JSON is non-production and symbolic; generated evidence contains judgments only.
