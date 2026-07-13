# Objective

Validate a repository-side AWS Security Group baseline that uses default-deny inbound, explicit required-service rules, restricted management and internal access, controlled public-web exceptions, and justified egress.

Success means the policy, matrix, and existing Terraform placeholder pass all safety checks without AWS authentication, Security Group queries, state, plans, or resource changes.

AWS network provisioning is handled in S003, provider declarations in S006, SSH controls in S011-S013, Azure NSG in S015, and OpenStack Security Groups in S016.
