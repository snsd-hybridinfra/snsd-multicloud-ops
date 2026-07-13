# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-load-balancing-health-check.ps1`.
2. Verify four baseline artifacts and three samples.
3. Validate pool members, `/health`, expected status, passive retry, timeouts, and unhealthy threshold.
4. Validate the ten-control matrix and five-command reference.
5. Parse load-balancer, backend-specific, and access-log samples.
6. Reject TLS material, credentials, sensitive headers, real domains/addresses, and unsupported active-health claims.
7. Confirm Static mode invoked no Nginx, curl, failover, or network action.
8. Review the generated log and summary.
9. Optionally run `-LiveHttp` with explicit load-balancer and backend URLs after approval.

The optional run remains `NOT_RUN` in committed Static evidence and never modifies routing state.
