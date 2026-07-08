# Expected Result

S018 is successful when the Kubernetes RBAC least privilege validation plan is complete and ready for future approved execution.

## Success Conditions

- Namespace separation is documented using placeholder namespace names.
- ServiceAccounts are separated by workload or validation purpose.
- Roles are namespace-scoped and grant only required verbs and resources.
- RoleBindings bind only intended ServiceAccounts to intended Roles.
- `kubectl auth can-i` allowed action checks are defined.
- `kubectl auth can-i` denied action checks are defined.
- Unnecessary cluster-admin bindings are denied.
- Secret read access is restricted.
- Workload access remains inside the intended namespace boundary.
- All validation checks map to required evidence files.

## Evidence Conditions

- `commands.md` lists planned command or review actions with TODO output placeholders.
- `validation.md` lists each check with `NOT_RUN` status until execution.
- Future supporting evidence is expected in `configs/kubernetes-rbac-summary.md`, `configs/kubernetes-rbac-policy.md`, `logs/kubernetes-rbac-validation.log`, and `screenshots/kubernetes-rbac-validation.png`.
