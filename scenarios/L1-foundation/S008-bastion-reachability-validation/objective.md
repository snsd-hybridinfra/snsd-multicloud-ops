# Objective

Validate the planned bastion reachability model for accessing on-prem and multi-cloud service nodes.

The scenario defines validation for:

- Management Zone to Bastion Zone reachability
- Bastion to On-Prem Internal Server Zone reachability
- Bastion to On-Prem Monitoring Zone reachability
- Bastion to AWS service node reachability
- Bastion to Azure service node reachability
- Bastion to OpenStack service node reachability
- SSH jump path validation plan
- Reachability failure condition definition
- Evidence collection path validation

Success means all bastion access paths are documented with placeholders, separated by zone and provider, and mapped to evidence without implementing SSH hardening or adding real credentials, private keys, public IPs, or account-specific values.
