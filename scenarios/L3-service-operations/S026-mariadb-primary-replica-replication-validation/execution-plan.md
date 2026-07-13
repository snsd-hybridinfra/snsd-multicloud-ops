# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-mariadb-primary-replica-replication.ps1`.
2. Verify the runbook, commands, Ansible placeholder, and three samples.
3. Validate topology, stream, account, thread, lag, failure, and mode documentation.
4. Validate safe status-command references and the debug-only Ansible example.
5. Parse IO and SQL thread health using modern or legacy fields.
6. Parse delay and compare it with the sample threshold.
7. Require empty IO/SQL error fields and symbolic master status.
8. Reject credentials, connection strings, dumps, concrete addresses/identifiers, database-client invocation, and destructive replication operations.
9. Review the generated log and summary.

Manual lab collection is outside execution; only already-sanitized evidence is parsed.
