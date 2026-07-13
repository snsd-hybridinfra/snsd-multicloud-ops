# Rollback Plan

Because validation is read-only, rollback means removing invalid generated evidence, correcting sanitized examples, and rerunning the validator. It never recreates or deletes infrastructure.

This skeleton does not delete resources or run cleanup commands, so rollback is documentation-focused.

1. Stop validation if credentials, billing account IDs, cloud account values, private keys, tfstate, kubeconfig content, public IPs, or account-specific data appear.
2. Remove unsafe evidence and replace it with sanitized placeholders.
3. Mark unsupported cleanup automation claims as `CLEANUP_BLOCKED`.
4. Record missing ownership, usage evidence, dependency review, approval, or rollback notes in `validation.md`.
5. If accidental real deletion is discovered, stop work and mark the scenario `BLOCKED` for human review.
6. Keep cost guardrail analysis in S045 and final reporting in S050.
7. Do not add lifecycle management tools, cleanup automation, or Terraform destroy workflows unless the repository scope is changed through an ADR.

No cloud cleanup, Terraform rollback, Kubernetes rollback, or automated recreation is performed by this scenario skeleton.
