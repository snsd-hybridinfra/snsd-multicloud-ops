# Excluded Scope

The following work is explicitly excluded from the initial repository foundation.

## Cloud and Infrastructure

- Repository automation that provisions, changes, or destroys resources in
  AWS, Azure, GCP, OCI, OpenStack, or any other cloud without a separately
  approved execution boundary.
- Terraform provider blocks, remote backends, tfvars, state files, or account-specific modules.
- Real VPC, VNet, subnet, IAM, firewall, load balancer, DNS, VPN, or Kubernetes cluster creation.

## Credentials and Secrets

- API keys, passwords, tokens, SSH private keys, certificates, kubeconfig files, vault files, and service account files.
- Any file containing real account IDs, tenant IDs, subscription IDs, project IDs, hostnames, public IPs, or private IPs tied to a real environment.

## Runtime Implementation

- Production deployment automation.
- CI/CD pipelines that deploy to real environments.
- Real monitoring integrations, alert routing, or incident paging.
- Real ML training jobs, model deployment, or production inference services.
- Committing raw terminal output from a live lab. Only normalized, sanitized,
  scenario-mapped text evidence is permitted.

## Technology Expansion

- Tools, platforms, or services outside the locked scope.
- Vendor-specific services not already represented by the foundation directories.
- Binary deliverables, screenshots, archives, or generated reports.

Excluded items may be reconsidered only through an ADR and explicit scope update.

Operator-authorized execution in the disposable non-production OpenStack lab
is not itself stored or automated here. Its sanitized results may be retained
under an existing scenario according to ADR-0002 and the evidence model.
