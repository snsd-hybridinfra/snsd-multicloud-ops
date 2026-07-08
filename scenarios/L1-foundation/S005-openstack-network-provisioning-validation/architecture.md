# Architecture

## Relevant Components

- Provider Network placeholder: external or shared network represented by `<openstack-provider-network-name>`. This scenario validates reference and reachability assumptions only; it does not create the provider network.
- Tenant Network: project-owned workload network represented by `<openstack-tenant-network-name>`.
- Tenant Subnet: tenant address segment represented by `<openstack-tenant-subnet-name>`.
- Router: tenant router represented by `<openstack-router-name>`.
- Router Interface: connection between router and tenant subnet represented by `<openstack-router-interface-id>`.
- Security Group baseline: minimum traffic boundary represented by `<openstack-security-group-name>`.
- Floating IP placeholder: future external access placeholder represented by `<openstack-floating-ip>`.
- Keypair placeholder: future access reference represented by `<openstack-keypair-name>`.
- Terraform or OpenStack CLI outputs: sanitized references for validation.

## Logical Flow

1. OpenStack CLI authentication validation is planned without storing credential files.
2. Network listing is planned to distinguish provider networks from tenant networks.
3. Provider Network existence is validated as a dependency, not as a provisioned resource.
4. Tenant Network, Tenant Subnet, Router, Router Interface, and Security Group baseline are validated as planned tenant-owned resources.
5. Floating IP and Keypair are treated as placeholders until future execution is explicitly approved.

## Out-of-Scope Components

No real OpenStack credentials, `openrc` files, `clouds.yaml`, Terraform state, private keys, provider resources, production networks, or account-specific values are used by this scenario.
