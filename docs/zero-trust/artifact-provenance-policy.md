# Artifact provenance boundary

Every promoted artifact should bind source commit, build authority, declared
inputs, artifact hash or immutable image digest, related SBOM, signature state,
verification state, storage location, promotion authority, and revocation path.

Approved statuses are `VERIFIED`, `SIGNED_NOT_VERIFIED`, `HASHED_ONLY`,
`UNSIGNED`, `NOT_AVAILABLE`, and `UNKNOWN`. The current monitoring images use
reviewed version tags from the Compose file, but their digests and signatures
are `UNKNOWN`; this is not `VERIFIED`. The Compose-derived SBOM is `PARTIAL`.
No signing service, production key, registry mutation, image push, or promotion
action is introduced by ZT-APP-001.
