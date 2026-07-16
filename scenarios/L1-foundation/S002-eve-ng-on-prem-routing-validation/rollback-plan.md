# Rollback Plan

1. Stop if the temporary ACL affects an unintended flow.
2. Remove the temporary ACL from the router subinterface.
3. Restore disconnected Cloud/LAN-segment links.
4. Restore the last known lab configuration if a trunk, duplex, route, or NAT
   change causes loss of reachability.
5. Verify baseline permitted traffic and management access.
6. Delete unsafe raw evidence and retain only sanitized outputs.

The temporary ACL was removed and the lab links were restored. Sanitized ACL
inventory, interface attachment state, and restored reachability output are
retained in the S002 evidence package.
