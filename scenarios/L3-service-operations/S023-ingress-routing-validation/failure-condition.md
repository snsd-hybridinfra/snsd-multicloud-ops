# Failure Condition

S023 fails if required artifacts, object scope, host/path, backend name/port, Service alignment, or endpoint evidence is missing; endpoint evidence is empty; unsafe wildcard/TLS/Secret content exists; credentials or real routing values are detected; or requested live resources are unavailable.

## Warning Condition

Static ADDRESS placeholder evidence produces WARN because a live routing address is intentionally outside default validation.

## Safety Failure

Any kubeconfig, token, certificate, TLS key, real domain/IP/endpoint, secret, raw sensitive live row, automatic curl, or cluster mutation violates the scenario boundary.
