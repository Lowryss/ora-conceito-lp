# Coding Conventions

**Analysis Date:** 2026-04-01

## Overview

This is a static HTML landing page project for ORA Conceito luxury design brand. The codebase consists of:
- Single-page HTML (`index.html`) - Primary deliverable
- Two Python utility scripts for asset management (`baixar_imagens.py`, `baixar_novos.py`)
- No JavaScript frameworks, TypeScript, or npm dependencies

## Naming Patterns

**Files:**
- Main page: `index.html` (lowercase, no underscores)
- Python scripts: kebab-case with descriptive Portuguese names
  - `baixar_imagens.py` - Download images helper
  - `baixar_novos.py` - Download new images helper
- Asset files: kebab-case (sf-buffet.png, foto-01.png, etc.)

**HTML IDs & Classes:**
- Element IDs: kebab-case, semantic names
  - `#nav`, `#hero`, `#sobre`, `#colecao`, `#numeros`, `#destaques`, `#diferenciais`, `#manifesto`, `#galeria`, `#contato`
- CSS Classes: kebab-case with semantic prefixes
  - Navigation: `.nav-logo`, `.nav-links`, `.btn-nav`
  - Sections: `.section-tag`, `.section-title`, `.section-header`
  - Cards: `.pc` (product card), `.dif` (diferencial), `.dest-item` (destaque item)
  - Form elements: `.form`, `.form-g`, `.form-submit`

**CSS Variables:**
- Prefixed with `--` (CSS custom properties)
- Semantic naming: `--preto`, `--grafite`, `--dourado`, `--offwhite`
- Two-tier naming for variations: `--dourado`, `--dourado2`

**Python Variables:**
- CONSTANTS: UPPERCASE (e.g., `ASSETS`, `FILES`, `USER_AGENT`)
- Functions: snake_case (e.g., `pip_install`)
- Local variables: snake_case (e.g., `ok`, `fail`, `fid`, `dest`)

## Code Style

**HTML:**
- Semantic tags (section, form, footer, nav)
- Self-closing tags use `/>` format
- Attributes quoted in double quotes
- SVG used inline for icons (viewBox format)
- No minification in source

**CSS (Embedded in `<style>`):**
- Property order: positional properties first, then display, then styling
- Line length: varies (some long property chains like backgrounds and gradients)
- Vendor prefixes: None used (modern browser target)
- Media queries: Mobile-first breakpoints (1200px, 700px)
- CSS Grid heavily used for layout
- Custom properties (CSS variables) for theming

**Python:**
- Minimal imports grouped at top
- Try/except blocks for import fallbacks
- Lazy dependency installation via `pip_install()`
- No type hints (Python 3.x without annotations)
- String formatting uses f-strings where present, simple concatenation elsewhere
- Exception handling prioritizes user-friendly messages with emojis

## Form & Structure

**HTML Organization:**
- Semantic sections: NAV → HERO → SOBRE → NUMEROS → COLECAO → DESTAQUES → DIFERENCIAIS → MANIFESTO → GALERIA → CONTATO → FOOTER
- Each section marked with HTML comment: `<!-- SECTION NAME -->`
- Consistent use of wrapper divs with class suffixes matching section function

**CSS Organization:**
- Global resets at top (box-sizing, margins, padding)
- CSS variables definition in `:root`
- Layout sections clearly marked with `/* ─── SECTION NAME ─── */` comments
- Components grouped logically (buttons, cards, forms)
- Responsive media queries at bottom
- Animations defined before media queries

**Python Organization:**
- Module docstring at top
- Imports with fallback installation
- Constants definition
- Main script logic
- Success/completion summary at end

## Import Organization

**HTML:**
- Google Fonts preconnect links first
- Font stylesheet links
- No module imports (single-file design)

**CSS:**
- Google Fonts imported via `@import` (implicit in link)
- No external CSS files (all embedded)
- No preprocessor (Sass/Less)

**Python:**
- Standard library first: `os`, `sys`, `subprocess`
- External dependencies: `requests`, `browser_cookie3`
- Lazy import pattern (import in try/except blocks)

## Color & Typography System

**Colors (CSS Variables):**
```
--preto:    #0E0E0E (primary dark)
--grafite:  #181818 (secondary dark)
--grafite2: #222222 (tertiary dark)
--dourado:  #C9A96E (accent gold)
--dourado2: #a88545 (accent gold darker - hover state)
--offwhite: #F2EFE9 (primary light)
```

**Fonts:**
```
--serif: 'Cormorant Garamond', Georgia, serif
--sans:  'Montserrat', sans-serif
```

**Typography Scale:**
- Headlines: Serif family, 300-500 weight, clamp() for responsive sizing
- Body: Sans-serif, 300-400 weight, typically 12-13.5px
- UI Labels: 9-10px uppercase with letter-spacing
- Line heights: 1.05 (tight, headlines), 1.9-2.1 (loose, body text)

## Animation & Transitions

**Pattern: Fade Up Animation**
```css
@keyframes fadeUp { 
  to { opacity: 1; transform: translateY(0); } 
}
```

**Pattern: Staggered Delays**
- Elements use `.d1` through `.d5` classes for staggered animation delays
- Base animation: 0.9s duration, easing: ease
- Delays cascade: 0.1s increments starting from 0.1s

**Scroll Reveal Pattern:**
- `.reveal` class: Initial state (opacity: 0, translateY: 24px)
- `.reveal.in` class: Final state (added by JavaScript IntersectionObserver)
- Uses threshold: 0.12, rootMargin: '0px 0px -40px 0px'

**Hover Effects:**
```css
/* Scale & lift on hover */
.pc:hover img { transform: scale(1.05); }
.pc:hover .pc-label { opacity: 1; }

/* Background color shifts */
.dif:hover { background: #272727; }

/* Color transition */
.nav-links a:hover { color: var(--dourado); }
```

## Spacing & Layout

**Vertical Spacing:**
- Section padding: 80px-120px (desktop), scaled for tablet/mobile
- Inner margins: 40px-72px padding
- Component gaps: 18-28px

**Grid Systems:**
- 12-column grid for product editorial: `grid-template-columns: repeat(12, 1fr)`
- Product cards use span classes: `.s3` (span 3), `.s4`, `.s6`
- 3-column grids for differentials: `repeat(3, 1fr)`
- Responsive breakpoints adjust spans and grid columns

## Comments & Documentation

**Inline Comments:**
- Section separators: `/* ─── SECTION NAME ─── */`
- Inline labels for semantic meaning (e.g., `<!-- NAV -->`, `<!-- HERO -->`)
- No verbose comments; structure is self-documenting

**Python Comments:**
- Module docstring at top: triple quotes with brief description
- No inline comments in main logic
- Labels for key sections: `# Instalar dependências`, `# Todos os arquivos`, `# Novas imagens`

## Form Handling

**HTML Form:**
- Located in `#contato` section (`index.html` lines 845-851)
- No action attribute: `onsubmit="return false"` (placeholder form)
- Input types: text, email, tel, textarea
- Labels use `.form-g` wrapper with semantic label/input pairing
- No validation attributes (client-side validation not implemented)

## Error Handling

**Python Pattern:**
- Try/except for imports with automatic dependency installation
- Session fallback: If cookie loading fails, create session without auth
- HTTP error handling: Check status code (200) and content size (>1000 bytes)
- User-friendly error output with emoji indicators
  - ✅ Success
  - ❌ Failure
  - ⚠️  Warning
  - ⏭ Skip
  - 📦 Summary

**HTML Pattern:**
- Image fallback using `onerror` attribute: Display text if image fails
  - Example: `<img src="logo.png" onerror="this.style.display='none';this.nextElementSibling.style.display='block'"/>`
  - Fallback text: `<span class="nav-logo-txt" style="display:none">ORA CONCEITO</span>`

## Logging

**Python:**
- Console output using `print()` statements
- Emoji-prefixed messages for visual scanning
- Progress tracking: Counter variables `ok` and `fail`
- Final summary: Completion status with file count

**JavaScript:**
- No logging implementation (no console statements in production code)

## Special Patterns

**Aspect Ratio Handling:**
- Uses `aspect-ratio` CSS property directly
- Examples: `aspect-ratio: 1` (square), `aspect-ratio: 16/9` (wide), `aspect-ratio: 3/4` (tall)
- Combined with `object-fit: contain` for image scaling

**SVG Icons:**
- Inline SVG in HTML (no external icon library)
- Consistent viewBox: `"0 0 24 24"` or custom per icon
- No fill on icon paths: `fill: none`
- Stroke-based rendering: `stroke-width: 1.3-1.5`, `stroke-linecap: round`

**Accessibility:**
- Semantic HTML (nav, section, form, footer)
- Alt text on images
- aria-label on social links
- Color contrast maintained with gold (#C9A96E) on dark backgrounds

---

*Convention analysis: 2026-04-01*
