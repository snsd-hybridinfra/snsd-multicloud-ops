# Scope

## Included

- Pre-failure DB Primary status validation plan.
- Pre-failure DB Replica status validation plan.
- Pre-failure replication status validation plan.
- Replica failure injection plan using placeholder commands.
- Replication channel interruption validation plan.
- Failed Replica detection validation plan.
- Primary write availability during Replica failure validation plan.
- Application DB dependency impact placeholder validation plan.
- Replica restoration validation plan.
- Replication resume validation plan.
- Post-recovery replica consistency validation plan.
- Replica failure evidence collection plan.

## Target DB Nodes

- `db-primary-01`
- `db-replica-01`
- `db-replica-02`

## Failure Injection Scope

- Simulate one DB Replica outage using placeholder commands.
- Validate Primary remains writable.
- Validate failed Replica is detected as unavailable.
- Validate replication status changes during failure.
- Validate Replica recovery and replication resume.
- Capture before, failure, and after evidence using TODO placeholders.

## Failure and Recovery Threshold Model

- DETECTED: Replica failure visible within `< 60 seconds`.
- WARNING: Replica recovery within `60-300 seconds`.
- CRITICAL: Replica recovery failed or replication does not resume.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real MariaDB configuration implementation.
- Real database passwords, credentials, private keys, tfstate, kubeconfig, cloud account values, public IPs, or account-specific values.
- MariaDB access control validation, which is handled in S017.
- Primary-Replica replication setup validation, which is handled in S026.
- DB replication lag validation, which is handled in S027.
- DB primary stop runbook validation, which is handled in S034.
- Backup and restore validation, which is handled in S038 and S039.
- Galera Cluster, ProxySQL, DB automatic failover, and split-brain automation.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
