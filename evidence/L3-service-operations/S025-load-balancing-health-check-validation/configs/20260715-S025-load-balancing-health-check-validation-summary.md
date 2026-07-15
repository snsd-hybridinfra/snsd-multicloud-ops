# S025 Real Virtual-Lab Load-Balancing Health-Check Validation Summary

| Field | Result |
|---|---|
| Evidence source | Pasted terminal output |
| Validation mode | Real virtual lab, sanitized |
| Backend replica count | 2 ready backend Pods |
| Initial readiness | PASS - both backend Pods were `1/1 Running` |
| Initial Service endpoint count | PASS - 2 ready endpoints |
| Initial EndpointSlice readiness | Two members were listed; explicit conditions were not printed in the initial wide view, so readiness is corroborated by Pod readiness and ready Service Endpoints rather than inferred |
| Initial request distribution | PASS - 24/24 requests succeeded; both masked backends were observed 12 times |
| Controlled readiness failure | Removed `/tmp/ready` inside `<backend-pod-a>` using a lab-only `kubectl exec`; no Pod deletion or container crash was used |
| Unhealthy Pod running state | PASS - `<backend-pod-a>` remained `Running` |
| Unhealthy Pod readiness | PASS - `<backend-pod-a>` became `0/1` |
| Unhealthy backend exclusion | PASS - ready Service Endpoints decreased from 2 to 1 and retained only `<backend-pod-b>` |
| Degraded EndpointSlice evidence | Wide output retained two member addresses but did not print readiness conditions; no false condition is inferred |
| Healthy backend traffic continuity | PASS - 20/20 degraded-state requests succeeded through `<backend-pod-b>` |
| HTTP response during degradation | PASS - application health marker passed on every request |
| NotReady backend traffic | No application response was attributed to `<backend-pod-a>` during degradation |
| Readiness restoration | PASS - `/tmp/ready` was restored and `<backend-pod-a>` returned to `1/1 Running` |
| Endpoint restoration | PASS - ready Service Endpoints returned to 2; final EndpointSlice conditions reported both endpoints `ready=true` and `serving=true` |
| Post-recovery distribution | PASS - 12/12 requests succeeded; both masked backends were observed 6 times |
| API warning | v1 Endpoints deprecation warning observed; EndpointSlice is preferred for future evidence collection |
| Sensitive-data sanitization | PASS - all users, hosts/nodes, namespace, workload resources, images, selectors/hashes, UIDs, resource versions, local DNS names, and addresses are masked or omitted |
| Raw output and response bodies | Not committed |
| Kubeconfig, tokens, certificates, keys, passwords, cookies, Authorization headers, credentials, and secrets | Not committed |
| S031 boundary | This scenario toggled readiness on a running Pod; it did not delete a Pod or validate Deployment self-healing. Full Web Pod failure recovery remains S031. |
| Final judgment | **READY** |

## Judgment Basis

Two healthy backends were initially eligible and served traffic. After a
controlled readiness-file removal, one Pod remained running but became NotReady,
disappeared from the Service-ready endpoint set, and received no observed
application traffic while all requests continued through the healthy backend.
Restoring the file returned the Pod to Ready, restored two ready endpoints, and
returned traffic distribution across both backends.

Validated path:

`Client -> Ingress Controller -> Kubernetes Service -> Ready backend endpoint`

## Evidence References

- `logs/20260715-S025-load-balancing-normal-state.sanitized.txt`
- `logs/20260715-S025-unhealthy-backend-exclusion.sanitized.txt`
- `logs/20260715-S025-backend-health-restoration.sanitized.txt`
