# Failure Condition

S025 fails if:

- A required artifact or sample is missing.
- The pool, either backend, health path, expected status, timeout, retry, or unhealthy threshold is missing.
- Load-balancer evidence lacks 200 OK or contains 5xx, refusal, timeout, unhealthy, or no-healthy-upstream indicators.
- Either backend-specific sample is absent or unhealthy.
- TLS material, credentials, tokens, cookies, authorization values, real domains, concrete URLs, or numeric addresses are detected.
- The example claims unsupported active health checking or automatic failover.
- LiveHttp lacks required targets, cannot connect, times out, or returns an unaccepted status.
- Nginx/curl is invoked by default or routing state is changed.

Live 401/403 is a warning requiring operator review, not proof of backend failure.
