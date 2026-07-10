# Execution Plan

1. Confirm that only placeholder endpoints, hostnames, and thresholds are used.
2. Capture pre-failure load balancer endpoint response for `<load-balancer-endpoint>`.
3. Capture pre-failure backend health for `<backend-service>`.
4. Reference pre-failure Ingress route behavior from S023.
5. Plan load balancer or reverse proxy entrypoint failure injection using placeholder commands.
6. Validate endpoint failure detection for web and API endpoints.
7. Validate health check failure detection for `<health-endpoint>`.
8. Reference Blackbox probe failure evidence from S030.
9. Validate backend service health during frontend failure.
10. Document manual recovery decision points and explicitly avoid automatic cross-cloud failover claims.
11. Plan load balancer or reverse proxy restoration using an approved placeholder action.
12. Validate post-recovery HTTP response and service health.
13. Measure detection and recovery timing against provisional thresholds.
14. Record future command output placeholders in `commands.md`.
15. Record future validation results in `validation.md`.
