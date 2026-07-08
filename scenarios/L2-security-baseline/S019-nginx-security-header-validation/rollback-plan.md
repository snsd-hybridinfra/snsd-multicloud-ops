# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing Nginx configuration.

## Rollback Steps

1. Stop validation if evidence includes TLS private keys, certificates, credentials, real public IPs, tfstate, kubeconfig content, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies missing security headers, exposed server version, invalid Nginx syntax, or unexplained response behavior, record the finding as `FAIL`.
5. Do not modify Nginx, TLS, ingress, or load balancing configuration from this scenario. Any future corrective change must be handled by an explicitly approved implementation task.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should tighten the proposed Nginx security header and response validation model, then repeat evidence collection with sanitized outputs.
