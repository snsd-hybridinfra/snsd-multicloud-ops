# Architecture

```text
least-privilege placeholder baseline
 -> labeled manual misconfiguration sample
 -> unsafe rule/source/port + severity detection
 -> affected-surface and rollback decision
 -> labeled manual rollback sample
 -> restricted post-state + safe final judgment
```

No live control plane or network is accessed.
