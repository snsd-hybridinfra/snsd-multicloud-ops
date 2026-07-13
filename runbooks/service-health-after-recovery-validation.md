# Service Health After Recovery Validation

S040 is the final L4 recovery health gate. It validates cross-domain sanitized evidence after recovery without performing recovery.

Required placeholders include `<web-service-url-placeholder>`, `<api-health-url-placeholder>`, `<load-balancer-url-placeholder>`, `<namespace-placeholder>`, `<deployment-name-placeholder>`, `<service-name-placeholder>`, `<pod-ip-placeholder>`, `<service-port-placeholder>`, `<db-primary-placeholder>`, `<db-replica-placeholder>`, `<prometheus-server-placeholder>`, `<scrape-job-name-placeholder>`, `<blackbox-target-placeholder>`, and `<evidence-path>`.

## Health gate

- Web, API, and load balancer return healthy status.
- Kubernetes rollout/Pods/endpoints are healthy.
- DB Primary and Replica are available; replication threads are healthy and lag is acceptable.
- Prometheus target is UP/up=1, Blackbox probe succeeds, and recovery-critical alerts are cleared.
- Backup/restore evidence references S038/S039, checksum verification, and consistency validation.

Static mode parses local evidence. Explicit LiveHttp, LiveKubectl, and LivePrometheus modes are read-only and retain sanitized judgments only. S040 performs no recovery, backup, restore, SQL, database connection, resource/configuration change, or failure injection and does not duplicate S031-S039 internals.
