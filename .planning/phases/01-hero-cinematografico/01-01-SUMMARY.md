---
phase: 01-hero-cinematografico
plan: 01
subsystem: hero-css
tags: [hero, background, parallax, drop-shadow, css]
requirements: [HERO-01, HERO-02, HERO-03]

dependency_graph:
  requires: []
  provides:
    - hero fundo real com foto-21.png
    - overlay recalibrado para foto colorida
    - margens de parallax (top/bottom -20%)
    - drop-shadow duplo na logo
  affects:
    - index.html (.hero-bg, .hero-logo img)

tech_stack:
  added: []
  patterns:
    - CSS multi-layer background (gradient + url)
    - CSS filter com drop-shadow encadeado
    - will-change: transform para hint de compositing
    - margens negativas de parallax (top/bottom -20%)

key_files:
  created: []
  modified:
    - index.html

decisions:
  - Usar top/bottom -20% em vez de inset:0 para garantir que o parallax nao descobre bordas durante translateY
  - Overlay topo subiu de .4 para .55 — necessario para texto legivel sobre foto com conteudo claro
  - Overlay meio caiu de .72 para .65 — gradiente mais natural, evita excesso de escuridao no centro
  - Drop-shadow duplo na logo: halo dourado ampliado + shadow escuro de separacao

metrics:
  duration: ~8min
  completed: 2026-04-01T21:53:09Z
  tasks_completed: 2
  files_modified: 1
---

# Phase 01 Plan 01: Hero Background — Foto Real e Drop-Shadow Duplo

**One-liner:** Substituicao do fundo preto placeholder por foto-21.png com overlay recalibrado e drop-shadow duplo na logo dourada para legibilidade sobre foto colorida.

## What Was Built

O hero da LP ORA Conceito agora exibe uma foto real de ambiente (`foto-21.png`) no lugar do placeholder escuro (`logo-bg-preta.jpg`). O visitante ve imediatamente o espaco e o padrao da marca nos primeiros 3 segundos.

### Changes Made

**`.hero-bg` (Task 1):**
- `inset: 0` substituido por `top: -20%; bottom: -20%; left: 0; right: 0` — margem extra garante que o parallax JS nao descobre bordas durante translateY
- `url('assets/logo-bg-preta.jpg')` trocado por `url('assets/foto-21.png')`
- Overlay topo: `.4` -> `.55` — mais denso para cobrir conteudo claro/colorido da foto sobre a area da nav
- Overlay meio: `.72` -> `.65` — levemente menos denso, gradiente mais natural
- `will-change: transform` adicionado — hinting de performance para o compositor do browser

**`.hero-logo img` (Task 2):**
- Halo dourado: radius `32px` -> `40px`, opacidade `.2` -> `.35` — mais visivel sobre foto
- Segundo drop-shadow adicionado: `0 2px 12px rgba(0,0,0,.6)` — separa a logo de areas claras da foto
- `width: 100%` e demais propriedades preservadas intactas

## Commits

| Task | Hash | Message |
|------|------|---------|
| 1 | 7e02460 | feat(01-01): substituir background do hero e recalibrar overlay |
| 2 | 47d35a9 | feat(01-01): reforcar drop-shadow da logo para fundo de foto |

## Verification Checklist

- [x] `.hero-bg` usa `url('assets/foto-21.png')` — sem referencias a logo-bg-preta.jpg
- [x] `.hero-bg` tem `top: -20%; bottom: -20%` e `will-change: transform`
- [x] Overlay topo e `rgba(14,14,14,.55)` — mais denso que o original .4
- [x] `.hero-logo img` tem dois drop-shadow aplicados via filter
- [x] `overflow: hidden` em `#hero` preservado — parallax nao vaza visualmente

## Deviations from Plan

None — plano executado exatamente como especificado.

## Self-Check: PASSED

- `index.html` existe e contem `foto-21.png` e `top: -20%`
- Commits 7e02460 e 47d35a9 confirmados no log
