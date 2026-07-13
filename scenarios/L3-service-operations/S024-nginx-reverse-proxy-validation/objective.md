# Objective

Validate that SNSD Multi-Cloud Ops defines a non-production Nginx reverse proxy configuration that safely routes `Client -> Nginx Reverse Proxy -> Backend Service`.

S024 validates the example configuration, routing directives, forwarded headers, timeout baseline, rule matrix, and sanitized sample response evidence. Static validation does not run Nginx, curl, or network requests. Live HTTP validation is optional and only runs with explicit `-LiveHttp -TargetUrl` input.

S024 does not provision infrastructure, authenticate to providers, modify Nginx, inspect real DNS, store a live target, or manage TLS. S019 owns Nginx response security headers, S023 owns Ingress routing, and S025 owns load-balancing health checks.
