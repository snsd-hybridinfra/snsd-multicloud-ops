# Prerequisites

- Repository scope lock and excluded-scope rules have been reviewed.
- Matching evidence directory exists at `evidence/L4-failure-recovery/S034-db-primary-stop-runbook-validation/`.
- S017 MariaDB access control validation is planned before access-related evidence is interpreted.
- S026 MariaDB Primary-Replica replication validation is planned before Primary stop behavior is reviewed.
- S027 DB replication lag validation is planned before lag-related evidence is interpreted.
- S033 DB Replica failure validation remains separate and must not be reimplemented here.
- S038 and S039 backup and restore validation remain separate and must not be reimplemented here.
- Placeholder values are available for `<db-primary-host>`, `<db-replica-host>`, `<replication-user>`, `<test-database>`, `<test-table>`, and `<primary-recovery-threshold-seconds>`.
- No real database passwords, credentials, private keys, tfstate, kubeconfig, cloud account values, public IPs, or account-specific values are required for this documentation skeleton.
