# Architecture

## Relevant Components

- Control Plane: `control.snsd.local` mapped to `<control-plane-ip>`.
- Bastion: `bastion.snsd.local` mapped to `<bastion-ip>`.
- On-Prem DB primary: `db-primary.snsd.local` mapped to `<db-primary-ip>`.
- On-Prem DB replicas: `db-replica-01.snsd.local` and `db-replica-02.snsd.local` mapped to placeholder replica IPs.
- Monitoring: `prometheus.snsd.local` and `grafana.snsd.local` mapped to monitoring placeholders.
- AWS service node: `aws-app-01.snsd.local` mapped to `<aws-app-node-ip>`.
- Azure service node: `azure-app-01.snsd.local` mapped to `<azure-app-node-ip>`.
- OpenStack service node: `openstack-app-01.snsd.local` mapped to `<openstack-app-node-ip>`.
- Kubernetes service hostname placeholders: future service names mapped without kubeconfig or live cluster data.
- Evidence target hostnames: named targets used to organize validation collection paths.

## Logical Flow

1. Hostnames follow the `*.snsd.local` convention.
2. Hostnames map to inventory placeholders, not real IP addresses.
3. Provider-specific hostnames are separated by AWS, Azure, and OpenStack prefixes.
4. Monitoring hostnames support Prometheus and Grafana target planning.
5. Evidence hostnames align with future collection targets.

## Out-of-Scope Components

Real DNS servers, `/etc/hosts` edits, lab DNS zones, kubeconfig files, public DNS records, provider DNS services, and live resolver changes are not part of S009.
