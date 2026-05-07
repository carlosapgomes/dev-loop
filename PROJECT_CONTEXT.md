# PROJECT_CONTEXT.md

## Purpose

DevLoop is a governance system for low-drift LLM-native software engineering. It extends OpenSpec with contract freeze, repository laws, context-zero slice handoffs, evidence reports, and reviewer gates.

## Current Refactor State

The prepared refactor prompts have been executed through Phase 8:

- Phase 1: structural stabilization and skills canonicalization
- Phase 2: lifecycle formalization
- Phase 4: repository laws
- Phase 5: slice handoff hardening
- Phase 6: evidence and reviewer gate
- Phase 7: engineering philosophy consolidation
- Phase 8: OpenSpec synchronization strategy

Phase 3 is represented through `design.md#contract-freeze` and slice inheritance, but still needs automation/enforcement.
Phase 9 remains future automation/validation work.

## Authoritative Sources

1. `openspec/project.md` — permanent repository laws
2. `docs/foundations/llm-engineering-principles.md` — principle interpretation for LLM agents
3. `SOP.md` — operating workflow
4. `templates/` — canonical lifecycle, slice, and report templates
5. `.devloop/skills/` — canonical skills source
6. `docs/openspec-compatibility.md` — OpenSpec upstream compatibility policy
7. `AGENTS.md` — local agent operating rules

## Canonical Structure

- OpenSpec: `openspec/project.md`, `openspec/specs/`, `openspec/changes/active/`, `openspec/changes/archive/`
- Skills source: `.devloop/skills/`
- Skills compatibility adapter: `skills -> .devloop/skills`
- Templates: `templates/`
- Deprecated paths: documented in `docs/deprecated-paths.md`

## Architecture Notes

DevLoop treats OpenSpec as upstream protocol/framework, not as internal implementation. DevLoop extensions are additive, file-based governance artifacts.

Core artifact flow:

```text
Proposal -> Design -> Contract Freeze -> Tasks -> Slice Handoff -> Implementation Report -> Planner Review -> Archive
```

## Quality / Validation

Current broad validation command:

```bash
./scripts/smoke-skills.sh
```

Quick validation command:

```bash
./scripts/smoke-skills.sh --quick
```

## Next Recommended Work

Implement Phase 9 lightweight validators:

1. lifecycle completeness checker
2. Contract Freeze presence checker
3. slice handoff structure checker
4. evidence/report existence checker
5. forbidden files checker
