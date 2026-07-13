# Scope

## Included

- Static baseline, HTTP/TCP modules, Prometheus scrape placeholder, nine-area matrix, commands, and four samples.
- `probe_success`, HTTP status, duration, DNS/connect placeholders, timeout/refusal/missing endpoint rules.
- Normal, warning, and negative failure fixture classification.
- Optional explicit exporter probe request with sanitized metric retention.
- Auth/TLS, URL/domain/address, account/UUID, and execution safety.

## Excluded

- Prometheus/Blackbox start, reload, config mutation, or default live query.
- Real endpoint/Prometheus/Blackbox/Kubernetes URLs, DNS, IPs, credentials, tokens, cookies, authorization, or TLS material.
- Grafana (S029), target discovery (S028), and load-balancer configuration (S025).
