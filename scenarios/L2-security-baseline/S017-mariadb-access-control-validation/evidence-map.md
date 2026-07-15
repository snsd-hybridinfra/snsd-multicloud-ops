# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Access-control baseline | `logs/mariadb-access-control-validation.log`; `configs/mariadb-access-control-summary.md` | yes |
| V002 | Grant matrix | same generated evidence | yes |
| V003 | SQL baseline example | same generated evidence | yes |
| V004 | Required account placeholders | same generated evidence | yes |
| V005 | Least privilege statements | same generated evidence | yes |
| V006 | Grant matrix role separation | same generated evidence | yes |
| V007 | Application grant | same generated evidence | yes |
| V008 | Replication grant | same generated evidence | yes |
| V009 | Monitoring grant | same generated evidence | yes |
| V010 | Dangerous application or monitoring privileges | same generated evidence | yes |
| V011 | Password and connection safety | same generated evidence | yes |
| V012 | Database dump safety | same generated evidence | yes |
| V013 | Account and address safety | same generated evidence | yes |
| V014 | Execution safety boundary | same generated evidence | yes |

`commands.md` documents execution and `validation.md` records final results. The generated log is ignored; the sanitized summary is tracked.

## Real Virtual-Lab Evidence Map

| Check ID | Validation Item | Evidence File | Status |
|---|---|---|---|
| LAB-001-LAB-002 | Service and listener | `logs/20260715-S017-mariadb-service-listener.sanitized.txt` | PASS with firewall WARN |
| LAB-003-LAB-005 | Host-scoped application/read-only grants | `logs/20260715-S017-mariadb-grants.sanitized.txt` | PASS |
| LAB-006-LAB-008 | Read-only allow/deny operations | `logs/20260715-S017-readonly-allow-deny.sanitized.txt` | PARTIAL - DDL denial missing |
| LAB-009-LAB-011 | Application allow/deny operations | `logs/20260715-S017-application-user-allow-deny.sanitized.txt` | PARTIAL - system-database denial missing |
| LAB-012 | Sanitization and final judgment | `configs/20260715-S017-mariadb-access-control-validation-summary.md` | PARTIAL |

Raw terminal output and authentication material are not evidence artifacts.
