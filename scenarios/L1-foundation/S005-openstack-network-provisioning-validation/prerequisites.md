# Prerequisites

## Required Previous Scenarios

- S002 EVE-NG On-Prem Routing Validation, including VLAN 70 gateway and NAT/PAT evidence.

## Required Platform Conditions

- Ubuntu Server 24.04 disposable AIO VM with nested virtualization.
- Dedicated management and provider interfaces.
- Kolla-Ansible configured for OpenStack 2026.1 and Open vSwitch.
- Passwordless non-interactive privilege escalation for the controlled deployment workflow.
- Kolla virtual environment dependencies installed in the interpreter actually used by Kolla-Ansible.

## Required Access Assumptions

- Authentication material and SSH keys are managed outside the repository.
- The operator runs Kolla/OpenStack commands in the lab and supplies only sanitized results.
- No `clouds.yaml`, openrc content, token value, password, or key is copied into evidence.
