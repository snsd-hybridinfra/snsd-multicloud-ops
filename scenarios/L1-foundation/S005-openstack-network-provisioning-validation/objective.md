# Objective

Validate the local Terraform definition for an OpenStack baseline network consisting of a private network, private subnet, external network reference, router, router interface, baseline security group, and security group rule placeholder.

Success means the repository contains the expected reviewable resources and safe non-production examples, and the local validator completes all required checks without OpenStack authentication, provider initialization, cloud API calls, state creation, or resource provisioning.

Terraform provider validation is handled in S006. OpenStack security group validation is handled in S016. Terraform drift detection is handled in S041, and cost guardrail validation is handled in S045.
