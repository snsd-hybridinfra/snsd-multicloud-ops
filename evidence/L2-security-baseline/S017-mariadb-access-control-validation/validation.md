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
