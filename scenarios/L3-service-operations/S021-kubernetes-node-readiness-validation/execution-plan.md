# Execution Plan

1. Run the validator without parameters for static local validation.
2. Confirm the baseline, command reference, and sample evidence.
3. Parse the required placeholder rows and evaluate Ready, NotReady, and SchedulingDisabled.
4. Scan repository filenames and evidence content for cluster credentials, endpoints, addresses, and secrets.
5. Confirm the optional live argument set is exactly `get nodes --no-headers` and contains no mutation command.
6. Review the generated log and summary.
7. Only when explicitly approved, rerun with `-LiveKubectl`; store status counts, not raw live rows.

## Execution Boundary

Default mode never invokes kubectl. Live mode performs one read-only listing and does not modify cluster state.
