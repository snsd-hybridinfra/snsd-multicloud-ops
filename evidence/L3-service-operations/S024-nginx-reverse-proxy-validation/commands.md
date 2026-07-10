# Commands

Scenario: S024-nginx-reverse-proxy-validation
Level: L3-service-operations
Capability: Nginx Reverse Proxy Validation
Target: `<ingress-endpoint>`
Execution timestamp: TODO

Record sanitized output only. Do not include TLS private keys, certificates, credentials, secrets, real public IPs, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Nginx service status validation plan | Plan service status checks for `<aws-reverse-proxy>`, `<azure-reverse-proxy>`, and `<openstack-reverse-proxy>`. | Confirm Nginx service status can be reviewed. | TODO: record sanitized output after approved execution. |
| V002 | Nginx configuration syntax validation plan using nginx -t | Plan `nginx -t` or approved equivalent. | Confirm Nginx configuration syntax is valid. | TODO: record sanitized output after approved execution. |
| V003 | AWS reverse proxy endpoint response validation plan | Plan HTTP response check for `<aws-reverse-proxy>`. | Confirm AWS provider entrypoint responds. | TODO: record sanitized output after approved execution. |
| V004 | Azure reverse proxy endpoint response validation plan | Plan HTTP response check for `<azure-reverse-proxy>`. | Confirm Azure provider entrypoint responds. | TODO: record sanitized output after approved execution. |
| V005 | OpenStack reverse proxy endpoint response validation plan | Plan HTTP response check for `<openstack-reverse-proxy>`. | Confirm OpenStack provider entrypoint responds. | TODO: record sanitized output after approved execution. |
| V006 | Reverse proxy upstream mapping validation plan | Review Nginx upstream mapping to `<upstream-service>`. | Confirm upstream target is correct. | TODO: record sanitized output after approved execution. |
| V007 | Reverse proxy to Ingress forwarding validation plan | Review forwarding path to `<ingress-endpoint>`. | Confirm forwarding reaches intended Kubernetes Ingress endpoint. | TODO: record sanitized output after approved execution. |
| V008 | HTTP 200 response validation plan | Plan HTTP response check through reverse proxy route. | Confirm valid route returns expected HTTP 200. | TODO: record sanitized output after approved execution. |
| V009 | Access log capture plan | Review sanitized Nginx access logs. | Confirm access logs support forwarding evidence. | TODO: record sanitized output after approved execution. |
| V010 | Error log capture plan | Review sanitized Nginx error logs. | Confirm error logs support failure analysis. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for Nginx down, invalid config, wrong upstream, route timeout, HTTP 5xx, or missing access/error logs | Review validation findings against failure criteria. | Confirm reverse proxy failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/nginx-reverse-proxy-summary.md`
- `configs/nginx-upstream-mapping.md`
- `logs/nginx-reverse-proxy-validation.log`
- `screenshots/nginx-reverse-proxy-test.png`
