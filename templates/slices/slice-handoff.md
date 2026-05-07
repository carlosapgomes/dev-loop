# Slice Handoff: <change-id> / <slice-id>

Goal: minimal sufficient context for one context-zero vertical slice.

## 1. Identification

- Change: `<change-id>`
- Slice: `<X.Y>`
- Title: `<short title>`
- Depends on: `<previous slices / none>`

## 2. Frozen Contracts

Source: `openspec/changes/active/<change-id>/design.md#contract-freeze`

- Interfaces/APIs used:
- DTOs/schemas/payloads used:
- Invariants to preserve:
- Contract changes allowed? `no` unless explicitly approved here:

## 3. Architectural Boundaries

Repository laws: `openspec/project.md`

- Layers/modules touched:
- Dependency direction to preserve:
- Integration/persistence boundaries:

## 4. Scope

### Allowed Files / Areas

- `path/to/file-or-dir`

### Forbidden Files / Areas

- `path/to/file-or-dir`

### Explicit Non-goals

- <what this slice must not do>

If scope must expand, stop and record justification before coding.

## 5. Vertical Objective

- User/business value:
- End-to-end flow covered:

## 6. TDD Plan

- RED: <failing test/behavior first>
- GREEN: <minimum implementation to pass>
- REFACTOR: <cleanup while preserving repository laws and frozen contracts>

## 7. Required Gates

- [ ] RED/GREEN/REFACTOR evidence captured
- [ ] Validation commands from `AGENTS.md` executed or explicitly justified
- [ ] Frozen contracts preserved
- [ ] Allowed/forbidden file rules respected
- [ ] `tasks.md` updated

## 8. Success Criteria

- [ ] Vertical behavior delivered
- [ ] Tests represent expected behavior/contracts
- [ ] No forbidden scope added
- [ ] No unapproved contract change
- [ ] Evidence report generated

## 9. Evidence Report

Implementation agent uses `templates/reports/implementation-report.md` and includes:

- files changed and why
- gates run and results
- contract/scope compliance notes
- reviewer focus and follow-ups

Reviewer/planner agent uses `templates/reports/planner-review.md` to approve, approve with follow-ups, or reject.

Required chat output:

```text
REPORT_PATH=<path-to-report.md>
```

## 10. Implementation Prompt

```text
Read openspec/project.md, docs/foundations/llm-engineering-principles.md, AGENTS.md, PROJECT_CONTEXT.md, the active change proposal/design/tasks, and this slice handoff.
Implement ONLY this slice.
Preserve frozen contracts and architectural boundaries.
Touch only allowed files/areas; do not touch forbidden files/areas.
Follow the TDD plan: RED -> GREEN -> REFACTOR.
Run required gates.
Generate the implementation report and reply with REPORT_PATH=<path-to-report.md>.
Do not approve your own work; reviewer/planner gate is separate.
STOP after this slice.
```
