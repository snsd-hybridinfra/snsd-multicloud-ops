# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing Azure infrastructure.

## Rollback Steps

1. Stop validation if evidence includes Azure credentials, subscription IDs, tenant IDs, private keys, tfstate, real public IPs, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If a future rule review identifies unrestricted SSH, unrestricted DB access, or all-ports inbound access, record the finding as `FAIL`.
5. Do not modify Azure resources from this scenario. Any future corrective resource change must be handled by an explicitly approved implementation task.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should tighten the proposed NSG rule model to least privilege, then repeat evidence collection with sanitized outputs.
