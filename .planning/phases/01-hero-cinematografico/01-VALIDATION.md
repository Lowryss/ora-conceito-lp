---
phase: 1
slug: hero-cinematografico
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-01
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Manual visual inspection (static HTML/CSS/JS — no test framework) |
| **Config file** | none |
| **Quick run command** | `open index.html` (browser) |
| **Full suite command** | Manual checklist below |
| **Estimated runtime** | ~2 minutes manual review |

---

## Sampling Rate

- **After every task commit:** Open `index.html` in browser, verify hero visually
- **After every plan wave:** Run full manual checklist
- **Before `/gsd:verify-work`:** Full checklist must pass
- **Max feedback latency:** ~30 seconds (open file in browser)

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Manual Steps | Status |
|---------|------|------|-------------|-----------|--------------|--------|
| 1-01-01 | 01 | 1 | HERO-01 | visual | Hero fundo é foto real (não logo preta) ao abrir index.html | ⬜ pending |
| 1-01-02 | 01 | 1 | HERO-01 | visual | Foto se move ao scrollar (parallax visível) | ⬜ pending |
| 1-01-03 | 01 | 1 | HERO-02 | visual | Texto do hero legível sobre foto — overlay escuro presente | ⬜ pending |
| 1-01-04 | 01 | 1 | HERO-03 | visual | Logo dourada centralizada com drop-shadow visível | ⬜ pending |
| 1-01-05 | 01 | 1 | HERO-04 | visual | Elementos entram com fadeUp ao carregar | ⬜ pending |
| 1-01-06 | 01 | 1 | HERO-05 | visual | Indicador scroll visível na base do hero | ⬜ pending |
| 1-01-07 | 01 | 2 | HERO-01 | visual | Mobile: fundo fixo (sem parallax quebrado em iOS) | ⬜ pending |
| 1-01-08 | 01 | 2 | HERO-02 | visual | Mobile: overlay legível em tela pequena | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Não se aplica — projeto estático sem framework de testes.

*Existing infrastructure covers all phase requirements (manual browser verification).*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Parallax suave no scroll | HERO-01 | Efeito visual não automatizável | Abrir index.html, scrollar devagar no hero, confirmar que fundo move-se mais lentamente que o conteúdo |
| Legibilidade do texto | HERO-02 | Percepção visual subjetiva | Verificar que headline e subtítulo são legíveis sem esforço sobre a foto de fundo |
| Drop-shadow da logo | HERO-03 | Percepção visual subjetiva | Confirmar que logo dourada tem contorno visível sobre a foto |
| Parallax desativado no mobile | HERO-01 | Requer device/DevTools | Redimensionar para mobile em DevTools, confirmar fundo fixo (não parallax) |
| Animações fadeUp | HERO-04 | Efeito temporal | Recarregar página, confirmar que elementos entram sequencialmente do baixo para cima |

---

## Validation Sign-Off

- [ ] Todas as tarefas têm verificação manual com passos claros
- [ ] Parallax verificado em desktop e mobile (DevTools)
- [ ] Overlay testado com foto real (não logo-bg-preta.jpg)
- [ ] Animações fadeUp verificadas em recarga limpa
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
