# Objective

## Objective Statement

Validate that repository-side Nginx reverse-proxy examples define the required security header baseline and reduce server token exposure.

## Success Measures

- Required policy, matrix, and marked non-production config exist.
- `server_tokens off` and all six required security headers are present.
- Header values and placeholders are exact and every security header uses `always`.
- Legacy header guidance, evidence handling, and static-validation limits are documented.
- No TLS key/certificate path, private material, real domain, numeric address, credential, or account-specific content is present.
