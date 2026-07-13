# Scope

## Included

- Static baseline, scrape example, six-job rule matrix, command reference, and three samples.
- Five symbolic static targets plus Kubernetes endpoint discovery.
- Valid targets/up JSON and sanitized job-label parsing.
- Required job existence, target `up`, and query value `1` checks.
- Optional explicit `/api/v1/targets` and `/api/v1/query?query=up` checks.
- Authentication/TLS, endpoint/domain/address, credential/token/cookie, account, and execution safety.

## Excluded

- Prometheus start, stop, reload, config change, or default network access.
- Grafana dashboards (S029) and Blackbox probe behavior (S030).
- Real Prometheus/Kubernetes endpoints, targets, clusters, labels, credentials, tokens, cookies, datasource secrets, or TLS material.
- Raw live API response/labels/endpoints in evidence.
