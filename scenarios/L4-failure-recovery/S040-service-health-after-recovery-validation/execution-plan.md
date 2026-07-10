# Execution Plan

1. Confirm that only placeholder endpoints, paths, hosts, and component names are used.
2. Plan Web service HTTP response validation for `<web-endpoint>`.
3. Plan API service HTTP response validation for `<api-endpoint>`.
4. Plan Ingress route validation for `<ingress-host>`.
5. Plan Nginx Reverse Proxy validation for `<reverse-proxy-host>`.
6. Plan load balancing health endpoint validation for `<health-endpoint>`.
7. Reference MariaDB Primary availability and Replica state evidence.
8. Plan Prometheus target UP validation for `<prometheus-endpoint>`.
9. Plan Grafana dashboard visibility validation for `<grafana-endpoint>`.
10. Plan Blackbox `probe_success` validation for recovered endpoints.
11. Compare evidence against the final judgment model.
12. Record future command output placeholders in `commands.md`.
13. Record future validation results and final judgment in `validation.md`.
