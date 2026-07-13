# Architecture

## Validation Flow

```text
Local PowerShell validator
  -> Nginx security-header policy
  -> required-header rule matrix
  -> non-production config snippet
  -> directive, value, always, and safety checks
  -> evidence log and summary
```

## Header Model

- Disclosure reduction: `server_tokens off`.
- Browser protections: frame, content type, referrer, CSP, HSTS, and permissions policy.
- Error responses: `always` on every required `add_header` directive.
- Service-specific controls remain placeholders pending separate implementation review.

## Trust Boundary

All inspection is repository-local; no Nginx process, host, upstream, service endpoint, TLS asset, or network path participates.
