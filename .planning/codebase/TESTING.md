# Testing Patterns

**Analysis Date:** 2026-04-01

## Overview

This project has **no automated testing framework** in place. It is a static HTML landing page with minimal JavaScript and Python utility scripts. Testing is manual only.

## Test Infrastructure Status

**Testing Framework:**
- Not configured (no Jest, Vitest, Pytest, or unittest)

**Configuration Files:**
- No `jest.config.js`, `vitest.config.ts`, `pytest.ini`, or similar
- No test runner defined
- No test coverage tooling

**Test Files:**
- None found (no `*.test.*` or `*.spec.*` files)
- No dedicated test directory

## Manual Testing Approach

Since there is no automated testing, manual testing procedures are implied:

### HTML/CSS Manual Testing

**Browser Compatibility:**
- Desktop browsers: Chrome, Firefox, Safari, Edge (target modern browsers)
- Mobile browsers: Chrome Android, Safari iOS
- Responsive breakpoints: 1200px, 700px (as defined in media queries)

**Visual Testing Areas:**
- `index.html` (lines 507-922): All visual sections
  - Hero section: background gradient overlay, logo positioning, animation timing
  - Navigation: sticky/scrolled state at 60px scroll threshold
  - Product grid: responsive grid reflow (12-col → 6-col → 4-col)
  - Animations: reveal animation timing via IntersectionObserver
  - Forms: input focus states, placeholder text, layout

**Interaction Testing:**
- Scroll event triggering nav state change (`.nav.scrolled` class)
- Anchor link navigation (smooth scroll)
- Hover states on buttons, cards, images
- Image fallback display (onerror handler)
- Form submission (currently stubbed: `onsubmit="return false"`)

**Responsive Testing:**
- Desktop: Full layout with 3-column grids, 12-column product grid
- Tablet (1200px): 2-column layouts, adjusted padding
- Mobile (700px): 1-column layouts, smaller font sizes via clamp()

### Python Script Manual Testing

**Script: `baixar_imagens.py` (lines 1-100)**

**Manual Test Procedure:**
1. Ensure Chrome is installed with Google Drive cookies
2. Delete `assets/` directory to start fresh
3. Run: `python baixar_imagens.py`
4. Verify:
   - Cookies loaded successfully (check console output)
   - All 24 files downloaded (21 produto photos + 3 logos)
   - Each file size > 1000 bytes (success condition on line 84)
   - Files saved to `assets/` directory
   - Skip behavior works for existing files
   - Error handling catches timeouts, HTTP errors (line 83: `timeout=30`)

**Expected Output Pattern:**
```
Carregando cookies do Chrome...
✅ Cookies carregados!
  ✅ logo-preta.png (XX KB)
  ✅ logo-dourada.png (XX KB)
  ... [21 more files]
  ⏭  Already existing files (if rerun)
  ❌ Failed downloads (if any)

📦 Concluído: 24 baixados, 0 falhas
✨ Todas as imagens estão em assets/
```

**Script: `baixar_novos.py` (lines 1-74)**

**Manual Test Procedure:**
1. Ensure Chrome is installed with Google Drive cookies
2. Run: `python baixar_novos.py`
3. Verify:
   - Cookie loading attempt (console message on line 44)
   - All 10 new files attempted (8 sem fundo products + 2 marca images)
   - Size validation (line 61: `len(r.content) > 1000`)
   - Status code check (line 61: `r.status_code == 200`)
   - Skip existing files (line 54-57)
   - Error handling for timeouts (line 59: `timeout=30`)

**Expected Output Pattern:**
```
Carregando cookies do Chrome...
Cookies carregados!
  OK: sf-buffet.png (XX KB)
  OK: sf-prod-02.png (XX KB)
  ... [more files]
  JA EXISTE: [if rerun]
  ERRO: [if connection fails]

Concluido: X ok, Y falhas
```

## Testing What Exists

### JavaScript Functionality (`index.html` lines 907-920)

**Scroll Event Handler:**
```javascript
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });
```

**Manual Test:**
- Scroll page to >60px
- Verify: Navigation background becomes darker, padding reduces, border appears
- Scroll back to top
- Verify: Navigation returns to original state
- Test on mobile: Ensure scroll threshold works on touch devices

**Intersection Observer (Reveal Animation):**
```javascript
const revealEls = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { 
    if (e.isIntersecting) { 
      e.target.classList.add('in'); 
      observer.unobserve(e.target); 
    } 
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
revealEls.forEach(el => observer.observe(el));
```

**Manual Test:**
- Load page with reduced viewport (mobile or DevTools)
- Scroll slowly through each section
- Verify: Elements fade in from bottom when 12% visible
- Verify: Once revealed, animation doesn't repeat
- Test threshold sensitivity: 0.12 means 12% of element in viewport
- Verify margin adjustment works (bottom -40px margin affects when reveal triggers)

### Asset Loading

**Manual Test Procedure:**
1. Verify `assets/` directory contains all required images
2. Test image loading:
   - Open DevTools Network tab
   - Reload page
   - Check that all `assets/*.png` and `assets/*.jpg` load successfully
   - Verify no 404 errors
3. Test image fallbacks:
   - Temporarily delete `assets/logo-preta.png`
   - Reload page
   - Verify text fallback "ORA CONCEITO" displays in nav and footer
   - Restore image file

### Form Interactivity

**Manual Test (`#contato` form, lines 845-851):**
1. Navigate to Contact section
2. Test input fields:
   - Click "Nome" input → verify focus state (border-color lighter, background lighter)
   - Type name → verify text input works
   - Tab to next field → verify focus moves
3. Test form submission:
   - Fill all fields with valid data
   - Click "Enviar Mensagem" button
   - Note: `onsubmit="return false"` prevents actual submission (not configured as real endpoint)
   - Button hover state should transition background color

## What Should Be Tested (Recommended)

**Missing Unit Tests:**
- JavaScript scroll event threshold accuracy (>60px boundary)
- IntersectionObserver threshold configuration (0.12 accuracy)
- Image onerror handler fallback logic
- Form validation (if implemented in future)

**Missing Integration Tests:**
- Asset file download success rate (in `baixar_imagens.py`)
- Google Drive API access reliability
- Cookie authentication flow
- Timeout handling under slow connection

**Missing E2E Tests:**
- Full page load performance
- Responsive layout breakpoints
- Animation timing on mobile devices
- Navigation scroll-to-section functionality
- Social media link routing (footer, line 894-902)

## Browser Testing Checklist

### Desktop (Chrome, Firefox, Safari)
- [ ] Layout renders correctly at 1920x1080
- [ ] Scroll trigger at 60px works smoothly
- [ ] All animations execute without stuttering
- [ ] Hover effects visible on buttons and cards
- [ ] Form inputs accessible and focusable

### Tablet (iPad, 1200px width)
- [ ] Grid layouts reflow to 2-3 columns
- [ ] Product cards maintain 2px gaps
- [ ] Text remains readable
- [ ] Navigation bar collapses properly
- [ ] Touch interactions work (no hover states needed)

### Mobile (iPhone 12, 390px width)
- [ ] Single-column layout
- [ ] Text sizes readable (clamp() ensures scaling)
- [ ] Images load fully (object-fit: contain maintains aspect)
- [ ] Form inputs are tap-friendly (padding: 14px)
- [ ] Hero section scales properly with clamp(52px, 8vw, 100px)

## Performance Testing

**What Should Be Monitored:**
- Page load time (target: <2s on 4G)
- Cumulative Layout Shift (CLS) from scroll event
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Asset file sizes (images should be optimized)

**Current Tools:**
- No automated performance monitoring configured
- Manual testing via Chrome DevTools (Lighthouse, Network, Performance tabs)

## Accessibility Testing

**Checklist:**
- [ ] Keyboard navigation: Tab through all interactive elements
- [ ] Alt text: All images have descriptive alt attributes (lines 514-535)
- [ ] Color contrast: Gold (#C9A96E) on dark background meets WCAG AA
- [ ] Focus indicators: Form inputs show focus state (line 415-417)
- [ ] Semantic HTML: nav, section, form, footer tags used correctly

## Asset Download Testing

**File Size Validation:**
- Minimum: 1000 bytes (enforced in line 84 of `baixar_imagens.py`)
- Expected range: 50-500 KB per image
- Verify Google Drive download limits not hit (may require manual retry)

**Cookie Authentication:**
- Python script uses browser_cookie3 to extract Chrome cookies
- Manual test: Clear Chrome cookies → script should fail gracefully
- Fallback: Script continues without auth (line 66, plain session)
- Timeout: 30 seconds per download (line 83)

**Error Scenarios:**
- [ ] Network timeout (connection drops)
- [ ] Invalid file ID (404 response)
- [ ] Corrupted download (file size < 1000 bytes)
- [ ] Chrome not installed (import error caught, falls back)

## Testing Strategy Going Forward

**Recommended for Production:**
1. **Visual Regression Testing:** Screenshot comparison tool (Playwright, Chromatic)
2. **Link Testing:** Verify all anchor links work (`#hero`, `#sobre`, etc.)
3. **Asset Verification:** Script to verify all image files exist and load
4. **Performance Budget:** Monitor LCP and CLS on production builds
5. **Form Validation:** Add client-side validation and server-side handling when endpoint is live

---

*Testing analysis: 2026-04-01*
