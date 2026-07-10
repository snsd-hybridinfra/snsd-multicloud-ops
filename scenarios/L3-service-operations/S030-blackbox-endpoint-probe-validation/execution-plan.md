# Execution Plan

1. Confirm that only placeholder endpoint names are used for probe planning.
2. Identify the Blackbox Exporter endpoint placeholder `<blackbox-exporter-endpoint>`.
3. Review the planned probe module placeholder for HTTP endpoint probing.
4. Map each target endpoint category to a probe target placeholder.
5. Plan Blackbox Exporter service status collection.
6. Plan direct probe checks for web, API, Ingress, reverse proxy, AWS, Azure, OpenStack, and health check endpoints.
7. Plan HTTP status code and response latency collection for each endpoint category.
8. Plan Prometheus query checks for `probe_success` and `probe_http_status_code`.
9. Record future command output placeholders in `commands.md`.
10. Record future validation results in `validation.md`.
11. Store future sanitized summaries, logs, and screenshots under the matching evidence directory.
12. Mark failed probes, route timeouts, DNS failures, unexpected status codes, excessive latency, or missing evidence as validation failures.
