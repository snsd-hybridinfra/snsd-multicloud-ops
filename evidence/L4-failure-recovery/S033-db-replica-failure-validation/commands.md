# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-db-replica-failure.ps1
Get-Content evidence/L4-failure-recovery/S033-db-replica-failure-validation/logs/db-replica-failure-validation.log
Get-Content evidence/L4-failure-recovery/S033-db-replica-failure-validation/configs/db-replica-failure-summary.md
```

Database connection, SQL, service stop/start, replication change, Ansible execution, Prometheus/Grafana query, and network access are `NOT_RUN`. Stop/start commands are manual disposable-lab references only.
