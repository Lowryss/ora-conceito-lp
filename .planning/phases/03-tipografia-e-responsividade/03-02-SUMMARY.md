---
phase: 03-tipografia-e-responsividade
plan: 02
subsystem: mobile-responsiveness
tags: [mobile, hero, parallax, svh, font-size, touch]
dependency_graph:
  requires: [03-01]
  provides: [MOB-01, MOB-02, MOB-05]
  affects: [index.html]
tech_stack:
  added: []
  patterns: [100svh-fallback, hover-none-media-query, mobile-font-floor]
key_files:
  created: []
  modified: [index.html]
decisions:
  - "@media (hover: none) escolhido para neutralizar .hero-bg em vez de max-width — critério de parada do parallax é touch detection, não breakpoint de largura"
  - "100svh com fallback implícito via CSS cascade — browsers sem suporte a svh mantêm 100vh da regra base"
  - "min-height reduzido de 680px para 580px em mobile — acomoda iPhone SE (667px de viewport)"
  - "Regras de 14px adicionadas apenas ao @media(max-width:700px) — desktop mantém 13px sem alteração"
metrics:
  duration: 2min
  completed_date: "2026-04-01"
  tasks_completed: 2
  files_modified: 1
---

# Phase 03 Plan 02: Mobile Hero e Legibilidade de Texto Summary

**One-liner:** `100svh` + `@media (hover: none)` corrigem hero overflow iOS Safari e parallax em touch; `14px` floor garante legibilidade sem pinch-zoom em todos os body text.

## Tasks Completed

| # | Task | Commit | Files |
|---|------|--------|-------|
| 1 | Neutralizar margens de parallax no hero mobile e corrigir altura com 100svh | `557c309` | index.html |
| 2 | Garantir font-size mínimo 14px no mobile para todos os body text | `7e34d62` | index.html |

## Changes Made

### Task 1 — Hero mobile: parallax e SVH

Duas edições CSS:

**`@media (hover: none)` — parallax reset:**
```css
.hero-bg { top: 0; height: 100%; }
```
O `.hero-bg` base tem `top: -20%; height: 140%` para dar margem ao parallax cinematográfico. Em touch devices o parallax para (via `isTouch.matches` no JS), mas as margens permanecem — causando overflow. Esta regra colapsa as margens apenas em touch, espelhando exatamente o critério do JS.

**`@media(max-width:700px)` — 100svh:**
```css
#hero { height: 100svh; min-height: 580px; }
```
`100svh` (Small Viewport Height) corresponde à altura visível com a barra de endereços do Safari iOS recolhida, eliminando o overflow clássico. Browsers sem suporte a `svh` ignoram a regra e mantêm `100vh` da regra base (fallback via cascata, sem media query adicional).

### Task 2 — Font-size floor 14px

```css
@media(max-width:700px){
  /* ... regras existentes ... */
  .sobre-txt > p,
  .dif p,
  .pilar-d,
  .contato-txt,
  .footer-col a { font-size: 14px; }
}
```
Os valores desktop (13px, definidos no plano 03-01) ficam abaixo do mínimo recomendado para mobile. A regra sobrepõe apenas em viewports ≤700px sem alterar a tipografia desktop.

Headings secundários (`.pilar-t` 20px, `.dif h3` 23px, `.dest-title` 26px) não requerem ajuste — quebra de linha em 2 linhas é visualmente aceitável e esperada.

## Success Criteria Verification

- [x] `.hero-bg` em touch devices: `top: 0; height: 100%` — sem overflow de margens de parallax
- [x] `#hero` em mobile: `height: 100svh` com fallback implícito para `100vh` via cascade
- [x] Todos os seletores de body text: `14px` em viewport ≤700px
- [x] Grid da Coleção: regras existentes (`repeat(4,1fr)` com spans) já cobrem 2 colunas em 375px — verificação confirmatória
- [x] Zero regressões em desktop — todas as regras dentro de media queries, base CSS inalterado

## Deviations from Plan

None — plano executado exatamente como escrito. Headings secundários inspecionados: nenhum ajuste necessário (zero regras opcionais adicionadas).

## Self-Check: PASSED

- `557c309` exists: confirmed via `git log`
- `7e34d62` exists: confirmed via `git log`
- `index.html` contains `100svh`: confirmed at line 507
- `index.html` contains `hover: none` with `.hero-bg`: confirmed at lines 521-524
- `index.html` contains `font-size: 14px` mobile rules: confirmed at lines 519-523
