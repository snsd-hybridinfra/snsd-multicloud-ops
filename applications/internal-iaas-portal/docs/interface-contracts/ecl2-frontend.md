# ecl2-portal frontend and backend contract

Canonical source: `Project-Team-Eclipse/ecl2-portal`, commit
`e8c4c1d26b9177929a0e04b7b9db1d6885ac5215`. The imported UI is in
`services/user-portal/eclipse`; source receipt is `upstream-source.json`.
See `docs/adr/ecl2-portal-frontend-integration.md` in the repository root.

## Run the connected local application

From this application's root, using the existing development environment:

```powershell
F:/2차프로젝트/.venv/Scripts/python.exe tools/dev_eclipse_portal.py --simulate-provisioning --simulate-llm
```

Open `http://127.0.0.1:18080/eclipse/local.html`. Enter `developer-user`,
`factory-user`, `finance-user`, `public-user`, `msp-admin` or `llm-user` in
the local account form. These are development identities, not password/OIDC
authentication. The banner says `LOCAL CONNECTED`; mocks are disabled and
records come from SQLite and the original three APIs. The loopback-only launcher
uses ports 18080/18081/18082 and persists databases under the OS temporary
directory, outside all Git checkouts. `--runtime-root` accepts an absolute,
external Git-free directory. Stop with Ctrl+C. No Terraform, Ansible, cloud or
external model command is executed. The signing key is process-local, so old
mock JWTs are invalid after restart; request, resource and grant rows persist.

`/eclipse/index.html` keeps the production organization-auth entry point;
`/eclipse/demo.html` keeps the upstream standalone sample demonstration. The
production user-portal build omits both demo/local HTML and dev runtime configs.
`compose.mvp.yaml` explicitly selects the local edition. There is no eighth
container image or new dependency.

## Routes

| Route | Authority and behavior |
| --- | --- |
| `GET /api/{domain}/workspace` | Catalog, persistent requests, callback resources, monitoring connectivity and cost estimates |
| `GET /api/{domain}/catalog` | Exactly eight approved composite blueprints and requestability |
| `GET/POST /api/{domain}/requests` | Tenant/domain partition; approved blueprint fields plus bounded project name |
| `GET /api/{domain}/requests/{id}` | Read only an authorized domain/tenant/owner request |
| `POST /api/{domain}/requests/{id}/cancel` | Existing PENDING-only cancellation and delivery |
| `POST /api/{domain}/requests/{id}/redeliver` | Retry FAILED delivery without a new request |
| `POST /api/{domain}/requests/{id}/destroy` | Exact owner/request/grant binding; revoke access before queueing recovery |
| `GET /api/{domain}/resources`, `/monitoring`, `/finops` | Callback projections; unknown health and billing remain null |
| `GET /api/admin/workspace` | Existing approval queue/jobs with sanitized cross-tenant operational summary |
| `POST /api/admin/requests/{id}/approve`, `/reject`, `/retry-sync` | Existing policy decision and callback retry; self approval denied |
| `POST /api/admin/jobs/{id}/retry` | Retry the already-approved job through the existing authority |
| `GET /api/admin/audit`, `/grants` | Sanitized audit/grant database view; no grant JWTs |
| `GET /api/admin/users` | Observed request actors; identity directory/role mutations are unconnected |
| `GET /api/portal/team` | Explicit unconnected directory response; no fabricated membership |
| `GET /api/llm/models`, `/usage`, `/cost`; `POST /api/llm/chat` | User/tenant/scope isolation; opt-in local simulator and persistent numeric units |
| `POST /api/llm/workspace-requests` | Small-only contract; unavailable workspace adapter returns 409 |
| `GET /auth/session`, `/api/portal/me` | Verified principal projection for the external session/PEP contract |

Domains are `developer`, `manufacturing`, `finance`, `public`. Each requires its
matching `*:read` scope and permitted portal role; customer reads/writes also
require `cloud:read`/`cloud:request`. MSP finance/public reads require domain
scope and `admin:read`. Writes require customer roles, not a read-only operator.
Manager tenant-wide views additionally require `team:read`. Admin decisions
require `approval:manage`; identity/grant views require MSP_ADMIN plus
`admin:write`, and audit requires MSP_ADMIN plus `audit:read`.

Request JSON: `project`, `blueprint_id`, `environment`, `size`,
`duration_hours`, `purpose`. Additional keys, raw HCL, provider choices,
arbitrary services, PROD and unapproved sizes/durations are rejected.
POST requests/chat require `Idempotency-Key`; retries of requests must preserve
the original payload. Presentation metadata never enters the execution manifest.

Costs are explicitly `LOCAL_ESTIMATE`, not actual charges. Monitoring is
`NOT_CONNECTED`; runtime is `NOT_VALIDATED` even when a mock callback reports
RUNNING. LLM units count characters, not provider tokens, and no prompt or prompt
hash is stored. Chat-key reuse returns the same inert receipt without another
meter record; it is not a real model generation. Actual charges remain null.

## External inputs before live integration

- Approved non-production OIDC issuer/audiences/JWKS, MFA/PEP session and service
  token-exchange bindings; task-scoped secret files outside Git.
- Approved OpenStack project/image/flavor/private network and externally stored
  credentials/state, plus separate live authorization and the B-stage campaign.
- k3s tenant adapters, approved signed images/registry, secret manager and
  service/observability bindings for the seven blocked products.
- Approved directory, monitoring and billing sources; separately selected model
  gateway and policy/budget configuration. No real financial or personal data.

## Deployment blockers

The loopback launcher is the validated local entry point. No Docker build,
PostgreSQL migration, registry release or cluster installation was executed.
The existing request-api image copies the Python package and migrations but
does not package the repository-level catalog authorities. Its current
`blueprints.py` root lookup also assumes the source checkout depth. These must
be corrected and checked against the canonical catalog before claiming that
image can serve the new facade. Do not replace the authorities with a permissive
embedded catalog or silently change the seven-image build policy.

The production request-api ConfigMap deliberately has no `GRANT_API_URL`; the
existing request-api egress policy does not permit port 8002. The new grant
read/recovery paths therefore fail closed there. Before enabling them, review
the exact request-to-grant, grant-to-request callback and grant-to-approval
recovery edges, corresponding service audiences/scopes and server identities.
Do not widen cluster policies or enable dev auth as a deployment shortcut.
`compose.mvp.yaml` provides the Grant URL only for its bounded local edition.

No credential values are needed for local use. The old two source-integrity
failures remain documented in `docs/platform/source-integrity-review.md`;
this integration does not alter those evidence authorities. At final validation,
the separately added `monitoring_assistant.py` also triggered secret-assignment
findings in three root tests and the retirement/architecture/Zero Trust scans.
Those concurrent changes were preserved; validators were not weakened.
