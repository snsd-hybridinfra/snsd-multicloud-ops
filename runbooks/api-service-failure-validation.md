# API Service Failure Validation

S032 validates a controlled API failure and recovery workflow without changing a cluster in the default **Static mode**.

## Controlled API failure model

1. Record the pre-failure Deployment `<api-deployment-name>`, Pod `<api-pod-name>`, Service `<api-service-name>`, endpoint, and HTTP health state in `<namespace>`.
2. A separately authorized operator may perform a **MANUAL FAULT INJECTION ONLY** in a disposable lab. The validator never deletes a Pod or scales a Deployment.
3. Record an API Pod/Deployment failure signal, endpoint loss/degradation, and an HTTP 5xx, timeout, or connection-refused signal.
4. Record the recovery action placeholder, replacement Pod `<replacement-api-pod-name>`, non-empty endpoint, healthy status `<expected-status-code>`, and rollout state.
5. Compare a sanitized elapsed value with `<recovery-time-threshold-seconds>` when available and store evidence under `<evidence-path>`.

The health target is `http://<api-url-placeholder>/<api-health-endpoint-placeholder>`. No real URL, payload, response body, cookie, API key, bearer token, or authorization value belongs in evidence.

## Interpretation

- `200` or a documented healthy status means the API is available.
- `<failure-status-code>` such as `5xx` means the route answered but the API path is unhealthy.
- Timeout or connection refused means the route or workload is unavailable.
- An empty Kubernetes Service endpoint means no ready backend is attached.
- A recovered API requires a Running/Ready replacement Pod, non-empty endpoint, healthy HTTP status, and successful rollout.

## Validation modes

- **Static**: parses committed non-production evidence; no kubectl, curl, network, kubeconfig, or cluster access.
- **LiveKubectl**: explicit, read-only Deployment/Pod/Service/endpoint/rollout queries only.
- **LiveHttp**: explicit unauthenticated HEAD request; stores only status, judgment, and timestamp.

S031 owns Web Pod recovery, S030 owns Blackbox probing, S035 owns load-balancer failure, and S040 owns final post-recovery health.
