# Expected Result

## Pass Criteria

- V001 through V014 return `PASS`.
- Application, replication, monitoring, administration, and root responsibilities remain separated.
- Application and monitoring grants contain no dangerous privilege.
- Password material remains an external-management placeholder only.
- No database connection, SQL execution, user change, or dump operation occurs.

## Evidence Criteria

The ignored log and tracked summary contain sanitized check results only and no real credentials, hosts, connection strings, dumps, secrets, or account-specific values.

## Sanitized Real-Lab Criteria

- `READY`: MariaDB is active on the intended internal interface; accounts are source-host restricted; read-only SELECT succeeds while INSERT and CREATE TABLE fail; application DML succeeds while CREATE USER and mysql.user access fail; no authentication material is retained.
- `PARTIAL`: service and grants are present but one or more allow/deny tests or listener/firewall evidence is incomplete.
- `BLOCKED`: service or intended remote access fails, wildcard account hosts are unjustified, read-only writes succeed, application administration is granted, or authentication material cannot be removed safely.
- Replication behavior remains S026 and is not inferred here.

## 2026-07-15 Real-Lab Result

**PARTIAL** - service, listener, exact source-host grants, read-only SELECT and
INSERT denial, application DML, and CREATE USER denial are evidenced. Read-only
CREATE TABLE denial and application mysql.user denial were not supplied. UFW
was inactive and is recorded as a warning.
