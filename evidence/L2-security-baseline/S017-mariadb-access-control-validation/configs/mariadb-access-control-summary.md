# MariaDB Access Control Summary

- Scenario: S017-mariadb-access-control-validation
- Generated: 2026-07-13T10:53:46+09:00
- Overall result: **PASS**
- Scope: local policy, matrix, SQL example, inventory placeholders, and safety checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Access-control baseline | PASS | Baseline document exists. |
| V002 | Grant matrix | PASS | Grant matrix exists. |
| V003 | SQL baseline example | PASS | Non-production SQL example exists. |
| V004 | Required account placeholders | PASS | All four account placeholders are documented. |
| V005 | Least privilege statements | PASS | Least privilege, root denial, password, host, separation, and evidence statements exist. |
| V006 | Grant matrix role separation | PASS | Application, replication, monitoring, administration, root, and host-scope expectations exist. |
| V007 | Application grant | PASS | Application account receives only required DML on the application database placeholder. |
| V008 | Replication grant | PASS | Replication account receives replication privileges only. |
| V009 | Monitoring grant | PASS | Monitoring account receives limited read-only metadata access. |
| V010 | Dangerous application or monitoring privileges | PASS | No dangerous privilege is assigned to application or monitoring accounts. |
| V011 | Password and connection safety | PASS | Only an angle-bracket password placeholder is used; no connection string or secret assignment exists. |
| V012 | Database dump safety | PASS | No database dump or export file exists. |
| V013 | Account and address safety | PASS | No private key, account identifier, UUID, or real-looking public IP is present. |
| V014 | Execution safety boundary | PASS | The validator contains no database client, SQL execution, host connection, or network command. |

## Safety Boundary

This validation read repository files only. It did not connect to MariaDB, execute SQL, read credentials, create or alter users, generate dumps, or contact external systems.
