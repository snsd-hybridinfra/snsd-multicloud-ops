# Naming Rules

Consistent naming keeps scenarios, evidence, and automation traceable.

## Scenario IDs

Scenario ID format:

```text
S###
```

`###` is a zero-padded number from `001` through `050`.

Scenario directory format:

```text
S###-kebab-case-scenario-name
```

Examples:

- `S001-control-plane-toolchain-validation`
- `S014-aws-security-group-least-privilege-validation`
- `S050-final-evidence-report-generation-validation`

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

The evidence directory must mirror the scenario directory path exactly.

```text
scenarios/<level>/S###-kebab-case-scenario-name/
evidence/<level>/S###-kebab-case-scenario-name/
```

Example:

```text
scenarios/L1-foundation/S001-control-plane-toolchain-validation/
evidence/L1-foundation/S001-control-plane-toolchain-validation/
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

## Zero Trust Names

- Capability ID: `ZT-<source-number>` using source numbering exactly, for
  example `ZT-1.1.1`, `ZT-3.1.1`, and `ZT-8.6`.
- English slugs: lowercase kebab-case stable identifiers such as
  `device-endpoint` and `visibility-analytics`.
- Korean display names: preserve canonical source spelling; do not replace it
  with an unofficial translation.
- Official maturity display values: `Traditional`, `Initial`, `Advanced`, and
  `Optimal`, paired with `기존 단계`, `초기 단계`, `향상 단계`, and
  `최적화 단계`.
- Repository maturity extensions: `UNASSESSED` and `NOT_APPLICABLE`.
- Capability workflow states: `REFERENCE_ONLY`, `MAPPED`, `PLANNED`,
  `IMPLEMENTED`, `PARTIALLY_VALIDATED`, `VALIDATED`, `GAP_IDENTIFIED`, and
  `NOT_APPLICABLE`.
- Evidence levels: `NONE`, `DESIGN`, `CONFIGURATION`, `RUNTIME`, and
  `CONTINUOUS`.
- Assessment confidence: `LOW`, `MEDIUM`, or `HIGH`.
- Evidence authority: `USER_EXECUTED_RUNTIME`, `CODEX_EXECUTED_LOCAL`,
  `CODEX_EXECUTED_LIVE_RUNTIME`, `DESIGN_ONLY`, `CONFIGURATION_ONLY`, or
  `MISSING`.
