# Excluded Scope

The following are outside the active repository boundary:

- Any numbered scenario framework or successor series.
- Scenario-count progress, scenario aggregate execution, or scenario/evidence directory parity.
- Unapproved live infrastructure, cloud, identity, monitoring, or enforcement changes.
- Production brokerage, customer, payment, order, market-data, or regulated personal-data workloads.
- A live public-cloud connection or provider-specific production landing zone until separately selected, authorized, implemented, and validated.
- Claiming active hybrid-cloud operation while every active service plane remains local/private.
- Nexus NX-OS, IOS-XE, virtual appliance, firmware, or other licensed binary distribution.
- A second site, multi-site DR fabric, DR orchestration, or DR availability claim. Data protection is limited to backup, restore, and declarative rebuild validation.
- Provider credentials, account-specific configuration, Terraform state, kubeconfigs, keys, tokens, certificates, or private data.
- Raw live logs, unsanitized terminal output, personal identity datasets, and binary evidence.
- Automatic status promotion, maturity assignment, compliance claims, certification claims, or production-readiness claims.
- Treating a Zero Trust or KISA mapping as implementation proof.
- Blind remediation without target-version, service-impact, exception, rollback, and evidence review.
- Autonomous writes to production repositories, production data access, direct `main` pushes, user SSH keys or browser sessions inside an agent sandbox, and unbounded model or tool execution.
- Treating a disposable Kubernetes pod, NetworkPolicy alone, or a plain default container runtime as sufficient proof of untrusted-code isolation or domain-only egress enforcement.

Excluded work requires a separate approved action and must preserve package and evidence truth.
