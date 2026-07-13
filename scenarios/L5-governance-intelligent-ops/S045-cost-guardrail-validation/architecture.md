# Architecture

Implemented flow: sanitized rules/inputs/evidence -> `validate-cost-guardrail.ps1` -> local log/summary and S046/S050 mappings.

S045 models cost guardrails as a placeholder resource review workflow.

## Components

- Provider placeholder: `<provider>`.
- Resource name placeholder: `<resource-name>`.
- Resource type placeholder: `<resource-type>`.
- Cost owner placeholder: `<cost-owner>`.
- Environment placeholder: `<environment>`.
- Monthly cost estimate placeholder: `<monthly-cost-estimate>`.
- Cost threshold placeholder: `<cost-threshold>`.
- Evidence directory: `evidence/L5-governance-intelligent-ops/S045-cost-guardrail-validation/`.

## Flow

1. Identify cost input artifacts using placeholders.
2. Review resource inventory placeholders across AWS, Azure, and OpenStack.
3. Check cost owner and environment tags or labels.
4. Review resource type, resource count, compute size, public IP, volume, load balancer, reverse proxy, and node count placeholders.
5. Document cleanup candidate decisions without performing cleanup.
6. Classify each result using the Cost Guardrail Judgment Model.
7. Capture TODO evidence references in commands, validation notes, configs, logs, and screenshots.

This architecture does not connect to billing APIs, provision resources, run Terraform, or perform cleanup.
