# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-api-service-failure.ps1`.
2. Verify three baseline artifacts and nine samples.
3. Validate workflow placeholders, criteria, and manual-only fault commands.
4. Parse healthy pre-state, failure signal, recovered Pod/endpoint/HTTP state, and rollout.
5. Warn if elapsed recovery time is unmeasured.
6. Reject unhealthy recovered state, sensitive content, real endpoints/addresses, or destructive validator logic.
7. Review generated log and summary.
8. Optionally run explicitly approved read-only LiveKubectl or LiveHttp.

Live access and real failure injection are `NOT_RUN` in committed evidence.
