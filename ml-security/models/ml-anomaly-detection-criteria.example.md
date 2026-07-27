# ML Anomaly Detection Criteria — Non-Production

| Detection Area | Input Evidence | Expected Normal Condition | Anomaly Condition | Score / Threshold Placeholder | Required Review | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|---|
| Prometheus target availability | `<evidence-path>` | up | down | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| Blackbox probe success | `<evidence-path>` | success | failure | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| HTTP status health | `<evidence-path>` | healthy | unhealthy | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| API latency | `<evidence-path>` | baseline | elevated | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTION_WARNING |
| Load balancer health | `<evidence-path>` | healthy | degraded | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| Kubernetes pod readiness | `<evidence-path>` | ready | degraded | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| Kubernetes restart count | `<evidence-path>` | baseline | elevated | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTION_WARNING |
| CPU utilization | `<evidence-path>` | baseline | elevated | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTION_WARNING |
| Memory utilization | `<evidence-path>` | baseline | elevated | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTION_WARNING |
| Disk utilization | `<evidence-path>` | baseline | elevated | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTION_WARNING |
| Database availability | `<evidence-path>` | available | unavailable | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| Replication lag | `<evidence-path>` | baseline | elevated | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_DETECTED |
| Backup/restore reference health | `<evidence-path>` | healthy | degraded | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_REVIEW_REQUIRED |
| Dataset quality reference | retired-numbered-case | DATASET_READY | incomplete | `<threshold-profile-placeholder>` | operator | retired-numbered-case | ANOMALY_EVIDENCE_INCOMPLETE |

Detection is retired-numbered-case, reporting is retired-numbered-case, and final evidence reporting is retired-numbered-case.
