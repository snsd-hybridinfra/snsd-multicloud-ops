# Commands

Scenario: S046-resource-cleanup-validation
Level: L5-governance-intelligent-ops
Capability: Resource Cleanup Validation

Record approved commands or manual review actions used during validation. Do not include real cleanup output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate cleanup input artifact placeholder. | Review `<cleanup-candidate>` and related input placeholders | Cleanup input placeholder | `configs/resource-cleanup-summary.md` |
| V002 | Review resource inventory placeholder. | Review `<provider>`, `<resource-name>`, `<resource-id>`, and `<resource-type>` mapping | Resource inventory placeholder | `configs/resource-cleanup-candidate-mapping.md` |
| V003 | Validate resource ownership. | Confirm owner placeholder is identified | `<resource-name>` | `configs/resource-cleanup-candidate-mapping.md` |
| V004 | Validate environment tag or label. | Confirm `<environment>` placeholder is present | `<resource-name>` | `configs/resource-cleanup-candidate-mapping.md` |
| V005 | Validate resource usage state. | Review usage state placeholder | `<resource-name>` | `configs/resource-cleanup-candidate-mapping.md` |
| V006 | Review dependency impact. | Document upstream and downstream dependency placeholders | `<resource-name>` | `configs/resource-cleanup-decision-record.md` |
| V007 | Document cleanup candidate. | Record `<cleanup-candidate>` status | `<resource-name>` | `configs/resource-cleanup-summary.md` |
| V008 | Document cleanup approval decision. | Record `<cleanup-decision>` and manual approval placeholder | `<resource-name>` | `configs/resource-cleanup-decision-record.md` |
| V009 | Document cleanup execution placeholder. | Record cleanup command or runbook placeholder without execution | `<resource-name>` | `logs/resource-cleanup-validation.log` |
| V010 | Document post-cleanup inventory check. | Record post-check placeholder without real deletion | `<resource-name>` | `screenshots/resource-cleanup-post-check.png` |
| V011 | Document rollback or recreation note. | Record recreation or rollback placeholder where applicable | `<resource-name>` | `configs/resource-cleanup-decision-record.md` |
| V012 | Apply cleanup judgment state. | Classify result as `CLEANUP_NOT_REQUIRED`, `CLEANUP_CANDIDATE`, `CLEANUP_APPROVED`, `CLEANUP_COMPLETED`, `CLEANUP_BLOCKED`, or `CLEANUP_INCONCLUSIVE` | `<cleanup-candidate>` | `configs/resource-cleanup-judgment-model.md` |

## Cleanup Judgment Placeholder

```text
Provider: <provider>
Resource name: <resource-name>
Resource ID: <resource-id>
Resource type: <resource-type>
Environment: <environment>
Cleanup candidate: <cleanup-candidate>
Cleanup decision: <cleanup-decision>
Judgment: TODO (CLEANUP_NOT_REQUIRED | CLEANUP_CANDIDATE | CLEANUP_APPROVED | CLEANUP_COMPLETED | CLEANUP_BLOCKED | CLEANUP_INCONCLUSIVE)
Rollback or recreation note: TODO
Reviewer: TODO
Timestamp: TODO
```

## Output Placeholder

```text
TODO: Paste sanitized cleanup governance review summaries or manual validation notes here after approval.
TODO: Do not paste real deletion output, Terraform destroy output, cloud account IDs, billing account IDs, credentials, tfstate content, subscription IDs, tenant IDs, kubeconfig content, private keys, public IPs, or account-specific values.
```
