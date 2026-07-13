# Prerequisites

## Static

- PowerShell and `tools/validate-grafana-dashboard.ps1`.
- Five dashboard artifacts and three sanitized JSON samples.
- No Grafana process, credentials, API token, curl, endpoint, or network.

## Optional LiveGrafana

- Explicit approval with `-LiveGrafana -GrafanaUrl`.
- Absolute HTTP(S) URL without user information.
- Optional placeholder `-DashboardTitle`.

No credentials/cookies/authorization are sent or requested, and URL/raw responses are not stored.
