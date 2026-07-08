# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Ingress Controller pod readiness validation plan | Plan read-only pod readiness lookup for `<ingress-controller>`. | Ingress Controller pods are Running and Ready. | `commands.md`, `configs/ingress-routing-summary.md`, `validation.md` |
| V002 | Ingress resource existence validation plan | Plan read-only lookup for Ingress resource in `<namespace>`. | Ingress resource is identifiable. | `commands.md`, `configs/ingress-routing-summary.md`, `validation.md` |
| V003 | Web route backend mapping validation plan | Review route mapping to `<web-service>`. | Web route maps to the intended backend Service. | `commands.md`, `configs/ingress-backend-mapping.md`, `validation.md` |
| V004 | API route backend mapping validation plan | Review route mapping to `<api-service>`. | API route maps to the intended backend Service. | `commands.md`, `configs/ingress-backend-mapping.md`, `validation.md` |
| V005 | Host-based routing validation plan | Plan request using placeholder host `<ingress-host>`. | Host-based route resolves to intended service path without real DNS records. | `commands.md`, `logs/ingress-routing-validation.log`, `validation.md` |
| V006 | Path-based routing validation plan | Plan path checks for Web and API placeholder paths. | Path-based routing reaches the intended backend Service. | `commands.md`, `logs/ingress-routing-validation.log`, `validation.md` |
| V007 | HTTP 200 response validation plan | Plan HTTP response check for valid route. | Valid route returns expected HTTP 200 response. | `commands.md`, `logs/ingress-routing-validation.log`, `screenshots/ingress-routing-test.png`, `validation.md` |
| V008 | Invalid path response validation plan | Plan HTTP response check for invalid path. | Invalid path returns expected not-found or denial response. | `commands.md`, `logs/ingress-routing-validation.log`, `validation.md` |
| V009 | Ingress event capture plan | Plan read-only ingress event capture. | Ingress events are available for troubleshooting evidence. | `commands.md`, `logs/ingress-routing-validation.log`, `validation.md` |
| V010 | Ingress controller log capture plan | Plan sanitized controller log capture. | Controller logs are available without sensitive values. | `commands.md`, `logs/ingress-routing-validation.log`, `validation.md` |
| V011 | Failure condition for missing ingress controller, missing ingress resource, wrong backend service, route timeout, HTTP 5xx, or unresolved hostname | Evaluate findings against explicit failure conditions. | Ingress routing failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates ingress routing only; workload deployment is handled in S022, security headers in S019, and load balancing health checks in S025.
