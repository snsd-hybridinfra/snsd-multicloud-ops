# Commands

Scenario: S023-ingress-routing-validation
Level: L3-service-operations
Capability: Kubernetes Ingress Routing Validation
Target: `<ingress-host>`
Execution timestamp: TODO

Record sanitized output only. Do not include kubeconfig files, Kubernetes Secrets, TLS private keys, credentials, real public IPs, real DNS records, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Ingress Controller pod readiness validation plan | Plan read-only readiness lookup for `<ingress-controller>`. | Confirm Ingress Controller pods are Running and Ready. | TODO: record sanitized output after approved execution. |
| V002 | Ingress resource existence validation plan | Plan read-only lookup for Ingress resource in `<namespace>`. | Confirm Ingress resource exists. | TODO: record sanitized output after approved execution. |
| V003 | Web route backend mapping validation plan | Review route mapping to `<web-service>`. | Confirm Web route backend is correct. | TODO: record sanitized output after approved execution. |
| V004 | API route backend mapping validation plan | Review route mapping to `<api-service>`. | Confirm API route backend is correct. | TODO: record sanitized output after approved execution. |
| V005 | Host-based routing validation plan | Plan request using placeholder host `<ingress-host>`. | Confirm host-based routing behavior. | TODO: record sanitized output after approved execution. |
| V006 | Path-based routing validation plan | Plan path checks for Web and API placeholder paths. | Confirm path-based routing behavior. | TODO: record sanitized output after approved execution. |
| V007 | HTTP 200 response validation plan | Plan HTTP response check for valid route at `<service-endpoint>`. | Confirm expected successful response. | TODO: record sanitized output after approved execution. |
| V008 | Invalid path response validation plan | Plan HTTP response check for invalid path. | Confirm expected not-found or denial response. | TODO: record sanitized output after approved execution. |
| V009 | Ingress event capture plan | Plan read-only capture of ingress events. | Confirm events are available for evidence. | TODO: record sanitized output after approved execution. |
| V010 | Ingress controller log capture plan | Plan sanitized log capture for `<ingress-controller>`. | Confirm controller logs are available for evidence. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for missing ingress controller, missing ingress resource, wrong backend service, route timeout, HTTP 5xx, or unresolved hostname | Review validation findings against failure criteria. | Confirm routing failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/ingress-routing-summary.md`
- `configs/ingress-backend-mapping.md`
- `logs/ingress-routing-validation.log`
- `screenshots/ingress-routing-test.png`
