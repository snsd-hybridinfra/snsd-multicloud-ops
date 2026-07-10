# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Backup directory structure validation plan | `commands.md`; `configs/backup-creation-summary.md`; `validation.md` | command plan, backup summary, validation record | yes |
| MariaDB backup creation placeholder validation plan | `commands.md`; `logs/backup-creation-validation.log`; `validation.md` | command plan, backup log, validation record | yes |
| Kubernetes manifest backup placeholder validation plan | `commands.md`; `configs/backup-creation-summary.md`; `validation.md` | command plan, backup summary, validation record | yes |
| Nginx configuration backup placeholder validation plan | `commands.md`; `configs/backup-creation-summary.md`; `validation.md` | command plan, backup summary, validation record | yes |
| Observability configuration backup placeholder validation plan | `commands.md`; `configs/backup-creation-summary.md`; `validation.md` | command plan, backup summary, validation record | yes |
| Backup file existence validation plan | `commands.md`; `screenshots/backup-file-list.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Backup file size sanity validation plan | `commands.md`; `screenshots/backup-file-list.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Backup checksum generation validation plan | `commands.md`; `screenshots/backup-checksum-validation.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Backup metadata capture validation plan | `commands.md`; `configs/backup-creation-summary.md`; `validation.md` | command plan, backup summary, validation record | yes |
| Backup log capture validation plan | `commands.md`; `logs/backup-creation-validation.log`; `validation.md` | command plan, backup log, validation record | yes |
| Backup retention placeholder validation plan | `commands.md`; `configs/backup-retention-placeholder.md`; `validation.md` | command plan, retention placeholder, validation record | yes |
| Failure condition for missing backup file, zero-size backup, missing checksum, missing metadata, backup command failure, sensitive data exposure, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real backup output, database dump, archive, checksum, or backup log has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
