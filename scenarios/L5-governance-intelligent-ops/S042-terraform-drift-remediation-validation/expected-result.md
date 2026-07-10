# Expected Result

S042 is successful when:

- Prior drift evidence from S041 is referenced before remediation planning.
- Terraform plan review is documented before any remediation decision.
- Manual approval or block decision is explicit.
- Terraform apply remains placeholder-based unless a future approved execution changes scope.
- AWS, Azure, OpenStack, security rule, tag/label, network route, subnet, and Terraform-managed resource drift categories are mapped.
- Post-remediation validation is documented through a follow-up Terraform plan placeholder.
- Remediation judgment state is recorded.
- Evidence files use TODO placeholders until sanitized output is collected.
- No credentials, tfstate, kubeconfig, private keys, cloud account values, subscription IDs, tenant IDs, public IPs, or account-specific values are introduced.

The scenario must not claim automated remediation or integration with Terraform Cloud, Spacelift, Atlantis, GitOps, or any new tool.
