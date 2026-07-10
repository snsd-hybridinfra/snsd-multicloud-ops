# Architecture

S046 models resource cleanup as a governance review workflow.

## Components

- Provider placeholder: `<provider>`.
- Resource name placeholder: `<resource-name>`.
- Resource ID placeholder: `<resource-id>`.
- Resource type placeholder: `<resource-type>`.
- Environment placeholder: `<environment>`.
- Cleanup candidate placeholder: `<cleanup-candidate>`.
- Cleanup decision placeholder: `<cleanup-decision>`.
- Evidence directory: `evidence/L5-governance-intelligent-ops/S046-resource-cleanup-validation/`.

## Flow

1. Identify cleanup input artifacts using placeholders.
2. Review inventory and ownership placeholders.
3. Review environment tag, usage state, and dependency impact.
4. Document the cleanup candidate and approval decision.
5. Document cleanup command or runbook placeholders without executing deletion.
6. Plan post-cleanup inventory validation.
7. Document rollback or recreation notes where applicable.
8. Classify each result using the Cleanup Judgment Model.
9. Capture TODO evidence references in commands, validation notes, configs, logs, and screenshots.

This architecture does not delete resources, run Terraform destroy, or perform automated lifecycle management.
