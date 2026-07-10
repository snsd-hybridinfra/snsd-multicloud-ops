# Architecture

## Relevant Components

- Grafana endpoint: represented by `<grafana-endpoint>`.
- Prometheus datasource: represented by `<prometheus-datasource>`.
- Dashboard placeholders: represented by `<dashboard-name>` and `<service-health-dashboard>`.
- Panel placeholders: represented by `<panel-name>`.
- Prometheus target discovery: prerequisite evidence source from S028.
- Screenshot evidence: planned proof of dashboard visibility and datasource rendering.

## Dashboard Model

- Grafana must be reachable through the approved access path.
- Login requirement is referenced from S020 and not reimplemented here.
- Prometheus datasource must exist and connect successfully.
- Dashboard categories must map to expected infrastructure, cloud, Kubernetes, database, blackbox, and service health views.
- Panels must render non-empty data for the selected placeholder time range.
- Screenshots must show dashboard visibility without exposing secrets or real public endpoints.

## Boundary Notes

This scenario validates dashboard visibility and datasource rendering only. Anonymous access denial, target discovery, blackbox probing, and alerting are separate or excluded responsibilities.
