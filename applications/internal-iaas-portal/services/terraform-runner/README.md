# OpenStack Terraform runner

The runner consumes approval-owned fixed jobs and defaults to `mock`. Real mode
fails closed unless `TF_OPENSTACK_DEPLOYMENT_AUTHORIZED=true` and all reviewed
OpenStack inputs are present.

Required real-mode inputs are `OS_CLIENT_CONFIG_FILE`, `OS_CLOUD`,
`OS_REGION_NAME`, `TF_OPENSTACK_NETWORK_ID`,
`TF_OPENSTACK_SECURITY_GROUP_IDS`, `TF_OPENSTACK_APPROVED_IMAGE_NAME`,
`TF_OPENSTACK_APPROVED_K3S_IMAGE_NAME`, `TF_OPENSTACK_KEYPAIR_NAME`, and the
three approved flavor names. The credentials file and Terraform state are
runtime-only and must be protected outside Git.

The customized supply-chain wrapper also requires
`TF_TERRAFORM_BINARY_SHA256`, `TF_SUPPLY_CHAIN_LOCK`,
`TF_TERRAFORM_CATALOG`, `TF_PROVIDER_MIRROR_ROOT`,
`TF_OPENSTACK_PROVIDER_PACKAGE`, and
`TF_OPENSTACK_PROVIDER_PACKAGE_SHA256`. The provider mirror, package and CLI
digest are external reviewed runtime inputs; the runner generates a
filesystem-mirror-only CLI configuration and does not contact the provider
registry.

k3s apply additionally requires `TF_K3S_CONFIGURATION_AUTHORIZED=true`, an
approved SSH remote user, private-key path, strict known-hosts authority,
runner-local k3s binary and matching air-gap image archive, and SHA-256 for both
artifacts. `ansible-core` 2.21.2 is pinned in the runner image. None of these
runtime files belongs in Git.

Before apply, the runner verifies the catalog and module authorities, exact
module file set, Terraform CLI version/digest, OpenStack provider
source/version/package digest, and the saved plan JSON. Only exact `create` or
`no-op` actions for one port and one instance may apply. Destroy and automatic
rollback use an inspected saved destroy plan with only `delete` or `no-op`;
replacement, update, import, provider substitution and uninspected destroy are
denied.
After apply, it rejects any state other than one Neutron port and one Nova VM,
checks private addressing, port security, exact security groups, image, flavor,
key pair, metadata, and the absence of a Floating IP. For k3s, the runner then
executes the digest-pinned Ansible playbook, validates API readiness and the
declared platform components, and returns `READY`. If configuration fails, the
runner automatically destroys the newly created Nova instance and port. A
failed or unvalidated configuration cannot authorize a Grant.
