# Restore Execution Criteria

| Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Backup manifest reference | precheck | valid placeholder | missing | ready | S038-S039 | precheck |
| Backup checksum verification | checksum | SHA256 verified/match | mismatch | integrity | S039 | checksum |
| Restore target preparation | precheck | disposable placeholder | production target | safe | S039 | precheck |
| Restore command execution evidence placeholder | command | manual lab completion | real execution | evidenced | S039 | command sample |
| Restore log review | command | completion placeholder | failure | reviewed | S039 | command sample |
| Restore artifact metadata | metadata | name/time/positive size/target | incomplete | evidenced | S039 | metadata |
| Restore consistency check | consistency | passed/count placeholder | failed | consistent | S039 | consistency |
| Restore completion summary | summary | required judgments | incomplete | complete | S039 | summary |
| Restore abort / rollback condition | manifest | documented | missing | controlled | S039 | manifest |
| Mapping to service health validation | manifest | S040 | missing | linked | S040 | manifest |
