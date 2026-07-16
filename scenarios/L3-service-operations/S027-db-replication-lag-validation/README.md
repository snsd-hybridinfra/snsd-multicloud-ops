# S027-db-replication-lag-validation

| Field | Value |
|---|---|
| Scenario ID | S027 |
| Scenario Name | DB Replication Lag Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Static lag-threshold evidence classification |
| Related Components | MariaDB replica fields, lag thresholds, metric placeholders |
| Validation Type | StaticEvidence |
| Evidence Directory | evidence/L3-service-operations/S027-db-replication-lag-validation/ |
| Status | NOT_STARTED |

## Objective Summary

Validate the replication-lag threshold model and safely classify sanitized normal, warning, critical, and NULL fixtures.

## Scope Summary

StaticEvidence mode parses committed files only. It performs no MariaDB, Prometheus, or Grafana query and makes no network request.

## Validation Summary

Sixteen checks cover artifacts, thresholds, metrics, four fixture classifications, thread/error parsing, terminology, credential/dump/observability/address safety, and execution boundaries.

## Evidence Output Summary

The warning fixture intentionally produces WARN. Critical and NULL files are negative fixtures whose unsafe states must be detected; they do not represent a healthy deployment or a live incident.
