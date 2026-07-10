# Execution Plan

1. Confirm the scenario evidence directory exists for S027.
2. Identify placeholder primary host as `<db-primary-host>`.
3. Identify placeholder replica hosts as `<db-replica-host>`.
4. Record planned replica status command capture.
5. Record planned `Seconds_Behind_Source` or `Seconds_Behind_Master` field review.
6. Record planned primary timestamp write to `<test-database>.<test-table>`.
7. Record planned replica timestamp read delay checks.
8. Record planned threshold comparison using provisional NORMAL, WARNING, and CRITICAL values.
9. Record planned lag validation for `db-replica-01` and `db-replica-02`.
10. Record planned DB exporter and Prometheus metric mapping placeholders.
11. Record planned lag evidence capture.
12. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not configure MariaDB, create users, set passwords, install exporters, configure Prometheus, or modify replication state. It only defines the review flow and evidence requirements for later approved validation.
