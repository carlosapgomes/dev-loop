# Inventário de Skills e Decisões de Consolidação

## Taxonomia atual

- `skills/core`: canônicos executáveis
- `skills/playbooks`: protocolos/guias (maioria com script auxiliar)
- `skills/domain`: especialização por stack
- `skills/legacy`: compatibilidade temporária

## Matriz de sobreposição

| Tema | Skill canônico | Skill sobreposto | Decisão |
|---|---|---|---|
| Classificação de risco | `classify-change-risk` | `esaa-classify-risk` | Canônico = script em `core`; `esaa-*` fica em `legacy` |
| Geração de AGENTS | `agents-md-generator` | `esaa-generate-agents` | Canônico = script em `core`; `esaa-*` fica em `legacy` |
| Contexto de projeto | `project-context-maintainer` | `esaa-generate-context` | Canônico = script em `core`; `esaa-*` fica em `legacy` |
| Sugestão de ADR | `adr-generator` + `suggest-adr` | `esaa-suggest-adr` | `suggest-adr` consolidado com script (`suggest_adr.py`); alias legado preservado |

## Decisão sobre skills sem script

| Skill | Estado atual | Decisão |
|---|---|---|
| `changelog-updater` | playbook + script `update_changelog.py` | ✅ Script criado (manter evolução) |
| `validate-agents` | playbook + script `validate_agents.py` | ✅ Script criado (manter evolução) |
| `release-evidence-pack-generator` | playbook + script `generate_release_pack.py` | ✅ Script criado (manter evolução) |
| `django-insights` | domain + script `django_insights.py` | ✅ Script criado (manter evolução) |
| `refactor-sprint-suggester` | playbook + script `suggest_refactor_sprint.py` | ✅ Script criado (manter evolução) |
| `project-resurrection` | playbook | Manter playbook por enquanto |
| `suggest-adr` | playbook + script `suggest_adr.py` | ✅ Script criado (manter evolução) |

## Ordem sugerida (estado atual)

1. `validate-agents` ✅
2. `changelog-updater` ✅
3. `release-evidence-pack-generator` ✅
4. `django-insights` ✅
5. `suggest-adr` ✅
6. `refactor-sprint-suggester` ✅
7. único playbook sem script por decisão: `project-resurrection`
