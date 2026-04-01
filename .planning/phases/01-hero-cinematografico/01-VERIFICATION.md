---
phase: 01-hero-cinematografico
verified: 2026-04-01T22:10:00Z
status: human_needed
score: 6/6 must-haves verified (automated)
human_verification:
  - test: "Abrir index.html no Chrome desktop e verificar foto de ambiente visível no hero"
    expected: "foto-21.png aparece como fundo do hero — ambiente da loja visível, não fundo preto"
    why_human: "Renderização visual de imagem não é verificável por grep"
  - test: "Rolar lentamente para baixo com o hero visível"
    expected: "A foto de fundo se move mais devagar que o conteúdo (efeito parallax perceptível)"
    why_human: "Comportamento de scroll e percepção de profundidade requer visualização em browser"
  - test: "Recarregar a página (Ctrl+Shift+R) e observar a entrada dos elementos"
    expected: "hero-line, hero-logo, eyebrow, h1, sub, cta-wrap e hero-scroll entram suavemente via fadeUp"
    why_human: "Animações CSS não são verificáveis estaticamente — requerem execução"
  - test: "Verificar o scroll indicator na parte inferior do hero"
    expected: "Linha dourada pulsante visível com texto SCROLL abaixo do conteúdo principal"
    why_human: "Visibilidade e elegância do elemento são qualidades visuais"
  - test: "Ativar emulação mobile no DevTools (ex: iPhone 12 Pro) e recarregar"
    expected: "Hero exibe foto estática sem jank; parallax NÃO aplicado (isTouch.matches = true)"
    why_human: "Comportamento de matchMedia em touch emulado requer execução no browser"
---

# Phase 01: Hero Cinematografico — Verification Report

**Phase Goal:** O visitante sente o nivel de sofisticacao da marca nos primeiros 3 segundos — hero com foto de ambiente real, parallax e animacoes imersivas
**Verified:** 2026-04-01T22:10:00Z
**Status:** HUMAN_NEEDED — todos os checks automatizados passaram; 5 itens requerem confirmacao visual
**Re-verification:** Nao — verificacao inicial

---

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | O hero exibe foto-21.png como fundo — nao mais logo-bg-preta.jpg | VERIFIED | `index.html:71` — `url('assets/foto-21.png') center/cover no-repeat`; sem nenhuma ocorrencia de `logo-bg-preta` no arquivo |
| 2 | O overlay escuro e mais denso no topo (.55) para cobrir conteudo da foto sobre a nav | VERIFIED | `index.html:67` — `rgba(14,14,14,.55) 0%`; `index.html:68` — `rgba(14,14,14,.65) 60%` |
| 3 | O .hero-bg tem top:-20% e bottom:-20% para nao descobrir bordas durante o parallax | VERIFIED | `index.html:64` — `top: -20%; bottom: -20%; left: 0; right: 0` |
| 4 | A logo dourada tem dois drop-shadows: halo dourado + shadow escuro de separacao | VERIFIED | `index.html:88-89` — dois `drop-shadow()` encadeados no `filter` |
| 5 | O parallax script usa requestAnimationFrame + ticking e move .hero-bg ao scroll | VERIFIED | `index.html:932-948` — script completo com `heroBg.style.transform = 'translateY(...)` |
| 6 | Em touch devices (hover:none) o parallax e desativado | VERIFIED | `index.html:935,941` — `isTouch.matches` guarda a transformacao dentro do rAF |

**Score:** 6/6 truths verificadas automaticamente

---

### Required Artifacts

| Artifact | Fornece | Status | Detalhes |
|----------|---------|--------|----------|
| `index.html` | CSS .hero-bg com foto-21.png, overlay recalibrado, margens de parallax, will-change | VERIFIED | Linhas 62-73: bloco completo presente e correto |
| `index.html` | CSS .hero-logo img com drop-shadow duplo | VERIFIED | Linhas 85-90: dois drop-shadow encadeados |
| `index.html` | Script parallax com requestAnimationFrame | VERIFIED | Linhas 932-948: script completo |
| `assets/foto-21.png` | Foto de ambiente real referenciada | VERIFIED | Arquivo existe em `assets/foto-21.png` (confirmado via ls) |

---

### Key Link Verification

| De | Para | Via | Status | Detalhes |
|----|------|-----|--------|----------|
| `.hero-bg` CSS | `assets/foto-21.png` | `url()` no background shorthand | WIRED | `index.html:71` — `url('assets/foto-21.png')` exato |
| `.hero-logo img` CSS | drop-shadow duplo | propriedade `filter` | WIRED | `index.html:87-89` — `filter:` com dois `drop-shadow()` encadeados |
| `window scroll listener` | `.hero-bg style.transform` | requestAnimationFrame + ticking pattern | WIRED | `index.html:933,942` — `heroBg.style.transform = 'translateY(...)` dentro do rAF |
| `matchMedia('(hover: none)')` | parallax desativado em touch | `isTouch.matches` check dentro do rAF | WIRED | `index.html:935,941` — `isTouch.matches` verificado antes de aplicar transform |

---

### Requirements Coverage

| Requisito | Plano | Descricao | Status | Evidencia |
|-----------|-------|-----------|--------|-----------|
| HERO-01 | 01-01, 01-02 | Hero exibe foto de ambiente de fundo com efeito parallax ao scroll | SATISFIED | foto-21.png no CSS + script parallax completo |
| HERO-02 | 01-01 | Overlay escuro graduado mantem legibilidade do texto sobre a foto | SATISFIED | Gradiente rgba(.55) -> rgba(.65) -> rgba(1) em index.html:66-70 |
| HERO-03 | 01-01 | Logo dourada centralizada com drop-shadow sutil | SATISFIED | Dois drop-shadow em index.html:87-89; .hero-logo centralizado por flexbox |
| HERO-04 | 01-02 | Animacoes de entrada suaves (fadeUp) preservadas | SATISFIED | fadeUp declarado em index.html:475; aplicado em hero-line, hero-logo, eyebrow, h1, sub, cta-wrap, hero-scroll (linhas 78, 83, 95, 102, 109, 114, 133) |
| HERO-05 | 01-02 | Indicador de scroll animado visivel e elegante | SATISFIED | `.hero-scroll` com `.scroll-line` em index.html:130-140, 556-558; animacao `pulse 2s infinite` |

**Todos os 5 requisitos da fase verificados — sem orfaos.**

Requisitos declarados nos PLANs: HERO-01, HERO-02, HERO-03 (01-01) + HERO-01, HERO-04, HERO-05 (01-02).
Uniao: HERO-01, HERO-02, HERO-03, HERO-04, HERO-05 — exatamente os 5 mapeados para Phase 1 em REQUIREMENTS.md.

---

### Anti-Patterns Found

| Arquivo | Linha | Padrao | Severidade | Impacto |
|---------|-------|--------|------------|---------|
| `index.html` | 350 | `url('assets/foto-21.png') ... fixed` em bloco de media query | Info | Background fixo em outro elemento (secao sobre?) — nao no hero; nao afeta o parallax do hero |

Nenhum anti-pattern bloqueante encontrado.
- Sem referencias a `logo-bg-preta.jpg`
- Sem stubs (`return null`, `TODO`, `FIXME`, `PLACEHOLDER`) relacionados ao hero
- Sem handlers vazios
- `overflow: hidden` em `#hero` preservado (linha 60) — parallax nao vaza

---

### Human Verification Required

#### 1. Foto de ambiente visivel no hero

**Test:** Abrir `index.html` no Chrome desktop
**Expected:** O hero mostra a foto de ambiente (foto-21.png) — loja visivel, nao fundo preto
**Why human:** Renderizacao visual de imagem nao e verificavel por grep

#### 2. Efeito parallax perceptivel

**Test:** Com a pagina aberta, rolar lentamente para baixo com o hero visivel
**Expected:** A foto de fundo se move mais devagar que o conteudo do hero (profundidade cinematografica)
**Why human:** Comportamento de scroll e percepcao visual requerem execucao no browser

#### 3. Animacoes fadeUp na entrada

**Test:** Recarregar a pagina (Ctrl+Shift+R) e observar a entrada dos elementos
**Expected:** hero-line, hero-logo, eyebrow, h1, sub, cta-wrap e hero-scroll entram sequencialmente com fadeUp suave (delays de .1s a 1.2s)
**Why human:** Animacoes CSS nao sao verificaveis estaticamente

#### 4. Scroll indicator visivel

**Test:** Apos o carregamento completo, verificar a parte inferior do hero
**Expected:** Linha dourada pulsante visivel com texto "SCROLL" — elegante e nao intrusiva
**Why human:** Visibilidade e qualidade estetica do elemento requerem visualizacao

#### 5. Parallax desativado em touch (sem jank)

**Test:** DevTools > Toggle device toolbar > iPhone 12 Pro > Ctrl+Shift+R
**Expected:** Hero exibe foto estatica, sem movimento ao scroll — sem jank, sem parallax
**Why human:** Comportamento de `matchMedia('hover:none')` em emulacao requer execucao no browser

---

### Observacao: background fixed em linha 350

Durante a verificacao foi encontrado `url('assets/foto-21.png') ... fixed` na linha 350, que parece ser um background com `background-attachment: fixed` em outra secao (possivelmente a secao "sobre" ou um parallax CSS alternativo). Isso nao afeta o hero — o hero usa o script JS com translateY — mas pode causar problemas em iOS Safari em outras secoes. Nao e um bloqueio para a Phase 1.

---

### Gaps Summary

Nenhum gap encontrado. Todos os must-haves da fase estao implementados e conectados corretamente no codigo.

O status `human_needed` reflete apenas que a qualidade visual e cinematografica do resultado (profundidade do parallax, suavidade das animacoes, legibilidade do texto sobre a foto) nao pode ser confirmada programaticamente — requer inspecao visual no browser.

---

_Verified: 2026-04-01T22:10:00Z_
_Verifier: Claude (gsd-verifier)_
