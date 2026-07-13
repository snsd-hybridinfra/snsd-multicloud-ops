# Nginx Security Header Summary

- Scenario: S019-nginx-security-header-validation
- Generated: 2026-07-13T11:06:49+09:00
- Overall result: **PASS**
- Scope: local policy, matrix, example config, and safety checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Security header baseline | PASS | Baseline document exists. |
| V002 | Security header rule matrix | PASS | Rule matrix exists. |
| V003 | Nginx example config | PASS | Non-production config example exists. |
| V004 | Server token reduction | PASS | server_tokens off is present. |
| V005 | Required security headers | PASS | All six required add_header directives exist. |
| V006 | Required header values | PASS | All required values and placeholders are exact. |
| V007 | Always directive | PASS | All six security headers use always. |
| V008 | Baseline and matrix completeness | PASS | All matrix entries, placeholders, legacy note, evidence model, and static limitations exist. |
| V009 | TLS material safety | PASS | No certificate path, private-key path, or private material exists. |
| V010 | Address and domain safety | PASS | No numeric address or real-looking domain is hardcoded. |
| V011 | Credential and account safety | PASS | No credential, secret assignment, or account-specific identifier exists. |
| V012 | Execution safety boundary | PASS | The validator contains no Nginx, curl, host, or network execution command. |

## Safety Boundary

This validation read repository files only. It did not run or reload Nginx, modify configuration, curl an endpoint, connect to a host, or validate live HTTP/TLS behavior.
