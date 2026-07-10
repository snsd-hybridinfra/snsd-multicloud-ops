# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing load balancer or service traffic state.

## Rollback Steps

1. Stop validation if evidence includes TLS private keys, certificates, credentials, secrets, real public IPs, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies all backends unhealthy, missing health endpoint, HTTP 5xx, route timeout, stale endpoint, or missing health evidence, record the finding as `FAIL`.
5. Do not create or modify load balancers, Kubernetes manifests, Nginx configuration, Blackbox probes, TLS assets, DNS records, or cloud resources from this scenario.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should restore backend health, endpoint freshness, health route behavior, or health log capture through a separately approved implementation task, then repeat evidence collection with sanitized outputs.
