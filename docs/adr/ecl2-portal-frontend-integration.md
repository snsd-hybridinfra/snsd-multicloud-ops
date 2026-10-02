# Use ecl2-portal as the frontend source

Date: 2026-10-02. Decision: accepted for bounded local implementation by the
user request to develop the backend for the frontend, corrected to use
`ecl-포탈` rather than the old second-project frontend.

## Source and boundary

Import the frontend from `Project-Team-Eclipse/ecl2-portal` commit
`e8c4c1d26b9177929a0e04b7b9db1d6885ac5215`. A read-only remote `main`
lookup matched the local checkout. Preserve its navy/gold theme, source artwork,
Developer, Manufacturing/PartnerHub, Finance, Public, LLM and MSP navigation,
and separate production/demo authentication entry points. The source checkout's
untracked `.deploy/` is left untouched. `upstream-source.json` records the
original source hashes and identifies downstream integration modifications.
The user's explicit instruction is to leave ECL untouched. All frontend edits
are confined to the SNSD copy; final read-only checks match all 25 imported
source hashes and show only the original `.deploy/` in the ECL working tree.

The frontend is a presentation asset, not a new cloud adapter, package,
composite product or production authorization. Reuse the existing seven-image
delivery boundary: the request-api hosts the facade and the user-portal image
hosts `/eclipse/`. Do not add a standalone portal-api image or import AWS/KT
executors. SNSD remains Financial Hybrid-Ready, private OpenStack/k3s and
synthetic/non-production only. No public-cloud or financial live connection is
introduced. The existing legacy portal remains available at its original path.

## Implementation

Keep upstream modules as source assets; separate `idp-*` scripts select
API-backed views when mock domains are disabled. Operational catalog and forms
use only the existing eight approved blueprints, sizes, environments and TTLs.
Seven unavailable composite paths remain blocked. Industry services and
PartnerHub remain explicitly marked design previews with no workload adapter.
The original standalone demo remains sample-only. `local.html` uses dev headers
with real local database/API state and the `LOCAL CONNECTED` marker.

Use strict server checks for domain scope, cloud scopes, role and tenant.
Store portal metadata on the existing request row; strip presentation metadata
before approval/runner delivery. Scoped idempotency binds the payload and project
to the requester, domain and tenant. Legacy read/cancel/resource routes must also
honor this tenant partition. Preserve the catalog's per-user quota.

Approval and rejection use the existing approval API; both facade and underlying
approval authority reject self approval. Recovery revokes the exact bound grant
before requesting the existing destroy workflow. Persist numeric simulator
usage without prompt text, prompt hashes, provider-token claims or invented
billing. The local LLM simulator is opt-in and dev-only. Identity directory,
role mutations, observability, billing, industry and workspace providers remain
explicitly unconnected rather than returning fabricated operational records.

## Consequences and validation

Production index keeps the upstream cookie/PEP session contract. `/auth/session`
can project a verified upstream bearer principal; the external OIDC/MFA/PEP must
still establish and protect the HttpOnly session and forward a token accepted
by each audience. No password login, homemade production session or privilege
elevation is introduced. Production image builds remove local/demo entry points
and runtime configs; the dev compose selects the local build edition.

Local API regressions and browser checks cover persistent requests, tenant and
domain isolation, scope denial, idempotency, rejection/cancellation, approval,
mock-runner callbacks, grant issuance, revocation/recovery and simulator meters.
They provide local application proof only. OpenStack/k3s, OIDC/MFA/PEP, image
build/signature/installation and external metering remain `NOT_VALIDATED`.
The request-api image recipe now packages exact canonical catalogs through the
existing application context and a fixed repository-local named context. The
protected pipeline supplies that input without adding a workflow or image;
source runs continue to read the original authorities. Isolated image-layout
API tests cover valid, missing and tampered catalogs. Readiness rejects an
unavailable catalog. Local PostgreSQL 16 migration, app DML/DDL boundaries and
last-revision rollback preserve the request row. Actual image build/release and
exact Grant/callback/recovery network paths remain unvalidated; local success
does not override those deployment gates. Production bindings remain fail-closed.
