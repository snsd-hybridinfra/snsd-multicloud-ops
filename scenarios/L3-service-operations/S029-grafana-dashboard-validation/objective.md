# Objective

Validate that SNSD Multi-Cloud Ops defines safe Grafana artifacts for infrastructure, Kubernetes, DB replication, reverse proxy, load balancer, Blackbox, and service-availability visibility.

S029 validates the datasource placeholder, parseable dashboard JSON, ten required panels, PromQL placeholders, rule matrix, and sanitized API samples. Optional live checks retain only sanitized match judgments.

S020 owns anonymous-access denial, S028 owns Prometheus target discovery, S030 owns Blackbox probing, S027 owns DB lag semantics, and S025 owns load-balancing health checks.
