# Objective

Validate the local Terraform definition for an Azure baseline network consisting of a resource group, virtual network, public-tier subnet, private-tier subnet, baseline network security group, route table, and subnet associations.

Success means the repository contains the expected reviewable resources and safe non-production examples, and the local validator completes all required checks without Azure authentication, provider initialization, cloud API calls, state creation, or resource provisioning.

Terraform provider validation is handled in S006. Azure NSG least-privilege rule validation is handled in S015. Terraform drift detection is handled in S041, and cost guardrail validation is handled in S045.
