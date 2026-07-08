# Objective

Validate the planned SSH key-based authentication model for management and operations access.

The scenario defines validation for:

- Control Plane to Bastion SSH key authentication
- Bastion to On-Prem DB node SSH key authentication
- Bastion to On-Prem Monitoring node SSH key authentication
- Bastion to AWS service node SSH key authentication
- Bastion to Azure service node SSH key authentication
- Bastion to OpenStack service node SSH key authentication
- SSH ProxyJump pattern validation
- SSH key permission validation plan
- SSH public key placement validation plan

Success means SSH key authentication is clearly documented with placeholder key paths, hosts, and users, while password-login denial remains in S012 and root-login denial remains in S013.
