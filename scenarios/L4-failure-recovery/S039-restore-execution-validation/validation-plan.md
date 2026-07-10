# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Backup artifact selection validation plan | Review selected artifact from `<backup-root>`. | Restore artifact is identified and mapped to the restore target. | `commands.md`, `configs/restore-artifact-selection.md`, `screenshots/restore-artifact-selection.png`, `validation.md` |
| V002 | Backup checksum verification before restore validation plan | Verify `<checksum-file>` before restore. | Selected artifact checksum matches expected value. | `commands.md`, `configs/restore-execution-summary.md`, `validation.md` |
| V003 | Restore target confirmation validation plan | Review `<restore-target>` before restore invocation. | Restore target is confirmed before execution. | `commands.md`, `configs/restore-execution-summary.md`, `validation.md` |
| V004 | MariaDB restore execution placeholder validation plan | Plan logical restore invocation for `<db-backup-file>`. | MariaDB restore placeholder is documented without real data. | `commands.md`, `logs/restore-execution-validation.log`, `validation.md` |
| V005 | Kubernetes manifest restore placeholder validation plan | Plan manifest restore invocation for `<manifest-backup-file>`. | Kubernetes manifest restore placeholder is documented. | `commands.md`, `configs/restore-execution-summary.md`, `validation.md` |
| V006 | Nginx configuration restore placeholder validation plan | Plan Nginx config restore invocation for `<config-backup-file>`. | Nginx configuration restore placeholder is documented. | `commands.md`, `configs/restore-execution-summary.md`, `validation.md` |
| V007 | Observability configuration restore placeholder validation plan | Plan Prometheus/Grafana config restore placeholder. | Observability configuration restore placeholder is documented. | `commands.md`, `configs/restore-execution-summary.md`, `validation.md` |
| V008 | Restore log capture validation plan | Review `<restore-log>` capture. | Restore execution log is recorded. | `commands.md`, `logs/restore-execution-validation.log`, `validation.md` |
| V009 | Restore result sanity validation plan | Review post-restore sanity checks. | Restore result has expected basic sanity evidence. | `commands.md`, `screenshots/restore-execution-result.png`, `validation.md` |
| V010 | Restore abort condition validation plan | Review abort conditions before execution. | Abort conditions are documented and actionable. | `commands.md`, `configs/restore-abort-conditions.md`, `validation.md` |
| V011 | Restore rollback placeholder validation plan | Review rollback placeholder. | Rollback placeholder is documented without claiming full DR. | `commands.md`, `configs/restore-abort-conditions.md`, `validation.md` |
| V012 | Failure condition for missing backup artifact, checksum mismatch, wrong restore target, restore command failure, incomplete restore, sensitive data exposure, missing restore log, or missing evidence | Evaluate findings against explicit failure conditions. | Restore execution issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates restore execution only; backup creation is handled in S038 and post-recovery service health is handled in S040.
