# Objective

Validate that SNSD Multi-Cloud Ops defines safe Blackbox HTTP 2xx/TCP connect probing and can classify sanitized probe metrics without external access by default.

S030 validates modules, scrape relabeling, metric thresholds, success/warning/failure fixtures, and Prometheus query sample JSON. Failure detection is proven with a negative fixture.

S028 owns Prometheus discovery, S029 dashboards, S025 load-balancer health, S023 Ingress, S024 reverse proxy, and S040 final recovery health.
