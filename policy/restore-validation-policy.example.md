# Restore Validation Policy Example

**NON-PRODUCTION POLICY EXAMPLE**

- A restore must reference a backup manifest and verify checksum before execution.
- The target must be `<disposable-restore-target-placeholder>`, never production.
- Restore evidence requires job ID, backup ID, source, target, start/completion time, duration, checksum result, consistency result, rollback condition, and evidence reference.
- A failed checksum or consistency result requires abort/rollback.
- S040 final service-health validation is mandatory after a future authorized restore exercise.
- No real backup, restore artifact, path, storage target, credential, row, or production data may be committed.
