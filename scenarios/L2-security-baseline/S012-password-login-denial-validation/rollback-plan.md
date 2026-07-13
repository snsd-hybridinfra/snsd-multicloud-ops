# Rollback Plan

S012 performs no SSH service, authentication, or host mutation and requires no infrastructure rollback.

If unsafe content is discovered:

1. Stop validation.
2. Remove only the unsafe artifact after confirming ownership and following repository safety procedures.
3. Restore placeholder-only denial policy and non-production directives.
4. Re-run the local validator and both repository QA scripts.
5. Record unresolved issues as `BLOCKED` or `FAIL` without reproducing password, key, or secret material.

Generated S012 log and summary files may be regenerated safely.
