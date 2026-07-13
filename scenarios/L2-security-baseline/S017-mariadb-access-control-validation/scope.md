# Scope

## Included

- Least-privilege account and host-scope policy validation.
- Grant matrix and non-production SQL example inspection.
- Application DML, replication, monitoring read-only, and administration separation checks.
- Root-use, remote-root, wildcard-host, password-storage, dangerous-privilege, dump, connection-string, and sensitive-content checks.
- Safe local evidence generation.

## Excluded

- MariaDB connections, client execution, SQL execution, or real user/grant changes.
- Real configuration, credentials, hosts, connection strings, database names, dumps, or exports.
- Replication validation (S026), replication lag (S027), replica failure (S033), primary stop runbook (S034), and backup/restore (S038/S039).
- Network-level database exposure, handled by S014, S015, and S016.
