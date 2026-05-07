# AGENTS.md

## Authority

Read first:

1. `openspec/project.md` — repository laws
2. `docs/foundations/llm-engineering-principles.md` — canonical principle interpretation
3. Active change `design.md#contract-freeze`
4. Active `tasks.md` and slice handoff

## Validation Commands

- Smoke skills: `./scripts/smoke-skills.sh --quick`
- Markdown lint/format: use scripts from `templates/markdown-automation/` when installed in a target project

## Operating Rules

- Implement one vertical slice at a time.
- Preserve the active Contract Freeze.
- Do not touch forbidden files/areas from the slice handoff.
- Generate a concise, diff-oriented implementation report and return `REPORT_PATH=<path>`.
- Do not approve your own work; reviewer/planner gate is separate.
- Stop after the slice; do not continue without explicit approval.

## Philosophy

Do not restate engineering principles in prompts. Reference:

`docs/foundations/llm-engineering-principles.md`
