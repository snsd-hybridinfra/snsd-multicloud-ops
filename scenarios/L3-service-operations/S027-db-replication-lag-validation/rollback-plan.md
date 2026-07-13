# Rollback Plan

S027 reads files and writes aggregate evidence only; no database or monitoring rollback applies.

1. Stop if concrete or sensitive environment content is found.
2. Remove the unsafe artifact and restore approved placeholders.
3. Correct threshold/parser/fixture inconsistencies without external access.
4. Rerun StaticEvidence validation.
5. Revert invalid repository changes through version control.

Never change replication, query monitoring systems, or trigger recovery/failover from this scenario.
