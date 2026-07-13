# Prerequisites

## Static Mode

- PowerShell capable of running `tools/validate-nginx-reverse-proxy.ps1`.
- The four `traffic-management/` baseline artifacts.
- The three marked, sanitized sample evidence files.
- Existing S019 security-header and S023 Ingress boundaries understood.

Static mode requires no Nginx binary, curl, DNS record, live service, credential, network access, or TLS material.

## Optional LiveHttp Mode

- Deliberate operator approval to contact a safe target.
- Both `-LiveHttp` and a non-credentialed absolute HTTP(S) `-TargetUrl`.
- A target where a HEAD request is safe.

The target must not contain embedded user information. The validator sends no authorization or cookie header and stores no target or response content.
