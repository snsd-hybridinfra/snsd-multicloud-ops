# Storage and Snapshot Policy

**Status: PLANNED - storage roles are policy assignments, not deployed assets.**

## Authoritative Storage Roles

| Storage Location | Allowed Use | Prohibited Use |
|---|---|---|
| Dedicated active-VM SSD (approximately 405GB available) | Active VM disks and bounded temporary snapshots | Long-term archive, raw evidence archive, unlimited snapshots |
| Secondary HDD (approximately 227GB available) | ISO files, VM exports, packet captures, backup payloads, and raw local-only evidence | Active performance-sensitive VM disks; committed repository content |
| System drive (approximately 31GB free) | Git repository, text documentation, and small sanitized artifacts | VM disks, OpenStack images, backup repositories, ISO files, packet captures |
| OneDrive-synchronized repository | Text source, plans, sanitized evidence after authorized real execution | VM images, ISO files, snapshots, packet captures, raw evidence, database dumps, backup payloads |

Backup VM data must be stored on the secondary HDD; its 12GB active-SSD disk is
for the operating system only.

## Snapshot Policy

- Retain no more than one short-lived snapshot per active VM unless a reviewed
  exception is documented.
- Create a snapshot only immediately before a bounded, reversible lab change.
- Delete it after rollback validation or successful acceptance of the change.
- A snapshot is not a database backup, OpenStack backup, or recovery proof.
- Do not retain chains of VMware snapshots.
- Check dedicated-SSD free space before and after every snapshot window.
- Never place snapshots inside the repository or OneDrive path.

## Evidence and Packet Capture Policy

- Raw terminal output and packet captures remain local-only on the secondary
  HDD until reviewed.
- Packet captures containing credentials, tokens, cookies, personal data, or
  sensitive traffic must not be committed.
- Only minimal sanitized text evidence from an authorized real execution may be
  copied into `evidence/`.
- VM exports, images, ISO files, database dumps, and backup payloads are never
  repository evidence.

## Capacity and Cleanup Checks

Before each profile:

1. Confirm the active SSD has space for thin-disk growth and a temporary
   snapshot window.
2. Confirm the secondary HDD has space for planned backup or capture volume.
3. Remove expired exports, snapshots, captures, and raw evidence under the
   approved retention process.
4. Verify that no binary lab artifact is inside the repository.

No disk serial number or unique hardware identifier is recorded by this policy.
