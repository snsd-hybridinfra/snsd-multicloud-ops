# ZT-NET-001 Rollback

Rollback is not executed as part of validation. A reviewed operator may:

1. Remove only the snsd-r1-validator block from the local SSH config.
2. Remove the dedicated router-validator public/private key pair outside Git.
3. Using the existing EVE operator path, remove the codex-router-validator
   account, its authorized key, the dedicated dispatcher and validator, and its
   exact sudoers fragment.
4. Remove repository wrappers and generated ZT-NET-001 evidence only through a
   separately reviewed repository change.

Rollback must preserve operator access, the existing OpenStack and EVE
validators, EVE lab files, Cisco and OpenStack configuration, and unrelated SSH
keys. It must not reload the router, change its startup or running
configuration, or delete runtime lab assets.
