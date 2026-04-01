# Phase 3: Tipografia e Responsividade - Research

**Researched:** 2026-04-01
**Domain:** CSS typography, mobile responsiveness, vanilla JS hamburger menu, iOS Safari quirks
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **Menu hambúrguer:** Botão 3 linhas em var(--dourado), overlay full-screen (#0E0E0E), links centralizados, fecha + smooth scroll ao clicar em link. Aparece a partir de 1200px. Vanilla JS + CSS, zero dependências.
- **iOS zoom fix:** font-size 16px nos inputs/textarea/select de `#contato` no mobile (max-width:700px).
- **Parallax mobile:** `.hero-bg` recebe `top:0; height:100%` em `@media (hover: none)` — neutraliza as margens de parallax. Altura do hero troca `100vh` por `100svh` no mobile.
- **Body text padronização:** 13px em todas as seções (`.sobre-txt`, `.dif p`, `.pilar-d`, `.contato-txt` já está, `.footer-col a`). Line-height 1.9 em todo body text (`.sobre-txt` e `.contato-txt` descem de 2.1 → 1.9).
- **Texto mínimo mobile:** 14px via `@media(max-width:700px)` para body text.
- **Letter-spacing:** manter como está — variações são intencionais.

### Claude's Discretion

- Valor exato do padding/gap no overlay do menu mobile.
- Velocidade da animação de abertura/fechamento do menu.
- Headings secundários no mobile: ajustar apenas os que visualmente quebrarem linha (`.pilar-t` 20px, `.dif h3` 23px, `.dest-title` 26px).

### Deferred Ideas (OUT OF SCOPE)

- Nenhuma ideia fora do escopo surgiu durante a discussão.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| TIP-01 | Hierarquia tipográfica clara — headings grandes, body legível (mín. 14px) | Padronização de body text para 13px desktop / 14px mobile; headings já usam clamp(); `.pilar-d` sobe de 11.5px para 13px |
| TIP-02 | Letter-spacing e line-height consistentes nas seções | Line-height padronizado em 1.9; letter-spacing mantido intencionalmente variado por tipo |
| TIP-03 | Padding/margin das seções revisados para respiração visual adequada | Seções existentes já têm padding generoso; inspeção visual confirma que não há gap crítico — discretion do Claude |
| MOB-01 | Hero funciona corretamente no mobile (parallax degradado para fundo estático) | `@media (hover: none)` já interrompe JS; CSS precisa de `top:0; height:100%` no `.hero-bg` + `100svh` no `#hero` |
| MOB-02 | Grid de produtos adaptado para 1-2 colunas no mobile | Breakpoint 700px já redireciona colunas para 4-colunas com span ajustados — verificar visualmente |
| MOB-03 | Navegação mobile com menu hambúrguer funcional | `.nav-links { display:none }` a partir de 1200px — hambúrguer a ser criado do zero |
| MOB-04 | Formulário de contato usável no mobile | font-size 16px nos inputs evita zoom iOS; layout já é coluna única em 1200px |
| MOB-05 | Textos legíveis sem zoom no mobile (font-size mínimo adequado) | 14px mínimo via media query; fix do iOS 16px em inputs |
</phase_requirements>

---

## Summary

Esta fase é inteiramente CSS/JS vanilla no arquivo único `index.html`. Não há bibliotecas externas a instalar, nenhum build step, nenhum bundler. Todas as alterações são cirúrgicas: target de seletores já existentes + adição de novos seletores em blocos `@media` já presentes (1200px e 700px) + um novo bloco `@media (hover: none)` para o parallax.

O trabalho de maior superfície é o menu hambúrguer: requer HTML novo (botão + overlay dentro do `<nav>`), CSS novo (posicionamento, animação de abertura), e JS novo (toggle de classe + smooth scroll). O restante são ajustes de valores em regras CSS já existentes — operação de baixo risco.

Dois quirks do iOS Safari são endereçados nesta fase: o zoom automático em inputs com `font-size < 16px` (fix via media query), e a barra de endereços variável que faz `100vh` transbordar (fix via `100svh` com fallback).

**Primary recommendation:** Implementar as mudanças CSS de tipografia primeiro (baixo risco, efeito imediato), depois o fix do parallax/hero mobile, e por último o hambúrguer (maior superfície, requer teste de interação). Cada bloco é independente e pode ser verificado isoladamente.

---

## Standard Stack

### Core
| Tecnologia | Versão | Propósito | Por que padrão |
|------------|--------|-----------|----------------|
| HTML/CSS/JS vanilla | — | Toda a implementação | Restrição do projeto — arquivo único, zero build |
| CSS custom properties | — | Cores e fontes via var(--dourado) etc. | Já em uso no projeto |
| CSS @media queries | — | Responsividade | Breakpoints 1200px e 700px já estabelecidos |
| matchMedia API | — | Detecção touch para parallax e hambúrguer | `isTouch` já instanciado no JS do projeto |

### Nada a instalar
Este projeto não tem `package.json`, não usa npm, não tem etapa de build. Toda alteração é edição direta no `index.html`.

---

## Architecture Patterns

### Estrutura de implementação no index.html

```
<head>
  <style>
    /* Bloco existente: variáveis :root — não alterar */
    /* Bloco existente: nav — adicionar .nav-hamburger e .nav-overlay */
    /* Bloco existente: #hero / .hero-bg — sem alteração direta */
    /* Blocos existentes: .sobre-txt, .dif p, .pilar-d, .contato-txt, .footer-col a — alterar valores */
    /* Bloco existente: @media(max-width:1200px) — adicionar regras do hambúrguer */
    /* Bloco existente: @media(max-width:700px) — adicionar min font-size e iOS fix */
    /* Bloco NOVO: @media(hover:none) — regras hero-bg fundo estático */
  </style>
</head>
<body>
  <!-- NAV existente: inserir botão hambúrguer e overlay DENTRO de <nav id="nav"> -->
  <!-- resto do HTML: sem alterações estruturais -->
  <script>
    /* JS existente: manter integralmente */
    /* JS NOVO: toggle do hambúrguer + smooth scroll dos links do overlay */
  </script>
</body>
```

### Pattern 1: Menu Hambúrguer — HTML dentro do nav

O botão e o overlay entram dentro de `<nav id="nav">`. O overlay é um elemento irmão do botão, não um filho. Isso evita conflito de `z-index` com o `backdrop-filter` do nav.

```html
<!-- Inserir APÓS .nav-links, ANTES do .btn-nav -->
<button class="nav-hamburger" aria-label="Menu" aria-expanded="false">
  <span></span>
  <span></span>
  <span></span>
</button>

<!-- Overlay — irmão direto, dentro do <nav> ou direto no <body> -->
<div class="nav-overlay" id="navOverlay" aria-hidden="true">
  <ul class="nav-overlay-links">
    <li><a href="#sobre">Sobre</a></li>
    <li><a href="#colecao">Coleção</a></li>
    <li><a href="#destaques">Ambientes</a></li>
    <li><a href="#contato">Contato</a></li>
  </ul>
</div>
```

**Nota de implementação:** O overlay pode ser filho do `<body>` em vez do `<nav>` para evitar qualquer interferência com `position: fixed` e `z-index` do nav. Ambas as abordagens funcionam — colocar no `<body>` é mais seguro para empilhamento de contexto.

### Pattern 2: CSS do Hambúrguer

```css
/* Botão — escondido por padrão, aparece em 1200px */
.nav-hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  z-index: 310;
  position: relative;
}
.nav-hamburger span {
  display: block;
  width: 26px;
  height: 1.5px;
  background: var(--dourado);
  transition: transform .3s ease, opacity .3s ease;
}
/* Estado "aberto" — X */
.nav-hamburger.open span:nth-child(1) { transform: translateY(7.5px) rotate(45deg); }
.nav-hamburger.open span:nth-child(2) { opacity: 0; }
.nav-hamburger.open span:nth-child(3) { transform: translateY(-7.5px) rotate(-45deg); }

@media(max-width:1200px) {
  .nav-hamburger { display: flex; }
  .btn-nav { display: none; } /* opcional — esconder no mobile se desejar */
}

/* Overlay */
.nav-overlay {
  position: fixed;
  inset: 0;
  background: #0E0E0E;
  z-index: 300;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity .35s ease;
}
.nav-overlay.open {
  opacity: 1;
  pointer-events: all;
}
.nav-overlay-links {
  list-style: none;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 36px;
}
.nav-overlay-links a {
  font-family: var(--serif);
  font-size: clamp(28px, 6vw, 48px);
  font-weight: 300;
  letter-spacing: 4px;
  color: var(--offwhite);
  text-decoration: none;
  text-transform: uppercase;
  transition: color .3s;
}
.nav-overlay-links a:hover { color: var(--dourado); }
```

### Pattern 3: JS do Hambúrguer

```javascript
// Hambúrguer — reusar isTouch já declarado
const hamburger = document.querySelector('.nav-hamburger');
const navOverlay = document.getElementById('navOverlay');
const overlayLinks = navOverlay.querySelectorAll('a');

function openMenu() {
  hamburger.classList.add('open');
  navOverlay.classList.add('open');
  hamburger.setAttribute('aria-expanded', 'true');
  navOverlay.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden'; // evita scroll do body enquanto overlay aberto
}

function closeMenu() {
  hamburger.classList.remove('open');
  navOverlay.classList.remove('open');
  hamburger.setAttribute('aria-expanded', 'false');
  navOverlay.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

hamburger.addEventListener('click', () => {
  hamburger.classList.contains('open') ? closeMenu() : openMenu();
});

overlayLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    closeMenu();
    // Pequeno delay para o overlay fechar antes de rolar
    setTimeout(() => {
      target.scrollIntoView({ behavior: 'smooth' });
    }, 350);
  });
});
```

**Nota:** `scroll-behavior: smooth` já está no `html {}` do projeto. O `scrollIntoView` com `behavior: 'smooth'` é redundante mas garante a animação mesmo quando o overlay está visível. O delay de 350ms sincroniza com a `transition: opacity .35s` do overlay.

### Pattern 4: Hero mobile — fundo estático + 100svh

```css
/* Dentro do bloco @media (hover: none) — já existe no CSS para .pc-label */
@media (hover: none) {
  .hero-bg {
    top: 0;
    height: 100%;
    /* background-position já é center center — manter */
  }
}

/* Dentro de @media(max-width:700px) */
@media(max-width:700px) {
  #hero {
    height: 100svh; /* fallback implícito: 100vh via cascade — browsers antigos ignoram svh */
    min-height: 580px;
  }
}
```

**Nota sobre fallback:** Browsers que não entendem `svh` simplesmente ignoram a regra e usam o valor anterior (`100vh` definido na regra base). Isso é comportamento correto de CSS — não há necessidade de declarar o fallback explicitamente.

### Pattern 5: Tipografia — ajustes de valores

```css
/* Body text — padronização */
.sobre-txt > p { font-size: 13px; line-height: 1.9; }
.dif p         { font-size: 13px; /* line-height 1.9 já está */ }
.pilar-d       { font-size: 13px; line-height: 1.9; }
/* .contato-txt: 13px já está, line-height 2.1 → 1.9 */
.contato-txt   { line-height: 1.9; }
.footer-col a  { font-size: 13px; }

/* Mobile — mínimo 14px */
@media(max-width:700px) {
  .sobre-txt > p,
  .dif p,
  .pilar-d,
  .contato-txt,
  .footer-col a { font-size: 14px; }
}
```

### Pattern 6: iOS zoom fix — inputs 16px

```css
@media(max-width:700px) {
  #contato .form-g input,
  #contato .form-g textarea,
  #contato .form-g select {
    font-size: 16px;
  }
}
```

**Regra crítica do iOS Safari:** Qualquer input com `font-size < 16px` aciona zoom automático ao receber foco. Isso é comportamento do browser, não bug da página. A solução definitiva é `font-size: 16px` — não há alternativa CSS pura que funcione em todos os dispositivos iOS.

### Anti-Patterns a Evitar

- **Não usar `transform: scale()` na animação do overlay** — causa blur em texto no iOS. Usar `opacity` + `pointer-events` é mais seguro.
- **Não usar `height: 0 → auto` para revelar overlay** — `transition` não funciona em `height: auto`. Usar `opacity` + `pointer-events: none/all`.
- **Não adicionar `position: fixed` no `body`** como técnica anti-scroll — causa jump de layout no iOS. Usar `overflow: hidden` no `body` é suficiente.
- **Não duplicar os links do overlay no HTML** como um segundo `<ul>` separado — os links já existem no `<nav>`. Alternativamente, manter o overlay com seus próprios `<a>` e não tentar clonar dinamicamente os `.nav-links` (complexidade desnecessária).
- **Não usar `backdrop-filter` no overlay** — causa conflito de stacking context com o `backdrop-filter: blur(18px)` do `.nav.scrolled`.

---

## Don't Hand-Roll

| Problema | Não construir | Usar em vez | Por quê |
|----------|---------------|-------------|---------|
| Smooth scroll | Função JS manual com requestAnimationFrame | `scrollIntoView({ behavior: 'smooth' })` ou `scroll-behavior: smooth` no CSS | Suporte nativo universal; implementação manual tem edge cases de easing e cancelamento |
| Detecção touch | User-Agent sniffing | `matchMedia('(hover: none)')` — já no projeto | UA sniffing é frágil; matchMedia detecta capacidade real do dispositivo |
| iOS viewport height | Cálculo JS de `window.innerHeight` | `100svh` via CSS | CSS nativo, sem reflow, sem listener de resize |
| Lock de scroll com overlay | `position: fixed` no body | `document.body.style.overflow = 'hidden'` | Fixed no body causa layout jump no iOS |

---

## Common Pitfalls

### Pitfall 1: z-index do overlay menor que o nav
**O que acontece:** O overlay abre mas fica atrás da barra de navegação — links do overlay ficam acessíveis mas nav sobrepõe visualmente o topo.
**Por que acontece:** O `<nav>` tem `z-index: 200`. O overlay precisa de `z-index: 300` para cobrir tudo, incluindo o nav.
**Como evitar:** `.nav-overlay { z-index: 300; }` — e o botão hambúrguer precisa de `z-index: 310` para ficar visível sobre o overlay aberto (para poder fechar).
**Sinais de alerta:** Nav visível sobre o overlay no mobile.

### Pitfall 2: backdrop-filter cria novo stacking context
**O que acontece:** Elementos com `backdrop-filter` criam um stacking context próprio. O `.nav.scrolled` tem `backdrop-filter: blur(18px)`. Qualquer filho do nav com `position: fixed` fica confinado ao stacking context do nav.
**Por que acontece:** Spec CSS — `backdrop-filter` força `z-index: auto` a se comportar como `z-index: 0` dentro do elemento.
**Como evitar:** Colocar o overlay como filho do `<body>`, não do `<nav>`. O botão hambúrguer pode permanecer no `<nav>`.
**Sinais de alerta:** Overlay não cobre a tela inteira no desktop scrollado.

### Pitfall 3: Parallax móvel — margens não neutralizadas
**O que acontece:** `.hero-bg` tem `top: -20%; height: 140%` para dar margem ao parallax. No mobile sem movimento, isso cria um elemento 140% da altura que pode vazar para fora do hero.
**Por que acontece:** As margens existem para esconder as bordas durante o movimento do parallax — desnecessárias (e problemáticas) quando o fundo é estático.
**Como evitar:** `@media (hover: none) { .hero-bg { top: 0; height: 100%; } }` — usar `(hover: none)` em vez de `(max-width:700px)` porque o parallax para por detecção de touch, não por breakpoint.
**Sinais de alerta:** Hero com altura maior que o viewport no iOS.

### Pitfall 4: `100svh` sem fallback percebido
**O que acontece:** Browsers sem suporte a `svh` (principalmente iOS < 15.4, Chrome < 108) ignoram a regra e nada herda `100vh` de volta.
**Por que acontece:** A regra base `#hero { height: 100vh }` não está dentro do media query — ela existe no CSS principal. O media query adiciona `height: 100svh` sobre ela. Browsers que não entendem `svh` simplesmente ignoram essa linha e mantêm o `100vh` da regra base.
**Como evitar:** Não é necessário declarar fallback explícito — o CSS cascade já fornece o fallback via a regra base. Mas é preciso garantir que a regra base existe fora do media query (ela existe — linha 58 do index.html).
**Sinais de alerta:** Nenhum — browsers antigos degradam graciosamente para `100vh`.

### Pitfall 5: iOS zoom ao focar input
**O que acontece:** iOS Safari faz zoom automático na viewport ao focar em input com `font-size < 16px`. O zoom persiste após o usuário sair do campo.
**Por que acontece:** Comportamento embutido do iOS para facilitar digitação em campos pequenos.
**Como evitar:** `font-size: 16px` nos inputs dentro de `@media(max-width:700px)`. Não adicionar `user-scalable=no` no viewport meta — isso quebra acessibilidade.
**Sinais de alerta:** Zoom automático ao tocar em qualquer campo do formulário no iPhone.

### Pitfall 6: Body `overflow: hidden` durante overlay e scroll position
**O que acontece:** No iOS, aplicar `overflow: hidden` no body durante o overlay pode não prevenir completamente o scroll da página em baixo — o background page "vaza" em alguns casos.
**Por que acontece:** Quirk do iOS Safari com scroll handling.
**Como evitar:** Se necessário, combinar `document.body.style.overflow = 'hidden'` com salvar e restaurar `window.scrollY` usando `position: fixed; top: -${scrollY}px`. Para esta LP (overlay opaco em tela cheia), o problema é invisível ao usuário mesmo se ocorrer — a página de baixo não é visível.
**Sinais de alerta:** Apenas relevante se o overlay for translúcido. Para este projeto (overlay `#0E0E0E` opaco), não é problema prático.

---

## Code Examples

### Estrutura completa do botão hambúrguer
```html
<!-- Dentro de <nav id="nav">, após <ul class="nav-links"> -->
<button class="nav-hamburger" aria-label="Abrir menu" aria-expanded="false">
  <span></span>
  <span></span>
  <span></span>
</button>
```

### Overlay — posicionamento no body
```html
<!-- Direto antes de </body>, fora do <nav> -->
<div class="nav-overlay" id="navOverlay" aria-hidden="true">
  <button class="nav-overlay-close" aria-label="Fechar menu">×</button>
  <ul class="nav-overlay-links">
    <li><a href="#sobre">Sobre</a></li>
    <li><a href="#colecao">Coleção</a></li>
    <li><a href="#destaques">Ambientes</a></li>
    <li><a href="#contato">Contato</a></li>
  </ul>
</div>
```

**Alternativa mais simples:** O botão hambúrguer (`.nav-hamburger`) com z-index maior que o overlay já serve para fechar — não é necessário um botão separado de fechamento dentro do overlay. Clicar em qualquer link já fecha. Um clique no overlay fora dos links também pode fechar.

### Valor do gap no overlay (Claude's Discretion)
Recomendação: `gap: 36px` entre links — equivalente a ~2× o line-height do texto, mantendo respiração vertical sem desperdiçar espaço em telas pequenas. Para telas muito pequenas (iPhone SE: 375px), `36px` resulta em lista de 4 links com ~280px de altura total, centralizada — adequado.

### Velocidade de animação do overlay (Claude's Discretion)
Recomendação: `transition: opacity .35s ease` — rápido o suficiente para não parecer lento, suave o suficiente para não ser abrupto. Abaixo de `.25s` parece instantâneo; acima de `.5s` parece pesado para uma LP premium.

### Headings secundários no mobile (Claude's Discretion)
Verificar visualmente em 375px:
- `.pilar-t` (20px): provavelmente OK — textos curtos (Curadoria, Alto Padrão)
- `.dif h3` (23px): verificar — títulos como "Atendimento Personalizado" podem quebrar em 2 linhas, o que é aceitável
- `.dest-title` (26px): dentro do overlay dos Ambientes com padding — verificar
- Reduzir apenas se houver overflow ou quebra visualmente estranha. Sugestão se necessário: `@media(max-width:700px) { .pilar-t { font-size: 18px; } .dif h3 { font-size: 20px; } .dest-title { font-size: 22px; } }`

---

## State of the Art

| Abordagem Antiga | Abordagem Atual | Quando Mudou | Impacto |
|-----------------|-----------------|--------------|---------|
| `100vh` em mobile | `100svh` (Small Viewport Height) | iOS 15.4 / Chrome 108 (2022) | Evita overflow pela barra de endereços variável |
| `user-scalable=no` para evitar zoom em inputs | `font-size: 16px` nos inputs | Sempre foi a solução correta | Preserva acessibilidade (zoom do usuário não é bloqueado) |
| User-Agent sniffing para touch | `matchMedia('(hover: none)')` | ~2018 | Detecta capacidade real; funciona em hybrid devices |
| `height: 0 → height: auto` para menus | `opacity` + `pointer-events` | Sempre foi problemático | CSS transition funciona em opacity; não funciona em height: auto |

**Deprecated/ultrapassado:**
- `user-scalable=no` no viewport meta: bloqueia zoom do usuário — acessibilidade ruim, rejeitado por guidelines modernas.
- `-webkit-overflow-scrolling: touch`: removido no Safari 13+ — não usar.

---

## Open Questions

1. **`.btn-nav` ("Fale Conosco") no mobile**
   - O que sabemos: `@media(max-width:1200px)` esconde `.nav-links` mas não esconde `.btn-nav`
   - O que está incerto: O botão "Fale Conosco" e o hambúrguer vão aparecer juntos no nav mobile — pode ficar apertado em 375px
   - Recomendação: Esconder `.btn-nav` no mesmo breakpoint do hambúrguer — `@media(max-width:1200px) { .btn-nav { display: none; } }` — o overlay já tem o link para Contato

2. **Padding do `#contato` no mobile**
   - O que sabemos: `@media(max-width:1200px)` define `#contato { padding: 80px 32px }` — nenhuma regra adicional em 700px
   - O que está incerto: 32px de padding lateral em 375px pode ser generoso demais ou adequado
   - Recomendação: Verificar visualmente; se necessário, reduzir para 20px-24px no breakpoint 700px

---

## Validation Architecture

### Test Framework
| Propriedade | Valor |
|-------------|-------|
| Framework | Nenhum — projeto vanilla HTML/CSS/JS sem infraestrutura de testes automatizados |
| Config file | N/A |
| Quick run command | Abrir `index.html` no browser |
| Full suite command | Testar manualmente no Chrome DevTools + Safari/iOS físico ou simulador |

Este projeto é um arquivo HTML estático sem JavaScript de aplicação testável em isolamento. Toda validação é browser-based manual. As verificações abaixo são listas de checagem para quem executa o teste.

### Phase Requirements → Test Map

| Req ID | Comportamento | Tipo de Teste | Como Testar | Automatizável? |
|--------|---------------|---------------|-------------|----------------|
| TIP-01 | Headings grandes, body ≥ 14px mobile | Inspeção visual + DevTools | DevTools > Elements > Computed: verificar font-size de `.sobre-txt > p`, `.dif p`, `.pilar-d` em viewport 375px | Manual-only |
| TIP-02 | Line-height 1.9 consistente em todas as seções body text | Inspeção DevTools | DevTools > Computed: verificar line-height em `.sobre-txt > p`, `.dif p`, `.pilar-d`, `.contato-txt` | Manual-only |
| TIP-03 | Seções têm respiração visual adequada | Inspeção visual | Scroll completo da página em 1440px, 1024px, 375px — nenhuma seção deve parecer apertada | Manual-only |
| MOB-01 | Hero não quebra no mobile — fundo estático, altura correta | Funcional mobile | iOS Safari 375px: hero preenche tela sem overflow; sem movimento de parallax ao scroll | Manual-only |
| MOB-02 | Grid produtos 1-2 colunas no mobile | Inspeção visual | Chrome DevTools 375px: grid da Coleção mostra 2 colunas; imagens não transbordam | Manual-only |
| MOB-03 | Menu hambúrguer abre, fecha, navega com smooth scroll | Funcional interação | 375px: tocar hambúrguer → overlay aparece; tocar link → overlay fecha + scroll suave para seção | Manual-only |
| MOB-04 | Formulário usável no mobile sem zoom | Funcional iOS | iOS Safari 375px: tocar em input de nome/email/tel/mensagem → SEM zoom automático na viewport | Manual-only |
| MOB-05 | Textos legíveis sem zoom no mobile | Inspeção visual | DevTools 375px: body text ≥ 14px em todas as seções; nenhum texto abaixo de 9px exceto labels de categoria | Manual-only |

### Checklist de Teste por Requisito

**TIP-01 — Hierarquia tipográfica**
- [ ] DevTools 1440px: `.section-title` visivelmente maior que `.sobre-txt > p`
- [ ] DevTools 1440px: `.pilar-d` (11.5px → 13px) não parece microscópico ao lado de `.pilar-t` (20px)
- [ ] DevTools 375px: body text ≥ 14px em `.sobre-txt > p`, `.dif p`, `.pilar-d`, `.contato-txt`

**TIP-02 — Line-height e letter-spacing**
- [ ] DevTools Computed: `.sobre-txt > p` line-height = 1.9 (era 2.1)
- [ ] DevTools Computed: `.contato-txt` line-height = 1.9 (era 2.1)
- [ ] Inspeção visual: nenhuma seção parece mais "arejada" ou "comprimida" que as outras

**TIP-03 — Respiração das seções**
- [ ] Scroll desktop: seções não colam umas nas outras
- [ ] Scroll 375px: padding lateral suficiente (nenhum texto toca a borda da tela)

**MOB-01 — Hero mobile**
- [ ] Chrome DevTools 375px (mobile preset): hero ocupa 100% da viewport
- [ ] Chrome DevTools 375px: scroll na página NÃO move o fundo do hero
- [ ] iOS Safari real ou simulador: hero não transborda por baixo da barra de endereços

**MOB-02 — Grid de produtos mobile**
- [ ] DevTools 375px: grid da Coleção mostra 2 colunas
- [ ] DevTools 375px: imagens não transbordam horizontalmente
- [ ] DevTools 375px: aspect-ratio das imagens mantido

**MOB-03 — Menu hambúrguer**
- [ ] Desktop 1440px: hambúrguer NÃO aparece; `.nav-links` visíveis
- [ ] 1200px ou menos: hambúrguer aparece; `.nav-links` ocultas
- [ ] Clicar hambúrguer: overlay abre com animação de opacidade
- [ ] Overlay aberto: fundo da página não é visível (overlay é opaco)
- [ ] Overlay aberto: clicar em "Sobre" → overlay fecha → smooth scroll para #sobre
- [ ] Overlay aberto: clicar hambúrguer novamente → overlay fecha
- [ ] Após fechar: scroll da página volta a funcionar normalmente (overflow: hidden removido)
- [ ] Acessibilidade: `aria-expanded` troca de false para true ao abrir

**MOB-04 — Formulário iOS**
- [ ] iOS Safari: tocar no campo "Nome" → SEM zoom na viewport
- [ ] iOS Safari: tocar no campo "E-mail" → SEM zoom na viewport
- [ ] iOS Safari: tocar no campo "Mensagem" → SEM zoom na viewport
- [ ] DevTools Computed (375px): font-size dos inputs = 16px

**MOB-05 — Textos legíveis**
- [ ] DevTools 375px: nenhum seletor de body text abaixo de 14px nos Computed Styles
- [ ] Inspeção visual 375px: todos os parágrafos são legíveis sem pinch-zoom

### Wave 0 Gaps
Nenhum — não há infraestrutura de teste a criar. Toda validação é manual no browser. O arquivo `index.html` já existe e é abrível diretamente.

---

## Sources

### Primary (HIGH confidence)
- Inspeção direta do `index.html` — todo o CSS e JS do projeto lido linha por linha
- `.planning/phases/03-tipografia-e-responsividade/03-CONTEXT.md` — decisões travadas do usuário
- MDN Web Docs (conhecimento verificado): `100svh`, `scrollIntoView`, `matchMedia`, `pointer-events`, `overflow: hidden`

### Secondary (MEDIUM confidence)
- Comportamento do iOS Safari com inputs `font-size < 16px` — documentado amplamente, confirmado por MDN e WebKit bug tracker histórico
- `backdrop-filter` criando stacking context — documentado na CSS spec e MDN

### Tertiary (LOW confidence)
- Detalhes específicos de versão do iOS para `100svh` (iOS 15.4) — baseado em conhecimento de treinamento; verificar se necessário

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — projeto 100% vanilla, sem dependências, código completo lido
- Architecture: HIGH — padrões extraídos diretamente do código existente
- Pitfalls: HIGH — baseados em comportamentos documentados de Safari/iOS e na estrutura CSS atual do projeto
- iOS quirks: MEDIUM-HIGH — comportamentos bem documentados, mas versões específicas de iOS não verificadas em tempo real

**Research date:** 2026-04-01
**Valid until:** Estável — HTML/CSS/JS vanilla, sem versões de biblioteca a expirar. iOS Safari quirks são estáveis desde 2022.
