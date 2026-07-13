# ML Anomaly Detection Validation — Non-Production

S048 statically validates metric-only anomaly evidence derived from the S047 `DATASET_READY` handoff. A run uses `<dataset-id-placeholder>`, `<dataset-file-placeholder>`, `<feature-name-placeholder>`, `<metric-name-placeholder>`, `<threshold-profile-placeholder>`, `<anomaly-score-placeholder>`, `<anomaly-id-placeholder>`, `<detection-run-id-placeholder>`, `<reviewer-role-placeholder>`, and `<evidence-path>`.

Required evidence includes dataset readiness, numeric features, a documented static threshold profile, numeric scores, valid decisions, false-positive review placeholders, operator review, S049 report mapping, and a conservative final judgment. This is deterministic sample scoring, not a trained model or live model execution.

Live Prometheus scraping, Grafana API queries, SIEM/Wazuh/EDR/firewall ingestion, packet capture or payload analysis, malware detection, threat hunting, deep-learning intrusion detection, LLM-based security analysis, model deployment, automated blocking, SOAR response, and production SOC alerting are out of scope.
