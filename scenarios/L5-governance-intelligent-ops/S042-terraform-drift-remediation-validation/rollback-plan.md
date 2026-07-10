# Rollback Plan

This skeleton does not execute real remediation, so rollback is documentation-focused.

1. Stop remediation validation if real credentials, tfstate, backend values, account identifiers, or account-specific data appear.
2. Remove unsafe evidence and replace it with sanitized placeholders.
3. Mark the remediation decision as `REMEDIATION_BLOCKED` if the plan is unsafe or unreviewed.
4. Mark the remediation decision as `REMEDIATION_FAILED` if post-remediation drift remains.
5. Record the blocker in `validation.md` and the implementation log.
6. Do not retry remediation until a safe plan and evidence collection path are documented.

No Terraform destroy, apply, or cloud cleanup is performed by this scenario skeleton.
