# Level 02: Resolution Dominoes (30 XP)

| Pair | Cards | Pivot | Resolvent | Factoring? |
|---|---|---|---|---|
| 1 | A `(G | H)` + I `(~G | ~H)` | G | `H | ~H` | No |
| 2 | B `(~T | U)` + G `(T | U)` | T | `U` | Yes, `U | U` -> `U` |
| 3 | C `(~Q | R)` + H `(P | Q)` | Q | `P | R` | No |
| 4 | D `(X | ~Y | Z)` + J `(Y | W)` | Y | `X | Z | W` | No |
| 5 | E `(M)` + L `(~M)` | M | `[]` (empty clause) | No |
| 6 | F `(A | B | S)` + K `(~A | R | S)` | A | `B | R | S` | Yes, `S | S` -> `S` |

## Trap pair: A and I
Resolving A and I on G gives `H | ~H`, a tautology, **not** the empty clause. A single resolution step removes only one complementary pair; it cannot also remove H and ~H in that same step. Resolving on H instead produces `G | ~G`, also a tautology.

The genuine empty clause comes from **E and L**, because they are opposing unit clauses.
