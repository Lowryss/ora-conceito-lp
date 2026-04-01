# ORA Conceito — Landing Page Redesign

## What This Is

Landing page estática para a ORA Conceito, marca de design de interiores e mobiliário de alto padrão. A página apresenta a identidade da marca, coleção de produtos, ambientes e formulário de contato. O objetivo é transmitir sofisticação, curadoria e experiência premium para atrair clientes de alto padrão.

## Core Value

O visitante deve sentir o nível de sofisticação da marca nos primeiros 3 segundos — o hero e o primeiro scroll precisam ser cinematográficos e imersivos.

## Requirements

### Validated

- ✓ Paleta escura com dourado (--preto #0E0E0E, --dourado #C9A96E) — existente
- ✓ Tipografia: Cormorant Garamond + Montserrat — existente
- ✓ Navegação fixa com blur ao scroll — existente
- ✓ Animações de reveal (fadeUp) — existente
- ✓ Seções: Hero, Sobre, Números, Coleção, Manifesto, Ambientes, Diferenciais, Galeria, Contato, Footer — existente

### Active

- [ ] Hero com efeito parallax e foto de ambiente impactante como fundo
- [ ] Coleção com layout editorial dark, produtos centralizados com fundo escuro
- [ ] Seção Ambientes com fotos de lifestyle/ambiente bem aproveitadas
- [ ] Tipografia revisada — tamanhos, pesos e espaçamentos mais consistentes
- [ ] Responsividade mobile corrigida e refinada
- [ ] Design geral mais luxuoso e clean dentro da identidade escuro/dourado

### Out of Scope

- Backend / envio real do formulário — apenas frontend estático
- Novas seções não existentes — refinar o que já existe
- Troca da identidade visual (cores, fontes) — manter DNA da marca
- CMS ou painel admin — página estática pura

## Context

- Stack: HTML + CSS + JS vanilla, arquivo único `index.html`
- Assets: 21 fotos PNG de produtos/ambientes em `/assets/`, logos dourada e preta, `logo-bg-preta.jpg` (imagem atual do hero — pequena, pouco impactante)
- Fotos relevantes para hero/parallax: `foto-21.png` (maior), `sf-buffet.png`, `sf-prod-02.png`, `sf-prod-03.png`
- Problema central do hero: background é `logo-bg-preta.jpg` (25KB, só logo no escuro) — sem foto de ambiente
- Coleção usa `object-fit: contain` com padding — produtos ficam pequenos no grid

## Constraints

- **Tech Stack**: HTML/CSS/JS puro — sem frameworks, sem build step
- **Arquivo único**: todo código em `index.html` (CSS inline + JS inline)
- **Assets existentes**: usar apenas fotos já em `/assets/` — não adicionar novas
- **Performance**: imagens já são PNG grandes — não piorar carregamento

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Manter escuro/dourado | Identidade já estabelecida e funcional | — Pending |
| Parallax no hero via CSS/JS | Sem frameworks, precisa ser vanilla JS | — Pending |
| Produto centralizado no escuro | Estilo editorial studio, mais sofisticado | — Pending |

---
*Last updated: 2026-04-01 após inicialização do projeto*
