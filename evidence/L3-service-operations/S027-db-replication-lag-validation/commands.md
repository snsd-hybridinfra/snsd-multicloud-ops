# Commands

Scenario: S027-db-replication-lag-validation
Level: L3-service-operations
Validation mode executed: StaticEvidence
Real database/Prometheus/Grafana collection: NOT_RUN

## Run Static Evidence Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-db-replication-lag.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence/L3-service-operations/S027-db-replication-lag-validation/logs/db-replication-lag-validation.log
Get-Content evidence/L3-service-operations/S027-db-replication-lag-validation/configs/db-replication-lag-summary.md
```

## Manual Lab Collection Boundary

An authorized operator may separately collect only the required lag/thread/error fields in an approved lab. Do not commit client commands or credentials. Replace hosts, users, channels, database names, binary-log/GTID values, labels, endpoints, and environment identifiers with approved placeholders before review. The S027 validator itself never collects data or queries MariaDB, Prometheus, or Grafana.

The generated `.log` is ignored; the summary and sanitized fixtures are committed evidence.
