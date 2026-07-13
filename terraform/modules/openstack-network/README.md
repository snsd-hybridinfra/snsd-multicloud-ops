# OpenStack Network Module

This module is a reviewable, non-production Terraform definition for S005. It defines a private network, subnet, external network reference, router, router interface, baseline security group, and one management rule placeholder.

The module contains no provider credentials, provider configuration, backend configuration, public IP resource, project identifiers, authentication URL, or production values. S005 does not run `terraform init`, `validate`, `plan`, or `apply`. Provider validation belongs to S006, and security group validation belongs to S016.
