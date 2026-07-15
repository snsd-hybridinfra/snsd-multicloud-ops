# S023 Real-Lab Ingress Routing Validation Summary

| Field | Result |
|---|---|
| Evidence source | Pasted terminal output |
| Validation mode | Real lab evidence, sanitized |
| Namespace | PASS - the masked namespace contained the expected workload and routing resources |
| Deployment | PASS - the masked Deployment reported `2/2` ready and available |
| Service | PASS - a masked `ClusterIP` Service and two masked backend endpoints were observed |
| Ingress resource | PASS - the masked Ingress mapped `<ingress-host-placeholder>` and `/` to the masked Service on port 80 |
| Ingress controller | PASS - the Traefik controller and service load-balancer Pods were `Running`; installation Pods were `Completed` |
| HTTP routing test | PASS - the request returned `HTTP/1.1 200 OK` and an HTML body |
| Host header routing | PASS - the successful request used `Host: <ingress-host-placeholder>` |
| Kubernetes events | PASS - the event query completed and reported no events in the masked namespace |
| Sensitive data sanitization | PASS - user, host/node, namespace, workload, Pod, Service, Ingress, host, image, selectors/hashes, addresses, and response identifiers are masked |
| Raw output | Not committed |
| Kubeconfig, tokens, certificates, keys, passwords, and secrets | Not committed |
| Exposure boundary | Local lab Ingress routing only; public internet exposure was not tested or claimed |
| Final judgment | **READY** |

## Judgment Basis

The Ingress resource existed with the expected host/path/backend mapping, its
controller was running, and the Host-header HTTP request returned `200 OK` with
an application response body. This satisfies the S023 real-lab READY criteria.

## Evidence Reference

- `logs/20260714-S023-ingress-routing.sanitized.txt`
