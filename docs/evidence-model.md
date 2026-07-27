# Evidence Model

## Authority chain

```text
capability -> package -> technical target -> validator execution
           -> sanitized evidence -> acceptance decision -> maturity assessment
```

Evidence records must identify the package, capability, target boundary, execution authority, validation class, result, sanitization decision, limitations, and immutable source references where applicable.

## Rules

- Mapping and design evidence do not prove implementation or runtime validation.
- Runtime claims require an approved execution record that resolves to sanitized evidence.
- Positive, negative, bypass, persistence, rollback, and repeatability results remain distinct.
- Evidence continuity and maturity remain separate from implementation and validation.
- `.runtime/**`, secrets, account values, raw logs, and personal data must never be tracked.
- Deleted numbered-scenario evidence is recoverable only through Git history and is not an active evidence authority.
