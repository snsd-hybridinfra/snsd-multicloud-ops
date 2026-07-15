# Kubernetes Ingress Routing Summary

- Scenario: S023-ingress-routing-validation
- Generated: 2026-07-15T09:16:51+09:00
- Validation mode: **Static**
- Required file check result: **PASS**
- Ingress manifest check result: **PASS**
- Backend service reference check result: **PASS**
- Endpoint evidence parsing result: **PASS**
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Ingress documentation | PASS | Baseline and command reference exist. |
| V002 | Ingress example files | PASS | Ingress manifest and README exist. |
| V003 | Ingress sample evidence | PASS | Ingress list, describe, and endpoint samples exist. |
| V004 | Required command examples | PASS | All kubectl and manual curl examples are documented. |
| V005 | Routing model and placeholders | PASS | Request path, objects, alignment, placeholders, evidence, and modes are documented. |
| V006 | Ingress object and scope | PASS | Ingress name, namespace, class, and example marker are correct. |
| V007 | Host and path routing | PASS | Approved example host, root path, and Prefix pathType exist. |
| V008 | Backend Service reference | PASS | Ingress and Service align on namespace, name, and port 80. |
| V009 | Ingress and TLS safety | PASS | No wildcard host, Secret resource, certificate, key, or TLS data exists. |
| V010 | Ingress list evidence | PASS | Ingress evidence contains the approved host and port 80. |
| V011 | Ingress backend evidence | PASS | Ingress describe and Service evidence contain the expected backend. |
| V012 | Endpoint evidence | PASS | Backend endpoint evidence contains at least one target on port 80. |
| V013 | Ingress address awareness | WARN | Static ingress ADDRESS is a placeholder; live address was intentionally not validated. |
| V014 | Kubernetes and TLS credential files | PASS | No kubeconfig, token, certificate, or private-key file exists. |
| V015 | Routing content safety | PASS | No real endpoint, numeric address, unexpected domain, token, certificate, key, password, or secret exists. |
| V016 | Execution safety boundary | PASS | Live mode contains four guarded read-only kubectl argument sets and no automatic curl. |
| V017 | Validation mode | PASS | Static mode completed without invoking kubectl or curl. |

## Safety Boundary

Static mode invokes neither kubectl nor curl. LiveKubectl runs only read-only resource queries and stores routing judgments rather than raw cluster details.
