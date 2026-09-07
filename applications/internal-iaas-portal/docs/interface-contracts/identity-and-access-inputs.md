# Identity and access inputs

Production mode requires an approved OIDC issuer, audience, JWKS URL, role and
scope claims, administrator MFA, service OAuth clients, TLS trust bundles, and
a PEP route that prevents direct browser access to backend APIs.

Roles remain separated: requester, approver, Grant administrator, auditor, and
runner service. A requester cannot approve the same request. User-supplied Grant
scopes are ignored; scopes come from the fixed product policy.

The current Compose demo uses development headers and is loopback-only. It is
not an identity implementation or runtime evidence. The Kubernetes candidate
uses OIDC mode but contains placeholder image and endpoint values and is not
authorized for deployment.
