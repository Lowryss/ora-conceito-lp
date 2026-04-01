# Requirements: ORA Conceito LP Redesign

**Defined:** 2026-04-01
**Core Value:** O visitante sente sofisticação nos primeiros 3 segundos — hero cinematográfico e imersivo

## v1 Requirements

### Hero

- [x] **HERO-01**: Hero exibe foto de ambiente de fundo com efeito parallax ao scroll
- [x] **HERO-02**: Overlay escuro graduado mantém legibilidade do texto sobre a foto
- [x] **HERO-03**: Logo dourada centralizada com drop-shadow sutil
- [x] **HERO-04**: Animações de entrada suaves (fadeUp) preservadas
- [x] **HERO-05**: Indicador de scroll animado visível e elegante

### Coleção

- [x] **COL-01**: Grid editorial de produtos com fundo escuro (#0E0E0E ou #181818)
- [x] **COL-02**: Fotos de produto usam `object-fit: cover` (sem padding excessivo) — produtos ocupam o espaço
- [x] **COL-03**: Hover revela label/nome do produto com transição suave
- [x] **COL-04**: Layout responsivo mantém hierarquia visual no mobile

### Ambientes

- [x] **AMB-01**: Seção Destaques/Ambientes usa fotos que mostram produtos em contexto
- [x] **AMB-02**: Cards de ambiente com overlay gradient + título elegante ao hover
- [x] **AMB-03**: Proporção das fotos consistente e bem aproveitada

### Tipografia & Espaçamentos

- [ ] **TIP-01**: Hierarquia tipográfica clara — headings grandes, body legível (mín. 14px)
- [ ] **TIP-02**: Letter-spacing e line-height consistentes nas seções
- [ ] **TIP-03**: Padding/margin das seções revisados para respiração visual adequada

### Mobile Responsivo

- [ ] **MOB-01**: Hero funciona corretamente no mobile (parallax degradado para fixed ou scroll normal)
- [ ] **MOB-02**: Grid de produtos adaptado para 1-2 colunas no mobile
- [ ] **MOB-03**: Navegação mobile com menu hambúrguer funcional
- [ ] **MOB-04**: Formulário de contato usável no mobile
- [ ] **MOB-05**: Textos legíveis sem zoom no mobile (font-size mínimo adequado)

## v2 Requirements

### Performance

- **PERF-01**: Lazy loading nas imagens
- **PERF-02**: Compressão/otimização das imagens PNG

### Funcional

- **FUNC-01**: Envio real do formulário de contato (backend/serviço externo)
- **FUNC-02**: Integração com WhatsApp no botão de contato

## Out of Scope

| Feature | Reason |
|---------|--------|
| Troca de paleta de cores | Identidade já estabelecida |
| Novas seções | Refinar existentes, não expandir |
| Backend / banco de dados | Landing page estática |
| CMS | Arquivo único sem build step |
| Novas fontes | Cormorant + Montserrat já definidos |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| HERO-01 | Phase 1 | Complete |
| HERO-02 | Phase 1 | Complete |
| HERO-03 | Phase 1 | Complete |
| HERO-04 | Phase 1 | Complete |
| HERO-05 | Phase 1 | Complete |
| COL-01 | Phase 2 | Complete |
| COL-02 | Phase 2 | Complete |
| COL-03 | Phase 2 | Complete |
| COL-04 | Phase 2 | Complete |
| AMB-01 | Phase 2 | Complete |
| AMB-02 | Phase 2 | Complete |
| AMB-03 | Phase 2 | Complete |
| TIP-01 | Phase 3 | Pending |
| TIP-02 | Phase 3 | Pending |
| TIP-03 | Phase 3 | Pending |
| MOB-01 | Phase 3 | Pending |
| MOB-02 | Phase 3 | Pending |
| MOB-03 | Phase 3 | Pending |
| MOB-04 | Phase 3 | Pending |
| MOB-05 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 20 total
- Mapped to phases: 20
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-01*
*Last updated: 2026-04-01 — Traceability confirmada após criação do roadmap*
