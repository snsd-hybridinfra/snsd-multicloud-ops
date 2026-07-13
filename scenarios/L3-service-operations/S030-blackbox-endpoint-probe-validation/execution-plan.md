# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-blackbox-endpoint-probe.ps1`.
2. Verify five baseline files and four fixtures.
3. Validate HTTP/TCP modules and Prometheus probe/relabel config.
4. Validate metrics, thresholds, matrix, and command references.
5. Parse healthy and warning fixtures, negative failure fixture, and query JSON.
6. Reject auth/TLS, real URLs/endpoints/domains/addresses, credentials/tokens/cookies, IDs, and unsafe execution.
7. Review generated log and summary.
8. Optionally run LiveBlackbox after explicit approval.

LiveBlackbox is `NOT_RUN` in committed Static evidence.
