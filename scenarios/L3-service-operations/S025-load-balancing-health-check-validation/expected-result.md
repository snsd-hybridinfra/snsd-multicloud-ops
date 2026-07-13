# Expected Result

S025 passes when the backend pool and two symbolic members exist, `/health` and expected status are defined, passive retry/timeouts/unhealthy threshold are complete, both backend samples and the load-balancer sample show 200 OK, and safety checks find no concrete or sensitive content.

Static mode performs no process or network execution. LiveHttp accepts 200/204, warns for 401/403, and fails for invalid/missing targets, connection/timeout errors, 5xx, or another unaccepted status.

Only aggregate results, indexed live statuses, and timestamps may be retained. No automatic failover or production active-health capability is inferred.
