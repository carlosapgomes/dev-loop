# Workflow Híbrido Recomendado (Base Original + LLM2 + LLM3)

Data: 2026-03-02
Objetivo: um workflow mais forte que as duas versões, mantendo a base teórica original (OpenSpec + rigor proporcional ao risco), com execução viável para dev solo.

> **Status:** documento histórico. Para uso atual, adotar `SOP.md`.

## 1) Base Teórica (mantida do original)

Princípios inegociáveis:

1. LLM executa, artefatos em disco guardam memória.
2. Evidência no Git > intenção no chat.
3. Rigor proporcional ao risco.
4. Um change por vez, slices pequenos.
5. Um slice = um commit.
6. Retomada deve ser possível após meses sem dor.

## 2) O que entra de LLM2

- Três modos operacionais claros: `QUICK`, `FEATURE`, `HIGH/ARCH`.
- `Stop Rule` estrita após cada slice.
- `Project Resurrection Protocol` para retomada.
- Templates curtos e operacionais para AGENTS/CONTEXT/proposal/tasks.
- Separação explícita de postura: projeto de cliente vs SaaS próprio.

## 3) O que entra de LLM3

- `Release Evidence Pack` (mas apenas quando fizer sentido).
- `Quality Gate Executor` como padrão antes de commit/release.
- `Classify Change Risk` automatizado.
- `Artifacts Consistency Checker` antes de release importante.
- Linguagem de auditabilidade e forkabilidade para contexto público.

## 4) Melhorias sobre os dois (proposta nova)

## 4.1 Perfil por tipo de trabalho (evita excesso de processo)

- `PROFILE_PUBLIC`: cliente/setor público, prioridade em rastreabilidade.
- `PROFILE_SAAS`: produto próprio, prioridade em velocidade com controle.

Regra:

- O perfil define a profundidade documental adicional, sem mudar os princípios base.

## 4.2 Gating progressivo (não binário)

- Gate de `slice`: testes + lint + type-check apenas no escopo alterado.
- Gate de `change`: validação completa ao finalizar o change.
- Gate de `release`: evidências + consistência + rollback plan (quando aplicável).

Assim, você mantém fluxo rápido no dia a dia e rigor alto na entrega.

## 4.3 Release Evidence Pack sob gatilho, não sempre

Obrigatório quando:

- `PROFILE_PUBLIC`, ou
- risco `HIGH/ARCH`, ou
- release com mudança de contrato externo/dados/safety.

Opcional (resumo curto) para releases rápidas de SaaS.

## 5) Fluxo operacional padrão (Golden Path híbrido)

Para cada change:

1. Classificar risco (0-8): QUICK / FEATURE / HIGH.
2. Definir perfil do trabalho: PUBLIC ou SAAS.
3. Criar change no OpenSpec.
4. Gerar artefatos conforme matriz abaixo.
5. Implementar por slices (TDD + Stop Rule).
6. Rodar quality gate do change.
7. Arquivar change.
8. Se gatilho de release: gerar release pack.

## 6) Matriz de artefatos (clara e enxuta)

### QUICK (0-1)

- Obrigatório: `proposal.md`, `tasks.md`
- Recomendado: atualização breve de `PROJECT_CONTEXT.md` se aprender algo relevante
- Sem `design.md` e sem ADR (exceto decisão arquitetural real)

### FEATURE (2-3)

- Obrigatório: `proposal.md`, delta specs, `design.md`, `tasks.md`
- ADR: apenas se houver decisão estrutural de médio/longo prazo

### HIGH/ARCH (4+)

- Obrigatório: tudo de FEATURE + ADR + plano de rollback
- Se perfil PUBLIC: Release Evidence Pack obrigatório

## 7) Contratos-base do repositório

## 7.1 `AGENTS.md` (obrigatório)

- Comandos reais do projeto (test/lint/type/build/check).
- Comandos de automação Markdown (`markdown-format` + `markdown-lint`).
- Pre-commit hook para auto-fix/lint de `.md` staged.
- Templates sugeridos em `templates/markdown-automation/` (`install.sh` incluso).
- CI opcional de enforcement em `templates/ci/github-actions-markdown.yml`.
- Stop Rule explícita.
- Anti-patterns proibidos.
- Definição de perfil atual (`PUBLIC` ou `SAAS`) no topo.

## 7.2 `PROJECT_CONTEXT.md` (obrigatório neste híbrido)

- Curto (600-1200 palavras), focado em retomada.
- Seções fixas: propósito, fontes autoritativas, arquitetura, regras não negociáveis, quality bar, próximos riscos.

## 7.3 `prompts/handoff.md` (condicional)

- Obrigatório para projetos novos complexos.
- Em brownfield, usar versão retroativa incremental.

## 8) Protocolo de retomada (resurrection)

Na volta ao projeto:

1. Ler `AGENTS.md` e `PROJECT_CONTEXT.md`.
2. Verificar changes ativos e último slice concluído.
3. Rodar teste rápido + lint rápido.
4. Executar apenas o próximo slice.
5. Commit e parar.

Tempo-alvo de aquecimento: 10-20 minutos.

## 9) Rotina mínima semanal (solo dev realista)

Diária:

- 1 a 3 slices por sessão.
- Stop Rule sempre.

Semanal:

- Revisar `PROJECT_CONTEXT.md` (10 min).
- Revisar backlog de débitos (15 min).

Mensal:

- 1 refactor sprint curto (2-4h).
- Revisão de `AGENTS.md`.

## 10) Estratégia dual: público + SaaS sem conflito

Para contratos públicos:

- padrão default: FEATURE.
- release pack quase sempre.
- ADR mais frequente.

Para SaaS próprio:

- default QUICK para experimentos.
- FEATURE para funcionalidades que entram no core.
- ADR só para fundações (auth, billing, tenancy, dados).

Você usa o mesmo workflow, só muda o perfil e os gatilhos.

## 11) Ferramentas/skills recomendadas (ordem prática)

Core imediato:

1. `classify-change-risk`
2. `quality-gate-executor`
3. `agents-md-generator`
4. `project-context-maintainer`

Para releases críticas:
5. `adr-generator`
6. `artifacts-consistency-checker`
7. `release-evidence-pack-generator`

## 12) Regras anti-burocracia (para não virar processo pesado)

1. Documento só existe se for usado na próxima retomada/release.
2. Tudo que não reduz risco ou retrabalho deve ser removido.
3. QUICK não pode virar FEATURE por ansiedade.
4. FEATURE/HIGH não pode virar QUICK por pressa.
5. Se um ritual ficou vazio por 30 dias, simplificar ou eliminar.

## 13) Resultado esperado após 60 dias

- Retomada consistente em qualquer projeto em < 20 min.
- Menos regressões por falta de contexto.
- Rastreabilidade suficiente para setor público quando necessário.
- Velocidade preservada para evolução do SaaS.
- Menor drift entre intenção, artefatos e código real.

## 14) Decisão recomendada de adoção

Adotar este híbrido em duas fases:

1. Semana 1-2: princípios base + 3 modos + Stop Rule + AGENTS/CONTEXT.
2. Semana 3-8: ligar automações (risk, quality gate, consistency, release pack por gatilho).

Esse caminho reduz fricção inicial e evita abandonar o processo por excesso de formalidade.
