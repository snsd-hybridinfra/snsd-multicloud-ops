# Rollback Plan

S014 performs no AWS or Terraform mutation and requires no cloud rollback.

If unsafe content is discovered:

1. Stop validation.
2. Remove only the unsafe artifact after confirming ownership.
3. Restore placeholder-only policy, safe matrix rows, and the empty Terraform Security Group placeholder.
4. Re-run the S003 and S014 validators plus both repository QA scripts.
5. Record unresolved issues as `BLOCKED` or `FAIL` without reproducing credentials or account data.

Generated S014 log and summary files may be regenerated safely.
