# Commands

Scenario: S009-dns-hostname-resolution-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-dns-hostname-resolution-model.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S009-dns-hostname-resolution-validation\logs\dns-hostname-resolution-validation.log
Get-Content evidence\L1-foundation\S009-dns-hostname-resolution-validation\configs\dns-hostname-resolution-summary.md
```

## Safety Notes

No planned command queries DNS, connects to hosts, changes a resolver, authenticates to a cloud provider, or requires live network access. The validator reads repository text only.

## Lab Phase 2 Manual Hostname and Resolution Evidence

Run these read-only commands inside the separately authorized disposable Bastion VM:

```bash
hostname
hostname -I
getent hosts <hostname-placeholder>
nslookup <hostname-placeholder>
```

`nslookup` is optional when no DNS or hosts-file mapping is configured. Record that check as `NOT_APPLICABLE` rather than claiming successful resolution.

Save raw output outside the repository. Before copying evidence to `<evidence-path>/logs/`:

- replace every actual IP or CIDR with `<lab-ip-masked>`;
- replace the actual hostname with `<hostname-masked>`;
- replace any user value with `<user-masked>`;
- remove resolver addresses, DNS suffixes, domains, prompts, and unrelated interface details;
- verify that no password, credential, private key, token, cloud identifier, or production value remains.

Only the reviewed sanitized output may be added alongside existing sample evidence.
