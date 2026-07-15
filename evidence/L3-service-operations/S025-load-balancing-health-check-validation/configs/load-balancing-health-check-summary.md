# Load Balancing Health Check Summary

- Scenario: S025-load-balancing-health-check-validation
- Generated: 2026-07-15T09:33:21+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Backend pool definition check result: **PASS**
- Health endpoint check result: **PASS**
- Timeout / retry / unhealthy threshold check result: **PASS**
- Evidence parsing result: **PASS**
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required baseline files | PASS | Baseline, rule matrix, upstream example, and command reference exist. |
| V002 | Sample evidence files | PASS | Load-balancer, backend, and access-log samples exist. |
| V003 | Health-check baseline | PASS | Path, pool, health settings, evidence, manual recovery, and validation modes are documented. |
| V004 | Backend pool definition | PASS | The symbolic pool contains both backend placeholders. |
| V005 | Health endpoint and expected status | PASS | The /health route, pool proxy, and expected status placeholder are defined. |
| V006 | Timeout retry and unhealthy handling | PASS | Passive retry, retry count, three timeouts, and unhealthy threshold are defined. |
| V007 | Health-check rule matrix | PASS | All ten controls and required columns are documented. |
| V008 | Safe command reference | PASS | All five symbolic command examples exist. |
| V009 | Load-balancer health evidence | PASS | The marked sample contains 200 OK and no failure indicator. |
| V010 | Backend health evidence | PASS | Both symbolic backends are marked 200 OK with no failure indicator. |
| V011 | Access-log health evidence | PASS | The sanitized access sample contains a symbolic /health request and 200 status. |
| V012 | TLS material safety | PASS | No certificate, key, or TLS path/material exists. |
| V013 | Credential and header safety | PASS | No credential, token, cookie, authorization value, auth directive, or secret assignment exists. |
| V014 | Address and domain safety | PASS | No numeric address, real domain, or concrete URL exists. |
| V015 | Active-health and failover boundary | PASS | Passive evidence scope is explicit and no active-health directive is claimed. |
| V016 | Execution safety boundary | PASS | Nginx and curl are never invoked; guarded live mode uses cookie-free HEAD requests. |
| V017 | Validation mode and live health result | PASS | Static mode completed without running Nginx, curl, failover, or a network request. |

## Safety Boundary

Static mode performs repository-side validation only. LiveHttp requires explicit load-balancer and backend URLs, sends HEAD requests without cookies or authorization, stores indexed statuses only, and never performs failover.
