# Architecture

This scenario models Blackbox Exporter as an observability component that probes external service endpoints and exposes probe metrics for Prometheus review.

## Relevant Components

- Blackbox Exporter endpoint: `<blackbox-exporter-endpoint>`.
- Probe targets: `<probe-target>`, `<web-endpoint>`, `<api-endpoint>`, `<ingress-host>`, `<reverse-proxy-host>`, `<health-endpoint>`.
- Provider endpoint placeholders: AWS service zone endpoint, Azure service zone endpoint, and OpenStack service zone endpoint.
- Prometheus query layer: placeholder queries for `probe_success`, `probe_http_status_code`, and probe duration metrics.
- Evidence store: `evidence/L3-service-operations/S030-blackbox-endpoint-probe-validation/`.

## Probe Flow

1. The reviewer identifies the target endpoint category.
2. Blackbox Exporter probes the placeholder endpoint using an approved probe module.
3. Prometheus records probe metrics.
4. The reviewer records sanitized command plans, query plans, status results, logs, and screenshots.

No endpoint address in this scenario should be a real public IP, real DNS record, or account-specific value.
