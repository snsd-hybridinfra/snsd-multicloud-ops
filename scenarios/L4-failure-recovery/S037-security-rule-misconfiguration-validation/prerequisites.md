# Prerequisites

- Repository scope lock and excluded-scope rules have been reviewed.
- Matching evidence directory exists at `evidence/L4-failure-recovery/S037-security-rule-misconfiguration-validation/`.
- S014 AWS Security Group least privilege validation is planned before AWS rule behavior is interpreted.
- S015 Azure NSG least privilege validation is planned before Azure rule behavior is interpreted.
- S016 OpenStack Security Group validation is planned before OpenStack rule behavior is interpreted.
- S017 MariaDB access control validation remains separate and must not be reimplemented here.
- S041 Terraform drift detection and S043 Policy as Code validation remain separate and must not be reimplemented here.
- Placeholder values are available for `<security-group-id>`, `<nsg-name>`, `<openstack-security-group>`, `<firewall-rule>`, `<allowed-cidr>`, `<unauthorized-cidr>`, and `<service-port>`.
- No real public IPs, cloud account IDs, credentials, secrets, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, or account-specific values are required for this documentation skeleton.
