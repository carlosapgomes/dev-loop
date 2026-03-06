# Workflow Híbrido ESAA - Checklist Executável (1 Página)

Data: 2026-03-02  
Uso: abrir este arquivo no início de cada sessão.

> **Status:** checklist histórico. Para checklist atual, usar `SOP.md` + `docs/appendices/rigor-by-complexity.md`.

## 0) Setup único (fazer 1x por projeto)

- [ ] `openspec init`
- [ ] Criar `AGENTS.md` com comandos reais de `test`, `lint`, `type-check`, `build/check`
- [ ] Criar `PROJECT_CONTEXT.md` curto (propósito, arquitetura, regras não negociáveis, quality bar)
- [ ] Definir perfil atual no topo do `AGENTS.md`: `PROFILE_PUBLIC` ou `PROFILE_SAAS`
- [ ] Configurar quality gate local (comando único), ex: `make verify` ou script equivalente
- [ ] Ativar automação de Markdown: `scripts/markdown-format.sh`, `scripts/markdown-lint.sh` e pre-commit hook

## 1) Classificação rápida antes de cada change (30s)

Marque 1 ponto por item:

- [ ] auth/autorização
- [ ] dados persistidos/migração
- [ ] API/contrato externo
- [ ] segurança
- [ ] performance crítica
- [ ] refatoração ampla (>5 arquivos)
- [ ] rollback caro
- [ ] impacto regulatório/documental

Resultado:

- [ ] `0-1` = `QUICK`
- [ ] `2-3` = `FEATURE`
- [ ] `4+` = `HIGH/ARCH`

## 2) Artefatos obrigatórios por modo

`QUICK`:

- [ ] `proposal.md` curto
- [ ] `tasks.md` curto

`FEATURE`:

- [ ] `proposal.md`
- [ ] delta specs
- [ ] `design.md`
- [ ] `tasks.md`

`HIGH/ARCH`:

- [ ] tudo de `FEATURE`
- [ ] ADR em `docs/adr/`
- [ ] plano de rollback

Gatilho de `Release Evidence Pack`:

- [ ] sempre em `PROFILE_PUBLIC`
- [ ] sempre em `HIGH/ARCH`
- [ ] em `PROFILE_SAAS`, apenas para release relevante

## 3) Ciclo diário por sessão (45-180 min)

1. [ ] Ler `AGENTS.md` e `PROJECT_CONTEXT.md` (5 min)
2. [ ] Escolher 1 change ativo e 1 slice apenas
3. [ ] Executar TDD: `RED -> GREEN -> REFACTOR`
4. [ ] Rodar gate de slice (escopo alterado): testes + lint + type-check
5. [ ] Se alterou `.md`: rodar `./scripts/markdown-format.sh`
6. [ ] Commit atômico (`1 slice = 1 commit`)
7. [ ] Marcar task `[x]` em `tasks.md`
8. [ ] Atualizar `PROJECT_CONTEXT.md` se houve aprendizado relevante (2-5 linhas)
9. [ ] **STOP RULE**: parar e decidir conscientemente próximo slice
10. [ ] Se encerrar o dia: `git status` limpo ou WIP explícito e documentado

## 4) Gate de finalização de change

- [ ] Todos os slices concluídos
- [ ] Gate completo do projeto executado
- [ ] Markdown lint sem erros (`./scripts/markdown-lint.sh`)
- [ ] Artefatos sincronizados com código real
- [ ] ADR criada (se necessário)
- [ ] Change arquivado

## 5) Rotina semanal (30-45 min)

- [ ] Revisar `PROJECT_CONTEXT.md` (remover desatualizado, manter objetivo claro)
- [ ] Revisar backlog técnico (top 3 dívidas reais)
- [ ] Planejar 1 mini refactor de alto impacto
- [ ] Verificar aderência ao Stop Rule (sem commits gigantes)
- [ ] Checar drift entre spec/design/tasks e implementação

## 6) Rotina mensal (2-4h)

- [ ] Refactor sprint curto (1 módulo crítico)
- [ ] Revisão do `AGENTS.md` (regras e comandos ainda válidos?)
- [ ] Consolidar decisões em ADR pendentes
- [ ] Revisar qualidade de testes em áreas de maior risco
- [ ] Revisar pipeline de release/evidência

## 7) Perfil de execução (alternar sem mudar o sistema)

`PROFILE_PUBLIC`:

- [ ] padrão default em `FEATURE`
- [ ] maior exigência de evidência e documentação
- [ ] release pack quase sempre

`PROFILE_SAAS`:

- [ ] default em `QUICK` para experimento
- [ ] promover para `FEATURE` ao entrar no core
- [ ] ADR só para decisões fundacionais

## 8) Prompt curto de reentrada (copiar/colar)

```txt
Read AGENTS.md and PROJECT_CONTEXT.md first.
Project profile: <PROFILE_PUBLIC|PROFILE_SAAS>.
Change ID: <change-id>.
Implement ONLY the next incomplete slice.
Run validation commands, update tasks/specs, commit, then STOP.
```

## 9) Regra anti-burocracia

- [ ] Se um artefato não ajuda retomada, qualidade ou release, simplifique ou elimine.
