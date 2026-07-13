# Security Rule Misconfiguration Validation

S037 validates a controlled security-rule misconfiguration detection and rollback workflow through sanitized local evidence only.

## Controlled model

1. Confirm least privilege before change for `<cloud-provider>` using `<security-rule-id-placeholder>`, `<security-group-placeholder>`, `<nsg-placeholder>`, `<openstack-security-group-placeholder>`, and `<kubernetes-network-policy-placeholder>` references.
2. Record a **MANUAL MISCONFIGURATION SAMPLE** that contrasts `<source-cidr-placeholder>` with `<approved-source-cidr-placeholder>`, `<restricted-admin-cidr-placeholder>`, or `<bastion-cidr-placeholder>` on `<service-port-placeholder>`.
3. Classify the affected surface, exposure impact, owner/reason/expiry/approval requirements, and rollback decision.
4. Record **MANUAL ROLLBACK SAMPLE** with `<rollback-change-id-placeholder>` and verify the post-rollback rule is restricted.
5. Store sanitized evidence under `<evidence-path>`.

StaticEvidence does not perform real cloud or network testing. Real AWS Security Group, Azure NSG, OpenStack Security Group, firewall rule, or Kubernetes NetworkPolicy modification/enforcement testing is out of scope. Automatic blocking, SOAR playbook execution, WAF integration, IDS/IPS integration, EDR response, and production emergency-change automation are out of scope.
