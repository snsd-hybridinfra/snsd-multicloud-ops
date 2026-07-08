# Rollback Plan

## Stop Condition

Stop immediately if a command prompts for credentials, attempts to authenticate to a live service, or exposes sensitive local configuration.

## Rollback Steps

1. Stop the validation command.
2. Remove any unsafe output from evidence files.
3. Replace unsafe details with a sanitized placeholder such as `<redacted>`.
4. Mark the affected validation item as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the reason in the implementation log if scenario progress is blocked.

## Recovery Validation

Confirm the evidence files contain only command names, purposes, sanitized TODO placeholders, and non-sensitive validation notes.
