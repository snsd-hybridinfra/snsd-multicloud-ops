# Scope

## Included

- Static review of the Nginx reverse proxy baseline, example, rule matrix, commands, and sanitized samples.
- Upstream, server, listener, symbolic `server_name`, location, and `proxy_pass` validation.
- Host, X-Real-IP, X-Forwarded-For, and X-Forwarded-Proto forwarding validation.
- Connect, send, and read timeout validation.
- Optional explicit HEAD request with `-LiveHttp -TargetUrl`.
- Generated sanitized log and summary evidence.

## Excluded

- Nginx start, stop, restart, reload, installation, or configuration changes.
- Default-mode Nginx, curl, or network execution.
- Credentials, cookies, tokens, authorization headers, TLS private keys, certificates, real domains, and numeric addresses.
- Response body or target URL persistence.
- Nginx security header validation (S019), Ingress routing (S023), load-balancing health checks (S025), public exposure control (S014/S015/S016), and DNS/hostname modeling (S009).

## Placeholder Rules

Use only `<reverse-proxy-host>`, `<public-service-domain>`, `<backend-service>`, `<backend-service-port>`, `<backend-health-path>`, `<upstream-name>`, and `<evidence-path>` or their clearly marked example variants.
