# S017-mariadb-access-control-validation

| Field | Value |
|---|---|
| Scenario ID | S017 |
| Scenario Name | MariaDB Access Control Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Related Components | MariaDB policy baseline, grant matrix, SQL example, inventory placeholders, local validator |
| Validation Type | Safe local repository validation |
| Evidence Directory | `evidence/L2-security-baseline/S017-mariadb-access-control-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate MariaDB least-privilege account separation and grants without connecting to a database, executing SQL, or storing credentials.

## Scope Summary

S017 reads local policy, matrix, SQL example, and inventory placeholders only. It does not create users, alter grants, query MariaDB, read credentials, or produce dumps.

## Validation Summary

Fourteen checks validate policy artifacts, account placeholders, grant separation, application/monitoring dangerous privileges, password and connection safety, dump absence, address safety, and execution boundaries.

## Evidence Output Summary

The validator writes an ignored execution log and a tracked sanitized Markdown summary under the S017 evidence directory.
