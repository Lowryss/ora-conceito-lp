# Roadmap: ORA Conceito LP Redesign

## Overview

Redesign em três fases da landing page estática da ORA Conceito. A fase 1 transforma o hero em ponto de entrada cinematográfico — o impacto que converte visitantes em primeiros 3 segundos. A fase 2 eleva as seções de produto e ambiente ao padrão editorial dark da marca. A fase 3 unifica tipografia e responsividade, garantindo a experiência premium em todos os dispositivos.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Hero Cinematográfico** - Substituir fundo do hero por foto de ambiente com parallax e animações de entrada (completed 2026-04-01)
- [ ] **Phase 2: Seções de Produto e Ambiente** - Refatorar grid da Coleção e seção Ambientes para padrão editorial dark
- [ ] **Phase 3: Tipografia e Responsividade** - Unificar hierarquia tipográfica e garantir experiência mobile completa

## Phase Details

### Phase 1: Hero Cinematográfico
**Goal**: O visitante sente o nível de sofisticação da marca nos primeiros 3 segundos — hero com foto de ambiente real, parallax e animações imersivas
**Depends on**: Nothing (first phase)
**Requirements**: HERO-01, HERO-02, HERO-03, HERO-04, HERO-05
**Success Criteria** (what must be TRUE):
  1. O hero exibe uma foto de ambiente real (não a logo-bg-preta.jpg) como plano de fundo que se move suavemente ao scrollar
  2. O texto do hero é legível sobre a foto — overlay escuro graduado impede conflito visual
  3. A logo dourada está centralizada com drop-shadow visível e sutil
  4. Os elementos do hero entram na tela com fadeUp suave ao carregar a página
  5. Um indicador de scroll animado é visível na parte inferior do hero
**Plans**: 2 plans

Plans:
- [ ] 01-01-PLAN.md — Substituir background do hero (foto-21.png + overlay recalibrado + drop-shadow da logo)
- [ ] 01-02-PLAN.md — Script de parallax vanilla + verificação visual completa do hero

### Phase 2: Seções de Produto e Ambiente
**Goal**: Coleção e Ambientes comunicam curadoria e sofisticação — produtos ocupam o espaço corretamente, ambiente conta uma história visual
**Depends on**: Phase 1
**Requirements**: COL-01, COL-02, COL-03, COL-04, AMB-01, AMB-02, AMB-03
**Success Criteria** (what must be TRUE):
  1. Os produtos da Coleção preenchem os cards sem espaços brancos excessivos — fundo escuro, produtos proeminentes
  2. Ao passar o mouse sobre um produto, o nome aparece com transição suave e elegante
  3. A seção Ambientes exibe fotos de produtos em contexto de uso, com proporções consistentes entre cards
  4. Ao hover nos cards de ambiente, um overlay gradient e título aparecem com transição refinada
  5. O grid da Coleção colapsa corretamente para 1-2 colunas no mobile sem quebrar a hierarquia visual
**Plans**: TBD

### Phase 3: Tipografia e Responsividade
**Goal**: A experiência é consistente e premium em desktop e mobile — hierarquia clara, textos legíveis, navegação funcional em qualquer tela
**Depends on**: Phase 2
**Requirements**: TIP-01, TIP-02, TIP-03, MOB-01, MOB-02, MOB-03, MOB-04, MOB-05
**Success Criteria** (what must be TRUE):
  1. Headings, subtítulos e corpo de texto têm tamanhos e pesos visivelmente distintos em todas as seções
  2. Letter-spacing e line-height são perceptivelmente consistentes — nenhuma seção parece "apertada" ou "solta" comparada às outras
  3. No mobile, o parallax do hero não quebra — degrada graciosamente para fundo fixo ou scroll normal
  4. O menu hambúrguer abre e fecha corretamente no mobile e permite navegação entre seções
  5. Formulário de contato é totalmente usável no mobile sem necessidade de zoom
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Hero Cinematográfico | 2/2 | Complete    | 2026-04-01 |
| 2. Seções de Produto e Ambiente | 0/TBD | Not started | - |
| 3. Tipografia e Responsividade | 0/TBD | Not started | - |
