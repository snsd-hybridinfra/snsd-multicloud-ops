# Rollback Plan

Static S024 validation changes only generated repository evidence, so no infrastructure rollback is required.

1. Stop immediately if sensitive or concrete environment content is found.
2. Remove the unsafe artifact and replace values with approved placeholders.
3. Correct the example or documentation without touching a real Nginx installation.
4. Rerun Static validation and review the aggregate evidence.
5. If an optional live request fails, retain only the sanitized judgment and investigate outside this scenario under separate authorization.
6. Revert repository changes through normal version control if the baseline itself is invalid.

Never restart, reload, modify, or roll back Nginx from this validator.
