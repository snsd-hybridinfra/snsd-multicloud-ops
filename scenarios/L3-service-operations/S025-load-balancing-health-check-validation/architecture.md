# Architecture

## Request and Health Path

`Client -> Load Balancing Layer -> Healthy Backend Service`

The symbolic `<backend-pool>` contains two backend placeholders. The example routes `/health` to the pool and uses open-source Nginx passive retry with explicit timeouts. Health samples establish backend-specific 200 evidence.

## Validation Flow

```text
Static -> inspect artifacts -> parse samples -> enforce safety -> aggregate evidence
LiveHttp -> require all target parameters -> send HEAD requests -> retain indexed statuses only
```

## Operational Boundary

An unhealthy observation supports a manual exclusion/recovery decision; it does not trigger failover. No active Nginx Plus health check, configuration mutation, target URL, header, body, or sensitive value is part of the evidence.
