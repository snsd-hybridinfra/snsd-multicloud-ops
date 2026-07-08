# Objective

S015 defines the Azure Network Security Group least privilege validation model for the SNSD Multi-Cloud Ops Azure Service Zone.

The scenario validates that Azure App Node access is planned around explicit source, destination, protocol, port, and priority requirements. It prevents broad inbound patterns such as unrestricted SSH, unrestricted database exposure, or all-ports access from being treated as acceptable baseline security.

This scenario does not provision Azure resources. It defines how the future Azure NSG rule set must be reviewed, captured, and validated before it can be considered ready for operational use.

## Operational Capability

- Confirm Azure NSG existence using placeholder identifiers.
- Confirm SSH inbound access is restricted to the Bastion source boundary.
- Confirm HTTP and HTTPS service exposure is intentional and documented.
- Confirm DB port `3306` is not exposed to Internet or unrestricted sources.
- Confirm Azure App-to-On-Prem DB and monitoring scrape paths are explicitly scoped.
- Confirm unrestricted inbound rules are treated as validation failures.
