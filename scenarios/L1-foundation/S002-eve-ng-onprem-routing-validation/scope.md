# Scope

## Included

- EVE-NG topology file existence check.
- Router configuration snapshot existence check.
- Management Zone gateway reachability check.
- Bastion Zone gateway reachability check.
- Internal Server Zone gateway reachability check.
- Monitoring Zone gateway reachability check.
- Transit Zone route existence check.
- Default route existence check where applicable.
- Inter-zone ping test plan.
- Route table capture plan.
- Firewall boundary awareness as documentation only.

## Excluded

- Firewall rule implementation or firewall policy changes.
- Real Terraform, Ansible, Kubernetes, cloud, monitoring, ML, or backup logic.
- Changes to live routing devices.
- Creation of credentials, private keys, tfstate, kubeconfig files, or account-specific files.
- Capture of real public IPs, private IPs, hostnames, account IDs, subscription IDs, tenant IDs, project IDs, or secrets.

## Assumptions

- Zone names are logical labels and do not expose real network details.
- Sanitized placeholders such as `<management-gateway>`, `<bastion-gateway>`, `<internal-server-gateway>`, `<monitoring-gateway>`, and `<transit-router>` are used until approved lab output is captured.
- Any future command output is reviewed and sanitized before commit.
