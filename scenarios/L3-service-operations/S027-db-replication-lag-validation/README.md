# S027-db-replication-lag-validation

| Field | Value |
|---|---|
| Scenario ID | S027 |
| Scenario Name | DB Replication Lag Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Database replication monitoring |
| Related Components | db-primary-01, db-replica-01, db-replica-02, replication status, lag thresholds, DB exporter metric placeholder |
| Validation Type | Service Operation Validation |
| Evidence Directory | evidence/L3-service-operations/S027-db-replication-lag-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate MariaDB replication lag measurement for the On-Prem Internal Server Zone Primary-Replica database layer.

## Scope Summary

This scenario validates replication lag only. It covers replica lag measurement, `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` lag fields, primary timestamp write placeholders, replica read delay checks, provisional lag thresholds, lag evidence collection, DB exporter metric mapping placeholders, and Prometheus metric integration placeholders.

## Validation Summary

Validation checks confirm that replica lag can be measured for `db-replica-01` and `db-replica-02`, compared against provisional NORMAL/WARNING/CRITICAL thresholds, and mapped to future metric evidence without installing exporters or configuring Prometheus in this scenario.

## Evidence Output Summary

Evidence must be recorded under `evidence/L3-service-operations/S027-db-replication-lag-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
