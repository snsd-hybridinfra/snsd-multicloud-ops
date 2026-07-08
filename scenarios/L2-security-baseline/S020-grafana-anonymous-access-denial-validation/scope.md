# Scope

## Included

- Grafana anonymous access configuration validation plan.
- Grafana login requirement validation plan.
- Dashboard unauthenticated access denial validation plan.
- Anonymous API access denial validation plan.
- Admin credential handling rule.
- Monitoring Zone access boundary placeholder.
- Grafana configuration evidence collection plan.
- Grafana access log evidence collection plan.

## Excluded

- Real Grafana configuration implementation.
- Grafana admin passwords, credentials, secrets, tfstate, kubeconfig, private keys, or account-specific files.
- Real public IP addresses or production endpoints.
- Grafana dashboard validation, which is handled in S029.
- Prometheus target discovery validation, which is handled in S028.
- Observability validation beyond anonymous access denial, which is handled in S028 to S030.
- TLS implementation.

## Placeholder Rules

Use placeholders such as `<grafana-endpoint>`, `<grafana-admin-user>`, and `<monitoring-zone-cidr>`.
