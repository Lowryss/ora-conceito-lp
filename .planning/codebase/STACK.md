# Technology Stack

**Analysis Date:** 2026-04-01

## Languages

**Primary:**
- HTML5 - Single-page application structure
- CSS3 - Inline styling with responsive design (mobile-first approach)
- JavaScript (ES6+) - Client-side interactivity, minimal script footprint

**Secondary:**
- Python 3 - Image asset management and Google Drive integration scripts

## Runtime

**Environment:**
- Browser-based (HTML/CSS/JS)
- No server-side runtime required for production deployment

**Package Manager:**
- pip (Python) - Used for utility scripts to manage asset downloads

## Frameworks

**Frontend:**
- No external frameworks used - Vanilla HTML, CSS, and JavaScript
- IntersectionObserver API - For scroll-based reveal animations (built-in browser feature)

**Development/Utilities:**
- Python script-based approach - For asset management (baixar_imagens.py, baixar_novos.py)

## Key Dependencies

**Browser APIs:**
- IntersectionObserver - Scroll-triggered element reveal animations
- DOM API - Element manipulation and event handling
- CSS Grid and Flexbox - Layout system (no CSS framework)

**External Python Libraries (Development/Scripting):**
- `requests` [version: unspecified] - HTTP requests for downloading files
  - Purpose: Retrieving images from Google Drive
  - Installed via pip

- `browser-cookie3` [version: unspecified] - Browser cookie extraction
  - Purpose: Authenticating with Google Chrome cookies for Google Drive access
  - Installed via pip

**Remote Resources (CDN):**
- Google Fonts API - Font loading
  - Fonts: Cormorant Garamond (serif, weights: 300, 400, 500, 600)
  - Fonts: Montserrat (sans-serif, weights: 300, 400, 500, 600)
  - Link: `https://fonts.googleapis.com`

## Configuration

**Environment:**
- No `.env` file required for production
- No build configuration files (no build process)
- Static asset references configured via relative paths: `assets/`

**Asset Management:**
- Images stored locally in `assets/` directory
- Google Drive integration via Python scripts (for content updates)
- Automatic fallback: `onerror` handlers on img tags display logo text if images fail to load

**Browser Support:**
- Modern browsers with ES6 support
- Graceful degradation: Uses `onerror` handlers for missing images

## Platform Requirements

**Development:**
- Python 3.6+ (for asset download scripts)
- Modern web browser with JavaScript enabled
- Chrome browser (for cookie-based Google Drive authentication in scripts)

**Production:**
- Any modern web browser with JavaScript support
- Static file hosting (no backend server required)
- HTTPS recommended (forms present but not functional - frontend-only)

**Asset Requirements:**
- ~39.6 MB of image assets (27 files in `assets/` directory)
- Network access to Google Fonts CDN
- Static file serving capability for:
  - `index.html` (~40 KB)
  - `assets/` directory (image files)

## File Structure

```
project-root/
├── index.html                  # Main HTML file (single-page application)
├── assets/                     # Static image assets
│   ├── logo-preta.png
│   ├── logo-dourada.png
│   ├── logo-bg-preta.jpg
│   ├── foto-*.png              # Product/environment photos (21 files)
│   ├── sf-*.png                # Background-removed product images
│   └── marca-room.PNG          # Brand showcase image
├── baixar_imagens.py           # Image download utility (Google Drive)
├── baixar_novos.py             # New image download utility (Google Drive)
└── .planning/                  # Documentation directory
```

---

*Stack analysis: 2026-04-01*
