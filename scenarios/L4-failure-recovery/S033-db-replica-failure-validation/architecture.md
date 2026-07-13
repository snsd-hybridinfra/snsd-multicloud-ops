# Architecture

```text
healthy replica threads/lag
  -> separately authorized manual replica stop in disposable lab
  -> replica down + thread No + lag NULL
  -> Primary remains reachable/read-write
  -> manual recovery placeholder
  -> threads Yes + lag 0 + catch-up/no-error judgment
```

Only committed sanitized artifacts are parsed.
