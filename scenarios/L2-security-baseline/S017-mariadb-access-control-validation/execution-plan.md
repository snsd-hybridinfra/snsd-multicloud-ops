# Execution Plan

1. Run `tools/validate-mariadb-access-control-baseline.ps1` from the repository root.
2. Confirm the policy, matrix, SQL example, required accounts, and required statements.
3. Parse SQL grant statements for application, replication, and monitoring placeholders.
4. Reject dangerous privileges assigned to application or monitoring identities.
5. Reject real-looking passwords, connection strings, dumps, secrets, identifiers, and public addresses.
6. Confirm the validator contains no database client, SQL execution, host connection, or network command.
7. Review the generated log and summary.

## Execution Boundary

The script does not connect to MariaDB, run `mysql`, `mariadb`, or `mysqldump`, execute SQL, read credentials, or create, alter, or drop users.
