# Commands

Scenario: S009-dns-hostname-resolution-validation
Level: L1-foundation
Capability: DNS Hostname Resolution Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include real public IPs, private IPs, credentials, SSH private keys, tokens, tfstate, kubeconfig content, cloud account IDs, subscription IDs, tenant IDs, or provider-specific secrets.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Hostname naming convention validation plan | Review planned hostnames for `*.snsd.local` convention. | Confirm hostname naming is consistent. | TODO: record sanitized result after review. |
| V002 | Hostname-to-inventory consistency validation plan | Compare planned hostnames to inventory placeholder entries. | Confirm hostnames map to inventory placeholders. | TODO: record sanitized result after review. |
| V003 | Control Plane hostname resolution plan | `Resolve-DnsName control.snsd.local` or approved equivalent after future approval. | Confirm planned control-plane lookup method. | TODO: record sanitized output after approved execution. |
| V004 | Bastion hostname resolution plan | `Resolve-DnsName bastion.snsd.local` or approved equivalent after future approval. | Confirm planned bastion lookup method. | TODO: record sanitized output after approved execution. |
| V005 | On-Prem DB hostname resolution plan | Resolve `db-primary.snsd.local`, `db-replica-01.snsd.local`, and `db-replica-02.snsd.local`. | Confirm planned DB hostname lookup method. | TODO: record sanitized output after approved execution. |
| V006 | On-Prem Monitoring hostname resolution plan | Resolve `prometheus.snsd.local` and `grafana.snsd.local`. | Confirm planned monitoring hostname lookup method. | TODO: record sanitized output after approved execution. |
| V007 | AWS service node hostname resolution plan | `Resolve-DnsName aws-app-01.snsd.local` or approved equivalent after future approval. | Confirm planned AWS service hostname lookup method. | TODO: record sanitized output after approved execution. |
| V008 | Azure service node hostname resolution plan | `Resolve-DnsName azure-app-01.snsd.local` or approved equivalent after future approval. | Confirm planned Azure service hostname lookup method. | TODO: record sanitized output after approved execution. |
| V009 | OpenStack service node hostname resolution plan | `Resolve-DnsName openstack-app-01.snsd.local` or approved equivalent after future approval. | Confirm planned OpenStack service hostname lookup method. | TODO: record sanitized output after approved execution. |
| V010 | Prometheus target hostname consistency plan | Review Prometheus target hostname placeholders. | Confirm Prometheus target hostnames are consistent. | TODO: record sanitized result after review. |
| V011 | Evidence target hostname consistency plan | Review evidence target hostname placeholders. | Confirm evidence target hostnames are consistent. | TODO: record sanitized result after review. |
| V012 | Unresolved hostname, duplicate hostname, inconsistent inventory mapping, or real public IP exposure failure condition | Review failed hostname validation findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/hostname-resolution-plan.md`
- `configs/hostname-inventory-mapping.md`
- `logs/hostname-resolution-validation.log`
- `screenshots/hostname-resolution-test.png`
