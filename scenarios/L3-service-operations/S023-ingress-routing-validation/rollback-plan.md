# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing Kubernetes ingress state.

## Rollback Steps

1. Stop validation if evidence includes kubeconfig files, Kubernetes Secrets, TLS private keys, credentials, real public IPs, real DNS records, tfstate, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies missing Ingress Controller, missing Ingress resource, wrong backend Service, route timeout, HTTP 5xx, or unresolved hostname, record the finding as `FAIL`.
5. Do not create or modify Kubernetes manifests, Ingress resources, Services, Secrets, TLS settings, DNS records, or load balancing behavior from this scenario.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should restore ingress controller readiness, route definition, backend mapping, host/path behavior, or service connectivity through a separately approved implementation task, then repeat evidence collection with sanitized outputs.
