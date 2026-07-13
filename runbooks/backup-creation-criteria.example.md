# Backup Creation Criteria

| Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Backup scope definition | runbook | explicit scope | missing | planned | S038 | runbook |
| Backup source identification | manifest | placeholder source | real path/data | safe | S038 | manifest |
| Backup target identification | manifest | placeholder target | real storage | safe | S038 | manifest |
| Backup command execution evidence placeholder | sample | sample completion | real execution | evidenced | S038 | command sample |
| Backup artifact metadata | metadata | name/time/size/owner | incomplete | evidenced | S038 | metadata sample |
| Backup manifest creation | manifest | required fields | incomplete | governed | S038 | manifest |
| Backup checksum generation | checksum | SHA256 placeholder | missing | integrity | S038 | checksum sample |
| Backup size sanity check | metadata | size greater than 0 | zero/missing | valid | S038 | metadata sample |
| Retention classification | manifest | retention assigned | missing | governed | S038 | policy/manifest |
| Encryption / access control placeholder | manifest | both documented | missing | protected | S038 | manifest |
| Backup creation final summary | summary | created/manifest/checksum/retention/no artifact | incomplete | complete | S038 | summary sample |
