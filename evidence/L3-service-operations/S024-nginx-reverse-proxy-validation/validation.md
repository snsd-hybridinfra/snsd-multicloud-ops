# Validation

Scenario: S024-nginx-reverse-proxy-validation
Level: L3-service-operations
Capability: Nginx Reverse Proxy Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Nginx reverse proxy output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Nginx service status validation plan | Nginx service status can be reviewed for each provider entrypoint. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log` |
| V002 | Nginx configuration syntax validation plan using nginx -t | Nginx configuration syntax is valid before forwarding checks. | TODO | NOT_RUN | `commands.md`; `configs/nginx-reverse-proxy-summary.md` |
| V003 | AWS reverse proxy endpoint response validation plan | AWS reverse proxy endpoint responds as expected. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log` |
| V004 | Azure reverse proxy endpoint response validation plan | Azure reverse proxy endpoint responds as expected. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log` |
| V005 | OpenStack reverse proxy endpoint response validation plan | OpenStack reverse proxy endpoint responds as expected. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log` |
| V006 | Reverse proxy upstream mapping validation plan | Upstream mapping points to the intended service target. | TODO | NOT_RUN | `commands.md`; `configs/nginx-upstream-mapping.md` |
| V007 | Reverse proxy to Ingress forwarding validation plan | Reverse proxy forwards to the intended Kubernetes Ingress endpoint. | TODO | NOT_RUN | `commands.md`; `configs/nginx-upstream-mapping.md` |
| V008 | HTTP 200 response validation plan | Valid reverse proxy route returns expected HTTP 200 response. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `screenshots/nginx-reverse-proxy-test.png` |
| V009 | Access log capture plan | Access logs can support forwarding evidence without sensitive values. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log` |
| V010 | Error log capture plan | Error logs can support failure analysis without sensitive values. | TODO | NOT_RUN | `commands.md`; `logs/nginx-reverse-proxy-validation.log` |
| V011 | Failure condition for Nginx down, invalid config, wrong upstream, route timeout, HTTP 5xx, or missing access/error logs | Reverse proxy failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Nginx reverse proxy summary is captured: NOT_READY
- Nginx upstream mapping is captured: NOT_READY
- Nginx reverse proxy validation log is captured: NOT_READY
- Nginx reverse proxy screenshot is captured: NOT_READY

## Notes

This scenario validates Nginx Reverse Proxy forwarding only. Nginx security header validation is handled in S019, Ingress routing validation in S023, load balancing health check validation in S025, and TLS implementation is excluded.
