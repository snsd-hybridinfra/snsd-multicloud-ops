# Rollback Plan

S008 performs no remote action and requires no infrastructure rollback.

If unsafe content is discovered:

1. Stop validation.
2. Remove only the unsafe artifact after confirming it belongs to this scenario change.
3. Restore symbolic access paths and angle-bracket placeholders.
4. Re-run the local validator and both repository QA scripts.
5. Record unresolved issues as `BLOCKED` or `FAIL` without reproducing sensitive content.

Generated S008 log and summary files may be regenerated safely.
