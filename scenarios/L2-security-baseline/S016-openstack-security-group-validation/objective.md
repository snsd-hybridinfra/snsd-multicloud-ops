# Objective

S016 defines the OpenStack Security Group least privilege validation model for the SNSD Multi-Cloud Ops OpenStack Private Cloud Service Zone.

The scenario validates that OpenStack App VM access is planned around explicit source, destination, protocol, and port requirements. It prevents broad ingress patterns such as unrestricted SSH, unrestricted database exposure, or all-ports access from being treated as acceptable baseline security.

This scenario does not provision OpenStack resources. It defines how the future OpenStack Security Group rule set must be reviewed, captured, and validated before it can be considered ready for operational use.

## Operational Capability

- Confirm OpenStack Security Group existence using placeholder identifiers.
- Confirm SSH ingress is restricted to the Bastion source boundary.
- Confirm HTTP and HTTPS service exposure is intentional and documented.
- Confirm DB port `3306` is not exposed to public or provider network sources.
- Confirm OpenStack App-to-On-Prem DB and monitoring scrape paths are explicitly scoped.
- Confirm unrestricted ingress rules are treated as validation failures.
