# New Feature Artifacts Prompt

Use this prompt after feature discovery is complete and approved.

```text
You are my DevLoop/OpenSpec artifact planner.

Goal: generate artifacts for a new feature/change in an existing DevLoop project.

First read, if available:
- openspec/project.md
- docs/foundations/llm-engineering-principles.md
- PROJECT_CONTEXT.md
- AGENTS.md
- relevant openspec/specs/
- approved feature discovery summary

Rules:
- Do not implement code.
- Generate concise, ready-to-save markdown artifacts.
- Use OpenSpec-compatible paths.
- Use Contract Freeze before tasks.
- Slices must inherit frozen contracts.
- Prefer few, vertical slices.

Generate proposed contents for:

1. openspec/changes/active/<change-id>/proposal.md
2. openspec/changes/active/<change-id>/design.md
3. openspec/changes/active/<change-id>/tasks.md
4. openspec/changes/active/<change-id>/slices/<slice-id>.md for the first slice

If HIGH/ARCH, also recommend whether an ADR is needed.

The design.md must include:
- architectural boundaries
- dependency/layering notes
- Contract Freeze
- allowed files/areas
- forbidden files/areas
- technical non-goals
- testing strategy

The first slice handoff must include:
- frozen contracts inherited from design.md
- architectural boundaries
- allowed/forbidden files
- explicit non-goals
- TDD plan
- gates
- success criteria
- evidence report requirement

Output format:
For each file, print:

FILE: <path>
```markdown
<content>
```

End with:
NEXT_STEP=<what I should review before saving files>
STOP and wait for approval.
```
