# Prerequisites

## Static Mode

- PowerShell and `tools/validate-prometheus-target-discovery.ps1`.
- Four baseline artifacts and three sanitized sample artifacts.
- No Prometheus process, endpoint, credentials, curl, kubeconfig, or network access.

## Optional LivePrometheus Mode

- Explicit approval and `-LivePrometheus -PrometheusUrl`.
- Absolute HTTP(S) URL without embedded user information.
- An API that can safely receive unauthenticated GET requests.

The validator sends no credentials/cookies/authorization and does not save the URL or raw API data.
