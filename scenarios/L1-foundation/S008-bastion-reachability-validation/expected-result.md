# Expected Result

## Success Conditions

- Both bastion model files exist.
- All required paths, targets, and address placeholders are documented.
- Bastion-only access and the four required SSH control statements are present.
- No numeric address, sensitive value, account identifier, private-key path, or active connection command is detected.
- The validator exits zero and generates evidence.

## Required Evidence

- `logs/bastion-reachability-validation.log`
- `configs/bastion-reachability-summary.md`
- `commands.md`
- `validation.md`

The result proves model completeness only; it does not prove reachability, authentication, DNS, route, firewall, or instance state.
