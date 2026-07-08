# Commands

Scenario: S019-nginx-security-header-validation
Level: L2-security-baseline
Capability: Nginx Security Header Validation
Target: `<service-endpoint>`
Execution timestamp: TODO

Record sanitized output only. Do not include TLS private keys, certificates, credentials, real public IPs, tfstate, kubeconfig content, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Nginx configuration syntax validation plan | Plan `nginx -t` or approved equivalent on `<reverse-proxy-host>`. | Confirm Nginx syntax can be validated before exposure. | TODO: record sanitized output after approved execution. |
| V002 | server_tokens off validation plan | Review planned Nginx security policy for `server_tokens off` or equivalent. | Confirm server version exposure reduction is planned. | TODO: record sanitized output after approved execution. |
| V003 | X-Content-Type-Options header validation plan | Plan response header review for `X-Content-Type-Options`. | Confirm required header is present. | TODO: record sanitized output after approved execution. |
| V004 | X-Frame-Options header validation plan | Plan response header review for `X-Frame-Options`. | Confirm required header is present. | TODO: record sanitized output after approved execution. |
| V005 | Referrer-Policy header validation plan | Plan response header review for `Referrer-Policy`. | Confirm required header is present. | TODO: record sanitized output after approved execution. |
| V006 | Content-Security-Policy placeholder validation plan | Plan response header review for `Content-Security-Policy`. | Confirm CSP placeholder is documented. | TODO: record sanitized output after approved execution. |
| V007 | HTTP response header capture using curl -I plan | Plan `curl -I <service-endpoint>` or approved equivalent. | Capture response headers for review. | TODO: record sanitized output after approved execution. |
| V008 | Access log capture plan | Review sanitized access logs from `<reverse-proxy-host>`. | Confirm access logs are available for evidence. | TODO: record sanitized output after approved execution. |
| V009 | Error log capture plan | Review sanitized error logs from `<reverse-proxy-host>`. | Confirm error logs are available for evidence. | TODO: record sanitized output after approved execution. |
| V010 | Failure condition for missing security header, exposed server version, invalid Nginx configuration, or unexplained response behavior | Review validation findings against failure criteria. | Confirm unsafe response patterns result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/nginx-security-header-summary.md`
- `configs/nginx-security-policy.md`
- `logs/nginx-security-header-validation.log`
- `screenshots/nginx-security-header-test.png`
