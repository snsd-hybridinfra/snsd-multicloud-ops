# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Nginx service status validation plan | Document planned service status check on each reverse proxy placeholder. | Nginx service status can be reviewed for each provider entrypoint. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `validation.md` |
| V002 | Nginx configuration syntax validation plan using nginx -t | Document planned `nginx -t` or approved equivalent. | Nginx configuration syntax is valid before forwarding checks. | `commands.md`, `configs/nginx-reverse-proxy-summary.md`, `validation.md` |
| V003 | AWS reverse proxy endpoint response validation plan | Plan HTTP response check for `<aws-reverse-proxy>`. | AWS reverse proxy endpoint responds as expected. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `validation.md` |
| V004 | Azure reverse proxy endpoint response validation plan | Plan HTTP response check for `<azure-reverse-proxy>`. | Azure reverse proxy endpoint responds as expected. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `validation.md` |
| V005 | OpenStack reverse proxy endpoint response validation plan | Plan HTTP response check for `<openstack-reverse-proxy>`. | OpenStack reverse proxy endpoint responds as expected. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `validation.md` |
| V006 | Reverse proxy upstream mapping validation plan | Review mapping from provider proxies to `<upstream-service>`. | Upstream mapping points to the intended service target. | `commands.md`, `configs/nginx-upstream-mapping.md`, `validation.md` |
| V007 | Reverse proxy to Ingress forwarding validation plan | Review forwarding path to `<ingress-endpoint>`. | Reverse proxy forwards to the intended Kubernetes Ingress endpoint. | `commands.md`, `configs/nginx-upstream-mapping.md`, `validation.md` |
| V008 | HTTP 200 response validation plan | Plan HTTP response check through reverse proxy path. | Valid reverse proxy route returns expected HTTP 200 response. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `screenshots/nginx-reverse-proxy-test.png`, `validation.md` |
| V009 | Access log capture plan | Plan sanitized Nginx access log capture. | Access logs can support forwarding evidence without sensitive values. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `validation.md` |
| V010 | Error log capture plan | Plan sanitized Nginx error log capture. | Error logs can support failure analysis without sensitive values. | `commands.md`, `logs/nginx-reverse-proxy-validation.log`, `validation.md` |
| V011 | Failure condition for Nginx down, invalid config, wrong upstream, route timeout, HTTP 5xx, or missing access/error logs | Evaluate findings against explicit failure conditions. | Reverse proxy failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates reverse proxy forwarding only; security headers are handled in S019, ingress routing in S023, and load balancing health checks in S025.
