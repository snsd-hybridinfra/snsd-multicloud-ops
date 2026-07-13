# Objective

## Objective Statement

Validate the route Client -> Ingress Controller -> Ingress Rule -> Service -> Pod through safe static artifacts and optional read-only observations.

## Success Measures

- A marked non-production Ingress uses `snsd-example`, class `nginx`, host `app.example.internal`, path `/`, and Prefix matching.
- Backend `sample-service-placeholder:80` aligns with the S022 Service.
- List and describe samples contain the expected route and endpoint evidence contains a target.
- Wildcard hosts, Secret resources, TLS material, credentials, real endpoints/domains/IPs, and mutation commands are absent.
- Static mode invokes neither kubectl nor curl.
