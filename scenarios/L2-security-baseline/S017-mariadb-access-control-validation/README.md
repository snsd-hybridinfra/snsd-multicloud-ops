# S017-mariadb-access-control-validation

| Field | Value |
|---|---|
| Scenario ID | S017 |
| Scenario Name | MariaDB Access Control Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Related Components | MariaDB policy baseline, grant matrix, SQL example, inventory placeholders, local validator |
| Validation Type | Safe local repository validation; sanitized operator-provided real virtual-lab evidence review |
| Evidence Directory | `evidence/L2-security-baseline/S017-mariadb-access-control-validation/` |
| Status | PARTIAL |

## Objective Summary

Validate MariaDB least-privilege account separation and grants without storing credentials. The repository validator remains static; the dated record separately reviews sanitized operator-provided real virtual-lab output.

## Scope Summary

S017 reads local policy, matrix, SQL example, and inventory placeholders only. It does not create users, alter grants, query MariaDB, read credentials, or produce dumps.

## Validation Summary

Fourteen static checks validate policy artifacts, account placeholders, grant separation, application/monitoring dangerous privileges, password and connection safety, dump absence, address safety, and execution boundaries. The real-lab evidence validates service/listener state, source-host grants, read-only SELECT and INSERT denial, application DML, and CREATE USER denial. Read-only CREATE TABLE denial and application mysql.user denial remain unevidenced.

## Evidence Output Summary

The validator writes an ignored execution log and a tracked sanitized Markdown summary. Four dated sanitized real-lab records and a PARTIAL summary retain no raw output, password/hash/authentication material, real infrastructure identifier, or secret.
