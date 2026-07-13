# ML Anomaly Report Generation Validation — Non-Production

S049 statically validates a human-reviewable report derived from S047 dataset evidence and S048 detection evidence, then maps it to S050. Inputs and metadata use `<dataset-id-placeholder>`, `<detection-run-id-placeholder>`, `<anomaly-id-placeholder>`, `<report-id-placeholder>`, `<report-file-placeholder>`, `<feature-name-placeholder>`, `<metric-name-placeholder>`, `<anomaly-score-placeholder>`, `<reviewer-role-placeholder>`, `<recommendation-placeholder>`, and `<evidence-path>`.

Required content includes metadata, anomaly/warning/review counts, top candidates, affected groups, deterministic operational interpretation, operator recommendations, evidence references, human review, quality checks, and a conservative final judgment.

Live Prometheus/Grafana queries, SIEM/Wazuh/EDR/firewall ingestion, packet capture/payload analysis, malware detection, threat hunting, deep learning, LLM-based analysis, model training/deployment, automated blocking, SOAR, production SOC alerting, and automatic incident creation are out of scope.
