# Prerequisites

## Static Mode

- PowerShell and `tools/validate-load-balancing-health-check.ps1`.
- Four `traffic-management/` artifacts and three sanitized samples.
- Awareness that S024 owns reverse proxy routing and S030 owns external probing.

No Nginx binary, curl, network, DNS, credential, or TLS material is required.

## Optional LiveHttp Mode

- Explicit approval for safe health targets.
- `-LiveHttp`, one `-LoadBalancerHealthUrl`, and one or more `-BackendHealthUrls`.
- Absolute HTTP(S) targets without embedded user information.

The validator sends no cookies or authorization and stores neither targets nor response content.
