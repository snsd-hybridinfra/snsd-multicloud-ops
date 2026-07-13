# Rollback Plan

S018 changes repository policy, examples, validator, evidence, and tracking only. It applies no resource and therefore has no cluster rollback.

## Repository Rollback

1. Stop if sensitive or account-specific content is found.
2. Remove unsafe content and replace it with approved examples or placeholders.
3. Correct an overbroad Role or RoleBinding.
4. Rerun the validator and retain only sanitized evidence.
5. Mark scenario and evidence status appropriately if validation cannot pass.
