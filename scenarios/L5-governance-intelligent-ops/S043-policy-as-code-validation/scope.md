# Scope

Implemented boundary: static local evidence only; no state/tfvars/plan binary/backend, credentials, real identifiers/network values, secrets, or external policy runtime.

## Included

- Terraform configuration policy validation placeholder.
- Cloud security rule policy validation placeholder.
- Required tag or label policy validation placeholder.
- Public exposure policy validation placeholder.
- DB port exposure policy validation placeholder.
- SSH exposure policy validation placeholder.
- Resource naming convention policy validation placeholder.
- Approved region or zone placeholder policy validation.
- Cost-related policy reference placeholder.
- Policy violation judgment model.
- Policy validation evidence collection plan.

## Target Policy Categories

- Public SSH exposure prohibition.
- Public DB port exposure prohibition.
- Least privilege security rule requirement.
- Required resource tag or label presence.
- Approved region or zone placeholder.
- Resource naming convention compliance.
- Terraform-managed resource policy placeholder.
- Cost guardrail reference placeholder.

## Policy Judgment Model

- `POLICY_PASS`: Resource or configuration satisfies the defined policy.
- `POLICY_FAIL`: Resource or configuration violates the defined policy.
- `POLICY_WARNING`: Resource is allowed but requires review.
- `POLICY_NOT_APPLICABLE`: Policy does not apply to this resource.
- `POLICY_INCONCLUSIVE`: Required input or evidence is missing.

## Excluded

- Real policy engine integration.
- New policy tools or policy engines.
- Production-grade CSPM.
- Real-time blocking.
- Automated remediation.
- OPA, Conftest, Checkov, Sentinel, Terraform Cloud, GitOps, or related integrations unless later added through scope change.
- Real Terraform runs against cloud accounts.
- tfstate, credentials, secrets, private keys, kubeconfig, cloud account IDs, subscription IDs, tenant IDs, public IPs, or account-specific values.
- Terraform drift detection, handled in S041.
- Terraform drift remediation, handled in S042.
- Kubernetes manifest policy validation, handled in S044.
- Cost guardrail validation, handled in S045.
- Resource cleanup validation, handled in S046.
- Security rule misconfiguration response, handled in S037.
