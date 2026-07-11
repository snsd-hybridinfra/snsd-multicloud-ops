# Rollback Plan

## Stop Condition

Stop if validation attempts remote access or if real addressing, credentials, or other sensitive content appears.

## Rollback Steps

1. Terminate validation.
2. Remove unsafe generated evidence.
3. Restore the affected topology or example file from the last reviewed Git version.
4. Replace environment-specific content with approved placeholders.
5. Rerun the repository-side validator.

## Recovery Validation

Confirm all eight checks pass and both generated evidence files contain only repository model results.
