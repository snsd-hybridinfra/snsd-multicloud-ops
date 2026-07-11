# Scope

## Included

- Validate the on-prem routing topology document exists.
- Validate five required zone names, five placeholder devices, and five CIDR placeholder tokens.
- Validate four non-production router example configs exist.
- Validate example configs contain placeholder interfaces and routes.
- Detect private-key markers, credential assignments, and literal IPv4 addresses.
- Generate a local log and Markdown summary.

## Excluded

- Live EVE-NG authentication or API access.
- SSH, console, or other connections to routers and network devices.
- Real reachability, routing table, or firewall validation.
- Cloud connectivity and AWS/Azure/OpenStack provisioning; those belong to S003, S004, and S005.
- Multi-cloud inventory, handled in S007.
- Bastion reachability, handled in S008.
- DNS and hostname resolution, handled in S009.
- Credentials, private keys, secrets, real addressing, tfstate, kubeconfig, and account-specific data.

## Assumptions

- Example configs intentionally use angle-bracket placeholders.
- Live routing validation will be designed in a later explicitly authorized scenario.
