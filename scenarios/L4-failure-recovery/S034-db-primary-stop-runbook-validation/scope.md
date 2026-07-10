# Scope

## Included

- Pre-failure DB Primary status validation plan.
- Pre-failure DB Replica status validation plan.
- Pre-failure replication status validation plan.
- Primary stop failure injection plan using placeholder commands.
- Primary write failure detection validation plan.
- Application DB dependency impact placeholder validation plan.
- Replica state during Primary outage validation plan.
- Manual runbook decision point validation plan.
- Recovery action placeholder.
- Primary restoration validation plan.
- Post-recovery replication state validation plan.
- Runbook evidence collection plan.

## Target DB Nodes

- `db-primary-01`
- `db-replica-01`
- `db-replica-02`

## Failure Injection Scope

- Simulate DB Primary stop using placeholder commands.
- Validate Primary write path failure.
- Validate Replica state during Primary outage.
- Validate application impact placeholder.
- Validate manual recovery procedure documentation.
- Validate Primary restoration and replication state after recovery.
- Capture before, failure, and after evidence using TODO placeholders.

## Important Boundary

- Do not promote a Replica automatically.
- Do not document automatic failover as implemented.
- Do not claim HA DB behavior.
- This scenario handles Primary outage through manual runbook validation only.

## Runbook Decision Model

- Confirm Primary outage.
- Confirm Replica replication state before outage.
- Confirm application impact.
- Decide whether to restore Primary or execute manual promotion in a future out-of-scope procedure.
- Validate restored Primary service.
- Validate replication state after recovery.
- Record evidence and incident notes.

## Failure and Recovery Threshold Model

- DETECTED: Primary outage visible within `< 60 seconds`.
- WARNING: Primary restoration within `60-300 seconds`.
- CRITICAL: Primary recovery failed or application dependency remains unavailable.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real MariaDB configuration implementation.
- Automatic DB failover, HA DB behavior, Galera Cluster, ProxySQL, and split-brain automation.
- Real database passwords, credentials, private keys, tfstate, kubeconfig, cloud account values, public IPs, or account-specific values.
- MariaDB access control validation, which is handled in S017.
- Primary-Replica replication setup validation, which is handled in S026.
- DB replication lag validation, which is handled in S027.
- DB Replica failure validation, which is handled in S033.
- Backup and restore validation, which is handled in S038 and S039.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
