# Rollback Plan

S017 changes repository policy, examples, validator, evidence, and tracking only. It performs no database action and therefore has no database rollback.

## Repository Rollback

1. Stop if sensitive or account-specific content is found.
2. Remove unsafe content and replace it with approved placeholders.
3. Correct an overbroad grant or incomplete policy statement.
4. Rerun the validator and retain only sanitized evidence.
5. Mark scenario and evidence status appropriately if validation cannot pass.
