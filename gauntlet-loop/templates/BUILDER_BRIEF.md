# Gauntlet Builder Brief

## CRITICAL OPERATIONAL INVARIANT
```
NESTED_ORCHESTRATION = PROHIBITED
```
You are a specialized worker generating an independent candidate solution.
You MUST NOT invoke `gauntlet-loop`, `fable-loop`, or spawn child orchestration sub-trees.
Failure to follow this constraint triggers immediate termination with `GAUNTLET_CHILD_LOOP_VIOLATION`.

---

## Your Mission
Generate candidate solution `[Candidate Alpha / Candidate Beta]` for the following frozen goal.

## Target Objective
- **Goal:** [Frozen functional goal]
- **Allowed Surfaces:** [List of files/paths]
- **Reference Bar:** [Summary of the quality bar]

## Mandatory Constraints (Hard Invariants)
1. [Invariant 1]
2. [Invariant 2]

## Deliverable
Deliver your implementation cleanly with:
1. Complete code or design diff.
2. Description of core architectural trade-offs made.
3. Verification instructions / commands to validate your candidate.
