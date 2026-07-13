# Scope

## Included

- Nginx security header policy, rule matrix, and config snippet validation.
- `server_tokens off`, required header presence, exact value, placeholder, and `always` checks.
- Legacy X-XSS-Protection guidance and static-validation limitation documentation.
- TLS path/material, real domain/address, credential, identifier, and active-command safety checks.

## Excluded

- Running or reloading Nginx, modifying configuration, connecting to hosts, or curling endpoints.
- Live response, TLS, inheritance, upstream, or production behavior validation.
- Reverse proxy operation (S024), ingress routing (S023), load-balancer health (S025), manifest policy (S044), and public exposure controls (S014-S016).
