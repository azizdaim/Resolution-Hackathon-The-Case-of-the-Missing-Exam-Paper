# Level 03: Solve the Case (40 XP)

The K-numbers below refer to `LEVEL_01_CNF.md`. Each case is a separate refutation, so R-numbering restarts.

## Case 3A: Prove KB |= O (15 XP)
Assume the opposite: **N1 = ~O**.

| Step | Parents | Pivot | Resolvent |
|---|---|---|---|
| R1 | K1, K2 | D | `S | O` |
| R2 | K3, K5 | C | `~S` |
| R3 | R1, R2 | S | `O` |
| R4 | R3, N1 | O | `[]` |

**Verdict:** Contradiction, so Omar took the paper.

## Case 3B: Prove KB |= ~S (10 XP)
Assume the opposite: **N1 = S**.

| Step | Parents | Pivot | Resolvent |
|---|---|---|---|
| R1 | K3, K5 | C | `~S` |
| R2 | R1, N1 | S | `[]` |

**Verdict:** Contradiction, so Sara did not take the paper.

## Case 3C: Lina (15 XP)

### Attempt 1: Prove L, so add ~L
No clause in the KB contains positive `L`. Consequently, `~L` cannot resolve with any clause on L, and no empty clause can be derived. **KB does not entail L.**

### Attempt 2: Prove ~L, so add L
| Step | Parents | Pivot | Resolvent |
|---|---|---|---|
| R1 | K6, N1=`L` | L | `Y` |
| R2 | R1, K7 | Y | `K` |
| R3 | R2, K9 | K | `~A` |

No contradiction follows. `~A` is consistent with the KB. **KB does not entail ~L.**

### Countermodels (stronger evidence)
Both assignments below satisfy all nine KB clauses:

| Variable | Model 1 | Model 2 |
|---|---|---|
| D | True | True |
| S | False | False |
| O | True | True |
| C | False | False |
| F | False | False |
| L | False | True |
| Y | False | True |
| K | False | True |
| A | False | False |

Because one valid model has L false and another has L true, neither accusation nor exoneration is logically provable. **Lina's status is unknown**, not proven innocent.

## Side quest: Prove KB |= ~F (+3 XP)
Add **N1 = F**.

| Step | Parents | Pivot | Resolvent |
|---|---|---|---|
| R1 | K4, K5 | C | `~F` |
| R2 | R1, N1 | F | `[]` |

**Verdict:** The door was not forced.
