---
phase: 01-hero-cinematografico
plan: 02
subsystem: hero-js
tags: [hero, parallax, vanilla-js, requestAnimationFrame, scroll, touch, accessibility]

# Dependency graph
requires:
  - phase: 01-hero-cinematografico plan 01
    provides: foto-21.png como background com margens de parallax (-20%) e will-change:transform
provides:
  - Script de parallax vanilla (requestAnimationFrame + translateY) no hero
  - Throttle nativo via ticking pattern (60fps)
  - Fallback touch: parallax desativado em hover:none devices
  - Fallback acessibilidade: parallax desativado em prefers-reduced-motion
affects:
  - index.html (bloco <script>)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - requestAnimationFrame + ticking pattern (throttle nativo de scroll 60fps)
    - matchMedia hover:none para deteccao de touch sem User-Agent sniffing
    - passive:true em scroll listeners (ja usado no nav scroll)

key-files:
  created: []
  modified:
    - index.html

key-decisions:
  - "Fator 0.4 (40% da velocidade do scroll) escolhido para efeito sutil e perceptivel"
  - "isTouch via matchMedia(hover:none) — mais confiavel que User-Agent para iOS Safari"
  - "passive:true obrigatorio — nao bloquear thread principal durante scroll"

patterns-established:
  - "Parallax pattern: rAF + ticking + matchMedia guards (accessibility + touch)"

requirements-completed: [HERO-01, HERO-04, HERO-05]

# Metrics
duration: ~4min
completed: 2026-04-01T21:55:28Z
---

# Phase 01 Plan 02: Script Parallax Vanilla no Hero

**Parallax por translateY com requestAnimationFrame, throttle ticking, fallback touch (matchMedia hover:none) e prefers-reduced-motion injetado no bloco script do hero.**

## Performance

- **Duration:** ~4 min
- **Started:** 2026-04-01T21:54:30Z
- **Completed:** 2026-04-01T21:55:28Z
- **Tasks:** 1 auto + 1 checkpoint (auto-aprovado)
- **Files modified:** 1

## Accomplishments
- Script de parallax vanilla adicionado ao bloco `<script>` existente sem dependencias externas
- Throttle via ticking pattern garante no maximo 1 rAF por frame — sem empilhamento de callbacks
- Touch devices nao recebem parallax (matchMedia `hover:none` cobre iOS Safari onde `background-attachment:fixed` e quebrado)
- prefers-reduced-motion respeitado por acessibilidade
- Hero cinematografico completo: foto real + overlay + logo com drop-shadow + parallax + animacoes fadeUp + scroll indicator

## Task Commits

Each task was committed atomically:

1. **Task 1: Injetar script de parallax no bloco script existente** - `47d0504` (feat)

**Plan metadata:** (docs commit — ver abaixo)

## Files Created/Modified
- `index.html` - Parallax script adicionado no bloco `<script>` existente (linhas 932-948)

## Decisions Made
- Fator `0.4` escolhido (40% da velocidade de scroll) — sutil mas claramente perceptivel, nao exagerado
- `matchMedia('(hover:none)')` para deteccao touch — mais semantico e confiavel que User-Agent sniffing, cobre iOS Safari
- `passive: true` no listener de scroll — padrao ja estabelecido pelo nav scroll, obrigatorio para performance

## Deviations from Plan

None — plano executado exatamente como especificado.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 1 completa. Todos os 5 criterios de sucesso implementados:
1. Hero exibe foto de ambiente real (foto-21.png) com parallax ao scroll
2. Texto legivel sobre a foto (overlay rgba .55 + .65 + 1)
3. Logo dourada centralizada com drop-shadow duplo visivel
4. Animacoes fadeUp preservadas (hero-line, hero-logo, eyebrow, h1, sub, cta-wrap)
5. Scroll indicator visivel (hero-scroll + scroll-line pulsante)

Pronto para Phase 2 (Colecao / produto cards).

---
*Phase: 01-hero-cinematografico*
*Completed: 2026-04-01*
