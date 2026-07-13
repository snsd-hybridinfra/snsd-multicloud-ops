# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-load-balancer-failure.ps1`.
2. Validate baselines, modes, criteria, manual-only commands, metrics, and response matrix.
3. Parse healthy pre-state, LB/client failure, direct-backend health, manual recovery, restored path, and bypass/rollback.
4. Warn for unmeasured recovery time.
5. Reject unsafe recovered state, sensitive content, real endpoints/addresses, or executable traffic/service changes.
6. Review generated log and summary; optionally run approved LiveHttp.

Live requests and fault injection are `NOT_RUN` in committed evidence.
