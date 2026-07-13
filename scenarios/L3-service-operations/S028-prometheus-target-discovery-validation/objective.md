# Objective

Validate that SNSD Multi-Cloud Ops defines Prometheus scrape discovery for self-monitoring, node, MariaDB, Nginx, Blackbox, and Kubernetes service discovery and can evaluate sanitized target evidence.

S028 validates repository config, rule matrix, API references, valid JSON samples, required job presence, `health: up`, `up=1`, labels, and secret/endpoint safety. Live API access is optional and explicit.

S027 owns DB lag threshold semantics, S029 owns Grafana dashboards, S030 owns Blackbox probe behavior, S022 owns workloads, and S025 owns load-balancing health checks.
