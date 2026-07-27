# Azure Network Module

This module is a reviewable, non-production Terraform definition for retired-numbered-case. It defines a resource group, virtual network, two subnets, a baseline network security group, a route table, and subnet associations.

The module contains no provider credentials, provider configuration, backend configuration, public IP resource, or production values. retired-numbered-case does not run `terraform init`, `validate`, `plan`, or `apply`. Provider validation belongs to retired-numbered-case, and NSG least-privilege rule validation belongs to retired-numbered-case.
