# Scope

## Included

- Metric dataset input validation reference.
- Baseline metric behavior placeholder.
- Statistical anomaly detection placeholder.
- Threshold-based anomaly detection placeholder.
- Node resource anomaly placeholder.
- Kubernetes workload anomaly placeholder.
- MariaDB metric anomaly placeholder.
- Blackbox probe anomaly placeholder.
- Endpoint latency anomaly placeholder.
- Anomaly judgment model.
- Anomaly evidence collection plan.

## Target Anomaly Categories

- CPU usage spike placeholder.
- Memory usage spike placeholder.
- Disk usage growth placeholder.
- Network traffic deviation placeholder.
- Pod restart count increase placeholder.
- Pod readiness degradation placeholder.
- DB availability or replication metric anomaly placeholder.
- Blackbox `probe_success` failure pattern placeholder.
- HTTP status code anomaly placeholder.
- Endpoint latency increase placeholder.

## Required Detection Inputs

- Dataset file placeholder.
- Metric name.
- Metric value.
- Timestamp.
- Target job.
- Target instance.
- Baseline window.
- Detection window.
- Threshold or anomaly score.
- Detection result.
- Review note placeholder.

## Anomaly Detection Judgment Model

- `ANOMALY_NOT_DETECTED`: Metric behavior remains within expected baseline.
- `ANOMALY_DETECTED`: Metric behavior exceeds defined anomaly threshold.
- `ANOMALY_WARNING`: Metric behavior is abnormal but requires human review.
- `ANOMALY_INCONCLUSIVE`: Dataset, baseline, or detection evidence is insufficient.
- `ANOMALY_OUT_OF_SCOPE`: Event requires SIEM, EDR, packet, log, malware, or threat hunting analysis.

## Excluded

- Production ML training.
- Deep learning.
- Real ML output or real dataset records in this skeleton.
- AI-based intrusion detection, malware detection, packet payload analysis, EDR, SIEM, SOAR, threat hunting capability, automatic response, automatic blocking, or production-grade ML security operations.
- SIEM, Wazuh, Elastic, EDR, SOAR, threat hunting, packet payload analysis, malware detection, commercial security tooling, or new technologies.
- Real public IPs, cloud account IDs, credentials, tokens, API keys, secrets, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values.
- ML metric dataset collection, handled in S047.
- ML anomaly report generation, handled in S049.
- Final evidence report generation, handled in S050.
- Prometheus target discovery validation, handled in S028.
- Grafana dashboard validation, handled in S029.
- Blackbox endpoint probe validation, handled in S030.
