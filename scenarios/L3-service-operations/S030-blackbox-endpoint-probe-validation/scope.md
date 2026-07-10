# Scope

## Included

- Blackbox Exporter service status validation plan.
- Blackbox probe module placeholder validation plan.
- Kubernetes Web service endpoint probe plan.
- Kubernetes API service endpoint probe plan.
- Ingress host endpoint probe plan.
- Nginx Reverse Proxy endpoint probe plan.
- AWS service zone endpoint placeholder probe plan.
- Azure service zone endpoint placeholder probe plan.
- OpenStack service zone endpoint placeholder probe plan.
- Health check endpoint probe plan.
- HTTP status code validation plan.
- Response duration and latency validation plan.
- Prometheus `probe_success` and `probe_http_status_code` query evidence plan.

## Target Endpoint Categories

- Kubernetes Web service endpoint.
- Kubernetes API service endpoint.
- Ingress host endpoint.
- Nginx Reverse Proxy endpoint.
- AWS service zone endpoint.
- Azure service zone endpoint.
- OpenStack service zone endpoint.
- Health check endpoint.

## Excluded

- Real Blackbox Exporter configuration implementation.
- Real Prometheus scrape configuration implementation.
- Real DNS records, public IPs, TLS keys, certificates, credentials, secrets, private keys, tfstate, kubeconfig, or account-specific values.
- TLS certificate validation.
- Prometheus target discovery validation, which is handled in S028.
- Grafana dashboard validation, which is handled in S029.
- Load balancing health check validation, which is handled in S025.
- Ingress routing validation, which is handled in S023.
- Nginx Reverse Proxy forwarding validation, which is handled in S024.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
