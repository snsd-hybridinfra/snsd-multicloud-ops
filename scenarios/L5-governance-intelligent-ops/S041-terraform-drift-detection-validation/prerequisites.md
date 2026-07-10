# Prerequisites

- Repository scope lock and excluded-scope rules have been reviewed.
- Matching evidence directory exists at `evidence/L5-governance-intelligent-ops/S041-terraform-drift-detection-validation/`.
- S006 Terraform provider validation is planned before provider placeholder evidence is interpreted.
- S014, S015, and S016 security group or NSG baseline scenarios are planned before security rule drift evidence is interpreted.
- S037 security rule misconfiguration response remains separate and must not be reimplemented here.
- S042 drift remediation remains separate and must not be reimplemented here.
- S043 Policy as Code, S044 Kubernetes manifest policy, and S045 cost guardrail validations remain separate.
- Placeholder values are available for `<terraform-env>`, `<provider>`, `<resource-name>`, `<drifted-resource>`, `<expected-state>`, and `<actual-state>`.
- No real credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values are required for this documentation skeleton.
