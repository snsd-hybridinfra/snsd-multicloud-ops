# Rollback Plan

Static mode changes repository evidence only. Live mode is read-only, so neither mode has a cluster rollback.

## Repository Rollback

1. Stop if unsafe or sensitive content appears.
2. Remove it and restore approved placeholder examples.
3. Correct route, backend, port, namespace, or endpoint evidence inconsistencies.
4. Rerun static validation and retain sanitized evidence only.
5. Mark scenario and evidence status appropriately if validation cannot pass.
