# Rollback Plan

1. Stop restore validation if real database dumps, credentials, secrets, private keys, kubeconfig, tfstate, or account-specific values appear in commands or evidence.
2. Abort the restore plan if checksum verification fails, restore target is unclear, or sensitive data exposure is suspected.
3. Remove or sanitize unsafe restore evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
4. Recheck that only placeholders such as `<backup-root>`, `<restore-target>`, `<db-backup-file>`, `<manifest-backup-file>`, `<config-backup-file>`, `<checksum-file>`, and `<restore-log>` remain.
5. Mark S039 as `BLOCKED` if artifact selection, checksum verification, restore target confirmation, or restore log evidence cannot be safely documented.
6. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No real restore scripts, production data restore, backup contents, credentials, or automated DR actions are created by this documentation skeleton.
