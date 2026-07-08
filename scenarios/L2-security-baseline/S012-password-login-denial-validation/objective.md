# Objective

Validate the planned password-based SSH login denial model across management and service nodes.

The scenario defines validation for:

- Bastion SSH password login denial
- On-Prem DB node SSH password login denial
- On-Prem Monitoring node SSH password login denial
- AWS service node SSH password login denial
- Azure service node SSH password login denial
- OpenStack service node SSH password login denial
- `sshd_config` `PasswordAuthentication` validation plan
- `sshd -T` effective configuration validation plan
- Authentication failure evidence collection plan

Success means password authentication denial is clearly documented and mapped to evidence, without reimplementing S011 SSH key authentication or S013 root login denial.
