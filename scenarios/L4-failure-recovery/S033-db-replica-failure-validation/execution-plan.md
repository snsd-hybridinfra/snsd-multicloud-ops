# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-db-replica-failure.ps1`.
2. Validate artifacts, placeholders, twelve criteria, debug-only Ansible, and symbolic metrics.
3. Parse healthy pre-state, manual event, failure detection, Primary availability, recovered state, and catch-up.
4. Warn when elapsed time is unmeasured.
5. Reject unsafe recovered state, sensitive content, dumps, real addresses, or executable DB/service/network logic.
6. Review generated log and summary.

Live database operations are `NOT_RUN`.
