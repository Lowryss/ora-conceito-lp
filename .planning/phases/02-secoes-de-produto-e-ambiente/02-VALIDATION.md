---
phase: 2
slug: secoes-de-produto-e-ambiente
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-01
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Nenhum — projeto HTML/CSS/JS vanilla sem test runner |
| **Config file** | none |
| **Quick run command** | Abrir `index.html` no browser e inspecionar visualmente |
| **Full suite command** | Checklist manual completo abaixo |
| **Estimated runtime** | ~5 minutos (cheklist manual completo) |

---

## Sampling Rate

- **After every task commit:** Abrir `index.html` no Chrome, navegar até a seção alterada, verificar visualmente
- **After every plan wave:** Checklist manual completo (todas as seções)
- **Before `/gsd:verify-work`:** Checklist manual completo deve estar verde
- **Max feedback latency:** ~2 minutos por tarefa (abrir browser + inspecionar)

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| COL-01 | 01 | 1 | COL-01 | Visual manual | DevTools: inspecionar `background` de `#colecao` e `.pc` — sem áreas brancas | ✅ index.html | ⬜ pending |
| COL-02a | 01 | 1 | COL-02 | Visual manual | Scroll até #colecao, fotos preenchem os cards sem produto pequeno/flutuando | ✅ index.html | ⬜ pending |
| COL-02b | 01 | 1 | COL-02 | Inspeção DevTools | Elements panel: confirmar ausência de `mix-blend-mode` em `.pc img` | ✅ index.html | ⬜ pending |
| COL-03a | 01 | 1 | COL-03 | Interação desktop | Mouse hover sobre cada card da Coleção — label aparece suavemente | ✅ index.html | ⬜ pending |
| COL-03b | 01 | 1 | COL-03 | Inspeção mobile | DevTools device toolbar (iPhone SE) — labels visíveis sem hover | ✅ index.html | ⬜ pending |
| COL-04 | 01 | 1 | COL-04 | Responsive manual | DevTools: 700px width — grid colapsa para 1-2 colunas sem quebra | ✅ index.html | ⬜ pending |
| AMB-01 | 02 | 1 | AMB-01 | Inspeção HTML | DevTools Elements: verificar src dos 3 `<img>` em `#destaques` = sf-prod-02/03/04 | ✅ index.html | ⬜ pending |
| AMB-02a | 02 | 1 | AMB-02 | Interação desktop | Mouse hover sobre cada card de Ambientes — overlay + título aparecem | ✅ index.html | ⬜ pending |
| AMB-02b | 02 | 1 | AMB-02 | Inspeção mobile | DevTools device toolbar — overlay/título visível sem interação | ✅ index.html | ⬜ pending |
| AMB-03 | 02 | 1 | AMB-03 | Visual manual | 3 cards lado a lado com mesma altura visual — proporções 4/5 consistentes | ✅ index.html | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements.

Não há framework de testes — todas as verificações são manuais no browser.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Produtos preenchem cards sem espaço branco | COL-01, COL-02 | CSS visual — impossível automatizar sem screenshot diff | Scroll até #colecao no Chrome, verificar que nenhum produto flutua no centro com fundo visível ao redor |
| mix-blend-mode removido | COL-02 | Inspeção de propriedade CSS | DevTools → Elements → .pc img → Computed styles → confirmar ausência de mix-blend-mode |
| Hover labels desktop | COL-03 | Interação de mouse | Hover em cada card — label dourado deve aparecer com transição suave |
| Labels visíveis mobile | COL-03 | Comportamento touch | DevTools device toolbar (iPhone SE 375px) — labels devem estar visíveis sem hover |
| Fotos Ambientes trocadas | AMB-01 | Verificação de src HTML | DevTools Elements → #destaques → 3 imgs → confirmar src = sf-prod-02/03/04 |
| Hover overlay Ambientes desktop | AMB-02 | Interação de mouse | Hover em cada card de Ambiente — overlay gradient + título aparecem |
| Overlay Ambientes mobile | AMB-02 | Comportamento touch | DevTools mobile — overlay de todos os 3 cards de Ambientes visível sem interação |
| Proporções consistentes Ambientes | AMB-03 | Visual | 3 cards com mesma altura aparente, sem distorção das fotos sf-prod-* |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 120s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
