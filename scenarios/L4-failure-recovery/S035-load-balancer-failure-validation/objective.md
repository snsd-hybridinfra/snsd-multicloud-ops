# Objective

Validate that LB/entrypoint failure is distinguishable from backend failure, client impact is recorded, both direct backends remain healthy, and manual recovery restores the normal path. S025 owns normal load balancing, S030 probes, and S040 final health.
