# Architecture

## Relevant Components

- Control Plane: records validation commands and evidence.
- Nginx reverse proxy: planned response header enforcement point.
- Ingress host: placeholder entry point for service exposure.
- Service endpoint: placeholder upstream service target.
- Access logs: source for request and response validation context.
- Error logs: source for syntax or runtime issue evidence.

## Header Model

- `X-Content-Type-Options` must be planned for MIME sniffing reduction.
- `X-Frame-Options` must be planned for clickjacking protection.
- `Referrer-Policy` must be planned for referrer leakage control.
- `Content-Security-Policy` must be documented as a placeholder policy until service-specific directives are approved.
- `Strict-Transport-Security` must remain a placeholder unless TLS is enabled later.
- Server version exposure must be reduced with `server_tokens off` or equivalent.

## Boundary Notes

This scenario validates the Nginx security header baseline only. Real TLS, ingress routing, and load balancing are separate scenario responsibilities.
