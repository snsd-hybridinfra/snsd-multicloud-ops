# Rollback Plan

S015 makes repository-only documentation, validator, evidence, and tracking changes. It creates no Azure resource and therefore has no cloud rollback.

## Repository Rollback

1. Stop if sensitive or account-specific content is found.
2. Remove the unsafe repository content and replace it with approved placeholders.
3. Correct an overbroad matrix row or incomplete policy statement.
4. Rerun the validator and retain only sanitized evidence.
5. Mark the scenario and evidence status appropriately if validation cannot pass.
