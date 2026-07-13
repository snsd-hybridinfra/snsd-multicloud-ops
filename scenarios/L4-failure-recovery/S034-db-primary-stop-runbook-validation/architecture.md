# Architecture

```text
active Primary + healthy replica
 -> manual disposable-lab Primary stop
 -> Primary down + write impact
 -> Replica stays read-only and not promoted
 -> manual Primary start
 -> Primary role restored + replica threads healthy + catch-up
```

Only sanitized repository evidence is parsed.
