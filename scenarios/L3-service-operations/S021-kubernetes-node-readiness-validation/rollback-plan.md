# Rollback Plan

Static mode changes repository evidence only. Live mode is read-only, so neither mode has a cluster rollback.

## Repository Rollback

1. Stop if sensitive or account-specific content appears.
2. Remove unsafe data and restore approved placeholders or sample rows.
3. Correct incomplete readiness documentation or parser expectations.
4. Rerun static validation and retain sanitized evidence only.
5. Mark scenario and evidence status appropriately if validation cannot pass.
