# Architecture

## Relevant Components

- Control Plane: planned origin for reverse proxy validation commands.
- AWS reverse proxy: represented by `<aws-reverse-proxy>`.
- Azure reverse proxy: represented by `<azure-reverse-proxy>`.
- OpenStack reverse proxy: represented by `<openstack-reverse-proxy>`.
- Kubernetes Ingress endpoint: represented by `<ingress-endpoint>`.
- Upstream service: represented by `<upstream-service>`.
- Nginx access and error logs: planned evidence sources for request forwarding and failure analysis.

## Forwarding Model

- Each provider-level reverse proxy must forward traffic to the intended `<ingress-endpoint>`.
- Upstream mappings must identify `<upstream-service>` without real public IPs.
- Nginx syntax validation must occur before response validation.
- HTTP response validation must confirm expected forwarding behavior.
- Health checks are placeholders only and are fully validated in S025.
- Access and error logs must support request and failure evidence.

## Boundary Notes

This scenario validates Nginx reverse proxy forwarding only. Security headers, ingress routing, load balancing health checks, and TLS implementation are separate scenario responsibilities.
