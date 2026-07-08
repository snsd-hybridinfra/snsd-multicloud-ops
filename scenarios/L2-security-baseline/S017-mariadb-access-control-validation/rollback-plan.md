# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing MariaDB configuration.

## Rollback Steps

1. Stop validation if evidence includes database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies root remote access, public DB exposure, overly broad grants, missing required users, or direct unauthorized DB access, record the finding as `FAIL`.
5. Do not modify MariaDB configuration from this scenario. Any future corrective database change must be handled by an explicitly approved implementation task.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should tighten the proposed MariaDB user, host, grant, and network exposure model to least privilege, then repeat evidence collection with sanitized outputs.
