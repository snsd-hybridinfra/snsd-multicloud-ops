# Azure Network Module

This module is a reviewable, non-production Terraform definition for S004. It defines a resource group, virtual network, two subnets, a baseline network security group, a route table, and subnet associations.

The module contains no provider credentials, provider configuration, backend configuration, public IP resource, or production values. S004 does not run `terraform init`, `validate`, `plan`, or `apply`. Provider validation belongs to S006, and NSG least-privilege rule validation belongs to S015.
