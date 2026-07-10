# Commands

Scenario: S045-cost-guardrail-validation
Level: L5-governance-intelligent-ops
Capability: Cost Guardrail Validation

Record approved commands or manual review actions used during validation. Do not include real billing output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate cost input artifact placeholder. | Review `<monthly-cost-estimate>` and `<cost-threshold>` placeholders | Cost input placeholder | `configs/cost-guardrail-summary.md` |
| V002 | Review resource inventory placeholder. | Review `<provider>`, `<resource-name>`, and `<resource-type>` mapping | Resource inventory placeholder | `configs/cost-risk-resource-mapping.md` |
| V003 | Validate required cost owner tag. | Confirm `<cost-owner>` placeholder is present | `<resource-name>` | `configs/cost-risk-resource-mapping.md` |
| V004 | Validate required environment tag. | Confirm `<environment>` placeholder is present | `<resource-name>` | `configs/cost-risk-resource-mapping.md` |
| V005 | Validate approved resource type. | Compare `<resource-type>` to approved scenario type placeholder | `<resource-type>` | `configs/cost-risk-resource-mapping.md` |
| V006 | Validate resource count threshold. | Compare resource count placeholder to `<cost-threshold>` | `<provider>` | `configs/cost-risk-resource-mapping.md` |
| V007 | Validate compute size threshold. | Review compute size placeholder against `<cost-threshold>` | Compute placeholder | `configs/cost-risk-resource-mapping.md` |
| V008 | Validate public IP justification. | Review public IP placeholder justification without real IP values | Public IP placeholder | `configs/cost-risk-resource-mapping.md` |
| V009 | Validate unattached volume placeholder. | Review volume attachment state placeholder | Volume placeholder | `configs/cost-risk-resource-mapping.md` |
| V010 | Validate load balancer or reverse proxy cost justification. | Review load balancer or reverse proxy placeholder | Load balancer or reverse proxy placeholder | `configs/cost-risk-resource-mapping.md` |
| V011 | Document cleanup candidate decision. | Record cleanup candidate and reference S046 | Cleanup placeholder | `configs/cost-guardrail-summary.md` |
| V012 | Apply cost guardrail judgment state. | Classify result as `COST_OK`, `COST_WARNING`, `COST_RISK`, `COST_UNKNOWN`, or `COST_OUT_OF_SCOPE` | `<resource-name>` | `configs/cost-guardrail-judgment-model.md` |

## Cost Guardrail Judgment Placeholder

```text
Provider: <provider>
Resource name: <resource-name>
Resource type: <resource-type>
Cost owner: <cost-owner>
Environment: <environment>
Monthly cost estimate: <monthly-cost-estimate>
Cost threshold: <cost-threshold>
Judgment: TODO (COST_OK | COST_WARNING | COST_RISK | COST_UNKNOWN | COST_OUT_OF_SCOPE)
Cleanup candidate: TODO
Reviewer: TODO
Timestamp: TODO
```

## Output Placeholder

```text
TODO: Paste sanitized cost guardrail review summaries or manual validation notes here after approval.
TODO: Do not paste real billing output, billing account IDs, cloud account IDs, credentials, tfstate content, subscription IDs, tenant IDs, kubeconfig content, private keys, public IPs, or account-specific values.
```
