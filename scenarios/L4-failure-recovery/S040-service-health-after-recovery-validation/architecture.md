# Architecture

This scenario models a final post-recovery health review across service, data, and observability layers.

## Relevant Components

- Web endpoint placeholder: `<web-endpoint>`.
- API endpoint placeholder: `<api-endpoint>`.
- Ingress host placeholder: `<ingress-host>`.
- Reverse proxy host placeholder: `<reverse-proxy-host>`.
- Health endpoint placeholder: `<health-endpoint>`.
- Prometheus endpoint placeholder: `<prometheus-endpoint>`.
- Grafana endpoint placeholder: `<grafana-endpoint>`.
- DB Primary and Replica placeholders: `<db-primary-host>`, `<db-replica-host>`.
- Evidence store: `evidence/L4-failure-recovery/S040-service-health-after-recovery-validation/`.

## Post-Recovery Review Flow

1. Review Web and API service HTTP responses.
2. Review Ingress and Nginx Reverse Proxy routing.
3. Review load balancing health endpoint response.
4. Reference MariaDB Primary and Replica state.
5. Review Prometheus targets and Grafana dashboard visibility.
6. Review Blackbox probe success.
7. Compare evidence against the post-recovery judgment model.
8. Record final judgment and supporting evidence.

This scenario consolidates evidence from recovery scenarios without implementing recovery automation.
