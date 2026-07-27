# ML Metric Feature Catalog — Sample / Non-Production

| Feature Group | Feature Name | Source Metric Placeholder | Operational Meaning | Expected Range Placeholder | Anomaly Interpretation Placeholder | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| HTTP service health | http_health | `<http-health-metric>` | Endpoint availability | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| API service latency | api_latency | `<api-latency-metric>` | API response latency | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Load balancer health | load_balancer_health | `<lb-health-metric>` | Backend health | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Kubernetes workload readiness | workload_readiness | `<workload-ready-metric>` | Ready workload ratio | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Kubernetes restart count | restart_count | `<restart-count-metric>` | Restart activity | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| CPU utilization | cpu_utilization | `<cpu-metric>` | Compute saturation | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Memory utilization | memory_utilization | `<memory-metric>` | Memory pressure | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Disk utilization | disk_utilization | `<disk-metric>` | Storage pressure | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Network throughput | network_throughput | `<network-metric>` | Traffic volume | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Prometheus target availability | target_availability | `<target-up-metric>` | Target discovery health | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case, retired-numbered-case | `<evidence-path>` |
| Blackbox probe success | probe_success | `<probe-success-metric>` | External probe outcome | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Database availability | database_availability | `<database-up-metric>` | Database health | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Replication lag | replication_lag | `<replication-lag-metric>` | Replica delay | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |
| Backup/restore reference health | recovery_health | `<recovery-health-metric>` | Recovery reference state | `<expected-range>` | `<anomaly-interpretation>` | retired-numbered-case | `<evidence-path>` |

Grafana dashboard context maps to retired-numbered-case. The validated catalog feeds retired-numbered-case anomaly detection and retired-numbered-case anomaly report generation.
