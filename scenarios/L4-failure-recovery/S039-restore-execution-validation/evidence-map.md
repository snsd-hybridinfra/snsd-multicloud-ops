# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Backup artifact selection validation plan | `commands.md`; `configs/restore-artifact-selection.md`; `screenshots/restore-artifact-selection.png`; `validation.md` | command plan, artifact selection, screenshot reference, validation record | yes |
| Backup checksum verification before restore validation plan | `commands.md`; `configs/restore-execution-summary.md`; `validation.md` | command plan, restore summary, validation record | yes |
| Restore target confirmation validation plan | `commands.md`; `configs/restore-execution-summary.md`; `validation.md` | command plan, restore summary, validation record | yes |
| MariaDB restore execution placeholder validation plan | `commands.md`; `logs/restore-execution-validation.log`; `validation.md` | command plan, restore log, validation record | yes |
| Kubernetes manifest restore placeholder validation plan | `commands.md`; `configs/restore-execution-summary.md`; `validation.md` | command plan, restore summary, validation record | yes |
| Nginx configuration restore placeholder validation plan | `commands.md`; `configs/restore-execution-summary.md`; `validation.md` | command plan, restore summary, validation record | yes |
| Observability configuration restore placeholder validation plan | `commands.md`; `configs/restore-execution-summary.md`; `validation.md` | command plan, restore summary, validation record | yes |
| Restore log capture validation plan | `commands.md`; `logs/restore-execution-validation.log`; `validation.md` | command plan, restore log, validation record | yes |
| Restore result sanity validation plan | `commands.md`; `screenshots/restore-execution-result.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Restore abort condition validation plan | `commands.md`; `configs/restore-abort-conditions.md`; `validation.md` | command plan, abort conditions, validation record | yes |
| Restore rollback placeholder validation plan | `commands.md`; `configs/restore-abort-conditions.md`; `validation.md` | command plan, rollback placeholder, validation record | yes |
| Failure condition for missing backup artifact, checksum mismatch, wrong restore target, restore command failure, incomplete restore, sensitive data exposure, missing restore log, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real restore output, database dump, backup content, or restore log has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
