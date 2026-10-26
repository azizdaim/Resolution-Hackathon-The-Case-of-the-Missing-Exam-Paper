# Level 04: Final Accusation (10 XP)

**Presenter:** Abdulaziz Abduldaim (S24109313)  
**Assigned case from mentor:** To be confirmed in class.

## Two-minute board explanation
1. Start with the numbered CNF clauses from Level 01.
2. **Omar:** K1 + K2 -> `S | O`; K3 + K5 -> `~S`; resolve to `O`; add `~O` and derive `[]`.
3. **Sara:** K3 + K5 -> `~S`; add `S` and derive `[]`.
4. **Lina:** KB contains `~L | Y` but no positive L. Adding `~L` cannot yield a contradiction; adding L gives Y, K, then `~A` without contradiction. Show the two countermodels from Level 03.
5. Explain the trap: A and I produce a tautology, not the empty clause.

## Code-review checklist
- Is the pivot present positively in one parent and negatively in the other?
- Does each resolution step remove **exactly one** complementary pair?
- Are remaining literals retained and duplicate literals factored correctly?
- Is `P | ~P` correctly recognized as a tautology rather than `[]`?
- Is an empty clause actually derived before claiming entailment?
- Is Lina correctly marked **undetermined** rather than innocent?

## Code review log
No other team's errors or accepted objections are claimed in advance. Record actual objections during the in-class session.

## Individual post-mortem: Abdulaziz Abduldaim
Resolution is proof by contradiction because we negate the claim and derive the empty clause; if the complete resolution process cannot derive an empty clause, the knowledge base does not entail that claim.

## Team information / XP
Other team member names, table number, mentor-assigned presentation case and earned XP: **pending in-class confirmation**.
