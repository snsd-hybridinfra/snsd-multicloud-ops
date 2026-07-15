# Validation

Scenario: S025-load-balancing-health-check-validation
Level: L3-service-operations
Mode: Static
Date: 2026-07-13
Overall status: PASS

| Check ID | Check Description | Expected Condition | Actual Result | Status | Evidence File |
|---|---|---|---|---|---|
| V001 | Required baseline files | Four artifacts exist. | All exist. | PASS | summary |
| V002 | Sample evidence files | Three samples exist. | All exist. | PASS | sample logs |
| V003 | Health-check baseline | Required model/settings/modes exist. | Complete. | PASS | baseline; summary |
| V004 | Backend pool definition | Pool has both symbolic backends. | Complete. | PASS | config; summary |
| V005 | Health endpoint and expected status | `/health`, proxy, status are defined. | Complete. | PASS | config/baseline; summary |
| V006 | Timeout retry and unhealthy handling | Retry, tries, timeouts, threshold exist. | Complete. | PASS | config/baseline; summary |
| V007 | Health-check rule matrix | Ten controls and columns exist. | Complete. | PASS | matrix; summary |
| V008 | Safe command reference | Five examples exist. | Complete. | PASS | command example; summary |
| V009 | Load-balancer health evidence | Marked 200 without failure indicator. | Healthy. | PASS | LB sample; summary |
| V010 | Backend health evidence | Both backends show 200 without failure. | Healthy. | PASS | backend sample; summary |
| V011 | Access-log health evidence | Symbolic `/health` 200 exists. | Sanitized. | PASS | access sample; summary |
| V012 | TLS material safety | No TLS material/path. | None detected. | PASS | log; summary |
| V013 | Credential and header safety | No sensitive content. | None detected. | PASS | log; summary |
| V014 | Address and domain safety | No concrete target. | None detected. | PASS | log; summary |
| V015 | Active-health and failover boundary | Passive-only scope explicit. | Confirmed. | PASS | baseline/config; summary |
| V016 | Execution safety boundary | No Nginx/curl; guarded HEAD only. | Confirmed. | PASS | script; summary |
| V017 | Validation mode and live health result | Static has no network/failover. | Completed safely. | PASS | log; summary |

## Generated Result

- Critical failures: 0
- Warnings: 0
- Optional LiveHttp: NOT_RUN
- Final judgment: PASS
- No Nginx, curl, network, failover, configuration change, target URL, response content, credential, cookie, token, TLS material, domain, or numeric address was used or stored.

## Real Virtual-Lab Evidence Validation - 2026-07-15

Validation mode: Real virtual lab evidence, sanitized

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| LAB-001 | Initial backend replicas | At least two backend Pods exist and are Ready. | normal-state log and summary | PASS |
| LAB-002 | Initial Service endpoints | Service contains at least two ready endpoints. | normal-state log and summary | PASS |
| LAB-003 | Initial request distribution | Requests succeed and identify both backends. | normal-state log and summary | PASS |
| LAB-004 | Controlled readiness failure | One running Pod becomes NotReady without deletion. | unhealthy-exclusion log and summary | PASS |
| LAB-005 | Unhealthy backend exclusion | NotReady Pod is absent from Service-ready endpoints. | unhealthy-exclusion log and summary | PASS |
| LAB-006 | Healthy traffic continuity | Requests continue through the healthy backend. | unhealthy-exclusion log and summary | PASS |
| LAB-007 | NotReady backend traffic | No degraded-state response identifies the NotReady backend. | unhealthy-exclusion log and summary | PASS |
| LAB-008 | Readiness restoration | Target Pod returns to Ready without replacement. | restoration log and summary | PASS |
| LAB-009 | Endpoint restoration | Service returns to two ready endpoints. | restoration log and summary | PASS |
| LAB-010 | EndpointSlice restoration | Both final EndpointSlice conditions report ready and serving. | restoration log and summary | PASS |
| LAB-011 | Post-recovery distribution | Requests again identify both backends. | restoration log and summary | PASS |
| LAB-012 | Sensitive-data handling | Raw identifiers, addresses, bodies, credentials, and secrets are absent. | all dated evidence | PASS |

Final judgment: **READY**

Validated traffic path:

`Client -> Ingress Controller -> Kubernetes Service -> Ready backend endpoint`

The controlled target remained `Running` but became `0/1`; Kubernetes removed
it from the Service-ready endpoint set. No Pod deletion or container crash was
used. Full Pod failure and Deployment self-healing remain separately owned by
S031 Web Pod Failure Recovery.

Evidence:

- `logs/20260715-S025-load-balancing-normal-state.sanitized.txt`
- `logs/20260715-S025-unhealthy-backend-exclusion.sanitized.txt`
- `logs/20260715-S025-backend-health-restoration.sanitized.txt`
- `configs/20260715-S025-load-balancing-health-check-validation-summary.md`

Raw output, response bodies, kubeconfig, service-account tokens, certificates,
private keys, passwords, cookies, Authorization headers, credentials, and
secrets are not committed.
