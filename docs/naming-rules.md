# Naming Rules

Consistent naming keeps scenarios, evidence, and automation traceable.

## Scenario IDs

Use:

```text
<level>-S<two-digit-number>
```

Examples:

- `L1-S01`
- `L3-S07`
- `L5-S10`

## Directory Names

- Use lowercase words separated by hyphens.
- Preserve validation level prefixes exactly, such as `L1-foundation`.
- Do not use spaces.
- Do not include cloud account names, regions tied to real accounts, tenant IDs, project IDs, or personal names.

## File Names

- Use lowercase words separated by hyphens.
- Use `.md` for documentation and evidence notes.
- Use `.tf`, `.yml`, `.yaml`, `.json`, or `.conf` only when a scenario requires a text configuration placeholder.

## Scenario Evidence Names

Use:

```text
evidence/<level>/<scenario-id>/<artifact-name>.md
```

Example:

```text
evidence/L2-security-baseline/L2-S04/result.md
```

## ADR Names

Use:

```text
docs/adr/NNNN-short-title.md
```

Example:

```text
docs/adr/0001-lock-foundation-scope.md
```
