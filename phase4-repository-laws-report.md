# Phase 4 Implementation Report — Repository Laws

## Summary

Implemented centralized repository laws for DevLoop v2.

Canonical law source:

```text
openspec/project.md
```

Purpose: make permanent engineering constraints explicit for probabilistic agents, reduce drift, and avoid repeating philosophy across prompts/templates.

## Changes Made

### 1. Created repository laws

Added:

```text
openspec/project.md
```

It centralizes:

- authority order
- architectural boundaries
- dependency rules
- layering constraints
- testing expectations
- DRY interpretation for low-drift agents
- YAGNI interpretation for low-drift agents
- SOLID interpretation for low-drift agents
- simplicity rules
- non-negotiable agent rules

The language is operational rather than dogmatic.

### 2. Updated docs to reference laws

Updated:

```text
README.md
SOP.md
docs/README.md
docs/getting-started.md
```

Key change: permanent engineering constraints now point to `openspec/project.md` instead of being re-explained across lifecycle docs.

### 3. Updated templates to inherit laws

Updated:

```text
templates/openspec/design.md
templates/slices/slice-handoff.md
templates/slices/slice-handoff-template.md
```

Slices now explicitly read and preserve:

```text
openspec/project.md
```

alongside the active `design.md#contract-freeze`.

### 4. Updated AGENTS generation references

Updated generated/fallback AGENTS behavior in:

```text
.devloop/skills/core/agents-md-generator/generate_agents_md.py
.devloop/skills/core/setup-solopreneur-project/setup_project.py
```

Generated AGENTS now references repository laws instead of duplicating clean-code-style philosophy.

### 5. Bootstrap support added

When bootstrapping with OpenSpec enabled, setup now creates:

```text
openspec/project.md
```

with concise default repository laws.

## Duplication Reduction

Removed repeated clean-code philosophy language from key prompts/templates and replaced it with operational references to:

```text
openspec/project.md
```

Detailed principle interpretation now lives in one place.

## Validation

Commands run successfully:

```bash
python3 .devloop/skills/core/setup-solopreneur-project/tests/test_setup_project.py
python3 .devloop/skills/core/agents-md-generator/tests/test_generate_agents_md.py
python3 .devloop/skills/core/artifacts-consistency-checker/tests/test_check_consistency.py
./scripts/smoke-skills.sh --quick
```

## Success Criteria Status

- Repository laws centralized: done
- Architectural/dependency/layering/testing rules included: done
- DRY/YAGNI/SOLID/simplicity interpreted for low-drift agents: done
- Duplicated philosophy reduced across prompts/templates: done
- Docs remain concise: done

## Deferred

Not implemented in this phase:

- automation/enforcement of repository laws
- repository law validator
- broader rewrite of all legacy skill documentation
- new abstractions beyond `openspec/project.md`
