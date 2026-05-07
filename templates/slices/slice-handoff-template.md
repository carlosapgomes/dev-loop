# Slice Handoff Template (LLM Contexto Zero)

> Compatibilidade: para novos changes, preferir `templates/slices/slice-handoff.md`.

Objetivo: contexto mínimo suficiente para uma slice vertical.

## 1) Identificacao

- Change: `<change-id>`
- Slice: `<X.Y>`
- Titulo: `<resumo curto>`
- Dependencias: `<slices previos / nenhuma>`

## 2) Contratos congelados

Fonte: `openspec/changes/active/<change-id>/design.md#contract-freeze`

- Interfaces/APIs usadas:
- DTOs/schemas/payloads:
- Invariantes:
- Mudanca de contrato permitida? `nao`, salvo aprovacao explicita aqui:

## 3) Fronteiras arquiteturais

Fonte: `openspec/project.md`

- Camadas/modulos tocados:
- Direcao de dependencia a preservar:
- Fronteiras de integracao/persistencia:

## 4) Escopo

### Arquivos/areas permitidos

- `caminho/arquivo-ou-diretorio`

### Arquivos/areas proibidos

- `caminho/arquivo-ou-diretorio`

### Non-goals explicitos

- <o que esta slice nao deve fazer>

Se precisar expandir escopo, parar e justificar antes de codar.

## 5) Objetivo vertical

- Valor entregue ao usuario/negocio:
- Fluxo completo coberto:

## 6) Plano TDD

- RED: <teste/comportamento falhando primeiro>
- GREEN: <implementacao minima para passar>
- REFACTOR: <limpeza preservando leis e contratos>

## 7) Gates

- [ ] Evidencia RED/GREEN/REFACTOR capturada
- [ ] Comandos de validacao do `AGENTS.md` executados ou justificados
- [ ] Contratos congelados preservados
- [ ] Arquivos permitidos/proibidos respeitados
- [ ] `tasks.md` atualizado

## 8) Criterios de sucesso

- [ ] Comportamento vertical entregue
- [ ] Testes representam comportamento/contratos
- [ ] Nenhum escopo proibido adicionado
- [ ] Nenhuma mudanca de contrato sem aprovacao
- [ ] Relatorio de evidencia gerado

## 9) Relatorio de evidencia

Agente implementador usa `templates/reports/implementation-report.md` e inclui:

- arquivos alterados e motivo
- gates executados e resultados
- aderencia aos contratos/escopo
- foco para reviewer e follow-ups

Agente reviewer/planner usa `templates/reports/planner-review.md` para aprovar, aprovar com follow-ups ou rejeitar.

Saida obrigatoria:

```text
REPORT_PATH=<caminho-do-relatorio.md>
```

## 10) Prompt para implementador

```text
Leia openspec/project.md, docs/foundations/llm-engineering-principles.md, AGENTS.md, PROJECT_CONTEXT.md, proposal/design/tasks do change ativo e este slice.
Implemente APENAS esta slice.
Preserve contratos congelados e fronteiras arquiteturais.
Toque apenas arquivos/areas permitidos; nao toque arquivos/areas proibidos.
Siga o plano TDD: RED -> GREEN -> REFACTOR.
Execute os gates obrigatorios.
Gere o relatorio de implementacao e responda com REPORT_PATH=<caminho-do-relatorio.md>.
Nao aprove o proprio trabalho; o reviewer/planner gate e separado.
PARE apos esta slice.
```
