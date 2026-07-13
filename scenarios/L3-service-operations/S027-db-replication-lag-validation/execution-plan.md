# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-db-replication-lag.ps1`.
2. Verify three baseline files and four fixtures.
3. Validate normal/warning/critical/NULL thresholds and the nine-row matrix.
4. Validate four metric names and S028/S029 ownership boundaries.
5. Parse each fixture's lag, IO/SQL threads, and IO/SQL errors.
6. Require normal classification, expected warning classification, and detection of critical/NULL negative fixtures.
7. Reject credentials, connection strings, dumps, observability credentials, addresses, IDs, URLs, and external execution paths.
8. Review the generated log and summary.

Real lab collection and all external queries are `NOT_RUN` in this scenario.
