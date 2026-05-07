# DevLoop Project Laws

This file is the permanent engineering constraint source for DevLoop-managed work.

Purpose: reduce agent drift, preserve architecture, and make context-zero execution predictable.

Canonical principle interpretation: `docs/foundations/llm-engineering-principles.md`.

## Authority

When instructions conflict, use this order:

1. `openspec/project.md` — permanent repository laws
2. Active change `design.md#contract-freeze` — change-specific frozen contracts
3. Active change `tasks.md` and slice handoff — execution scope
4. `AGENTS.md` — local commands and agent operating rules
5. Other docs/templates

## Architectural Boundaries

- Keep domain behavior separate from transport, UI, CLI, and persistence details.
- Put orchestration at explicit boundaries; do not hide business decisions in glue code.
- A slice may cross layers only to deliver a vertical outcome, not to bypass boundaries.
- If a boundary is unclear, document the decision in `design.md` before coding.

## Dependency Rules

- Dependencies point inward toward stable domain concepts, not outward toward frameworks.
- Framework/library code may call application code through narrow adapters.
- Shared utilities must be behavior-neutral; domain-specific helpers belong near the domain.
- New dependencies require an explicit reason in `design.md` or the slice handoff.

## Layering Constraints

- Presentation/transport layers validate input and delegate; they do not own business rules.
- Application/service layers coordinate use cases and transactions.
- Domain/model layers hold invariants and core decisions.
- Persistence/integration layers translate external systems into internal contracts.

## Documentation Quality

- Every created or edited Markdown file must pass `markdownlint-cli2` before delivery or commit.
- Implementation reports and planner reviews are Markdown artifacts and must be linted before handoff.
- Fix Markdown lint errors; do not leave formatting cleanup to the next agent.

## Testing Expectations

- Use TDD for slice behavior: RED -> GREEN -> REFACTOR.
- Tests should describe observable behavior and frozen contracts, not implementation trivia.
- Add characterization tests before changing risky legacy behavior.
- Every slice report must state which gates ran and why any gate did not run.

## Engineering Principles

Use `docs/foundations/llm-engineering-principles.md` as the canonical interpretation of Clean Code, DRY, SOLID, YAGNI, TDD, and KISS for low-drift agent work.

Operationally: choose the option that reduces hidden assumptions, preserves frozen contracts, and makes the next slice easier to execute with zero context.

## Current Architecture Decisions

- OpenSpec remains the lifecycle backbone and upstream compatibility target.
- DevLoop extensions are additive governance artifacts, not OpenSpec forks.
- `.devloop/skills/` is the canonical skills source.
- `skills -> .devloop/skills` remains a compatibility adapter.
- `templates/` remains the canonical template location for now; it was not moved under `.devloop/templates` to avoid churn.
- Contract Freeze is a section in `design.md`, not a separate `contracts.md` file for now.
- Implementation and review are separate roles using implementation reports and planner reviews.

## Non-Negotiable Agent Rules

- Do not change frozen contracts without explicit reviewer/planner approval.
- Do not touch forbidden files listed in the active Contract Freeze or slice handoff.
- Do not continue to the next slice after finishing the current one.
- Do not introduce broad refactors inside a feature/bugfix slice unless the slice explicitly allows it.
