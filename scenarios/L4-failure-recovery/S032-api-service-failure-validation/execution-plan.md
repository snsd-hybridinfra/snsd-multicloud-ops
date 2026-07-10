# Execution Plan

1. Confirm that only placeholder workload names, namespaces, paths, and endpoints are used.
2. Capture the pre-failure API Deployment status for `<api-deployment>`.
3. Capture the pre-failure API Pod Ready status for `<api-pod>`.
4. Capture the pre-failure API Service endpoint status for `<api-service>`.
5. Capture a pre-failure API route and health endpoint plan for `<ingress-host><api-path>` and `<api-health-endpoint>`.
6. Plan API failure injection using a placeholder command.
7. Validate that the API route failure or degraded response is detectable.
8. Validate that the API health endpoint reflects failure or degradation.
9. Reference Ingress API path, Nginx Reverse Proxy, Blackbox probe, and Prometheus metric observations without reimplementing those scenarios.
10. Plan API workload restoration using an approved placeholder rollback action.
11. Validate API health and route recovery.
12. Measure detection and recovery timing against provisional thresholds.
13. Capture post-recovery workload status.
14. Record future command output placeholders in `commands.md`.
15. Record future validation results in `validation.md`.
