---
phase: 02-secoes-de-produto-e-ambiente
plan: 01
subsystem: ui
tags: [css, object-fit, mix-blend-mode, hover, touch, media-query]

# Dependency graph
requires:
  - phase: 01-hero-cinematografico
    provides: identidade visual escuro/dourado (#0E0E0E + #C9A96E) estabelecida
provides:
  - CSS .pc img com object-fit:cover + padding:14px, sem mix-blend-mode
  - "@media (hover: none) com .pc-label opacity:1 para touch"
  - classe wide no div da Mesa de Centro, sem inline style no img filho
affects:
  - 02-secoes-de-produto-e-ambiente (planos subsequentes)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "object-fit: cover para preenchimento de cards de produto"
    - "@media (hover: none) para labels sempre visíveis em touch"

key-files:
  created: []
  modified:
    - index.html

key-decisions:
  - "object-fit: cover substitui contain — produtos preenchem o card com respiro sutil de 14px ao invés de flutuarem no centro"
  - "mix-blend-mode: multiply removido completamente — sobre fundo #0E0E0E o modo multiply apagava as imagens"
  - "padding uniforme 14px em tall/wide — consistência visual entre todos os tamanhos de card"
  - "Classe wide adicionada ao div pai da Mesa de Centro — migração de inline style para CSS declarativo"
  - "@media (hover: none) CSS-only para labels touch — evita dependência de JS e timing de execução"

patterns-established:
  - "Detecção de touch via @media (hover: none): mesmo padrão já usado no JS do parallax (isTouch)"

requirements-completed: [COL-01, COL-02, COL-03, COL-04]

# Metrics
duration: 8min
completed: 2026-04-01
---

# Phase 2 Plan 01: Seção Coleção — object-fit e Touch Labels Summary

**CSS da Coleção corrigido: object-fit cover com padding 14px, mix-blend-mode removido, e labels sempre visíveis em dispositivos touch via @media (hover: none)**

## Performance

- **Duration:** 8 min
- **Started:** 2026-04-01T22:49:00Z
- **Completed:** 2026-04-01T22:57:03Z
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments

- `.pc img` atualizado de `object-fit: contain; padding: 36px; mix-blend-mode: multiply` para `object-fit: cover; padding: 14px` — produtos agora preenchem os cards sem aparecerem apagados
- `.pc.tall img` e `.pc.wide img` com `padding: 14px` uniforme — consistência visual entre todos os tamanhos de card
- Card Mesa de Centro migrado de inline style para classe `wide` no div pai — CSS declarativo sem exceções inline
- `@media (hover: none) { .pc-label { opacity: 1; } }` adicionado — labels dourados visíveis em touch sem JS adicional

## Task Commits

Cada task foi commitada atomicamente:

1. **Task 1: Atualizar CSS object-fit e remover mix-blend-mode da Coleção** - `40fce5d` (feat)
2. **Task 2: Adicionar @media (hover: none) para labels touch da Coleção** - `c2508cb` (feat)

## Files Created/Modified

- `index.html` — CSS `.pc img` (object-fit, padding, mix-blend-mode), `.pc.tall img`, `.pc.wide img`, div Mesa de Centro (classe wide), img Mesa de Centro (sem inline style), bloco `@media (hover: none)`

## Decisions Made

- `object-fit: cover` com `padding: 14px` uniforme — respiro sutil nas bordas sem os produtos parecerem pequenos/flutuando como com `contain + 36px`
- `mix-blend-mode: multiply` removido completamente (não substituído) — sobre fundo escuro `#0E0E0E`, multiply torna qualquer imagem quase invisível
- Abordagem CSS-only para touch labels (`@media (hover: none)`) ao invés de JS — declarativa, sem dependência de timing, mesma heurística já usada no parallax JS existente

## Deviations from Plan

None - plano executado exatamente como especificado.

## Issues Encountered

None.

## User Setup Required

None - nenhuma configuração de serviço externo necessária.

## Next Phase Readiness

- Seção Coleção: produtos visíveis com preenchimento correto, labels touch funcionais
- Próximo plano (02-02): seção Ambientes — `.dest-overlay` já é sempre visível (sem opacity:0), tratado no próximo plano conforme nota no PLAN.md
- Regressão: hero parallax e animações reveal não foram alterados

---
*Phase: 02-secoes-de-produto-e-ambiente*
*Completed: 2026-04-01*
