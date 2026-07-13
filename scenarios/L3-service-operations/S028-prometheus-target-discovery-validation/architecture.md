# Architecture

## Discovery Model

```text
<prometheus-server>
  -> symbolic static targets: self/node/MariaDB/Nginx/Blackbox
  -> symbolic Kubernetes endpoints service discovery
  -> targets health = up
  -> up query value = 1
  -> sanitized evidence
```

## Validation Modes

Static mode reads config and samples. LivePrometheus requires `-PrometheusUrl`, validates an HTTP(S) URI without user information, queries two API paths with a cookie-free client, and retains only the six known job names plus health/up judgments.

No live URL, raw endpoint, arbitrary job/label, response body, authentication material, or configuration is persisted.
