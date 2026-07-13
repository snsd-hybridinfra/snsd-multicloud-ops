# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Access-control baseline | Baseline exists. | generated log and summary |
| V002 | Grant matrix | Matrix exists. | generated log and summary |
| V003 | SQL baseline example | Non-production example exists. | generated log and summary |
| V004 | Required account placeholders | Four accounts exist. | generated log and summary |
| V005 | Least privilege statements | Root, password, host, separation, and evidence rules exist. | generated log and summary |
| V006 | Grant matrix role separation | Required role expectations exist. | generated log and summary |
| V007 | Application grant | Required DML only. | generated log and summary |
| V008 | Replication grant | Replication privileges only. | generated log and summary |
| V009 | Monitoring grant | Limited read-only metadata access. | generated log and summary |
| V010 | Dangerous application or monitoring privileges | No dangerous assignment exists. | generated log and summary |
| V011 | Password and connection safety | Only approved placeholders; no connection string. | generated log and summary |
| V012 | Database dump safety | No dump or export exists. | generated log and summary |
| V013 | Account and address safety | No private material, identifier, or real public address exists. | generated log and summary |
| V014 | Execution safety boundary | No database client, SQL execution, host, or network command exists. | generated log and summary |

Every check maps by ID to `logs/mariadb-access-control-validation.log` and `configs/mariadb-access-control-summary.md`.
