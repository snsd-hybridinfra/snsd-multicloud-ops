# S019-nginx-security-header-validation

| Field | Value |
|---|---|
| Scenario ID | S019 |
| Scenario Name | Nginx Security Header Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Related Components | Nginx header policy, rule matrix, non-production config example, local validator |
| Validation Type | Safe local repository validation |
| Evidence Directory | `evidence/L2-security-baseline/S019-nginx-security-header-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate a baseline set of Nginx reverse-proxy security headers without connecting to services, running or reloading Nginx, or modifying server configuration.

## Scope Summary

S019 inspects a local policy, matrix, and non-production config snippet only. It checks required directives, exact values, `always`, and sensitive-content safety.

## Validation Summary

Twelve checks validate required artifacts, `server_tokens off`, six headers, exact values, `always`, documentation completeness, TLS material safety, domain/address safety, credentials, and execution boundaries.

## Evidence Output Summary

The validator writes an ignored execution log and a tracked sanitized Markdown summary under the S019 evidence directory.
