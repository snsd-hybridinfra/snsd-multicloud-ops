# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-discovery.ps1`.
2. Verify four baseline files and three samples.
3. Validate six job definitions, symbolic targets, and Kubernetes endpoint discovery.
4. Validate matrix and command references.
5. Reject auth/TLS config, concrete endpoints/domains/addresses, credentials/tokens/cookies, IDs, and reload/client paths.
6. Parse targets and up JSON plus job-label text.
7. Require all six jobs at `health: up` and `up=1`.
8. Review generated log and summary.
9. Optionally run LivePrometheus after explicit approval.

LivePrometheus is `NOT_RUN` in committed Static evidence. It never writes the URL or raw response.
