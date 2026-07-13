# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-db-primary-stop-runbook.ps1`.
2. Validate artifacts, placeholders, no-promotion boundary, thirteen criteria, debug-only Ansible, and symbolic metrics.
3. Parse pre-state, manual stop, Primary-down, write impact, Replica no-promotion, manual recovery, restored state, and catch-up.
4. Warn for unmeasured recovery time.
5. Reject unsafe recovered state, sensitive data, or executable DB/service/network logic.
6. Review generated log and summary.

Live actions are `NOT_RUN`.
