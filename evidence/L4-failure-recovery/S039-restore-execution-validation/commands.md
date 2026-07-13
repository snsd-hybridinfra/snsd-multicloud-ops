# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-restore-execution.ps1
Get-Content evidence/L4-failure-recovery/S039-restore-execution-validation/logs/restore-execution-validation.log
Get-Content evidence/L4-failure-recovery/S039-restore-execution-validation/configs/restore-execution-validation-summary.md
```

Real restore, SQL import, extraction, download, storage query, and Ansible actions are `NOT_RUN`. Future collection must use a separately approved disposable target and sanitized evidence only.
