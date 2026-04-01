# Phase 1: Hero Cinematográfico — Research

**Researched:** 2026-04-01
**Domain:** Vanilla JS parallax, CSS hero layout, animações de entrada, mobile Safari fallback
**Confidence:** HIGH

---

## Summary

A fase 1 é cirúrgica: trocar um background estático (`logo-bg-preta.jpg`, 25 KB, só logo no escuro) por uma foto de ambiente real com parallax suave. O código existente já tem tudo que precisa — overlay gradiente, animações fadeUp, scroll indicator — faltando apenas (1) a troca do asset de background, (2) o script JS de parallax, e (3) um fallback correto para iOS Safari.

O parallax em hero com arquivo único HTML/CSS/JS vanilla segue um padrão bem estabelecido: `background-attachment: fixed` não funciona em iOS Safari — a solução padrão é `translateY()` via `requestAnimationFrame` no scroll, desativado em touch devices via media query `hover: none`. O overlay já existe no código (`.hero-bg` tem `linear-gradient` na frente) e o scroll indicator (`.hero-scroll` + `.scroll-line`) já está implementado — apenas precisa ser verificado visualmente.

**Recomendação primária:** Usar `foto-21.png` (840 KB, foto de ambiente já em uso na seção `#sobre`) como background do hero. Implementar parallax via `transform: translateY()` com `requestAnimationFrame`, desativado em mobile via detecção de `matchMedia('(hover: none)')`.

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| HERO-01 | Hero exibe foto de ambiente de fundo com efeito parallax ao scroll | Parallax via `translateY()` em `.hero-bg`, script JS com `requestAnimationFrame` |
| HERO-02 | Overlay escuro graduado mantém legibilidade do texto sobre a foto | `.hero-bg` já tem `linear-gradient` — ajustar opacidade para foto real (não logo no escuro) |
| HERO-03 | Logo dourada centralizada com drop-shadow sutil | `.hero-logo img` já tem `filter: drop-shadow(0 0 32px rgba(201,169,110,.2))` — verificar visibilidade sobre foto |
| HERO-04 | Animações de entrada suaves (fadeUp) preservadas | Keyframe `fadeUp` e delays `.1s`→`1.2s` já implementados — não remover |
| HERO-05 | Indicador de scroll animado visível e elegante | `.hero-scroll` + `.scroll-line` + `@keyframes pulse` já implementados — verificar contraste |
</phase_requirements>

---

## Standard Stack

### Core (todos já presentes no projeto)

| Técnica | Versão | Propósito | Por que é o padrão |
|---------|--------|-----------|-------------------|
| CSS `background-size: cover` | CSS3 | Foto de fundo que preenche o hero | Nativo, sem dependências |
| CSS `linear-gradient` overlay | CSS3 | Legibilidade do texto sobre foto | Já implementado em `.hero-bg` |
| JS `requestAnimationFrame` | ES6 browser API | Parallax performático sem jank | Sincroniza com repaint do browser |
| `window.scrollY` | browser API | Leitura da posição de scroll | Passivo com `{ passive: true }` |
| `matchMedia('(hover: none)')` | browser API | Detecção de touch/mobile | Desativa parallax onde `fixed` não funciona |
| CSS `transform: translateY()` | CSS3 | Mover `.hero-bg` verticalmente | Usa compositor do browser (não relayout) |
| CSS `will-change: transform` | CSS3 | Hinting de performance ao browser | Promove elemento a layer separada |

### Sem dependências externas
Nenhuma biblioteca nova necessária. O projeto é arquivo único — não há npm, não há build step.

---

## Architecture Patterns

### Estrutura atual do hero (sem alteração de HTML)

```html
<section id="hero">
  <div class="hero-bg"></div>        <!-- background: foto + overlay -->
  <div class="hero-content">...</div>
  <div class="hero-scroll">...</div>
</section>
```

O `#hero` já tem `overflow: hidden` e `position: relative`. O `.hero-bg` já tem `position: absolute; inset: 0`. Essa estrutura é compatível com parallax por `translateY` — apenas adicionar `will-change: transform` e deixar `.hero-bg` um pouco maior que o container.

### Pattern 1: Parallax por translateY (correto para HTML único)

**O que é:** Mover `.hero-bg` verticalmente com `transform: translateY(scrollY * fator)` a cada frame.

**Por que não usar `background-attachment: fixed`:** Desativado por padrão no iOS Safari e em vários navegadores mobile modernos. Causa "flickering" e não funciona em elementos com `overflow: hidden`.

**Implementação:**

```javascript
// Adicionar ao bloco <script> existente
const heroBg = document.querySelector('.hero-bg');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const isTouchDevice = window.matchMedia('(hover: none)');

function updateParallax() {
  if (prefersReducedMotion.matches || isTouchDevice.matches) return;
  const scrolled = window.scrollY;
  // Fator 0.4 = movimento sutil (40% da velocidade do scroll)
  heroBg.style.transform = 'translateY(' + (scrolled * 0.4) + 'px)';
}

window.addEventListener('scroll', () => {
  requestAnimationFrame(updateParallax);
}, { passive: true });
```

**CSS para o `.hero-bg`:**

```css
.hero-bg {
  position: absolute;
  inset: 0;
  /* Altura extra para o parallax não descobrir bordas */
  top: -20%; bottom: -20%;
  background:
    linear-gradient(to bottom, rgba(14,14,14,.35) 0%, rgba(14,14,14,.65) 65%, rgba(14,14,14,1) 100%),
    url('assets/foto-21.png') center/cover no-repeat;
  will-change: transform;
}
```

**Nota sobre a altura extra:** Com fator 0.4 e um hero de 100vh (~900px), o `.hero-bg` pode se mover até ~360px antes do usuário sair do hero. Adicionar `top: -20%; bottom: -20%` garante que a foto cubra o espaço independentemente do scroll.

### Pattern 2: Overlay graduado calibrado para foto real

O overlay atual (`rgba(14,14,14,.4) 0%` → `rgba(14,14,14,.72) 70%` → `rgba(14,14,14,1) 100%`) foi calibrado para `logo-bg-preta.jpg` que já é quase preta. Com uma foto de ambiente real (conteúdo claro/colorido), o overlay precisa ser mais denso no topo:

```css
/* Overlay ajustado para foto de ambiente real */
linear-gradient(
  to bottom,
  rgba(14,14,14,.55) 0%,    /* mais denso no topo — cobre a nav */
  rgba(14,14,14,.65) 60%,
  rgba(14,14,14,1) 100%
)
```

### Pattern 3: Drop-shadow da logo sobre foto

O drop-shadow atual (`0 0 32px rgba(201,169,110,.2)`) é sutil demais sobre uma foto. Com foto de ambiente, pode ser necessário um halo mais pronunciado ou um segundo shadow escuro para destacar a logo dourada:

```css
.hero-logo img {
  filter:
    drop-shadow(0 0 40px rgba(201,169,110,.35))
    drop-shadow(0 2px 12px rgba(0,0,0,.6));
}
```

### Anti-patterns a evitar

- **`background-attachment: fixed` no `.hero-bg`:** Não funciona em iOS Safari (bug histórico, nunca corrigido). O `#manifesto` já usa isso — funcionar em desktop não garante mobile.
- **Parallax via `top` ou `margin-top`:** Causa reflow (layout recalc). Sempre usar `transform: translateY()`.
- **`scroll` listener sem `passive: true`:** Bloqueia o thread principal. O projeto já usa `passive: true` no nav — manter o padrão.
- **Remover `overflow: hidden` do `#hero`:** O parallax com `.hero-bg` maior que o container depende disso para não vazar visualmente.

---

## Don't Hand-Roll

| Problema | Não construir | Usar em vez disso | Por que |
|---------|---------------|-------------------|---------|
| Parallax library | `rellax.js`, `Skrollr`, `ScrollMagic` | `requestAnimationFrame` vanilla | Arquivo único sem npm/CDN |
| Detecção de iOS | User-agent sniffing | `matchMedia('(hover: none)')` | UA string não é confiável, matchMedia é spec |
| Throttle do scroll | Custom debounce/throttle | `requestAnimationFrame` + `passive: true` | rAF já é 60fps-limited, passive elimina bloqueio |
| Intersection Observer para hero | Adicionar `.reveal` ao `.hero-bg` | Animações CSS com `animation:` direto | Hero está sempre visível no load — IO é para seções abaixo |

---

## Common Pitfalls

### Pitfall 1: iOS Safari e background-attachment: fixed

**O que acontece:** Em iOS Safari, `background-attachment: fixed` é ignorado — o background se comporta como `scroll`. Isso quebra o efeito parallax completamente e pode causar jump visual.

**Por que acontece:** Bug histórico do WebKit relacionado ao compositing de elementos com `overflow: hidden`. Nunca corrigido. O `#manifesto` no projeto atual usa `background-attachment: fixed` — funciona em desktop mas é estático no iOS.

**Como evitar:** Usar `transform: translateY()` com detecção via `matchMedia('(hover: none)')`. Em dispositivos touch, simplesmente não aplicar o transform — a foto cobre normalmente.

**Sinais de alerta:** Ver parallax "broken" só no Safari mobile, foto estática quando deveria mover, ou foto "jumping" ao scroll.

### Pitfall 2: Hero-bg descobrindo bordas no scroll

**O que acontece:** Com `.hero-bg` no tamanho exato do container e `translateY` positivo, a parte inferior do background fica sem cobertura — aparece o fundo do `body` (preto) por baixo.

**Por que acontece:** `translateY(N)` move o elemento para baixo, descobrindo a parte de cima.

**Como evitar:** Dimensionar `.hero-bg` com `top: -20%; bottom: -20%` para ter margem de movimentação.

### Pitfall 3: Overlay insuficiente — texto ilegível sobre foto colorida

**O que acontece:** A foto de ambiente tem cores quentes (madeira, estofados, iluminação) que conflitam com o texto offwhite e a logo dourada.

**Por que acontece:** O overlay foi calibrado para `logo-bg-preta.jpg` que já é escuro. Uma foto real precisa de overlay mais denso, especialmente no centro e topo onde estão os elementos de texto.

**Como evitar:** Aumentar opacidade do gradiente na faixa central (30%–70% do height) onde ficam logo e título. Testar visualmente com a foto real.

### Pitfall 4: fadeUp quebra se `opacity: 0` + `animation` colidem com parallax

**O que acontece:** Se `.hero-bg` receber `opacity: 0; animation: fadeUp` como os outros elementos do hero, o parallax JS tenta transformar um elemento invisível, causando flicker.

**Por que acontece:** As animações CSS do hero (`.hero-line`, `.hero-logo`, etc.) usam `opacity: 0` inicial + `animation: fadeUp forwards`. O `.hero-bg` não deve participar desse sistema.

**Como evitar:** Confirmar que `.hero-bg` não tem classe `.reveal` e não recebe animação de entrada — deve ser visível imediatamente (é o background, não conteúdo).

### Pitfall 5: drop-shadow da logo invisível sobre foto clara

**O que acontece:** A logo dourada (`logo-dourada.png`) some ou perde definição sobre trechos claros da foto.

**Por que acontece:** O drop-shadow atual é sutil (20% opacidade) — suficiente sobre fundo preto, insuficiente sobre foto.

**Como evitar:** Adicionar segundo drop-shadow escuro para separação: `drop-shadow(0 2px 12px rgba(0,0,0,.6))`.

---

## Code Examples

### Exemplo completo do parallax vanilla

```javascript
// Source: padrão estabelecido documentado em MDN (requestAnimationFrame + passive scroll)
// Inserir no <script> existente, após o bloco do IntersectionObserver

const heroBg = document.querySelector('.hero-bg');
const noMotion  = window.matchMedia('(prefers-reduced-motion: reduce)');
const isTouch   = window.matchMedia('(hover: none)');

let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      if (!noMotion.matches && !isTouch.matches) {
        heroBg.style.transform = 'translateY(' + (window.scrollY * 0.4) + 'px)';
      }
      ticking = false;
    });
    ticking = true;
  }
}, { passive: true });
```

**Nota:** O padrão `ticking` evita empilhar múltiplos `requestAnimationFrame` por evento de scroll. Isso é o equivalente a um throttle de 60fps nativo.

### CSS final do .hero-bg

```css
.hero-bg {
  position: absolute;
  top: -20%; bottom: -20%; left: 0; right: 0;  /* margem para parallax */
  background:
    linear-gradient(to bottom,
      rgba(14,14,14,.55) 0%,
      rgba(14,14,14,.65) 60%,
      rgba(14,14,14,1)  100%
    ),
    url('assets/foto-21.png') center/cover no-repeat;
  will-change: transform;
}
```

### Seleção de asset para o hero

Assets disponíveis e seus pesos:

| Asset | Tamanho | Tipo | Adequação para hero |
|-------|---------|------|---------------------|
| `foto-21.png` | 840 KB | Foto de ambiente (já em uso em `#sobre`) | ALTA — foto real, tamanho razoável |
| `sf-buffet.png` | 2.1 MB | Produto sem fundo | BAIXA — produto isolado, não ambiente |
| `sf-prod-02.png` | 2.3 MB | Produto sem fundo | BAIXA — produto isolado, pesado |
| `logo-bg-preta.jpg` | 25 KB | Logo no escuro | REMOVER — não é foto de ambiente |

**Recomendação:** `foto-21.png` é a candidata principal. Já é usada na seção `#sobre`, garantindo que o asset existe e carrega. Para hero precisamos de uma foto de ambiente de alta qualidade — verificar visualmente se `foto-21.png` mostra o ambiente de forma impressionante (sofás, sala de exposição, etc). Se necessário, `foto-05.png` ou `foto-10.png` (2.2–2.3 MB) são alternativas com mais detalhe de ambiente.

---

## State of the Art

| Abordagem antiga | Abordagem atual | Impacto |
|-----------------|-----------------|---------|
| `background-attachment: fixed` | `transform: translateY()` via rAF | Funciona em iOS Safari |
| Parallax via `top`/`margin` | `transform: translateY()` | Evita reflow — usa compositor |
| Scroll throttle manual | `requestAnimationFrame` + `passive` | Performance nativa 60fps |
| Detecção iOS por user-agent | `matchMedia('(hover: none)')` | Confiável, spec-compliant |

**Deprecated/Outdated:**
- `background-attachment: fixed` para parallax em mobile: nunca funciona em iOS Safari, não usar.
- Parallax libraries (Rellax, Skrollr): overkill para um elemento único em arquivo sem build step.

---

## Open Questions

1. **Qual foto usar no hero?**
   - O que sabemos: `foto-21.png` (840 KB) é foto de ambiente, já no projeto. `sf-buffet.png` (2.1 MB) é produto sem fundo.
   - O que está indefinido: Não foi possível inspecionar o conteúdo visual das fotos. `foto-21.png` pode ser ambiente de exposição (ideal) ou apenas produto.
   - Recomendação: Verificar visualmente `foto-21.png`. Se mostrar ambiente sofisticado com luz e mobiliário, usá-la. Caso contrário, revisar `foto-05.png`, `foto-10.png`, `foto-12.png` (todas 2.1–2.3 MB, mais detalhadas).

2. **Intensidade do overlay para a foto escolhida**
   - O que sabemos: Overlay atual calibrado para fundo preto. Foto real exige recalibração.
   - Recomendação: Começar com `.55 / .65` (centro/topo) e ajustar iterativamente até texto ser legível sem tornar a foto irreconhecível.

3. **Fator de parallax ideal**
   - O que sabemos: Fator 0.3–0.5 é o range suave padrão. 0.4 é o ponto de equilíbrio entre "sutil" e "percebido".
   - Recomendação: Iniciar com 0.4. Se o efeito parecer exagerado, reduzir para 0.3.

---

## Validation Architecture

> Projeto HTML/CSS/JS vanilla — sem framework de testes automatizados. Validação é visual/manual.

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Nenhum (arquivo único, sem build step) |
| Config file | N/A |
| Quick run command | Abrir `index.html` no browser |
| Full suite command | Testar em Chrome desktop + Safari mobile (ou DevTools Device Emulation) |

### Phase Requirements → Test Map

| Req ID | Comportamento | Tipo de Teste | Comando | Arquivo existe? |
|--------|--------------|---------------|---------|----------------|
| HERO-01 | Foto de ambiente visível no hero; background se move ao scroll | Visual/manual | Scroll em Chrome desktop | index.html — a modificar |
| HERO-02 | Texto do hero legível sobre a foto | Visual/manual | Inspecionar contraste em DevTools | index.html — a modificar |
| HERO-03 | Logo dourada centralizada com drop-shadow visível | Visual/manual | Inspecionar elemento `.hero-logo img` | index.html — a modificar |
| HERO-04 | Animações fadeUp disparam no page load | Visual/manual | Hard reload (Ctrl+Shift+R) e observar | index.html — existente |
| HERO-05 | Scroll indicator visível e animado | Visual/manual | Inspecionar `.hero-scroll` na viewport | index.html — existente |
| MOB-01 | Hero funciona em mobile (parallax desativado, foto estática) | Visual/manual | DevTools > iPhone 12 Pro emulation | index.html — a modificar |

### Sampling Rate

- **Por tarefa:** Abrir `index.html` no browser e verificar visualmente o hero.
- **Ao final da fase:** Testar em Chrome desktop + Safari (ou emulação iOS no DevTools). Verificar que parallax está ativo no desktop e graciosamente ausente no mobile.
- **Gate da fase:** Hero passa na inspeção visual com todos os 5 critérios de sucesso confirmados antes do `/gsd:verify-work`.

### Wave 0 Gaps

Nenhum — não há infraestrutura de testes a criar. Validação é inteiramente visual/manual conforme o stack do projeto.

---

## Sources

### Primary (HIGH confidence)

- Inspeção direta de `index.html` (linhas 56–130, 529–549, 907–920) — CSS do hero e JS existente
- Inspeção de `assets/` — lista e tamanhos dos arquivos disponíveis
- MDN Web Docs: `requestAnimationFrame`, `matchMedia`, `passive event listeners` — APIs usadas

### Secondary (MEDIUM confidence)

- Comportamento de `background-attachment: fixed` em iOS Safari: documentado extensivamente em bug reports do WebKit e artigos CSS-Tricks/web.dev. Reproduzível e não corrigido desde iOS 13+.
- Padrão `ticking + rAF` para scroll throttle: amplamente adotado, documentado em MDN e Google Web Fundamentals.

### Tertiary (LOW confidence)

- Nenhum item de baixa confiança nesta pesquisa. Todos os achados críticos são baseados em inspeção direta do código ou APIs nativas bem documentadas.

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — arquivo único vanilla, sem decisões de dependências novas
- Architecture: HIGH — baseado em inspeção direta do código existente
- Pitfalls: HIGH — iOS Safari/fixed é comportamento verificado e documentado; outros pitfalls derivam da estrutura do código atual
- Asset selection: MEDIUM — requer verificação visual das fotos (não é possível inspecionar conteúdo de imagens neste contexto)

**Research date:** 2026-04-01
**Valid until:** 2026-06-01 (stack estável, APIs nativas sem deprecação prevista)
