# S024 Real Virtual-Lab Nginx Reverse Proxy Validation Summary

| Field | Result |
|---|---|
| Evidence source | Pasted terminal output |
| Validation mode | Real virtual lab, sanitized |
| Deployment availability | PASS - two desired replicas were ready and available |
| Pod readiness | PASS - both masked backend Pods were `1/1 Running` with zero restarts |
| Service selector | PASS - the masked Service selector aligned with the workload |
| Endpoint discovery | PASS - two ready masked endpoints were discovered on port 80; the v1 Endpoints deprecation warning is non-blocking |
| Ingress backend mapping | PASS - `<ingress-host-placeholder>` and `/` mapped to the masked Service on port 80 |
| HTTP response | PASS - the reverse-proxy request returned `200 OK` |
| Health endpoint | PASS - `/healthz` returned `200 OK` and the expected health marker |
| Backend Pod identification | PASS - masked backend identity markers were present |
| Repeated requests | PASS - 10 of 10 requests succeeded and both ready backends were observed five times each |
| Nginx log evidence | NOT PRESENT - no Nginx log output was included in the source |
| Traefik log evidence | NOT PRESENT - no Traefik log output was included in the source |
| Kubernetes events | PASS - normal rollout and lifecycle events were observed without failure events |
| Sensitive-data sanitization | PASS - all environment identifiers, addresses, selectors/hashes, image names, response identifiers, and backend names are masked or reduced to aggregate results |
| Raw output and response body | Not committed |
| Kubeconfig, tokens, certificates, keys, passwords, cookies, Authorization headers, and secrets | Not committed |
| Exposure boundary | Local virtual-lab reverse proxy only; public internet exposure was not tested or claimed |
| Final judgment | **READY** |

## Judgment Basis

The Deployment and both backend Pods were available, the Service exposed two
ready endpoints, the Ingress mapped the expected host/path to that Service, and
both the root and health requests returned successful responses. Repeated
requests identified both masked backend Pods, confirming processing beyond the
Ingress controller and Service layers.

Validated path:

`Client -> Ingress Controller -> Kubernetes Service -> Nginx Backend Pod`

## Evidence Reference

- `logs/20260715-S024-nginx-reverse-proxy.sanitized.txt`
