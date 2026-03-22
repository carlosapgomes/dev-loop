# Apêndice — Rigor por Complexidade e Contexto

Este apêndice complementa o SOP com recomendações de rigor.

## Objetivo

Evitar dois extremos:

- burocracia desnecessária em mudanças simples
- falta de evidência em mudanças críticas

## Sinais para aumentar rigor

Aplique o modo mais formal (`FEATURE`/`HIGH`) quando houver:

- impacto em autenticação/autorização
- migração de dados ou contrato externo
- risco regulatório/compliance
- integração crítica com terceiros
- rollback caro
- mudança arquitetural de longo prazo

## Recomendação prática

- QUICK sem `design.md`: apenas bugfix simples, localizado e reversivel.
- Qualquer mudanca que nao seja bugfix simples: usar FEATURE com `design.md`.
- Planejamento de implementacao: preferir slices verticais (end-to-end) e evitar slice horizontal por camada.
- Mudanças estruturais/arriscadas: inclua ADR + plano de rollback + validação completa.
- Entregas formais (cliente enterprise/governo/regulado): gere release evidence pack com rastreabilidade.

## Regra de ouro

Em caso de duvida, escolha o modo mais rigoroso (`FEATURE` com `design.md`).
