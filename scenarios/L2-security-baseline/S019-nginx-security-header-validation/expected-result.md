# Expected Result

## Pass Criteria

- V001 through V012 return `PASS`.
- The config contains `server_tokens off` and all required header directives with exact values and `always`.
- Static limitations and service-specific placeholders remain explicit.
- No TLS, address, domain, credential, or account-specific value is introduced.
- No Nginx process or live service is accessed.

## Evidence Criteria

The ignored log and tracked summary contain sanitized static-validation results only and no server, TLS, credential, secret, or account-specific content.
