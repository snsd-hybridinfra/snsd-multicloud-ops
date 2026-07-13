# Architecture

## Repository Components

- `bastion-reachability-map.example.md`: symbolic source, bastion, zone, target, and address relationships.
- `bastion-ssh-access-policy.example.md`: expected administrative access controls.
- `validate-bastion-reachability-model.ps1`: text-only completeness and safety validation.
- S008 evidence directory: generated validation log and summary.

## Reachability Model

The control plane reaches administrative targets only through `bastion-host-01`. The model separates internal servers, monitoring, databases, Kubernetes nodes, on-premises network devices, and cloud service nodes while retaining placeholder-only addresses.

## Validation Flow

The validator reads two Markdown artifacts, checks required paths and policy statements, scans for unsafe values, checks its own source for prohibited connection commands, and writes evidence. No route, DNS, security rule, SSH session, or host is inspected.
