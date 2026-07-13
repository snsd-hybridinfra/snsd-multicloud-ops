# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-down.ps1`.
2. Validate baselines, workflow, placeholder alert, criteria, response matrix, and manual boundaries.
3. Parse UP/up=1, manual stop, DOWN/up=0/firing, manual start, UP/up=1/resolved evidence.
4. Warn for unmeasured recovery time.
5. Reject unresolved recovered state, sensitive content, real endpoints/targets, or executable mutation logic.
6. Review generated log and summary; optionally run approved LivePrometheus.

Live queries and service actions are `NOT_RUN` in committed evidence.
