# Bastion Reachability Evidence Collection (Legacy Filename)

**Status: PLANNED — no Bastion VM or reachability evidence exists.**

> Canonical phase mapping: this guide belongs to **Lab Phase 1** under
> `docs/lab-build-order.md`. The filename is retained to avoid breaking existing
> links; it is not an independent phase-order authority.

## Purpose

Lab Phase 1 prepares a safe, repeatable workflow for collecting sanitized Bastion VM reachability evidence from a disposable non-production lab. It does not change the locked architecture or scenario list, and it does not claim that live Bastion validation has already occurred.

## Related Scenarios

| Scenario | Lab Phase 1 Relationship |
|---|---|
| S001 Control Plane Toolchain Validation | Confirms the host workstation has Git, PowerShell, SSH, and Python available before collection |
| S008 Bastion Reachability Validation | Owns the SSH path, Bastion access boundary, and sanitized reachability result |
| S009 DNS / Hostname Resolution Validation | Owns hostname and optional resolution evidence |
| S010 Evidence Directory Structure Validation | Confirms collected artifacts use the matching evidence paths and required directory model |

## Bastion VM Role

The Bastion VM is the controlled administrative entry point between the Host PC and internal lab roles. It should:

- accept SSH only through the approved non-production lab path;
- provide basic hostname, identity, uptime, interface, SSH-service, and listening-socket evidence;
- avoid storing application data or committed credentials;
- act as a boundary for later internal host access without becoming a public production jump host.

Repository references use `<bastion-ip-placeholder>`, `<ssh-user-placeholder>`, and `<hostname-placeholder>`. Actual values must remain outside the repository until evidence is sanitized.

## Recommended VM Specification

| Resource | Reference Size | Notes |
|---|---|---|
| vCPU | 1 virtual CPU | Authoritative Lab Phase 0 allocation |
| Memory | 1 GB | Authoritative Lab Phase 0 allocation |
| Disk | 12 GB | Active-VM SSD; no production data or long-term evidence archive |
| Network adapters | 2 | One NAT adapter and one host-only/lab adapter |
| Operating system | Supported non-production Linux distribution | Keep package and security updates current before evidence collection |

These values are planning guidance aligned with
`docs/vm-resource-allocation-plan.md`, not proof that the Bastion VM exists.

## Recommended Network Model

- **NAT adapter:** provides outbound internet access for package installation and updates. It is not an inbound public service path.
- **Host-only or lab adapter:** provides internal connectivity between the Host PC and `<bastion-ip-placeholder>` and, in later phases, between the Bastion and internal lab roles.
- **Administrative path:** Host PC → Bastion SSH only. Direct public exposure and production routing remain out of scope.

Do not commit the actual NAT address, lab address, route table, interface identifier, DNS suffix, or host-only network range.

## Required Packages

Install these packages in the disposable Bastion VM using the guest operating system's approved package manager:

- `openssh-server`
- `curl`
- `wget`
- `vim`
- `net-tools`
- `iputils-ping`
- `dnsutils`
- `traceroute`
- `git`

Package installation output is optional evidence and must be sanitized before commit.

## Commands to Run Inside Bastion

Run only the commands required for the owning validation check:

```bash
hostname
whoami
uptime
ip addr
systemctl is-active ssh
ss -tulpen
```

If `ss` is unavailable, use the read-only fallback:

```bash
netstat -tulpen
```

For S009 hostname/resolution evidence:

```bash
hostname
hostname -I
getent hosts <hostname-placeholder>
nslookup <hostname-placeholder>
```

`nslookup` is optional when no DNS or hosts-file mapping is configured. Its absence must be recorded as `NOT_APPLICABLE`, not presented as successful resolution.

## Commands to Run from Host PC

Confirm the local SSH client and then perform a read-only, non-interactive connection:

```powershell
Get-Command ssh
ssh -V
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes <ssh-user-placeholder>@<bastion-ip-placeholder> "hostname; whoami; uptime; systemctl is-active ssh"
```

Use the sample collector with an output directory outside the repository:

```powershell
powershell -ExecutionPolicy Bypass -File tools\collect-bastion-evidence.example.ps1 `
  -BastionHost '<bastion-ip-placeholder>' `
  -SshUser '<ssh-user-placeholder>' `
  -OutputRoot '<local-output-root-placeholder>'
```

The Bastion host key must already be trusted through a separately reviewed manual step. The sample collector does not disable host-key checking, prompt for a password, read a private key, or copy raw output into `<evidence-path>`.

## Evidence Files to Collect

| Evidence | Owning Scenario | Destination after Sanitization |
|---|---|---|
| Host-side SSH client and connection result | S001, S008 | `evidence/L1-foundation/S008-bastion-reachability-validation/logs/` |
| Bastion hostname, user, uptime, interface, SSH service, and listening sockets | S008 | `evidence/L1-foundation/S008-bastion-reachability-validation/logs/` |
| Hostname and optional resolution output | S009 | `evidence/L1-foundation/S009-dns-hostname-resolution-validation/logs/` |
| Updated command/result mapping | S008, S009 | Each scenario's `commands.md` and `validation.md` |
| Directory and filename conformance result | S010 | S010 validation output and the matching `<evidence-path>` |

Only `.sanitized.txt` output may be copied into an evidence directory. Keep `.raw.txt` outside the repository and delete it securely after review according to the local lab procedure.

## Sanitization Before Commit

- Replace every IPv4/IPv6 value with `<lab-ip-masked>`.
- Replace the SSH username and reported user with `<user-masked>`.
- Replace the Bastion hostname with `<hostname-masked>`.
- Remove MAC/interface identifiers, local paths, domains, prompts, and unrelated output.
- Never commit passwords, tokens, credentials, private keys, `known_hosts` content, `/etc/shadow`, kubeconfig, or cloud profiles.
- Review the entire sanitized file and `git diff` before commit.
- If safe sanitization is uncertain, commit a short sanitized summary instead.

## Completion Criteria

The Bastion evidence portion of Lab Phase 1 is complete only when:

- S001 confirms the Host PC SSH tool is available;
- the Host PC can connect to the Bastion through the approved lab SSH path;
- the Bastion returns hostname, user, and uptime evidence;
- the SSH service reports active;
- S009 hostname and applicable resolution evidence are collected;
- actual addresses, usernames, and hostnames are replaced by approved mask placeholders;
- sanitized files exist under the correct S008/S009 evidence paths;
- S010 and repository validators confirm directory and safety rules;
- raw evidence, credentials, private keys, tokens, and infrastructure identifiers remain outside the repository.

## Non-Production Disclaimer

This workflow is for a disposable reference lab only. It is not production Bastion validation, security certification, cloud authorization, or permission to connect to any organizational host.
