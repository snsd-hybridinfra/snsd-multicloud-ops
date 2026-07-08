# Objective

S014 defines the AWS Security Group least privilege validation model for the SNSD Multi-Cloud Ops AWS Service Zone.

The scenario validates that AWS service node access is planned around explicit source, destination, protocol, and port requirements. It prevents broad ingress patterns such as unrestricted SSH, unrestricted database exposure, or all-ports access from being treated as acceptable baseline security.

This scenario does not provision AWS resources. It defines how the future AWS Security Group rule set must be reviewed, captured, and validated before it can be considered ready for operational use.

## Operational Capability

- Confirm AWS Security Group existence using placeholder identifiers.
- Confirm SSH ingress is restricted to the Bastion source boundary.
- Confirm HTTP and HTTPS service exposure is intentional and documented.
- Confirm DB port `3306` is not exposed to the public internet.
- Confirm app-to-On-Prem DB and monitoring scrape paths are explicitly scoped.
- Confirm unrestricted ingress rules are treated as validation failures.
