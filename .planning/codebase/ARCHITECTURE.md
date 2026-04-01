# Architecture

**Analysis Date:** 2026-04-01

## Pattern Overview

**Overall:** Single-Page Landing Site (Static HTML with CSS and Vanilla JavaScript)

**Key Characteristics:**
- Monolithic HTML file with embedded CSS and JavaScript
- Semantic section-based layout using native HTML elements
- Progressive enhancement with intersection observer for scroll-triggered animations
- Mobile-first responsive design with CSS custom properties for theming
- No build tools, frameworks, or bundlers required

## Layers

**Presentation (View):**
- Purpose: Render visual content and UI components
- Location: `index.html` (lines 512-905)
- Contains: HTML semantic sections, form controls, navigation, product grid, gallery
- Depends on: CSS styling, JavaScript interactivity
- Used by: Browser rendering engine

**Styling (CSS):**
- Purpose: Visual presentation, animations, responsive layout, color theming
- Location: `index.html` (lines 11-511, embedded `<style>` tag)
- Contains: Design system with CSS custom properties, animations, grid layouts, responsive breakpoints
- Depends on: Google Fonts (Cormorant Garamond, Montserrat)
- Used by: HTML elements with class names

**Interactivity (JavaScript):**
- Purpose: DOM manipulation, event handling, scroll-based animations
- Location: `index.html` (lines 907-920, embedded `<script>` tag)
- Contains: Navigation scroll detection, intersection observer for reveal animations
- Depends on: Browser Intersection Observer API, Window scroll events
- Used by: Browser event loop

**Data & Assets:**
- Purpose: Store static images and brand materials
- Location: `assets/` directory
- Contains: Logo variations (logo-preta.png, logo-dourada.png, logo-bg-preta.jpg), product photography (21 fotos), furniture backgrounds (sf-*.png), room brand (marca-room.PNG)
- Depends on: Google Drive for source (via Python download scripts)
- Used by: HTML image references in `<img>` and CSS `background-image` properties

**Utility Scripts (Python):**
- Purpose: Asset management and image synchronization
- Location: `baixar_imagens.py`, `baixar_novos.py`
- Contains: Google Drive downloader with browser cookie authentication
- Depends on: Python 3, requests library, browser-cookie3 library, Chrome browser cookies
- Used by: Development workflow for keeping assets synchronized

## Data Flow

**Page Load:**

1. Browser requests `index.html`
2. HTML parser encounters `<link>` for Google Fonts (preconnect optimization)
3. CSS loads and applies styles to semantic sections
4. JavaScript registers IntersectionObserver and scroll listener
5. Images load from `assets/` directory (lazy-loaded by browser)
6. Page becomes interactive

**User Interaction - Scroll Navigation:**

1. User scrolls page
2. `scroll` event fires on window
3. JavaScript checks `window.scrollY > 60`
4. Navigation bar toggles `scrolled` class (background and styling change)
5. CSS applies hover states and transitions

**User Interaction - Scroll Reveal:**

1. User scrolls to section containing `.reveal` elements
2. IntersectionObserver detects element intersection (threshold 0.12, rootMargin -40px bottom)
3. `in` class added to element
4. CSS animation triggers (fadeUp, staggered with `d1`, `d2`, `d3`, `d4` delay classes)

**Form Submission:**

1. User fills contact form (no backend integration currently)
2. Form `onsubmit="return false"` prevents default behavior
3. No data transmission (form is UI placeholder)

**State Management:**

- Navigation state: CSS class toggle (`nav.scrolled`)
- Reveal state: CSS class toggle (`.in` on reveal elements)
- No persistent state or client-side storage
- No component state management
- Animations managed entirely by CSS transitions and keyframes

## Key Abstractions

**Section Component Pattern:**

```html
<section id="[sectionId]">
  <div class="section-header">
    <p class="section-tag reveal">Label</p>
    <h2 class="section-title reveal d1">Title with <em>Emphasis</em></h2>
  </div>
  <div class="[section-content]">
    <!-- Content -->
  </div>
</section>
```

- Purpose: Consistent sectional layout with header and content
- Examples: `#sobre`, `#colecao`, `#numeros`, `#destaques`, `#diferenciais`, `#galeria`
- Pattern: Structural convention for major sections of the page

**Product Card Pattern:**

```html
<div class="pc s3 reveal d1">
  <img src="assets/foto-01.png" alt="Product" />
  <div class="pc-label"><span>Cadeiras</span><svg>...</svg></div>
</div>
```

- Purpose: Display furniture products in masonry-style grid
- Examples: 15+ product cards in `#colecao`
- Pattern: Grid sizing classes (s3, s4, s6) control grid position and span

**Reveal Animation Abstraction:**

```html
<div class="reveal d2">Content</div>
```

- Purpose: Lazy-load animations for elements as they enter viewport
- Examples: Applied to all major content elements
- Pattern: IntersectionObserver adds `in` class → CSS animation triggers; delay classes (d1, d2, d3, d4) create stagger effect

**Color Theme System:**

```css
:root {
  --preto:    #0E0E0E;
  --grafite:  #181818;
  --grafite2: #222222;
  --dourado:  #C9A96E;
  --dourado2: #a88545;
  --offwhite: #F2EFE9;
  --serif: 'Cormorant Garamond', Georgia, serif;
  --sans:  'Montserrat', sans-serif;
}
```

- Purpose: Centralized color and font management
- Examples: Used throughout CSS for consistency (dark luxury aesthetic)
- Pattern: CSS custom properties enable theme updates without code changes

## Entry Points

**Primary Entry Point - Browser:**
- Location: `index.html`
- Triggers: User navigates to domain or opens file in browser
- Responsibilities: Render full page content, apply styling, initialize JavaScript functionality

**Secondary Entry Points - Hash Navigation:**
- Locations: Navigation links and CTAs throughout page (`#hero`, `#sobre`, `#colecao`, `#contato`, etc.)
- Triggers: User clicks navigation links or scroll position
- Responsibilities: Browser's native anchor navigation scrolls to section with matching ID

**Asset Management Entry Points - Development:**
- Locations: `baixar_imagens.py`, `baixar_novos.py`
- Triggers: Manual execution by developer (`python baixar_imagens.py`)
- Responsibilities: Download images from Google Drive and populate `assets/` directory

## Error Handling

**Strategy:** Graceful degradation with fallback fonts and images

**Patterns:**

- **Missing Images:** Browser displays alt text or broken image icon; layout does not break due to CSS max-width constraints
- **Font Loading Failures:** System fonts (Georgia, sans-serif) serve as fallbacks to Google Fonts
- **JavaScript Disabled:** Page remains fully readable and navigable; scroll animations simply don't trigger (IntersectionObserver not supported in very old browsers, but page is still functional)
- **Network Issues:** CSS and HTML load first; images may fail but don't cascade failures
- **Form Submission:** `onsubmit="return false"` prevents navigation away on form submit (placeholder behavior)

## Cross-Cutting Concerns

**Responsive Design:**
- Approach: CSS media queries and `clamp()` functions for fluid typography
- Key breakpoint: Tablet/mobile adjustments in CSS for navigation, hero title size, grid layouts
- Example: `.hero-h1 { font-size: clamp(52px, 8vw, 100px); }`

**Accessibility:**
- Navigation: Semantic `<nav>`, `<section>`, `<footer>` elements
- Links: All CTAs use `<a>` tags; buttons use `<button>` type
- Aria labels: Social icons have `aria-label` attributes
- Alt text: Images have `alt` attributes (though some missing in product cards)
- Form labels: All form inputs have explicit `<label>` elements with `for` attributes
- Color contrast: Dark background + gold accents + light text meet WCAG AA standards

**Performance:**
- Images: Local asset loading (no external CDN dependency except Google Fonts)
- Preconnect: `rel="preconnect"` hints for Google Fonts reduce latency
- Lazy Loading: Browser native lazy-loading could be added to images; currently all load immediately
- CSS: Single stylesheet (embedded) - no HTTP overhead, critical CSS loaded inline
- JavaScript: Minimal (52 lines); no frameworks or heavy dependencies
- Animations: CSS-based (performant) rather than JavaScript-driven

**SEO:**
- Meta tags: Title, description present
- Semantic HTML: Proper heading hierarchy, sections
- Schema markup: Not present (could be added)
- Open Graph: Not present (could be added for social sharing)
- Sitemap/robots.txt: Not present

**Styling & Theming:**
- Dark luxury aesthetic: Black background, gold accents, elegant serif fonts
- Two-font system: Serif (Cormorant Garamond) for headings, sans (Montserrat) for body
- Animation: Fade-in + slide-up with staggered delays (`fadeUp` keyframes, delay classes)
- Consistent spacing: Padding/margin use relative units for responsiveness
