# Scope

## Included

- Static baseline, matrix, Nginx upstream example, command reference, and sample review.
- Two symbolic backend members and a `/health` endpoint.
- Expected status, interval, timeout, retry/unhealthy threshold, and manual recovery model.
- Passive `proxy_next_upstream` routing evidence.
- Optional explicit load-balancer/backend HEAD checks.
- Sanitized generated log and summary.

## Excluded

- Nginx or load-balancer installation, start, stop, restart, reload, or modification.
- Automatic failover, automatic backend removal, Nginx Plus active health checks, and production HA claims.
- Default-mode Nginx, curl, or network execution.
- Real targets, domains, addresses, DNS, TLS material, credentials, tokens, cookies, authorization headers, and response bodies.
- S023, S024, S030, S031, and S035 responsibilities.

Only documented placeholders or their clearly marked example variants are permitted.
