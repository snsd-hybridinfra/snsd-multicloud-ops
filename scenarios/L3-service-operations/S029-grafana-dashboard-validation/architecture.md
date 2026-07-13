# Architecture

```text
Prometheus Placeholder datasource
  -> SNSD Ops Overview Placeholder
  -> 10 infrastructure/service panels
  -> static dashboard and sanitized API evidence
```

Static validation checks the provisioning YAML and dashboard JSON. LiveGrafana queries only search and datasource endpoints after explicit request. It stores only placeholder-title match, panel-count-not-queried, and known datasource match judgments.

Authentication-required responses are WARN under S020. No API token or raw live response is used.
