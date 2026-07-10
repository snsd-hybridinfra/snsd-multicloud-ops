# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing Nginx or cloud routing state.

## Rollback Steps

1. Stop validation if evidence includes TLS private keys, certificates, credentials, secrets, real public IPs, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies Nginx down, invalid config, wrong upstream, route timeout, HTTP 5xx, or missing access/error logs, record the finding as `FAIL`.
5. Do not create or modify Nginx configuration, TLS assets, Ingress resources, load balancers, DNS records, or cloud resources from this scenario.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should restore Nginx service status, syntax validity, upstream mapping, forwarding behavior, or logging through a separately approved implementation task, then repeat evidence collection with sanitized outputs.
