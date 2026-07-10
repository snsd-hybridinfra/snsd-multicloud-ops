# Rollback Plan

1. Stop Replica failure validation if real database passwords, credentials, private keys, public IPs, or account-specific values appear in commands or evidence.
2. If future execution leaves a Replica unavailable, pause additional failure injection and restore the expected Replica state using approved operational procedures.
3. Remove or sanitize unapproved evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
4. Recheck that only placeholders such as `<db-primary-host>`, `<db-replica-host>`, `<replication-user>`, `<test-database>`, `<test-table>`, and `<replica-recovery-threshold-seconds>` remain.
5. Mark S033 as `BLOCKED` if safe failure detection, restoration, or replication resume observation cannot be completed.
6. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No MariaDB configuration, database credentials, or runtime resources are created by this documentation skeleton.
