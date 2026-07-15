# S017 Real Virtual-Lab MariaDB Access-Control Validation Summary

| Field | Result |
|---|---|
| Evidence source | Pasted terminal output |
| Validation mode | Real virtual lab, sanitized |
| MariaDB service | PASS - service reported active |
| MariaDB listener | PASS - MariaDB listened on the masked internal database interface and port 3306 |
| Host firewall | WARN - UFW reported inactive |
| Source-host restriction | PASS - both lab-role accounts were scoped to `<client-host-placeholder>`; no wildcard account host was observed |
| Application account grant | PASS - `SELECT`, `INSERT`, `UPDATE`, and `DELETE` were scoped to `snsd_app.*`; global effective privilege was USAGE only |
| Read-only account grant | PASS - `SELECT` was scoped to `snsd_app.*`; global effective privilege was USAGE only |
| Read-only SELECT | PASS - the query returned one row |
| Read-only write denial | PASS - INSERT was denied with database error 1142 |
| Read-only DDL denial | **NOT EVIDENCED** - no CREATE TABLE denial test was included |
| Application DML | PASS - INSERT affected one row and SELECT returned the expected aggregate row count |
| Application administrative denial | PASS - CREATE USER was denied with database error 1227 |
| Application system-database denial | **NOT EVIDENCED** - no application-account mysql.user denial test was included |
| Password/authentication sanitization | PASS - interactive input, attempted credential value, authentication clauses, and password hashes were removed |
| Other sensitive data | PASS - real users/hosts/addresses, process and connection IDs, returned row values/timestamps, tokens, keys, certificates, cookies, Authorization headers, cloud credentials, kubeconfig, and secrets are absent or masked |
| S026 boundary | S017 validates database access control only; primary-replica replication validation remains S026 |
| Final judgment | **PARTIAL** |

## Judgment Basis

Service, listener, host-scoped accounts, least-privilege grants, read-only SELECT,
read-only INSERT denial, application DML, and application CREATE USER denial are
supported by sanitized evidence. READY cannot be claimed until the read-only
CREATE TABLE denial and application-account `mysql.user` denial are captured.
UFW inactivity is recorded as a warning rather than hidden.

Validated path:

`<client-node-masked> -> MariaDB listener -> source-host account match -> database-scoped privilege evaluation`

## Evidence References

- `logs/20260715-S017-mariadb-service-listener.sanitized.txt`
- `logs/20260715-S017-mariadb-grants.sanitized.txt`
- `logs/20260715-S017-readonly-allow-deny.sanitized.txt`
- `logs/20260715-S017-application-user-allow-deny.sanitized.txt`
