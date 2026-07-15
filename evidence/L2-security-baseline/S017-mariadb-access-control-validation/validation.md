# Validation

Scenario: S017-mariadb-access-control-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | Access-control baseline | File exists. | Baseline exists. | generated log and summary | PASS |
| V002 | Grant matrix | File exists. | Matrix exists. | generated log and summary | PASS |
| V003 | SQL baseline example | File exists. | Non-production example exists. | generated log and summary | PASS |
| V004 | Required account placeholders | Four accounts exist. | All are documented. | generated log and summary | PASS |
| V005 | Least privilege statements | Required statements exist. | All are documented. | generated log and summary | PASS |
| V006 | Grant matrix role separation | Role expectations exist. | All are documented. | generated log and summary | PASS |
| V007 | Application grant | Required DML only. | Grant is correctly limited. | generated log and summary | PASS |
| V008 | Replication grant | Replication privileges only. | Grant is correctly limited. | generated log and summary | PASS |
| V009 | Monitoring grant | Read-only metadata access. | Grant is correctly limited. | generated log and summary | PASS |
| V010 | Dangerous application or monitoring privileges | No dangerous assignment. | None detected. | generated log and summary | PASS |
| V011 | Password and connection safety | Placeholder only; no connection string. | No unsafe value detected. | generated log and summary | PASS |
| V012 | Database dump safety | No dump or export exists. | None detected. | generated log and summary | PASS |
| V013 | Account and address safety | No sensitive or account-specific content. | None detected. | generated log and summary | PASS |
| V014 | Execution safety boundary | No live database or network command. | None detected. | generated log and summary | PASS |

## Generated Result

All fourteen checks passed using repository files only. Evidence is recorded in `logs/mariadb-access-control-validation.log` and `configs/mariadb-access-control-summary.md`.

## Real Virtual-Lab Evidence Validation - 2026-07-15

Validation mode: Real virtual lab evidence, sanitized

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| LAB-001 | MariaDB service | Service is active. | service-listener log; dated summary | PASS |
| LAB-002 | Internal listener | MariaDB listens on the intended masked internal interface. | service-listener log; dated summary | PASS |
| LAB-003 | Source-host restrictions | Application and read-only accounts match only the intended client host. | grants log; dated summary | PASS |
| LAB-004 | Application grants | DML is scoped to `snsd_app.*` without global administration. | grants log; dated summary | PASS |
| LAB-005 | Read-only grants | SELECT only is scoped to `snsd_app.*`. | grants log; dated summary | PASS |
| LAB-006 | Read-only SELECT | Read-only account can query authorized data. | read-only allow/deny log; dated summary | PASS |
| LAB-007 | Read-only write denial | Read-only INSERT is denied. | read-only allow/deny log; dated summary | PASS |
| LAB-008 | Read-only DDL denial | Read-only CREATE TABLE is denied. | read-only allow/deny log; dated summary | NOT EVIDENCED |
| LAB-009 | Application DML | Application INSERT and SELECT succeed. | application allow/deny log; dated summary | PASS |
| LAB-010 | Application administration denial | Application CREATE USER is denied. | application allow/deny log; dated summary | PASS |
| LAB-011 | Application system-database denial | Application query against mysql.user is denied. | application allow/deny log; dated summary | NOT EVIDENCED |
| LAB-012 | Authentication-data safety | Password prompts, hashes, clauses, and secret values are absent. | all dated evidence | PASS |

Final judgment: **PARTIAL**

Validated path:

`<client-node-masked> -> MariaDB listener -> source-host account match -> database-scoped privilege evaluation`

Passwords were entered interactively in the source session and were not
captured. Raw terminal output, authentication strings, password hashes,
credential values, kubeconfig, tokens, certificates, keys, cookies,
Authorization headers, cloud credentials, and secrets are not committed.
Replication validation is handled separately by S026.

Evidence:

- `logs/20260715-S017-mariadb-service-listener.sanitized.txt`
- `logs/20260715-S017-mariadb-grants.sanitized.txt`
- `logs/20260715-S017-readonly-allow-deny.sanitized.txt`
- `logs/20260715-S017-application-user-allow-deny.sanitized.txt`
- `configs/20260715-S017-mariadb-access-control-validation-summary.md`
