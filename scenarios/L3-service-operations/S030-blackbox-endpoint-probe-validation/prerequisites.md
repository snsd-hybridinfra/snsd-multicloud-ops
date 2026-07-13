# Prerequisites

## Static

- PowerShell and `tools/validate-blackbox-endpoint-probe.ps1`.
- Five baseline artifacts and four sanitized fixtures.
- No exporter, Prometheus, curl, credential, DNS, TLS, or network requirement.

## Optional LiveBlackbox

- Explicit approval and both `-BlackboxExporterUrl` and `-TargetUrl`.
- Absolute HTTP(S) URLs without embedded user information.

No credentials/cookies/authorization are sent; URLs and raw response are not stored.
