# Architecture

Implemented flow: sanitized schema/rules/inputs/evidence -> `validate-policy-as-code.ps1` -> local log/summary, with no external execution edge.

S043 models Policy as Code as a reviewable governance control, not as a deployed policy platform.

## Components

- Policy placeholder: `<policy-name>`.
- Resource placeholder: `<resource-name>`.
- Resource type placeholder: `<resource-type>`.
- Allowed CIDR placeholder: `<allowed-cidr>`.
- Denied CIDR placeholder: `<denied-cidr>`.
- Required tag placeholder: `<required-tag>`.
- Policy result placeholder: `<policy-result>`.
- Evidence directory: `evidence/L5-governance-intelligent-ops/S043-policy-as-code-validation/`.

## Flow

1. Identify policy input artifacts using placeholders.
2. Map each policy category to a resource or configuration placeholder.
3. Review public SSH, public DB, least privilege, tag/label, naming, approved location, Terraform configuration, and cost-reference policies.
4. Classify each result using the Policy Judgment Model.
5. Capture TODO evidence references in commands, validation notes, configs, logs, and screenshots.

No policy engine, cloud account, Terraform execution, or automated enforcement path is created by this architecture.
