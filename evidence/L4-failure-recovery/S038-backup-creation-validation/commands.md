# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-backup-creation.ps1
Get-Content evidence/L4-failure-recovery/S038-backup-creation-validation/logs/backup-creation-validation.log
Get-Content evidence/L4-failure-recovery/S038-backup-creation-validation/configs/backup-creation-validation-summary.md
```

Real backup, dump, archive, upload, storage query, and Ansible actions are `NOT_RUN`. Future collection must be separately approved and sanitized; no real artifact belongs in this repository.
