# Scope

## Included

- Prometheus metric query placeholder.
- Node metric dataset collection placeholder.
- Kubernetes workload metric dataset collection placeholder.
- MariaDB metric dataset collection placeholder.
- Blackbox probe metric dataset collection placeholder.
- Nginx or service endpoint metric placeholder.
- Dataset schema definition.
- Dataset timestamp validation.
- Dataset label consistency validation.
- Dataset export placeholder.
- Dataset evidence collection plan.

## Target Metric Categories

- Node CPU usage placeholder.
- Node memory usage placeholder.
- Node disk usage placeholder.
- Network receive/transmit metric placeholder.
- Kubernetes pod restart count placeholder.
- Kubernetes pod readiness metric placeholder.
- MariaDB availability or replication metric placeholder.
- Blackbox `probe_success` metric placeholder.
- Blackbox `probe_http_status_code` metric placeholder.
- HTTP endpoint latency metric placeholder.

## Required Dataset Fields

- `timestamp`
- `metric_name`
- `metric_value`
- `target_job`
- `target_instance`
- `provider_or_zone` placeholder
- `component_type` placeholder
- `collection_window` placeholder
- `anomaly_label` placeholder for future use
- `notes` placeholder

## Dataset Quality Model

- `DATASET_READY`: Required metric fields and timestamps are present.
- `DATASET_PARTIAL`: Dataset exists but some metric categories are missing.
- `DATASET_INVALID`: Dataset format, timestamp, or label structure is invalid.
- `DATASET_EMPTY`: Dataset contains no usable metric records.
- `DATASET_INCONCLUSIVE`: Required collection evidence is missing.

## Excluded

- Real ML model training.
- Real anomaly detection.
- Real Prometheus output or real dataset records in this skeleton.
- SIEM, Wazuh, Elastic, EDR, SOAR, threat hunting, packet payload analysis, malware detection, deep learning tooling, or production-grade ML security operations.
- Real public IPs, cloud account IDs, credentials, tokens, API keys, secrets, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values.
- ML anomaly detection validation, handled in S048.
- ML anomaly report generation, handled in S049.
- Prometheus target discovery validation, handled in S028.
- Grafana dashboard validation, handled in S029.
- Blackbox endpoint probe validation, handled in S030.
- Final evidence report generation, handled in S050.
