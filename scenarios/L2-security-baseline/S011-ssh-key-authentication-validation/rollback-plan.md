# Rollback Plan

S011 performs no SSH service or host mutation and requires no infrastructure rollback.

If unsafe content is discovered:

1. Stop validation.
2. Remove only the unsafe artifact after confirming ownership and following repository safety procedures.
3. Restore placeholder-only policy text and the non-production example.
4. Re-run the local validator and both repository QA scripts.
5. Record unresolved issues as `BLOCKED` or `FAIL` without reproducing key or secret material.

Generated S011 log and summary files may be regenerated safely.
