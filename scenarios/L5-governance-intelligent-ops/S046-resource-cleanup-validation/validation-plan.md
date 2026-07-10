# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Cleanup input artifact validation plan | Review cleanup input placeholders. | Cleanup input is identified or marked missing. | `commands.md`, `configs/resource-cleanup-summary.md`, `validation.md` |
| V002 | Resource inventory review validation plan | Review placeholder inventory of cleanup targets. | Resource inventory is reviewable. | `commands.md`, `configs/resource-cleanup-candidate-mapping.md`, `validation.md` |
| V003 | Resource ownership validation plan | Review ownership placeholder. | Resource owner is identified or issue is recorded. | `configs/resource-cleanup-candidate-mapping.md`, `validation.md` |
| V004 | Environment tag or label validation plan | Review `<environment>` placeholder. | Environment tag or label is present. | `configs/resource-cleanup-candidate-mapping.md`, `validation.md` |
| V005 | Resource usage state validation plan | Review usage state placeholder. | Usage state is documented. | `configs/resource-cleanup-candidate-mapping.md`, `validation.md` |
| V006 | Dependency impact review validation plan | Review dependency impact placeholder. | Dependency impact is documented before cleanup approval. | `configs/resource-cleanup-decision-record.md`, `validation.md` |
| V007 | Cleanup candidate documentation validation plan | Record `<cleanup-candidate>` status. | Cleanup candidate is documented. | `configs/resource-cleanup-summary.md`, `configs/resource-cleanup-candidate-mapping.md`, `validation.md` |
| V008 | Cleanup approval decision validation plan | Record `<cleanup-decision>` placeholder. | Manual cleanup decision is explicit. | `configs/resource-cleanup-decision-record.md`, `validation.md` |
| V009 | Cleanup execution placeholder validation plan | Document cleanup command or runbook placeholder. | Cleanup remains placeholder-only with no real deletion. | `commands.md`, `logs/resource-cleanup-validation.log`, `validation.md` |
| V010 | Post-cleanup inventory validation plan | Review post-cleanup inventory check placeholder. | Post-cleanup inventory validation is documented. | `commands.md`, `screenshots/resource-cleanup-post-check.png`, `validation.md` |
| V011 | Rollback or recreation note validation plan | Review rollback or recreation note placeholder. | Recovery note is documented where applicable. | `configs/resource-cleanup-decision-record.md`, `validation.md` |
| V012 | Cleanup judgment state validation plan | Apply cleanup judgment states. | Result is classified as `CLEANUP_NOT_REQUIRED`, `CLEANUP_CANDIDATE`, `CLEANUP_APPROVED`, `CLEANUP_COMPLETED`, `CLEANUP_BLOCKED`, or `CLEANUP_INCONCLUSIVE`. | `configs/resource-cleanup-judgment-model.md`, `validation.md` |
| V013 | Failure condition for missing ownership, missing usage evidence, unsafe cleanup decision, undocumented dependency impact, unsupported automated cleanup claim, accidental real resource deletion, or missing evidence | Evaluate findings against explicit failure conditions. | Cleanup issues produce `FAIL` or `BLOCKED` status. | `validation.md`, `logs/resource-cleanup-validation.log`, `screenshots/resource-cleanup-candidate-review.png` |

Every validation item must map to evidence. This scenario validates cleanup governance through placeholder review only.
