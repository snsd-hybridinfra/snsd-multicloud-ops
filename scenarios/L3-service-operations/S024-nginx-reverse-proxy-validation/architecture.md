# Architecture

## Request Path

`Client -> Nginx Reverse Proxy -> Backend Service`

The example `server` and `location /` blocks route to a symbolic named `upstream`. Forwarding headers preserve Host, source-address context, proxy-chain context, and original scheme. Explicit connection, send, and read timeouts bound proxy operations.

## Validation Flow

```text
Static (default)
  -> read repository artifacts
  -> validate directives and safety
  -> parse sanitized samples
  -> write aggregate log and summary

LiveHttp (explicit)
  -> require operator-supplied TargetUrl
  -> validate HTTP(S) URI without user information
  -> send one cookie-free HEAD request
  -> retain status code and timestamp only
```

## Boundaries

No Nginx process or configuration is changed. No response body, response header, target URL, credential, cookie, key, certificate, domain, or numeric address is committed. S019, S023, and S025 retain ownership of security headers, Ingress, and load-balancer health respectively.
