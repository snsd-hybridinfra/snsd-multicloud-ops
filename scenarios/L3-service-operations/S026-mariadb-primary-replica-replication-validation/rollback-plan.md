# Rollback Plan

S026 reads files and writes aggregate evidence only; database rollback is never applicable.

1. Stop if an artifact contains concrete or sensitive database content.
2. Remove the unsafe artifact and sanitize from an authorized source outside the repository workflow.
3. Correct parser/sample inconsistencies without connecting to MariaDB.
4. Rerun StaticEvidence validation.
5. Revert invalid repository changes through version control.

Never start, stop, reset, repair, reconfigure, or fail over replication from this scenario.
