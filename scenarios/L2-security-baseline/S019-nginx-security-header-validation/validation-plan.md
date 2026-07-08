# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Nginx configuration syntax validation plan | Document planned `nginx -t` or approved equivalent syntax check. | Nginx syntax validation can be performed before service exposure. | `commands.md`, `configs/nginx-security-header-summary.md`, `validation.md` |
| V002 | server_tokens off validation plan | Document planned review for `server_tokens off` or equivalent. | Nginx server version exposure is reduced. | `commands.md`, `configs/nginx-security-policy.md`, `validation.md` |
| V003 | X-Content-Type-Options header validation plan | Plan response header capture for `X-Content-Type-Options`. | Header is present with an approved value. | `commands.md`, `configs/nginx-security-policy.md`, `validation.md` |
| V004 | X-Frame-Options header validation plan | Plan response header capture for `X-Frame-Options`. | Header is present with an approved value. | `commands.md`, `configs/nginx-security-policy.md`, `validation.md` |
| V005 | Referrer-Policy header validation plan | Plan response header capture for `Referrer-Policy`. | Header is present with an approved value. | `commands.md`, `configs/nginx-security-policy.md`, `validation.md` |
| V006 | Content-Security-Policy placeholder validation plan | Plan response header capture for `Content-Security-Policy` placeholder. | CSP placeholder is documented until service-specific directives are approved. | `commands.md`, `configs/nginx-security-policy.md`, `validation.md` |
| V007 | HTTP response header capture using curl -I plan | Plan `curl -I <service-endpoint>` or approved equivalent. | Response headers can be captured and reviewed. | `commands.md`, `logs/nginx-security-header-validation.log`, `screenshots/nginx-security-header-test.png`, `validation.md` |
| V008 | Access log capture plan | Plan sanitized access log capture from `<reverse-proxy-host>`. | Access logs can be reviewed without sensitive values. | `commands.md`, `logs/nginx-security-header-validation.log`, `validation.md` |
| V009 | Error log capture plan | Plan sanitized error log capture from `<reverse-proxy-host>`. | Error logs can be reviewed for configuration or response issues. | `commands.md`, `logs/nginx-security-header-validation.log`, `validation.md` |
| V010 | Failure condition for missing security header, exposed server version, invalid Nginx configuration, or unexplained response behavior | Evaluate findings against explicit failure conditions. | Unsafe or unexplained response patterns produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates Nginx security headers only; ingress routing is handled in S023 and load balancing is handled in S025.
