# Phase 3: Tipografia e Responsividade - Context

**Gathered:** 2026-04-01
**Status:** Ready for planning

<domain>
## Phase Boundary

Unificar hierarquia tipográfica em todas as seções e garantir experiência mobile completa: menu hambúrguer funcional, formulário usável sem zoom, parallax degradado graciosamente, body text consistente. Novas seções e troca de identidade visual estão fora do escopo.

</domain>

<decisions>
## Implementation Decisions

### Menu hambúrguer (criação do zero)
- Botão: 3 linhas minimalistas em var(--dourado) — sem ícone de emoji, sem texto
- Comportamento ao abrir: overlay full-screen (#0E0E0E ou próximo), links centralizados na tela
- Ao clicar em link: fechar overlay, rolar suavemente até a seção (smooth scroll)
- O botão hambúrguer aparece a partir de 1200px (breakpoint onde `.nav-links` some)
- Implementação: vanilla JS + CSS, zero dependências

### Formulário de contato — iOS zoom fix
- Aumentar font-size dos inputs de 13px para 16px no mobile
- Evita o zoom automático do iOS Safari ao focar em campos de texto
- Aplicar em `input`, `textarea`, `select` dentro de `#contato`

### Parallax no mobile
- Fundo hero: `background-position: center center` estático — sem movimento
- JS do parallax já para via `isTouch` (`matchMedia('(hover: none)')`) — não precisa de novo código JS
- Remover ou neutralizar o `top: -20%; height: 140%` do `.hero-bg` em touch (esses valores existem para dar margem ao parallax — no mobile, fundo estático pode usar `top: 0; height: 100%`)
- Altura do hero: trocar `height: 100vh` por `height: 100svh` no mobile — evita overflow atrás da barra do Safari no iOS 15.4+

### Body text — padronização
- Tamanho: padronizar body text em **13px** em todas as seções principais
  - `.sobre-txt`: 13.5px → 13px
  - `.dif p`: 12.5px → 13px
  - `.pilar-d`: 11.5px → 13px
  - `.contato-txt`: 13px → manter
  - `.footer-col a`: 12.5px → 13px
- Line-height: padronizar em **1.9** em todo body text
  - `.sobre-txt`: 2.1 → 1.9
  - `.contato-txt`: 2.1 → 1.9
  - `.dif p`: 1.9 → manter
- Letter-spacing: manter como está — variações por tipo de elemento são intencionais

### Tamanho mínimo de texto no mobile
- Body text mínimo: **14px** no mobile (via @media max-width:700px)
- Headings secundários (.pilar-t 20px, .dif h3 23px, .dest-title 26px): Claude decide caso a caso se algo quebrar no mobile

### Claude's Discretion
- Valor exato do padding/gap no overlay do menu mobile
- Velocidade da animação de abertura/fechamento do menu
- Headings secundários no mobile: ajustar apenas os que visualmente quebrarem linha

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `isTouch` via `matchMedia('(hover: none)')`: já no código (parallax + labels touch) — reusar para o menu hambúrguer também
- `.nav-links { display: none }` a partir de 1200px: ponto de inserção do hambúrguer
- `scroll-behavior: smooth` não existe no CSS atual — adicionar ao `html {}` ou usar `scrollIntoView({ behavior: 'smooth' })` no JS

### Established Patterns
- Breakpoints: `@media(max-width:1200px)` (tablet) e `@media(max-width:700px)` (mobile)
- Detecção touch: `matchMedia('(hover: none)')` — padrão da Fase 1
- Animações: `transition` CSS-only em geral, JS para comportamentos complexos (parallax)
- Cores: var(--preto) #0E0E0E, var(--dourado) #C9A96E, var(--offwhite) #F2EFE9

### Integration Points
- `<nav id="nav">`: adicionar botão hambúrguer e overlay de menu mobile
- `.hero-bg`: ajustar `top`/`height` em `@media (hover: none)` para fundo estático
- `.hero` ou `#hero`: trocar `height: 100vh` → `100svh` no breakpoint mobile
- `#contato` inputs: aumentar font-size para 16px em `@media(max-width:700px)`
- Body text classes: `.sobre-txt`, `.dif p`, `.pilar-d` — alterar font-size e line-height

</code_context>

<specifics>
## Specific Ideas

- O overlay do menu deve ser consistente com a estética do hero: fundo muito escuro (#0E0E0E), links em Cormorant Garamond ou Montserrat uppercase, dourado como accent
- 100svh é a solução moderna para o problema clássico do iOS — vale a pena usar com fallback `100vh` para browsers mais antigos

</specifics>

<deferred>
## Deferred Ideas

- Nenhuma ideia fora do escopo surgiu durante a discussão

</deferred>

---

*Phase: 03-tipografia-e-responsividade*
*Context gathered: 2026-04-01*
