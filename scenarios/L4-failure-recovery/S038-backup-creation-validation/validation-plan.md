# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Backup directory structure validation plan | Review `<backup-root>` placeholder structure. | Backup destination structure is documented. | `commands.md`, `configs/backup-creation-summary.md`, `validation.md` |
| V002 | MariaDB backup creation placeholder validation plan | Plan logical backup invocation for `<db-backup-file>`. | MariaDB backup placeholder is documented without real dump content. | `commands.md`, `logs/backup-creation-validation.log`, `validation.md` |
| V003 | Kubernetes manifest backup placeholder validation plan | Plan manifest backup invocation for `<manifest-backup-file>`. | Kubernetes manifest backup placeholder is documented. | `commands.md`, `configs/backup-creation-summary.md`, `validation.md` |
| V004 | Nginx configuration backup placeholder validation plan | Plan Nginx config backup invocation for `<config-backup-file>`. | Nginx configuration backup placeholder is documented. | `commands.md`, `configs/backup-creation-summary.md`, `validation.md` |
| V005 | Observability configuration backup placeholder validation plan | Plan Prometheus/Grafana config backup placeholder. | Observability configuration backup placeholder is documented. | `commands.md`, `configs/backup-creation-summary.md`, `validation.md` |
| V006 | Backup file existence validation plan | Review expected backup file listing. | Backup files are expected to exist after approved execution. | `commands.md`, `screenshots/backup-file-list.png`, `validation.md` |
| V007 | Backup file size sanity validation plan | Review planned non-zero size check. | Backup files are expected to be non-zero and plausible. | `commands.md`, `screenshots/backup-file-list.png`, `validation.md` |
| V008 | Backup checksum generation validation plan | Plan checksum creation for `<checksum-file>`. | Checksum is created for each required backup artifact. | `commands.md`, `screenshots/backup-checksum-validation.png`, `validation.md` |
| V009 | Backup metadata capture validation plan | Review metadata fields for date, category, filename, size, and checksum. | Backup metadata is recorded and reviewable. | `commands.md`, `configs/backup-creation-summary.md`, `validation.md` |
| V010 | Backup log capture validation plan | Review backup command or runbook log capture. | Backup logs are recorded. | `commands.md`, `logs/backup-creation-validation.log`, `validation.md` |
| V011 | Backup retention placeholder validation plan | Review retention placeholder documentation. | Retention placeholder is documented without claiming enterprise retention. | `commands.md`, `configs/backup-retention-placeholder.md`, `validation.md` |
| V012 | Failure condition for missing backup file, zero-size backup, missing checksum, missing metadata, backup command failure, sensitive data exposure, or missing evidence | Evaluate findings against explicit failure conditions. | Backup creation issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates backup creation only; restore execution is handled in S039 and post-recovery service health is handled in S040.
