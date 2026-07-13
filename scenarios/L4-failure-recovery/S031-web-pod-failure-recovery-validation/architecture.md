# Architecture

```text
healthy Deployment/Pods
  -> separately authorized manual Pod deletion in disposable lab
  -> original terminates
  -> Deployment creates replacement
  -> replacement Running/Ready
  -> rollout succeeds
  -> Service endpoint remains non-empty
```

Static mode parses samples. LiveKubectl performs read-only get/status queries and stores only deployment-found, Ready Pod count, rollout-success, and nonempty-endpoint count judgments.

No live fault is injected and no raw cluster details are retained.
