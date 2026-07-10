# Prerequisites

- Repository foundation and evidence directory structure exist.
- S023 Ingress routing validation is planned before Ingress endpoint probing.
- S024 Nginx Reverse Proxy validation is planned before reverse proxy endpoint probing.
- S025 load balancing health check validation is planned before comparing probe results with health check behavior.
- S028 Prometheus target discovery validation is planned before Prometheus query evidence is collected.
- S029 Grafana dashboard validation is planned before dashboard views are used for probe visualization.
- Placeholder endpoint names are available for `<web-endpoint>`, `<api-endpoint>`, `<ingress-host>`, `<reverse-proxy-host>`, and `<health-endpoint>`.
- No real Blackbox Exporter configuration, Prometheus configuration, credentials, secrets, TLS keys, certificates, kubeconfig, tfstate, or account-specific values are required for this documentation skeleton.
