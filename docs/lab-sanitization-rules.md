# Lab Evidence Sanitization Rules

## Purpose

All evidence entering this repository must be safe for public portfolio review. Sanitization happens before an artifact is copied into `evidence/`, not after it is committed.

## Remove Before Committing

Remove or replace every occurrence of:

- real IP addresses and CIDRs;
- real hostnames, DNS names, domains, and production URLs;
- usernames, email addresses, personal paths, and workstation identifiers;
- passwords, passphrases, tokens, API keys, and client secrets;
- cookies, session identifiers, and Authorization headers;
- private keys, key material, and unapproved certificates;
- kubeconfig files and service-account credentials;
- `terraform.tfstate`, state backups, `terraform.tfvars`, and automatic variable files;
- `clouds.yaml`, openrc files, and cloud CLI profiles;
- cloud account IDs, subscription IDs, tenant IDs, project IDs, and billing identifiers;
- VPC, VNet, subnet, security-group, NSG, instance, volume, cluster, and other resource IDs;
- database credentials, connection strings, dumps, and non-synthetic records;
- real Prometheus/Grafana endpoints, labels, cookies, datasource identifiers, and raw production exports;
- unrelated terminal history, browser tabs, notifications, and personal information.

## Allowed After Review

The following may be committed when they are non-production and fully sanitized:

- command output limited to the owning validation check;
- masked screenshots with environment identifiers removed;
- synthetic or sanitized metric CSV files;
- non-production configuration examples using placeholders;
- validation logs without secrets or environment-specific values;
- sanitized summaries that describe a result without reproducing unsafe raw output;
- synthetic database records created solely for the disposable lab.

## Standard Masking Format

Use consistent explicit placeholders:

| Sensitive Value | Replacement |
|---|---|
| Address or CIDR | `<lab-ip-masked>` |
| Hostname or DNS name | `<hostname-masked>` |
| Token, API key, cookie, or Authorization value | `<token-redacted>` |
| Cloud or billing account identifier | `<account-id-redacted>` |
| Resource identifier | `<resource-id-redacted>` |
| Username | `<username-masked>` |
| URL or endpoint | `<endpoint-masked>` |
| Secret or password | `<secret-redacted>` |

Do not partially reveal a value. Retaining prefixes, suffixes, lengths, or checksums may still identify the source environment.

## Text Evidence Procedure

1. Copy raw output to a location outside the repository.
2. Reduce it to the lines required by the scenario validation check.
3. Replace every sensitive value with a standard placeholder.
4. Search the sanitized file for addresses, URLs, identifiers, tokens, key blocks, and secret assignments.
5. Copy only the reviewed sanitized version into the matching evidence directory.

## Screenshot Procedure

1. Crop to the required state or panel.
2. Apply opaque masking to sensitive regions; do not use transparent blur alone.
3. Check address bars, tooltips, legends, labels, terminal prompts, taskbars, and notifications.
4. Reopen the exported image and inspect it at full resolution.
5. Store the reviewed image using the evidence naming convention.

## Config and Structured Data Procedure

- Replace environment values while preserving valid example structure.
- Remove secret fields entirely when a placeholder could be misused as a real value.
- Keep datasets bounded and synthetic or sanitized.
- Do not commit encrypted secrets as a substitute for removing them.
- Do not commit raw packet, malware, exploit, SIEM, Wazuh, EDR, or production telemetry artifacts.

## Pre-Commit Safety Check

- Review `git diff` and the complete contents of every new evidence file.
- Run `tools\validate-repo-structure.ps1` and `tools\validate-scenario-quality.ps1`.
- Run the owning scenario validator where available.
- Confirm the artifact is mapped in the scenario evidence documentation.
- Record a blocker in `docs/risk-register.md` if an unsafe value cannot be confidently removed.

## Final Safety Rule

If unsure, do not commit the raw artifact. Add a sanitized summary instead. Repository completeness never takes priority over protecting credentials, identifiers, personal data, or infrastructure details.
