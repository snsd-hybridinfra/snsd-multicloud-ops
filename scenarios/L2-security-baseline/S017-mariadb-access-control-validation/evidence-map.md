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

`commands.md` contains a `NOT_RUN` record and `validation.md` records the current
`NOT_RUN` result. Every listed evidence path is planned and currently absent.
Previous static, sample, or pasted artifacts are quarantined and are not
evidence artifacts.
