# Commands

Scenario: S026-mariadb-primary-replica-replication-validation
Level: L3-service-operations
Validation mode executed: StaticEvidence
Real database or lab collection: NOT_RUN

## Run Static Evidence Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-mariadb-primary-replica-replication.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence/L3-service-operations/S026-mariadb-primary-replica-replication-validation/logs/mariadb-primary-replica-replication-validation.log
Get-Content evidence/L3-service-operations/S026-mariadb-primary-replica-replication-validation/configs/mariadb-primary-replica-replication-summary.md
```

## Manual Lab Collection Boundary

In a separately approved lab, an authorized operator may manually run the SHOW/SELECT references in `runbooks/mariadb-replication-commands.example.md`. Do not commit client commands or credentials. Copy only the required status fields, replace every host/user/channel/binlog/position/GTID/database/environment value with an approved placeholder, verify no connection string remains, and then rerun StaticEvidence validation.

The validator itself never performs collection. The generated `.log` is ignored; committed samples and summary are sanitized evidence.
