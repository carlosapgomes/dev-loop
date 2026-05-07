# LLM Engineering Principles

This is the canonical interpretation of engineering principles for DevLoop.

Goal: reduce entropy for probabilistic agents, not enforce slogans.

## Clean Code = semantic predictability

Code should make the next agent's likely interpretation correct. Prefer clear names, direct control flow, visible invariants, and removal of dead paths when they increase ambiguity.

## DRY = avoid semantic divergence

Do not repeat business meaning in multiple places. Mechanical duplication is acceptable when an abstraction would hide intent or increase context required to change safely.

## SOLID = explicit boundaries

Use responsibilities, interfaces, and dependency direction to make architecture easier to preserve. Do not add classes, interfaces, or layers just to satisfy a pattern.

## YAGNI = context control

Do not add extension points, generic frameworks, or future-proof branches unless required by the active Contract Freeze. Unused flexibility is extra search space for agents.

## TDD = constrain behavioral search

RED -> GREEN -> REFACTOR narrows the agent's solution space. Tests should describe observable behavior, contracts, and invariants rather than implementation trivia.

## KISS = minimize coordination cost

Prefer the smallest understandable change that satisfies the frozen contract and leaves less ambiguity for the next planner, implementer, or reviewer.

## Operational Rule

When in doubt, choose the option that reduces hidden assumptions, preserves frozen contracts, and makes the next slice easier to execute with zero context.
