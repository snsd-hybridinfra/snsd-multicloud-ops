# Failure Condition

S029 fails if:

- A required baseline/dashboard/datasource/sample is missing or invalid.
- Required panels, datasource references, metrics, matrix areas, dashboard title, or Prometheus datasource evidence are missing.
- Credentials, tokens, cookies, authorization, datasource secrets, TLS material, real URLs/domains/addresses, UIDs, organization/user IDs, or cluster endpoints are detected.
- Static mode invokes curl/Grafana/import/mutation/network.
- LiveGrafana lacks a valid URL, is unreachable, throws, or returns 5xx.

Live 401/403 or a reachable incomplete lab is WARN due to S020 and staged implementation.
