# Commands

Scenario: S043-policy-as-code-validation
Level: L5-governance-intelligent-ops
Capability: Policy as Code Validation

Record approved commands or manual review actions used during validation. Do not include real policy engine output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate policy input artifact placeholder. | Review `<policy-name>` and related input placeholders | `<policy-name>` | `configs/policy-as-code-summary.md` |
| V002 | Validate public SSH exposure policy. | Compare SSH rule placeholder with `<denied-cidr>` | `<resource-name>` | `configs/policy-control-mapping.md` |
| V003 | Validate public DB port exposure policy. | Compare DB port rule placeholder with `<denied-cidr>` | `<resource-name>` | `configs/policy-control-mapping.md` |
| V004 | Validate least privilege security rule policy. | Review allowed source and port placeholders | `<resource-type>` | `configs/policy-control-mapping.md` |
| V005 | Validate required tag or label policy. | Confirm `<required-tag>` placeholder is present | `<resource-name>` | `configs/policy-control-mapping.md` |
| V006 | Validate resource naming convention policy. | Compare `<resource-name>` with documented naming rules | `<resource-name>` | `configs/policy-control-mapping.md` |
| V007 | Validate approved region or zone placeholder policy. | Review approved location placeholder | `<resource-name>` | `configs/policy-control-mapping.md` |
| V008 | Validate Terraform configuration policy placeholder. | Review Terraform-managed resource placeholder without running Terraform | `<resource-type>` | `configs/policy-as-code-summary.md` |
| V009 | Validate cost guardrail reference. | Confirm cost policy remains referenced to S045 | Cost guardrail placeholder | `configs/policy-as-code-summary.md` |
| V010 | Apply policy judgment state. | Classify result as `POLICY_PASS`, `POLICY_FAIL`, `POLICY_WARNING`, `POLICY_NOT_APPLICABLE`, or `POLICY_INCONCLUSIVE` | `<policy-result>` | `configs/policy-judgment-model.md` |
| V011 | Capture policy evidence set. | Record review notes, sanitized summaries, logs, and screenshot placeholders | S043 evidence directory | `validation.md`, `logs/policy-as-code-validation.log` |

## Policy Judgment Placeholder

```text
Policy name: <policy-name>
Resource name: <resource-name>
Resource type: <resource-type>
Allowed CIDR: <allowed-cidr>
Denied CIDR: <denied-cidr>
Required tag: <required-tag>
Policy result: <policy-result>
Judgment: TODO (POLICY_PASS | POLICY_FAIL | POLICY_WARNING | POLICY_NOT_APPLICABLE | POLICY_INCONCLUSIVE)
Reviewer: TODO
Timestamp: TODO
```

## Output Placeholder

```text
TODO: Paste sanitized policy review summaries or manual validation notes here after approval.
TODO: Do not paste real policy engine output, credentials, backend configuration, tfstate content, account IDs, subscription IDs, tenant IDs, kubeconfig content, private keys, public IPs, or account-specific values.
```
