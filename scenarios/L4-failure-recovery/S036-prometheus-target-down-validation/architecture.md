# Architecture

```text
target UP + up=1
 -> manual disposable-lab exporter stop
 -> target DOWN + up=0 + alert firing
 -> manual exporter start
 -> target UP + up=1 + alert resolved
```

Static samples are authoritative. Optional LivePrometheus performs read-only targets/query/alerts requests and retains sanitized judgments only.
