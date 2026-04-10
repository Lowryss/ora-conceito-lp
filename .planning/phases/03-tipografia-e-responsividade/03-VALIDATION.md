---
phase: 3
slug: tipografia-e-responsividade
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-01
---

# Phase 3 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Nenhum — projeto vanilla HTML/CSS/JS sem test runner |
| **Config file** | none |
| **Quick run command** | Abrir `index.html` no Chrome |
| **Full suite command** | Checklist manual completo abaixo (Chrome + DevTools + iOS simulado) |
| **Estimated runtime** | ~10 minutos (checklist completo) |

---

## Sampling Rate

- **After every task commit:** Abrir `index.html`, verificar a seção alterada visualmente
- **After every plan wave:** Checklist manual completo
- **Before `/gsd:verify-work`:** Checklist completo deve estar verde
- **Max feedback latency:** ~3 minutos por tarefa

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Como Testar | File Exists | Status |
|---------|------|------|-------------|-----------|-------------|-------------|--------|
| TIP-01 | 01 | 1 | TIP-01 | Visual + DevTools | DevTools 1440px: section-title > body text; body text ≥ 13px | ✅ index.html | ⬜ pending |
| TIP-02 | 01 | 1 | TIP-02 | DevTools Computed | Verificar line-height 1.9 em .sobre-txt, .dif p, .pilar-d, .contato-txt | ✅ index.html | ⬜ pending |
| TIP-03 | 01 | 1 | TIP-03 | Visual scroll | Scroll desktop 1440px — seções respiram, nenhuma parece apertada | ✅ index.html | ⬜ pending |
| MOB-01 | 02 | 1 | MOB-01 | Mobile iOS | DevTools 375px: hero preenche tela, sem parallax ao scroll, sem overflow | ✅ index.html | ⬜ pending |
| MOB-02 | 02 | 1 | MOB-02 | Visual mobile | DevTools 375px: grid Coleção 2 colunas, sem imagens transbordando | ✅ index.html | ⬜ pending |
| MOB-03 | 03 | 2 | MOB-03 | Interação mobile | 375px: hambúrguer → overlay abre; link → overlay fecha + smooth scroll | ✅ index.html | ⬜ pending |
| MOB-04 | 03 | 2 | MOB-04 | iOS zoom test | iOS Safari 375px: focar input → SEM zoom automático na viewport | ✅ index.html | ⬜ pending |
| MOB-05 | 02 | 1 | MOB-05 | DevTools Computed | 375px: body text ≥ 14px em todas as seções | ✅ index.html | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements. Projeto vanilla sem test runner — todas as verificações são manuais no browser.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Hierarquia tipográfica visível | TIP-01 | CSS visual | DevTools Elements 1440px: comparar section-title vs body text |
| Line-height 1.9 consistente | TIP-02 | CSS computed | DevTools Computed: verificar line-height em cada seletor de body text |
| Hero mobile sem quebra | MOB-01 | iOS-specific | DevTools device toolbar iPhone SE 375px: scroll hero sem movimento |
| Menu hambúrguer funcional | MOB-03 | Interação touch | DevTools 375px: abrir/fechar overlay, clicar links, verificar smooth scroll |
| Sem zoom iOS no form | MOB-04 | Safari-specific | Simulador iOS ou DevTools com UA Safari: focar inputs do form |
| Body text ≥ 14px mobile | MOB-05 | CSS computed | DevTools 375px: inspecionar font-size de .sobre-txt, .dif p, .pilar-d |

---

## Validation Sign-Off

- [ ] All tasks have manual verify instructions
- [ ] Sampling continuity: cada tarefa tem verify detalhado
- [ ] No watch-mode flags
- [ ] Feedback latency < 180s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
