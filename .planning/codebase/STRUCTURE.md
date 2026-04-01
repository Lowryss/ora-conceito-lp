# Codebase Structure

**Analysis Date:** 2026-04-01

## Directory Layout

```
ORA CONCEITO/
├── index.html                  # Main landing page (single entry point, ~900 lines)
├── assets/                     # Static image assets
│   ├── logo-preta.png         # Black logo
│   ├── logo-dourada.png       # Gold logo
│   ├── logo-bg-preta.jpg      # Hero background
│   ├── foto-01.png to foto-21.png  # Product photography (21 images)
│   ├── sf-buffet.png          # Furniture: buffet (transparent background)
│   ├── sf-cadeira-f.png       # Furniture: chair front (transparent background)
│   ├── sf-cadeira-t.png       # Furniture: chair top (transparent background)
│   ├── sf-estante.png         # Furniture: shelving (transparent background)
│   ├── sf-prod-02.png to sf-prod-08.png  # Product variations (transparent background)
│   └── marca-room.PNG         # Room brand mark
├── baixar_imagens.py          # Asset downloader script (main batch)
├── baixar_novos.py            # Asset downloader script (new/variant images)
└── .git/                       # Git repository (not committed to docs)
```

## Directory Purposes

**Root Directory (`/`):**
- Purpose: Landing page entry point and project root
- Contains: Single HTML file (self-contained with embedded CSS and JavaScript), Python utility scripts
- Key files: `index.html` (application core)

**`assets/`:**
- Purpose: Store all static images and visual media
- Contains: PNG and JPG files (logos, product photography, furniture backgrounds, brand marks)
- Key files: 
  - `logo-dourada.png`, `logo-preta.png` (brand identity)
  - `logo-bg-preta.jpg` (hero section background)
  - `foto-01.png` through `foto-21.png` (product showcase images)
  - `sf-*.png` (furniture with transparent backgrounds for overlay compositions)

## Key File Locations

**Entry Points:**
- `index.html`: Single-file application; serves as HTML structure, embedded styles, and embedded JavaScript

**Configuration:**
- None (no build config, no env files, no package managers required)

**Core Logic:**
- `index.html` (embedded `<style>` tag, lines 11-511): All CSS
- `index.html` (embedded `<script>` tag, lines 907-920): All JavaScript

**Asset Management:**
- `assets/`: All images referenced via relative paths
- `baixar_imagens.py`: Python script to download logos and product photos from Google Drive (21 images)
- `baixar_novos.py`: Python script to download variant/transparent-background images from Google Drive (9 images)

**Development Utilities:**
- `baixar_imagens.py`: Batch downloader for initial asset setup; uses Google Drive file IDs and browser cookies for authentication
- `baixar_novos.py`: Downloader for new/updated assets; manages transparent-background variants (sf-*.png) and room brand

## Naming Conventions

**Files:**
- HTML: Single `index.html` (monolithic pattern)
- Images: Kebab-case naming with semantic prefixes
  - Logos: `logo-[variant].ext` (e.g., `logo-preta.png`, `logo-dourada.png`)
  - Product photos: `foto-[number].png` (sequential, 01-21)
  - Furniture (transparent): `sf-[type].png` (e.g., `sf-buffet.png`, `sf-cadeira-f.png`)
  - Brand: `marca-[descriptor].PNG` (e.g., `marca-room.PNG`)
- Python scripts: Kebab-case with clear purpose (`baixar_imagens.py`, `baixar_novos.py`)

**Directories:**
- Simple, descriptive names: `assets/` for images (no nested subdirectories)
- Hidden directories: `.git/` for version control, `.planning/` for documentation

**CSS Classes:**
- BEM-inspired but simplified naming: `[block]-[element]`, `[block]--[modifier]`
  - Navigation: `.nav`, `.nav-logo`, `.nav-links`, `.nav-logo-txt`, `.btn-nav`
  - Hero: `.hero-bg`, `.hero-content`, `.hero-line`, `.hero-logo`, `.hero-h1`, `.hero-cta`
  - Sections: `.section-tag`, `.section-title`, `.section-header`
  - Cards: `.pc` (product card), `.dest-item` (destination/showcase item), `.dif` (differentiator)
  - Grid items: `.gm-item` (gallery mosaic item)
  - Forms: `.form`, `.form-g` (form group), `.form-submit`
  - Utilities: `.reveal` (animation hook), `.scrolled` (navigation state), `.in` (animation triggered)
  - Delay classes: `.d1`, `.d2`, `.d3`, `.d4` (stagger animation delays)

**HTML IDs (Anchor Points):**
- Kebab-case, semantic section naming: `#hero`, `#sobre`, `#numeros`, `#colecao`, `#manifesto`, `#destaques`, `#diferenciais`, `#galeria`, `#contato`
- Navigation: `#nav`
- Correspond to major page sections for hash-based navigation

## Where to Add New Code

**New Section/Feature:**
- Location: Add `<section>` block in `index.html` before closing `</footer>` tag
- Styling: Add CSS rules in the `<style>` block (lines 11-511)
- Interactivity: Add JavaScript in the `<script>` block (lines 907-920)
- Pattern: Follow existing section structure with `.section-header`, content wrapper, and `.reveal` animation hooks

**New Images:**
- Location: Place in `assets/` directory with kebab-case naming
- Reference: Update `index.html` to reference via relative path `assets/[filename]`
- Download Script: Add file ID mapping to `baixar_imagens.py` or `baixar_novos.py` if sourcing from Google Drive

**Navigation Updates:**
- Location: Edit `.nav-links` list in HTML (around line 519)
- Styling: Navigation styles in CSS section (around lines 27-54)
- Links: Use anchor navigation with hash IDs (e.g., `href="#contato"`)

**Product/Showcase Updates:**
- Location: `.products-editorial` grid in `#colecao` section (around line 622)
- Pattern: Add `.pc` div with class indicating size (`s3`, `s4`, `s6`), `.reveal` with delay class, image, and `.pc-label`
- Images: Place product images in `assets/` and reference by relative path

**Form Enhancements:**
- Location: `.form` element in `#contato` section (around line 845)
- Current: Form has `onsubmit="return false"` (non-functional placeholder)
- Integration: To enable, replace with actual form handling (POST endpoint, email service, or form service)

## Special Directories

**`.git/`:**
- Purpose: Git repository for version control
- Generated: Yes (managed by git)
- Committed: No (git metadata, not part of source)

**`.planning/`:**
- Purpose: Documentation and planning artifacts (created during mapping)
- Generated: Yes (created by GSD mapping process)
- Committed: Yes (should be tracked for reference)

**`assets/`:**
- Purpose: Static media serving
- Generated: Yes (via `baixar_imagens.py` and `baixar_novos.py`)
- Committed: Depends on project preference; images can be large, often excluded via `.gitignore`

## File Size & Complexity

- `index.html`: ~900 lines (monolithic; contains HTML structure, CSS, and JavaScript)
  - Structure: Lines 1-10 (doctype, head), 11-511 (style), 512-905 (HTML body), 907-920 (script)
- `baixar_imagens.py`: 100 lines (asset management utility)
- `baixar_novos.py`: 74 lines (asset management utility)
- `assets/`: ~35 image files (sizes vary from ~50KB to ~500KB per image)

## Modification Workflow

1. **View Changes:** Edit `index.html` directly (no build step)
2. **Test Changes:** Open `index.html` in browser; refresh to see updates
3. **Style Updates:** Edit CSS in `<style>` block and refresh
4. **Interactivity Updates:** Edit JavaScript in `<script>` block; may require browser cache clear
5. **Asset Updates:** 
   - Add new images to `assets/`
   - Update Python script file mappings if using Google Drive sync
   - Run `python baixar_imagens.py` or `python baixar_novos.py` to fetch from Drive
6. **No Build/Compile Step:** File changes take effect immediately on page refresh

## Deployment Structure

**For Static Hosting (Netlify, Vercel, GitHub Pages):**
- Upload entire directory structure
- Ensure `assets/` images are included
- Set `index.html` as root/home page
- Python scripts not needed in production (dev-only utilities)

**For Traditional Web Hosting (cPanel, etc.):**
- Upload `index.html` to public root
- Create `assets/` subdirectory and upload all images
- Python scripts optional (development only)
- No server-side processing required
