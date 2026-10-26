# Level 01: CNF Relay (20 XP)

**Submitted by:** Abdulaziz Abduldaim (S24109313)

## Clue 1: D -> (S | O)
1. `~D | (S | O)` — eliminate implication.
2. `(~D | S) | O` — associativity.
3. `~D | S | O` — flatten disjunction (CNF).

## Clue 3: (S | F) -> C
1. `~(S | F) | C` — eliminate implication.
2. `(~S & ~F) | C` — De Morgan.
3. `(~S | C) & (~F | C)` — distribute OR over AND.

## Clue 6: Y <-> K
1. `(Y -> K) & (K -> Y)` — eliminate biconditional.
2. `(~Y | K) & (~K | Y)` — eliminate implications.
3. `(~Y | K) & (~K | Y)` — already CNF.

## Clue 7: ~(K & A)
1. `~(K & A)` — original.
2. `~K | ~A` — De Morgan.
3. `~K | ~A` — CNF.

## Complete knowledge base
| Clause | CNF clause | Source |
|---|---|---|
| K1 | `~D | S | O` | Clue 1 |
| K2 | `D` | Clue 2 |
| K3 | `~S | C` | Clue 3 |
| K4 | `~F | C` | Clue 3 |
| K5 | `~C` | Clue 4 |
| K6 | `~L | Y` | Clue 5 |
| K7 | `~Y | K` | Clue 6 |
| K8 | `~K | Y` | Clue 6 |
| K9 | `~K | ~A` | Clue 7 |

**Total:** 9 clauses, K1–K9. The worksheet has space for K10 but no tenth clause is needed.
