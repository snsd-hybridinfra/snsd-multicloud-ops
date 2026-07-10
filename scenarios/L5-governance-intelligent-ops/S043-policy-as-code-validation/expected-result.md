# Expected Result

S043 is successful when:

- Policy input artifacts are documented as placeholders.
- Public SSH exposure prohibition is represented.
- Public DB port exposure prohibition is represented.
- Least privilege security rule policy is represented.
- Required tag or label policy is represented.
- Resource naming convention policy is represented.
- Approved region or zone policy is represented with placeholders.
- Terraform configuration policy is represented without running Terraform.
- Cost guardrail validation is referenced but left to S045.
- Policy judgment state is recorded.
- Evidence files use TODO placeholders until sanitized output is collected.
- No credentials, tfstate, kubeconfig, private keys, cloud account values, subscription IDs, tenant IDs, public IPs, or account-specific values are introduced.

The scenario must not claim CSPM, real-time blocking, automated remediation, OPA, Conftest, Checkov, Sentinel, Terraform Cloud, GitOps, or any new policy engine integration.
