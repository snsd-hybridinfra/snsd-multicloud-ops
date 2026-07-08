# Failure Condition

S017 fails if the MariaDB access control model allows unsafe or undocumented database access.

## Failure Conditions

- MariaDB bind-address or listener behavior exposes DB access outside the intended boundary.
- MariaDB user and host mappings include public or unrestricted sources.
- `<app-db-user>` is missing or has overly broad privileges.
- `<replication-user>` is missing or shares application or backup privileges.
- `<backup-user>` is missing or shares application or replication privileges.
- Root remote access is allowed.
- DB port `3306` is publicly exposed.
- Cloud App/API node DB access is not scoped to an approved placeholder source.
- Direct Web node DB access is allowed without explicit approval.
- Administrative access is not limited to Bastion or management boundaries.
- Evidence contains database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder user or host model exists.
- Future MariaDB command output or network exposure evidence is unavailable.
- Required evidence files are missing.
