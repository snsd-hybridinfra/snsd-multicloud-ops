# Objective

Validate the planned direct root SSH login denial model across management and service nodes.

The scenario defines validation for:

- Bastion root SSH login denial
- On-Prem DB node root SSH login denial
- On-Prem Monitoring node root SSH login denial
- AWS service node root SSH login denial
- Azure service node root SSH login denial
- OpenStack service node root SSH login denial
- `sshd_config` `PermitRootLogin` validation plan
- `sshd -T` effective configuration validation plan
- Root login failure evidence collection plan

Success means direct root SSH login denial is clearly documented and mapped to evidence, without reimplementing S011 SSH key authentication or S012 password login denial.
