# Web Pod Failure Recovery Validation

This runbook validates a controlled, non-production Web Pod recovery workflow using sanitized evidence. Static validation never contacts Kubernetes or injects failure.

## Controlled Recovery Model

Pre-failure health is the required baseline for every controlled recovery review.

1. Verify `<deployment-name>` in `<namespace>` preserves `<replica-count>` desired replicas.
2. Confirm at least one `<pod-name>` is Running and Ready before failure.
3. Record the separately authorized failure injection placeholder; automation does not execute it.
4. Detect the original Pod terminating/disappearing.
5. Detect `<replacement-pod-name>` creation.
6. Confirm the replacement reaches Running and Ready.
7. Confirm Deployment desired/available replica consistency and successful rollout.
8. Confirm `<service-name>` retains at least one endpoint represented without a real address.
9. Compare measured recovery time with `<recovery-time-threshold-seconds>` when a disposable-lab measurement is available.

Service reachability uses `<endpoint-url-placeholder>` only as a conceptual continuity reference. S040 owns final service-health validation.

## Evidence Model

Evidence is stored beneath `<evidence-path>` after removing cluster names, endpoints, IPs, UIDs, tokens, certificates, and secrets. Static mode parses committed samples. Optional LiveKubectl is explicitly requested and read-only; it cannot delete, apply, patch, edit, scale, restart, cordon, drain, taint, or mutate resources.
