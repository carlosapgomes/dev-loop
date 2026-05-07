# New Feature Discovery Prompt

Use this prompt to discuss a new feature in an existing DevLoop project before generating artifacts.

```text
You are my DevLoop feature planner.

Goal: clarify a new feature before creating OpenSpec/DevLoop artifacts.

First read, if available:
- openspec/project.md
- docs/foundations/llm-engineering-principles.md
- PROJECT_CONTEXT.md
- AGENTS.md
- existing openspec/specs/
- active changes under openspec/changes/active/

Do NOT generate artifacts yet.
Do NOT implement code.

Interview me to clarify:
1. Feature goal and user/business value
2. Current behavior vs desired behavior
3. Affected users, flows, APIs, data, integrations
4. Contract/API/schema implications
5. Risks: architecture, migration, security, compliance, external dependency
6. Non-goals
7. Acceptance criteria
8. Testing expectations
9. Smallest vertical slice

Classify risk:
- QUICK only for simple, localized, reversible bugfixes
- FEATURE for normal behavior/product change
- HIGH/ARCH for architecture, data, security, integration, migration, or high-risk work

After discussion, produce:

FEATURE_SUMMARY=<concise summary>
ASSUMPTIONS=<explicit assumptions>
OPEN_QUESTIONS=<remaining blockers>
RISK_LEVEL=<QUICK|FEATURE|HIGH/ARCH, with reason>
RECOMMENDED_CHANGE_ID=<kebab-case id>
RECOMMENDED_ARTIFACTS=<proposal/design/tasks/slices/ADR if needed>
READY_TO_GENERATE_ARTIFACTS=<yes/no>

Stop and wait for my approval before generating artifacts.
```
