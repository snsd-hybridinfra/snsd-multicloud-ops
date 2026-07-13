# Rollback Plan

S005 creates no OpenStack resource and therefore requires no cloud rollback or Terraform destroy operation.

If an unsafe repository artifact is discovered:

1. Stop validation.
2. Remove only the unsafe artifact after confirming it belongs to this scenario change.
3. Replace account-specific content with approved non-production examples and placeholders.
4. Re-run the local validator and both repository QA scripts.
5. Record any unresolved issue as `BLOCKED` or `FAIL` without exposing the sensitive value.

Generated S005 log and summary files may be regenerated safely by re-running the validator.
