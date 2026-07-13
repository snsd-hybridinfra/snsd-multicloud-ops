# ML Metric Dataset Collection Validation — Non-Production

S047 validates a metric-only, sanitized dataset workflow through static local evidence. Metric source, query, job, service, and instance values remain `<metric-source-placeholder>`, `<prometheus-query-placeholder>`, `<scrape-job-placeholder>`, `<service-placeholder>`, and `<instance-placeholder>`.

## Controlled model

1. Define `<collection-window-placeholder>` and `<dataset-id-placeholder>`.
2. Validate `<dataset-file-placeholder>` against the schema.
3. Map every `<feature-name-placeholder>` to the feature catalog.
4. Restrict `<label-placeholder>` to `normal`, `suspected_anomaly`, or `unknown`.
5. Require synthetic or sanitized metric-only evidence at `<evidence-path>`.
6. Review missing values, duplicates, collection metadata, privacy, and secret safety.
7. Pass a validated dataset reference to S048; S049 owns human-reviewable anomaly reports.

Static validation differs from real scraping: the validator reads repository-local examples only. Live Prometheus scraping, Grafana API queries, SIEM ingestion, Wazuh ingestion, EDR telemetry ingestion, packet capture ingestion, packet payload analysis, malware detection, threat hunting, deep-learning intrusion detection, LLM-based security analysis, model training, model deployment, automated blocking, and production SOC alerting are out of scope.

No raw logs, production identifiers, monitoring exports, usernames, hostnames, IPs, domains, URLs, credentials, or secrets may be committed.
