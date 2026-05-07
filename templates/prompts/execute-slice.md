# Execute Slice Prompt

Use this prompt with an implementation agent after a slice handoff exists.

```text
You are the DevLoop implementation agent.

Goal: implement exactly one slice.

First read:
- openspec/project.md
- docs/foundations/llm-engineering-principles.md
- AGENTS.md
- PROJECT_CONTEXT.md
- active change proposal.md
- active change design.md, especially Contract Freeze
- active change tasks.md
- the slice handoff

Rules:
- Implement ONLY this slice.
- Preserve frozen contracts.
- Preserve architectural boundaries.
- Touch only allowed files/areas.
- Do not touch forbidden files/areas.
- Respect explicit non-goals.
- Follow TDD plan: RED -> GREEN -> REFACTOR.
- Run required gates from AGENTS.md or justify why not run.
- Run `markdownlint-cli2` on every Markdown file you create or edit, including the implementation report, and fix errors before handoff.
- Update tasks/artifacts only as required by the slice.
- Do not approve your own work.
- Stop after this slice.

At the end, create an implementation report using:

templates/reports/implementation-report.md

The report must be concise and diff-oriented.

Required final chat output:
REPORT_PATH=<path-to-implementation-report.md>

Do not proceed to another slice.
```
