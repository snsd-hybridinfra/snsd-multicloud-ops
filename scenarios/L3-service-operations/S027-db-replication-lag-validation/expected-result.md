# Expected Result

S027 is successful when the MariaDB replication lag validation plan is complete and ready for future approved execution.

## Success Conditions

- Replica status command validation is planned.
- `Seconds_Behind_Source` or `Seconds_Behind_Master` field validation is planned.
- Primary timestamp write validation is planned.
- Replica timestamp read validation is planned.
- Provisional NORMAL, WARNING, and CRITICAL threshold comparison is documented.
- Lag validation is planned for `db-replica-01`.
- Lag validation is planned for `db-replica-02`.
- DB exporter and Prometheus metric mapping placeholders are documented.
- Lag evidence capture is planned.
- All validation checks map to required evidence files.

## Evidence Conditions

- `commands.md` lists planned command or review actions with TODO output placeholders.
- `validation.md` lists each check with `NOT_RUN` status until execution.
- Future supporting evidence is expected in `configs/db-replication-lag-threshold.md`, `configs/db-replication-lag-metric-mapping.md`, `logs/db-replication-lag-validation.log`, and `screenshots/db-replication-lag-status.png`.
