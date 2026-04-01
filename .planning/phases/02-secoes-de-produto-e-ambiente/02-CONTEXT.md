# Phase 2: Seções de Produto e Ambiente - Context

**Gathered:** 2026-04-01
**Status:** Ready for planning

<domain>
## Phase Boundary

Refatorar grid da Coleção (#colecao) e seção Ambientes (#destaques) para padrão editorial dark. Produtos devem ocupar o espaço corretamente, ambientes comunicam curadoria com overlay elegante. Tipografia e responsividade geral ficam na Fase 3.

</domain>

<decisions>
## Implementation Decisions

### object-fit e padding dos cards
- Trocar `object-fit: contain` por `object-fit: cover` com leve padding (12–16px) em ambas as seções
- Remover `mix-blend-mode: multiply` das imagens — com fundo escuro (#0E0E0E), multiply escurece/apaga o produto
- Manter `aspect-ratio` atuais dos cards da Coleção (1:1 para s3, 3:4 para tall, 16:9 para wide)
- Cards de Ambientes: cover com leve padding, manter aspect-ratio 4/5 atual

### Fotos da seção Ambientes
- Trocar as fotos atuais (sf-buffet.png, foto-10.png, sf-estante.png) por: sf-prod-02.png, sf-prod-03.png, sf-prod-04.png
- Critério: fotos sf-prod-* não usadas ainda nos Ambientes, evitando repetição visual com a Coleção
- sf-buffet.png permanece apenas na Coleção (não há repetição entre seções)

### Títulos dos cards de Ambientes
- Manter estilo atual: [Nome da Peça] + adjetivo premium
- Ex: "Poltrona Exclusiva", "Mesa Contemporânea", "Aparador Premium"
- Tag de categoria mantida acima do título (ex: "Sala de Estar")

### Distribuição de fotos entre seções
- Coleção: manter fotos atuais (sf-buffet, sf-cadeira-f, sf-cadeira-t, sf-estante, foto-10, sf-prod-03, foto-01, sf-prod-05, foto-06, foto-13, sf-prod-08, foto-05, foto-09, foto-15)
- Ambientes: trocar para sf-prod-02, sf-prod-03, sf-prod-04
- Nenhuma foto duplicada entre as duas seções após a troca

### Hover/labels no mobile (touch)
- Labels da Coleção (`.pc-label`): sempre visíveis em dispositivos touch — `opacity: 1` fixo via `@media (hover: none)`
- Overlays dos Ambientes (`.dest-overlay`): mesma lógica — sempre visíveis em touch
- Desktop mantém comportamento atual (opacity 0 → 1 no hover)
- Detectar touch via `matchMedia('(hover: none)')` — padrão já usado no parallax da Fase 1

### Claude's Discretion
- Valor exato do padding cover (entre 12px e 16px — escolher pelo visual)
- Títulos/labels exatos dos novos cards de Ambientes (sf-prod-02/03/04)
- Ajuste fino do gradiente dos overlays se necessário com as novas fotos

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `.pc-label`: label hover já implementado na Coleção — só precisa de ajuste opacity no mobile
- `.dest-overlay`: overlay gradient + título nos Ambientes já implementado — mesmo ajuste mobile
- `isTouch` via `matchMedia('(hover: none)')`: padrão de detecção touch já no código (parallax Fase 1) — reusar

### Established Patterns
- `mix-blend-mode: multiply` atual nas `.pc img` e `.dest-item img` — REMOVER (incompatível com fundo escuro)
- Reveal animations (`reveal`, `d1`, `d2`, `d3`) já em todos os cards — manter sem alteração
- `object-fit: contain` + `padding: 36px` na Coleção e `padding: 28px 20px` nos Ambientes — SUBSTITUIR por cover + padding 12–16px

### Integration Points
- Seção `#colecao`: CSS em `.pc img` (linha ~245) e `.pc-label` (linha ~253)
- Seção `#destaques`: CSS em `.dest-item img` (linha ~293) e `.dest-overlay` (linha ~297)
- HTML dos 3 cards de Ambientes: src das imagens em `#destaques .dest-item img` (linhas ~732–760)
- JS de touch: adicionar lógica após o bloco `isTouch` do parallax (linha ~937)

</code_context>

<specifics>
## Specific Ideas

- O `mix-blend-mode: multiply` foi provavelmente pensado para fundo branco — com o redesign para fundo escuro, ele é o maior bloqueador visual atual
- A detecção `matchMedia('(hover: none)')` já usada no parallax é o padrão correto para iOS Safari — reutilizar para os labels mobile

</specifics>

<deferred>
## Deferred Ideas

- Nenhuma ideia fora do escopo surgiu durante a discussão

</deferred>

---

*Phase: 02-secoes-de-produto-e-ambiente*
*Context gathered: 2026-04-01*
