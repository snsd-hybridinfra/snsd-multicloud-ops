# Lab Execution Profiles

**Status: PLANNED - no profile has been executed or validated.**

## Profile Summary

| Profile | Powered-On Roles | Guest vCPU | Guest RAM | Nominal Active VM Disk | Host Memory Margin After 8GB Reserve |
|---|---|---:|---:|---:|---:|
| A - Network and Local Services | EVE-NG, Bastion, k3s-node, DB Primary, DB Replica, Monitoring, Backup | 10 | 17GB | 174GB | Approximately 6.9GiB |
| B - OpenStack Build | EVE-NG, OpenStack All-in-One | 8 | 20GB | 170GB | Approximately 3.9GiB |
| C - OpenStack Integration | EVE-NG, OpenStack All-in-One, Bastion | 9 | 21GB | 182GB | Approximately 2.9GiB |
| D - AWS and Azure Validation | Terraform on Windows; local VMs only when directly required | Variable | Variable | Variable | Must preserve at least 8GB |

Margins are planning arithmetic based on approximately 31.9GiB effective host
memory. Actual hypervisor overhead and host workload may reduce them, so a
profile must be stopped if pressure appears.

## Profile A - Network and Local Services

- OpenStack All-in-One must be powered off.
- Intended roles: EVE-NG, Bastion, k3s-node, DB Primary, DB Replica,
  Monitoring, and Backup.
- Use for staged on-prem network and local-service work only.
- Power off roles not required for the current scenario even though the profile
  defines their maximum combined envelope.

## Profile B - OpenStack Build

- EVE-NG and OpenStack All-in-One only.
- Bastion, k3s-node, both database VMs, Monitoring, and Backup must be powered
  off.
- Nested virtualization must be available before OpenStack installation.
- Initial Nova workload is limited to one approximately 1-vCPU/1GB instance.

## Profile C - OpenStack Integration

- EVE-NG, OpenStack All-in-One, and Bastion only.
- k3s-node, both database VMs, Monitoring, and Backup must be powered off.
- This is the tightest memory profile; avoid unrelated host workloads and stop
  if paging or hypervisor pressure appears.

## Profile D - AWS and Azure Validation

- Terraform runs on the Windows host.
- Public-cloud compute remains temporary and cost-guarded.
- Local VMs run only when directly required for the validation path.
- Do not start OpenStack or the complete local-service profile by default.
- Destroy temporary compute and verify cleanup after sanitized evidence
  collection.

## Profile Transition Checklist

1. Finish or explicitly suspend the current scenario without claiming PASS.
2. Collect only authorized, sanitized evidence from real execution.
3. Power off the current profile; do not rely on VM suspend for resource release.
4. Remove expired snapshots and confirm active-SSD headroom.
5. Start only the next profile's required roles.
6. Confirm the 8GB host reserve before validation.

Full simultaneous execution of all planned VMs is prohibited.
