# Prometheus Target Down Criteria

| Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Pre-failure target discovery | targets | target exists | missing | baseline | S036 | pre targets |
| Pre-failure target UP state | targets/up | health up and value 1 | down/0 | baseline | S036 | pre samples |
| Manual target-down injection | event | manual stop marker | automated | controlled | S036 | injection |
| Prometheus target DOWN detection | targets | health down | not detected | detected | S036 | down targets |
| up metric equals 0 | query | value 0 | value 1 | detected | S036 | down query |
| Alert rule evaluation placeholder | rule | placeholder defined | missing | governed | S036 | alert example |
| Alert firing placeholder | alerts | firing | absent | alerted | S036 | down alerts |
| Recovery action placeholder | event | manual start marker | automated | recovering | S036 | recovery |
| Post-recovery target UP state | targets/up | health up/value 1 | down/0 | recovered | S036 | post samples |
| Alert cleared placeholder | alerts | inactive/resolved | firing | recovered | S036 | cleared alerts |
| Recovery time threshold | timing | within threshold | exceeded/missing | review | S036 | summary |
