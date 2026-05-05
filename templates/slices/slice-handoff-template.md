# Slice Handoff Template (LLM Contexto Zero)

## 1) Identificacao
- Change: `<change-id>`
- Slice: `<X.Y>`
- Titulo: `<resumo curto>`
- Dependencias: `<slices previos / nenhuma>`

## 2) Objetivo vertical (end-to-end)
- Valor entregue ao usuario/negocio:
- Fluxo completo coberto:

## 3) Escopo enxuto (so o necessario)
- Arquivos permitidos para alteracao:
  - `caminho/arquivo-1`
  - `caminho/arquivo-2`
- Limite alvo: poucos arquivos (ideal <= 5).
- Se precisar expandir escopo, registrar justificativa antes de codar.

## 4) Handoff funcional/tecnico
- Contexto minimo de negocio:
- Regras nao negociaveis:
- Contratos/interfaces que nao podem quebrar:
- Riscos conhecidos:

## 5) Prompt pronto para implementador (copiar/colar)
```text
Leia AGENTS.md, PROJECT_CONTEXT.md e este slice.
Implemente APENAS este slice com visao vertical.
Siga TDD: RED -> GREEN -> REFACTOR.
No REFACTOR, priorize clean code (coesao, nomes claros, baixo acoplamento, sem codigo morto).
Toque apenas os arquivos permitidos; se extrapolar, justifique.
Ao final, execute os gates, gere relatorio detalhado com snippets antes/depois e salve em markdown temporario.
Responda com REPORT_PATH=<caminho-do-arquivo.md>.
```

## 6) Criterios de sucesso
- [ ] Comportamento esperado entregue ponta a ponta
- [ ] Testes novos/ajustados representam o comportamento
- [ ] Nenhum contrato quebrado
- [ ] Escopo mantido enxuto

## 7) Gates de autoavaliacao
- [ ] RED documentado (teste falhando antes da implementacao)
- [ ] GREEN documentado (teste passando com minimo)
- [ ] REFACTOR documentado (limpeza sem regressao)
- [ ] Testes/lint/type-check da secao 2 do AGENTS.md
- [ ] Artefatos do change atualizados (`tasks.md`, specs, notas)

## 8) Relatorio obrigatorio para o planner
Gerar markdown temporario com:
1. resumo do que foi implementado
2. lista de arquivos alterados e justificativa
3. evidencias dos gates executados
4. snippets antes/depois das mudancas principais
5. riscos pendentes e proximos passos

Saida obrigatoria no chat:
- `REPORT_PATH=<caminho-do-relatorio-temporario.md>`
