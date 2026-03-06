# Backlog de Scripts (status de scriptização dos playbooks)

Status atual: todos os playbooks prioritários já possuem script inicial. Apenas `project-resurrection` permanece intencionalmente como playbook puro.

## Prioridade alta

1. `validate-agents` ✅
   - status: script inicial implementado em `skills/playbooks/validate-agents/validate_agents.py`
   - próximos incrementos: regras por linguagem e fixers adicionais
2. `changelog-updater` ✅
   - status: script inicial implementado em `skills/playbooks/changelog-updater/update_changelog.py`
   - próximos incrementos: templates customizáveis e integração com release pack
3. `release-evidence-pack-generator` ✅
   - status: script inicial implementado em `skills/playbooks/release-evidence-pack-generator/generate_release_pack.py`
   - próximos incrementos: coletar evidências de validação automaticamente

## Prioridade média

4. `django-insights` ✅
   - status: script inicial implementado em `skills/domain/django-insights/django_insights.py`
   - próximos incrementos: detectar padrões adicionais de ORM/migrações

## Prioridade baixa

5. `suggest-adr` ✅
   - status: script inicial implementado em `skills/playbooks/suggest-adr/suggest_adr.py`
   - próximos incrementos: enriquecer sinais com diff de código e histórico de ADRs
6. `refactor-sprint-suggester` ✅
   - status: script inicial implementado em `skills/playbooks/refactor-sprint-suggester/suggest_refactor_sprint.py`
   - próximos incrementos: métricas extras de complexidade e churn por módulo

## Mantém como playbook

- `project-resurrection` (ritual orientado a decisão humana)
