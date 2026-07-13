# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-db-primary-stop-runbook.ps1
Get-Content evidence/L4-failure-recovery/S034-db-primary-stop-runbook-validation/logs/db-primary-stop-runbook-validation.log
Get-Content evidence/L4-failure-recovery/S034-db-primary-stop-runbook-validation/configs/db-primary-stop-runbook-summary.md
```

Database/SQL, service stop/start, promotion/failover, replication changes, Ansible, monitoring, and network actions are `NOT_RUN`. Stop/start references are manual disposable-lab-only.
