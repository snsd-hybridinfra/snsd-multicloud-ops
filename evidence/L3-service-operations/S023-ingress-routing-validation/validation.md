# Validation

Scenario: S023-ingress-routing-validation

Level: L3-service-operations

Date: 2026-07-13

Overall status: PASS

Validation mode: Static

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | Ingress documentation | Baseline and commands exist. | Both exist. | generated evidence | PASS |
| V002 | Ingress example files | Manifest and README exist. | Both exist. | files, generated evidence | PASS |
| V003 | Ingress sample evidence | Three samples exist. | All found. | samples, generated evidence | PASS |
| V004 | Required command examples | All examples exist. | All documented. | generated evidence | PASS |
| V005 | Routing model and placeholders | Required model exists. | All terms found. | generated evidence | PASS |
| V006 | Ingress object and scope | Correct scope/class/marker. | All pass. | manifest, generated evidence | PASS |
| V007 | Host and path routing | Approved host, `/`, Prefix. | Route found. | manifest, generated evidence | PASS |
| V008 | Backend Service reference | Name/port/namespace align. | Alignment passes. | manifests, generated evidence | PASS |
| V009 | Ingress and TLS safety | No unsafe pattern/material. | None detected. | generated evidence | PASS |
| V010 | Ingress list evidence | Host and port 80 present. | Both found. | sample, generated evidence | PASS |
| V011 | Ingress backend evidence | Describe and Service match. | Backend found. | sample, generated evidence | PASS |
| V012 | Endpoint evidence | Port-80 target exists. | Placeholder target found. | sample, generated evidence | PASS |
| V013 | Ingress address awareness | Placeholder produces WARN. | Live address intentionally not validated. | generated evidence | WARN |
| V014 | Kubernetes/TLS credential files | No forbidden file. | None detected. | generated evidence | PASS |
| V015 | Routing content safety | No real endpoint/domain/IP/secret. | None detected. | generated evidence | PASS |
| V016 | Execution safety boundary | Four read-only queries; no curl. | Boundary confirmed. | generated evidence | PASS |
| V017 | Validation mode | Static no execution. | kubectl/curl not invoked. | generated evidence | PASS |

## Generated Result

Static validation completed with sixteen PASS results and one expected ADDRESS-placeholder WARN. Optional LiveKubectl mode was not run and curl was not executed.
