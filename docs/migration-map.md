# Migration Map — Nomenclatura e Diretórios

## Projeto

- Nome antigo (interno): `Workflow-Beta`
- Nome alvo: `dev-loop` (marca: **DevLoop**)

## SOP

- Nome antigo: `Workflow Híbrido ...`
- Nome canônico novo: `SOP` (`SOP.md`)

## Skills — Diretórios

| Antigo | Novo |
|---|---|
| `skills/deepseek/adr-generator` | `skills/core/adr-generator` |
| `skills/deepseek/agents-md-generator` | `skills/core/agents-md-generator` |
| `skills/deepseek/artifacts-consistency-checker` | `skills/core/artifacts-consistency-checker` |
| `skills/deepseek/classify-change-risk` | `skills/core/classify-change-risk` |
| `skills/deepseek/project-context-maintainer` | `skills/core/project-context-maintainer` |
| `skills/deepseek/quality-gate-executor` | `skills/core/quality-gate-executor` |
| `skills/deepseek/setup-solopreneur-project` | `skills/core/setup-solopreneur-project` |
| `skills/deepseek/changelog-updater` | `skills/playbooks/changelog-updater` |
| `skills/deepseek/refactor-sprint-suggester` | `skills/playbooks/refactor-sprint-suggester` |
| `skills/deepseek/release-evidence-pack-generator` | `skills/playbooks/release-evidence-pack-generator` |
| `skills/k2.5/esaa-project-resurrection` | `skills/playbooks/project-resurrection` |
| `skills/k2.5/esaa-suggest-adr` | `skills/playbooks/suggest-adr` |
| `skills/k2.5/esaa-validate-agents` | `skills/playbooks/validate-agents` |
| `skills/k2.5/esaa-django-insights` | `skills/domain/django-insights` |
| `skills/k2.5/esaa-classify-risk` | `skills/legacy/esaa-classify-risk` |
| `skills/k2.5/esaa-generate-agents` | `skills/legacy/esaa-generate-agents` |
| `skills/k2.5/esaa-generate-context` | `skills/legacy/esaa-generate-context` |

## Installer

- `skills/install_all_skills.sh` agora instala por grupos (`core`, `playbooks`, `domain`).
- Para compatibilidade, usar `--include-legacy`.
