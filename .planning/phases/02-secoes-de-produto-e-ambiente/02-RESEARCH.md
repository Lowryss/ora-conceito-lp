# Phase 2: Seções de Produto e Ambiente - Research

**Researched:** 2026-04-01
**Domain:** CSS Layout, object-fit, hover/touch interactions — HTML/CSS/JS vanilla
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- Trocar `object-fit: contain` por `object-fit: cover` com leve padding (12–16px) em ambas as seções
- Remover `mix-blend-mode: multiply` das imagens — com fundo escuro (#0E0E0E), multiply escurece/apaga o produto
- Manter `aspect-ratio` atuais dos cards da Coleção (1:1 para s3, 3:4 para tall, 16:9 para wide)
- Cards de Ambientes: cover com leve padding, manter aspect-ratio 4/5 atual
- Trocar fotos Ambientes: sf-buffet.png, foto-10.png, sf-estante.png → sf-prod-02.png, sf-prod-03.png, sf-prod-04.png
- sf-buffet.png permanece apenas na Coleção (sem duplicação entre seções)
- Labels da Coleção (`.pc-label`): sempre visíveis em dispositivos touch via `@media (hover: none)` com `opacity: 1`
- Overlays dos Ambientes (`.dest-overlay`): mesma lógica de visibilidade em touch
- Desktop mantém comportamento atual (opacity 0 → 1 no hover)
- Detectar touch via `matchMedia('(hover: none)')` — padrão já no código (parallax Fase 1)

### Claude's Discretion
- Valor exato do padding cover (entre 12px e 16px — escolher pelo visual)
- Títulos/labels exatos dos novos cards de Ambientes (sf-prod-02/03/04)
- Ajuste fino do gradiente dos overlays se necessário com as novas fotos

### Deferred Ideas (OUT OF SCOPE)
- Nenhuma ideia fora do escopo surgiu durante a discussão
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| COL-01 | Grid editorial de produtos com fundo escuro (#0E0E0E ou #181818) | Fundo já é `var(--grafite)` = #181818 no `#colecao`. Nenhuma alteração de cor necessária — confirmar visualmente |
| COL-02 | Fotos de produto usam `object-fit: cover` (sem padding excessivo) — produtos ocupam o espaço | Alterar `.pc img` de `contain + padding:36px` para `cover + padding:12–16px`; remover `mix-blend-mode: multiply` |
| COL-03 | Hover revela label/nome do produto com transição suave | `.pc-label` já implementado com `opacity 0 → 1`; adicionar `@media (hover: none)` para fixar opacity:1 em touch |
| COL-04 | Layout responsivo mantém hierarquia visual no mobile | Breakpoints existentes em 1200px e 700px cobrem o colapso de colunas; validar que cover não quebra proporções |
| AMB-01 | Seção Destaques/Ambientes usa fotos que mostram produtos em contexto | Trocar src de 3 `<img>` dentro de `#destaques .dest-item` para sf-prod-02/03/04 |
| AMB-02 | Cards de ambiente com overlay gradient + título elegante ao hover | `.dest-overlay` já implementado sem opacity; adicionar `@media (hover: none)` para sempre visível em touch |
| AMB-03 | Proporção das fotos consistente e bem aproveitada | Alterar `.dest-item img` de `contain + padding:28px 20px` para `cover + padding:12–16px`; manter aspect-ratio 4/5 |
</phase_requirements>

---

## Summary

Esta fase corrige dois problemas visuais centrais que impedem as seções de transmitir sofisticação: o `object-fit: contain` com padding excessivo que deixa os produtos pequenos e flutuando no card, e o `mix-blend-mode: multiply` que escurece/apaga produtos sobre o fundo escuro #0E0E0E. Ambos foram provavelmente configurados pensando em fundo branco — com o redesign dark, são os maiores bloqueadores visuais.

A mudança é cirúrgica: três blocos CSS (`#colecao .pc img`, `.pc.tall img`, `.pc.wide img` e `#destaques .dest-item img`), três src de imagens, e um bloco JS/CSS para comportamento touch. Todo o infrastructure já existe — `.pc-label`, `.dest-overlay`, `isTouch` via `matchMedia` e animações `reveal` permanecem intactos.

A lógica touch com `@media (hover: none)` é o padrão mais confiável para iOS Safari e Android Chrome, alinhado ao que já foi implementado na Fase 1 para o parallax. O planner deve tratar as duas seções como operações independentes e paralelas.

**Primary recommendation:** Migrar `contain → cover` + remover `mix-blend-mode`, depois ajustar touch labels — nessa ordem, pois é a sequência de impacto visual mais direta.

---

## Standard Stack

### Core
| Técnica | Versão | Propósito | Por que padrão |
|---------|--------|-----------|----------------|
| `object-fit: cover` | CSS3 | Preenche o container sem distorção, cortando bordas se necessário | Padrão universal para imagens em cards — comportamento "previsível" independente da proporção da foto |
| `object-position: center` | CSS3 | Ponto de foco do crop | Default já é center — apenas declarar explicitamente se precisar ajustar para foco no produto |
| `@media (hover: none)` | CSS4 MQ Level 4 | Detecta dispositivos sem hover (touch) | Mais confiável que `pointer: coarse` para diferenciar touch de mouse em iOS Safari |
| `matchMedia('(hover: none)')` | JS | Equivalente JS da media query | Já em uso no código para parallax — reutilizar sem nova dependência |

### Padrões de comportamento
| Problema | Não usar | Usar | Motivo |
|----------|----------|------|--------|
| Imagem pequena no card | `contain + padding grande` | `cover + padding pequeno` | Cover garante preenchimento total do card |
| Produto apagado no dark | `mix-blend-mode: multiply` | Sem blend mode | Multiply escurece sobre fundo escuro — remove-se completamente |
| Labels inacessíveis no touch | `opacity:0` sem fallback | `@media (hover:none) { opacity:1 }` | Touch não dispara `:hover` — sem fallback o usuário nunca vê o label |

---

## Architecture Patterns

### Padrão 1: Cover com padding mínimo

`object-fit: cover` não aceita padding como parte do crop — o padding reduz a área visível do elemento, fazendo o cover operar em uma área menor. O resultado com padding 12–16px é: produto ocupa ~85–90% do card com um respiro perimetral sutil, eliminando o excesso branco dos 36px atuais.

```css
/* ANTES — problema */
.pc img {
  object-fit: contain;
  padding: 36px;
  mix-blend-mode: multiply;
}

/* DEPOIS — correção */
.pc img {
  object-fit: cover;
  padding: 14px;          /* Claude's discretion: 12–16px */
  /* mix-blend-mode removido */
}
```

Notar que as variantes `.pc.tall img` e `.pc.wide img` também precisam ter seus paddings atualizados — elas sobrescrevem o valor base com valores ainda maiores (40px/28px e 32px/48px respectivamente).

### Padrão 2: Cover em Ambientes

Mesma lógica para `.dest-item img`. O aspect-ratio 4/5 permanece, apenas o fit e padding mudam:

```css
/* ANTES */
.dest-item img {
  object-fit: contain;
  padding: 28px 20px;
}

/* DEPOIS */
.dest-item img {
  object-fit: cover;
  padding: 14px;
}
```

### Padrão 3: Touch visibility via CSS media query

```css
/* Mobile touch — labels e overlays sempre visíveis */
@media (hover: none) {
  .pc-label {
    opacity: 1;
  }
  .dest-overlay {
    /* dest-overlay não usa opacity — já é sempre visível via position:absolute */
    /* Se necessário ajustar gradiente de visibilidade em touch: */
    background: linear-gradient(to top, rgba(10,10,10,.92) 0%, rgba(10,10,10,.15) 60%, transparent 100%);
  }
}
```

Atenção: `.dest-overlay` não tem `opacity:0` no CSS atual (linha ~298–303) — ele já é sempre visível. A lógica touch para Ambientes pode não precisar de CSS adicional. Verificar no HTML se há algum hover que oculta o overlay no desktop.

### Padrão 4: Touch visibility via JS (complementar)

O padrão já existe no código e pode ser estendido após a linha ~950:

```javascript
// Após o bloco do parallax existente (~linha 950)
if (isTouch.matches) {
  // Labels da Coleção — garantir visibilidade
  document.querySelectorAll('.pc-label').forEach(el => {
    el.style.opacity = '1';
  });
}
```

A abordagem CSS-only com `@media (hover: none)` é preferível por ser declarativa e não depender de timing de execução JS.

### Troca de fotos nos Ambientes

As 3 imagens a trocar estão nas linhas 734, 741, 748 do HTML:

| Card | Atual | Novo | Título atual | Título a definir |
|------|-------|------|--------------|-----------------|
| 1 | sf-buffet.png | sf-prod-02.png | Aparador Exclusivo | A definir (discretion) |
| 2 | foto-10.png | sf-prod-03.png | Mesa de Centro Orgânica | A definir (discretion) |
| 3 | sf-estante.png | sf-prod-04.png | Estante Premium | A definir (discretion) |

Notar que sf-prod-03.png já é usado na Coleção (linha 663). A decisão em CONTEXT.md lista sf-prod-03 para Ambientes também — verificar se isso cria duplicação visual indesejada entre seções. A CONTEXT.md confirma que "sf-buffet.png permanece apenas na Coleção" mas não menciona sf-prod-03 especificamente. O planner deve manter sf-prod-03 em Ambientes como decidido, mas notar que esse card já aparece na Coleção como "Sala de Estar".

### Anti-Patterns a Evitar

- **Inline style override sem remover a regra CSS base:** A linha 659 tem `style="aspect-ratio:16/9;padding:40px 80px"` no img da Mesa de Centro. Ao atualizar `.pc img` no CSS, esse inline override não será afetado automaticamente — precisa ser atualizado junto ou removido se o padding geral já for adequado.
- **Remover `object-fit` sem remover padding:** Cover com padding grande ainda cria área morta. Os dois precisam mudar juntos.
- **Usar `pointer: coarse` ao invés de `hover: none`:** `coarse` detecta caneta stylus como touch em alguns devices; `hover: none` é mais preciso para separar mouse de touch.

---

## Don't Hand-Roll

| Problema | Não construir | Usar em vez disso | Motivo |
|----------|---------------|-------------------|--------|
| Detecção de touch | User-Agent sniffing | `matchMedia('(hover: none)')` | UA sniffing quebra com bots e novos devices; MQ é spec do browser |
| Animação de overlay | Keyframes customizados | `transition: opacity .4s` já presente | A transição já está implementada — apenas ajustar o estado inicial |
| Crop de imagem responsivo | JS para calcular dimensões | `object-fit: cover` nativo | CSS nativo é mais performático que qualquer solução JS |

---

## Common Pitfalls

### Pitfall 1: Cover sem height definida perde proporção
**O que vai errado:** `object-fit: cover` em um `<img>` precisa que o elemento pai (ou o próprio img) tenha height definida — seja via `aspect-ratio`, `height` fixo, ou o container com `height`. Sem isso, o cover colapsa para a altura intrínseca da imagem.
**Por que acontece:** `width: 100%` define a largura mas não a altura. Cover só funciona quando ambas as dimensões do container estão definidas.
**Como evitar:** O código atual já usa `aspect-ratio: 1` no `.pc img` e `aspect-ratio: 4/5` no `.dest-item img` — manter esses valores. Apenas substituir o padding e o fit.
**Sinal de alerta:** Imagem esticada verticalmente ou colapsada após a mudança.

### Pitfall 2: Inline styles sobrescrevem CSS base
**O que vai errado:** `.pc img` na linha 659 tem `style="aspect-ratio:16/9;padding:40px 80px"` — esse padding inline não será sobrescrito pela mudança na regra CSS.
**Por que acontece:** Inline styles têm especificidade máxima no cascade.
**Como evitar:** Remover ou atualizar esse inline style junto com a regra CSS base. O planner deve incluir essa linha como parte da tarefa COL-02.
**Sinal de alerta:** Outros cards com cover correto mas esse card ainda com padding excessivo.

### Pitfall 3: dest-overlay não tem opacity — não precisa de fix
**O que vai errado:** Implementar JS touch para `.dest-overlay` quando ele já é sempre visível (sem `opacity:0` no CSS).
**Por que acontece:** Leitura superficial do CONTEXT.md sem verificar o CSS atual.
**Como evitar:** Verificar o CSS de `.dest-overlay` (linhas 298–303) — ele usa apenas `position:absolute + inset:0 + background gradient`. Não há opacity. A lógica touch para Ambientes pode ser apenas visual (reforçar gradiente em touch) ou completamente desnecessária.
**Sinal de alerta:** Código JS adicionando `style.opacity = '1'` em elemento que nunca teve opacity 0.

### Pitfall 4: mix-blend-mode no .gm-item img (Galeria) — fora do escopo
**O que vai errado:** Ao remover `mix-blend-mode: multiply` da Coleção e Ambientes, o desenvolvedor pode notar que `.gm-item img` (linha 388) também usa `mix-blend-mode: multiply` e fazê-la também.
**Por que acontece:** Scope creep — tentação de "consertar tudo de uma vez".
**Como evitar:** A Fase 2 cobre apenas `#colecao` e `#destaques`. A Galeria (`#galeria`) fica para a Fase 3 ou avaliação separada. O planner deve documentar isso explicitamente.
**Sinal de alerta:** Alterações em `.gm-item img` nas tarefas desta fase.

### Pitfall 5: sf-prod-03 duplicado entre Coleção e Ambientes
**O que vai errado:** sf-prod-03.png está na Coleção (linha 663, card "Sala de Estar") e será inserido nos Ambientes conforme decisão do CONTEXT.md.
**Por que acontece:** A lista de exclusões no CONTEXT.md foca em sf-buffet.png mas não exclui explicitamente sf-prod-03 dos Ambientes.
**Como evitar:** A decisão está travada — manter sf-prod-03 nos Ambientes. Para minimizar impacto visual, o título do card de Ambientes deve diferenciá-lo suficientemente do card da Coleção. Não é um bloqueador, apenas um ponto de atenção.

---

## Code Examples

### Estado atual completo das regras afetadas (linhas reais do index.html)

```css
/* ATUAL — linha ~243 */
.pc img {
  width: 100%; height: 100%;
  object-fit: contain;
  padding: 36px;
  aspect-ratio: 1;
  mix-blend-mode: multiply;
  transition: transform .7s ease;
}
.pc.tall img { aspect-ratio: 3/4; padding: 40px 28px; }
.pc.wide img { aspect-ratio: 16/9; padding: 32px 48px; }

/* ATUAL — linha ~291 */
.dest-item img {
  width: 100%; aspect-ratio: 4/5;
  object-fit: contain;
  padding: 28px 20px;
  transition: transform .8s ease;
}
```

### Estado alvo após Fase 2

```css
/* ALVO */
.pc img {
  width: 100%; height: 100%;
  object-fit: cover;
  padding: 14px;              /* ou 12px — discretion */
  aspect-ratio: 1;
  /* mix-blend-mode REMOVIDO */
  transition: transform .7s ease;
}
.pc.tall img { aspect-ratio: 3/4; padding: 14px; }
.pc.wide img { aspect-ratio: 16/9; padding: 14px; }

/* ALVO */
.dest-item img {
  width: 100%; aspect-ratio: 4/5;
  object-fit: cover;
  padding: 14px;
  transition: transform .8s ease;
}

/* Touch — adicionar ao bloco @media(max-width:700px) ou separado */
@media (hover: none) {
  .pc-label { opacity: 1; }
}
```

### Inline style a corrigir (linha 659 do HTML)

```html
<!-- ATUAL -->
<img src="assets/foto-10.png" alt="Mesa de Centro" style="aspect-ratio:16/9;padding:40px 80px"/>

<!-- ALVO — remover inline style, deixar regra CSS base gerenciar -->
<img src="assets/foto-10.png" alt="Mesa de Centro"/>
<!-- com .pc.wide img já definindo aspect-ratio:16/9 e padding:14px -->
```

Nota: o card da Mesa de Centro (linha 658) usa classe `.pc s6` mas não usa `.wide`. A regra `.pc.wide` não se aplica a ele — o aspect-ratio 16/9 vem apenas do inline style. Para migrar corretamente, adicionar classe `wide` ao card pai ou manter o inline style com o padding atualizado.

### Troca de src nos Ambientes (linhas ~734–752)

```html
<!-- ATUAL -->
<img src="assets/sf-buffet.png" alt="Aparador"/>
<img src="assets/foto-10.png" alt="Mesa de Centro"/>
<img src="assets/sf-estante.png" alt="Estante"/>

<!-- ALVO -->
<img src="assets/sf-prod-02.png" alt="[Peça]"/>
<img src="assets/sf-prod-03.png" alt="[Peça]"/>
<img src="assets/sf-prod-04.png" alt="[Peça]"/>
```

---

## State of the Art

| Abordagem antiga | Abordagem atual | Contexto | Impacto |
|-----------------|----------------|----------|---------|
| `mix-blend-mode: multiply` para fundos brancos | Sem blend mode em fundos escuros | Design system migrou de light para dark | Multiply sobre #0E0E0E elimina a imagem visualmente |
| `contain + padding grande` para mostrar produto inteiro | `cover + padding mínimo` para editorial | Estética studio/editorial prefere preenchimento | Produtos parecem maiores e mais proeminentes |
| Hover como única forma de revelar info | `@media (hover: none)` para touch | Mobile-first design | Conteúdo acessível em qualquer dispositivo |

---

## Open Questions

1. **Classe `.wide` no card da Mesa de Centro (s6)**
   - O que sabemos: card usa `s6` sem `wide`; aspect-ratio 16/9 vem de inline style
   - O que é incerto: ao remover o inline style, o card perde o aspect-ratio 16/9 (fica com o default 1:1 da regra base)
   - Recomendação: planner deve decidir — adicionar classe `wide` ao `<div class="pc s6">`, ou manter inline style apenas com `padding` atualizado

2. **sf-prod-03 compartilhado entre Coleção e Ambientes**
   - O que sabemos: decisão travada no CONTEXT.md usa sf-prod-03 em Ambientes; esse asset já aparece na Coleção
   - O que é incerto: impacto visual de ver a mesma foto em duas seções distintas
   - Recomendação: manter a decisão travada; compensar com títulos distintos que contextualizam diferentemente o produto

3. **dest-overlay — necessidade real do fix de touch**
   - O que sabemos: CSS atual de `.dest-overlay` não usa opacity — o overlay é sempre visível
   - O que é incerto: se o CONTEXT.md antecipou uma futura mudança de opacity no desktop ou apenas seguiu o padrão da Coleção
   - Recomendação: planner deve verificar se o comportamento atual de Ambientes no desktop é "overlay sempre visível" (confirmado pelo CSS) — se sim, nenhuma alteração touch é necessária para AMB-02 além de verificação visual

---

## Validation Architecture

`nyquist_validation: true` — seção obrigatória.

### Test Framework

| Propriedade | Valor |
|-------------|-------|
| Framework | Nenhum framework automatizado — projeto HTML/CSS/JS vanilla sem test runner |
| Config file | Não existe |
| Quick run command | Abrir `index.html` no browser e inspecionar visualmente |
| Full suite command | Checklist manual completo abaixo |

### Phase Requirements → Test Map

| Req ID | Comportamento a validar | Tipo de teste | Comando / Ação | Arquivo existe? |
|--------|------------------------|---------------|----------------|-----------------|
| COL-01 | Cards da Coleção têm fundo escuro (#181818) sem áreas brancas | Visual manual | DevTools: inspecionar `background` de `#colecao` e `.pc` | ✅ index.html |
| COL-02 | Fotos preenchem os cards sem padding excessivo — nenhum produto pequeno/flutuando | Visual manual | Scroll até #colecao, comparar before/after com DevTools screenshot | ✅ index.html |
| COL-02 | mix-blend-mode removido — produtos visíveis sobre fundo escuro | Inspeção DevTools | Elements panel: confirmar ausência de `mix-blend-mode` em `.pc img` | ✅ index.html |
| COL-03 | Hover no desktop revela label com transição suave | Interação desktop | Mouse hover sobre cada card da Coleção | ✅ index.html |
| COL-03 | Labels sempre visíveis em mobile touch | Inspeção mobile | Chrome DevTools device toolbar (iPhone SE / Pixel) — sem hover | ✅ index.html |
| COL-04 | Grid colapsa corretamente em 700px — 1-2 colunas sem quebra visual | Responsive manual | DevTools: 700px width — verificar colunas e proporções | ✅ index.html |
| AMB-01 | Fotos trocadas: sf-prod-02/03/04 nos 3 cards de Ambientes | Inspeção HTML | DevTools Elements: verificar src dos 3 `<img>` em `#destaques` | ✅ index.html |
| AMB-02 | Overlay com título visível em hover (desktop) | Interação desktop | Mouse hover sobre cada card de Ambientes | ✅ index.html |
| AMB-02 | Overlay/título visível em mobile touch sem hover | Inspeção mobile | Chrome DevTools device toolbar — overlay visível sem interação | ✅ index.html |
| AMB-03 | Proporções 4/5 mantidas, sem distorção — fotos aproveitadas consistentemente | Visual manual | 3 cards lado a lado com mesma altura visual | ✅ index.html |

### Sampling Rate

- **Por tarefa:** Abrir `index.html` no Chrome, navegar até a seção alterada, verificar visualmente
- **Por wave:** Checklist manual completo com DevTools — desktop 1440px + mobile 375px
- **Phase gate:** Todos os 10 itens da tabela acima passando antes do `/gsd:verify-work`

### Checklist de Validação Manual Completo

**Setup:**
1. Abrir `index.html` diretamente no Chrome (sem servidor local é suficiente para CSS/HTML)
2. DevTools aberto (F12)

**Desktop (1440px ou resolução real):**
- [ ] Scroll até `#colecao` — produtos preenchem os cards, sem grande área vazia ao redor
- [ ] Nenhum produto "apagado" ou com tom muito escurecido (mix-blend-mode removido)
- [ ] Hover em 3+ cards diferentes — label aparece com transição suave
- [ ] Scroll até `#destaques` — 3 novas fotos carregam corretamente (sf-prod-02/03/04)
- [ ] Proporções dos 3 cards de Ambientes são consistentes visualmente
- [ ] Hover em cards de Ambientes — overlay/título visível (já era comportamento atual)
- [ ] DevTools Elements: `.pc img` sem `mix-blend-mode` e com `object-fit: cover`
- [ ] DevTools Elements: `.dest-item img` com `object-fit: cover`

**Mobile — DevTools Device Toolbar (375px / iPhone SE):**
- [ ] Labels da Coleção visíveis sem hover (opacity:1 via `@media (hover: none)`)
- [ ] Cards da Coleção colapsam corretamente — 2 colunas na maioria dos cards
- [ ] Overlays dos Ambientes visíveis sem interação
- [ ] Grid de Ambientes vira 1 coluna (já existe `grid-template-columns:1fr` no breakpoint 1200px)
- [ ] Nenhuma imagem distorcida ou quebrada

**Verificação de regressão:**
- [ ] Hero parallax ainda funciona (não foi alterado)
- [ ] Animações reveal ainda funcionam ao scrollar
- [ ] Nav blur ao scroll ainda funciona

### Wave 0 Gaps

Nenhum — não há framework de testes a instalar. Toda validação é manual via browser. O "Wave 0" desta fase é: ter `index.html` abrindo corretamente no Chrome com os assets disponíveis em `assets/`.

---

## Sources

### Primary (HIGH confidence)
- Inspeção direta do `index.html` — linhas 243–252 (CSS Coleção), 291–295 (CSS Ambientes), 634–754 (HTML das seções), 920–951 (JS)
- Inspeção direta de `/assets/` — confirmação de existência de sf-prod-02.png, sf-prod-03.png, sf-prod-04.png
- MDN CSS `object-fit` — comportamento de `cover` com `aspect-ratio` e `padding` é spec estável desde CSS3
- MDN Media Queries Level 4 — `@media (hover: none)` é spec estável, suporte universal desde Safari 9+ / Chrome 41+

### Secondary (MEDIUM confidence)
- Comportamento de `mix-blend-mode: multiply` sobre fundo escuro — verificável visualmente; o efeito de escurecer/apagar sobre #0E0E0E é previsível pela spec (multiply multiplica valores de pixel, onde escuro × qualquer coisa = escuro)

### Tertiary (LOW confidence)
- Nenhum item nesta categoria

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — CSS puro, sem dependências externas, spec estável
- Architecture: HIGH — código existente verificado linha a linha; mudanças são localizadas e não introduzem novos padrões
- Pitfalls: HIGH — identificados por inspeção direta do código (inline style, overlap de assets, scope do gm-item)

**Research date:** 2026-04-01
**Valid until:** Indeterminado — arquivo único sem dependências externas; só invalida com alteração do index.html
