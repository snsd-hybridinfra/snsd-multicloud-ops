# Expected Result

S025 passes when the backend pool and two symbolic members exist, `/health` and expected status are defined, passive retry/timeouts/unhealthy threshold are complete, both backend samples and the load-balancer sample show 200 OK, and safety checks find no concrete or sensitive content.

Static mode performs no process or network execution. LiveHttp accepts 200/204, warns for 401/403, and fails for invalid/missing targets, connection/timeout errors, 5xx, or another unaccepted status.

Only aggregate results, indexed live statuses, and timestamps may be retained. No automatic failover or production active-health capability is inferred.

## Sanitized Real-Lab Criteria

- `READY`: at least two Pods are initially Ready; one running Pod becomes NotReady; Service-ready endpoints exclude it; traffic continues through a healthy endpoint; restoration returns the Pod and endpoint membership.
- `PARTIAL`: readiness probes and multiple Pods exist, but exclusion, continuity, or restoration evidence is incomplete.
- `BLOCKED`: readiness cannot be failed, no healthy endpoint remains, requests fail despite a healthy backend, endpoint membership contradicts readiness, or workload configuration is broken.
- The readiness test does not delete Pods, induce a container crash, or validate Deployment self-healing; S031 owns Web Pod Failure Recovery.
- Raw response bodies and sensitive environment data are not retained.

## Current Result

`NOT_RUN`. No load balancer, Kubernetes workload, or backend service is
implemented in the confirmed lab.
