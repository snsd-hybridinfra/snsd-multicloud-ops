# ML Metric Feature Catalog — Sample / Non-Production

| Feature Group | Feature Name | Source Metric Placeholder | Operational Meaning | Expected Range Placeholder | Anomaly Interpretation Placeholder | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|---|
| HTTP service health | http_health | `<http-health-metric>` | Endpoint availability | `<expected-range>` | `<anomaly-interpretation>` | S040 | `<evidence-path>` |
| API service latency | api_latency | `<api-latency-metric>` | API response latency | `<expected-range>` | `<anomaly-interpretation>` | S040 | `<evidence-path>` |
| Load balancer health | load_balancer_health | `<lb-health-metric>` | Backend health | `<expected-range>` | `<anomaly-interpretation>` | S040 | `<evidence-path>` |
| Kubernetes workload readiness | workload_readiness | `<workload-ready-metric>` | Ready workload ratio | `<expected-range>` | `<anomaly-interpretation>` | S028 | `<evidence-path>` |
| Kubernetes restart count | restart_count | `<restart-count-metric>` | Restart activity | `<expected-range>` | `<anomaly-interpretation>` | S036 | `<evidence-path>` |
| CPU utilization | cpu_utilization | `<cpu-metric>` | Compute saturation | `<expected-range>` | `<anomaly-interpretation>` | S028 | `<evidence-path>` |
| Memory utilization | memory_utilization | `<memory-metric>` | Memory pressure | `<expected-range>` | `<anomaly-interpretation>` | S028 | `<evidence-path>` |
| Disk utilization | disk_utilization | `<disk-metric>` | Storage pressure | `<expected-range>` | `<anomaly-interpretation>` | S028 | `<evidence-path>` |
| Network throughput | network_throughput | `<network-metric>` | Traffic volume | `<expected-range>` | `<anomaly-interpretation>` | S028 | `<evidence-path>` |
| Prometheus target availability | target_availability | `<target-up-metric>` | Target discovery health | `<expected-range>` | `<anomaly-interpretation>` | S028, S036 | `<evidence-path>` |
| Blackbox probe success | probe_success | `<probe-success-metric>` | External probe outcome | `<expected-range>` | `<anomaly-interpretation>` | S030 | `<evidence-path>` |
| Database availability | database_availability | `<database-up-metric>` | Database health | `<expected-range>` | `<anomaly-interpretation>` | S040 | `<evidence-path>` |
| Replication lag | replication_lag | `<replication-lag-metric>` | Replica delay | `<expected-range>` | `<anomaly-interpretation>` | S040 | `<evidence-path>` |
| Backup/restore reference health | recovery_health | `<recovery-health-metric>` | Recovery reference state | `<expected-range>` | `<anomaly-interpretation>` | S040 | `<evidence-path>` |

Grafana dashboard context maps to S029. The validated catalog feeds S048 anomaly detection and S049 anomaly report generation.
