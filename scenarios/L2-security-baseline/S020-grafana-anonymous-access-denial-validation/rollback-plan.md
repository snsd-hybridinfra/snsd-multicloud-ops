# Rollback Plan

S020 changes repository policy, example config, validator, evidence, and tracking only. It modifies no Grafana instance and therefore has no service rollback.

## Repository Rollback

1. Stop if sensitive or account-specific content is found.
2. Remove unsafe content and restore approved placeholders.
3. Correct an anonymous enablement or incomplete denial policy.
4. Rerun the validator and retain only sanitized evidence.
5. Mark scenario and evidence status appropriately if validation cannot pass.
