# External Integrations

**Analysis Date:** 2026-04-01

## APIs & External Services

**Google Fonts:**
- Service: Google Fonts API
  - What it's used for: Web font delivery (Cormorant Garamond, Montserrat)
  - Implementation: Link tag in HTML head
  - URL: `https://fonts.googleapis.com/css2?family=...`
  - Preconnect hints: `https://fonts.googleapis.com`, `https://fonts.gstatic.com`
  - Fallback: System fonts (Georgia, sans-serif)

**Google Drive:**
- Service: Google Drive file sharing and download
  - What it's used for: Asset management and image hosting (development/content update)
  - Implementation: Python scripts with authenticated requests
  - Scripts: `baixar_imagens.py`, `baixar_novos.py`
  - Files downloaded: 21+ product images, logos, brand images
  - Authentication: Chrome browser cookie extraction via `browser-cookie3`
  - API endpoint: `https://drive.google.com/uc?export=download&id={file_id}&confirm=t`

## Data Storage

**File Storage:**
- Type: Local filesystem
- Implementation: Static assets stored in `assets/` directory
- Total size: ~39.6 MB
- Content:
  - Product images: 21 photos (foto-01.png through foto-21.png)
  - Background-removed product images: 8 files (sf-*.png)
  - Brand/showcase images: logo files, background images
  - Logos: 2 versions (preta and dourada)

**Database:**
- Not applicable - No backend database used
- All content is static HTML/CSS/JavaScript

**Caching:**
- Browser caching: HTML standard cache headers (if configured server-side)
- No explicit caching service (Memcached, Redis, etc.)

## Authentication & Identity

**Auth Provider:**
- Custom/None for production
- Development-only authentication: Google Drive access via Chrome cookies
  - Credentials location: Browser cookie store (local to development machine)
  - Used by: `baixar_imagens.py`, `baixar_novos.py` scripts
  - Method: `browser-cookie3` library extracts authentication from Chrome

**Form Submission:**
- Contact form present in `#contato` section
- Current state: Non-functional (form submit handler: `onsubmit="return false"`)
- Fields: Nome, Email, Telefone, Mensagem
- No backend endpoint configured
- Would require server-side integration to process submissions

## Monitoring & Observability

**Error Tracking:**
- Not detected - No error tracking service integrated

**Logs:**
- Python scripts: Console output only
  - Download success/failure logged to stdout
  - No log aggregation service

**Frontend Monitoring:**
- Not detected - No analytics or monitoring service

## CI/CD & Deployment

**Hosting:**
- Static file hosting required
- No server-side runtime needed
- Deployable to:
  - GitHub Pages
  - Netlify
  - Vercel
  - AWS S3 + CloudFront
  - Any static hosting service

**CI Pipeline:**
- Not detected - No build or CI configuration files

**Deployment Method:**
- Manual: Copy `index.html` and `assets/` directory to hosting server
- Asset management: Use Python scripts to sync new images from Google Drive

## Environment Configuration

**Required env vars:**
- None for production deployment
- Development-only: Chrome browser and cookies for Google Drive access

**Secrets location:**
- No secrets file detected
- Google Drive file IDs are hardcoded in Python scripts (not sensitive)
- Email and phone number are placeholder values in HTML: `(XX) XXXXX-XXXX`, `contato@oraconceito.com.br`

## Webhooks & Callbacks

**Incoming:**
- None detected - No webhook endpoints

**Outgoing:**
- None detected - No external service callbacks configured

## Form & Contact

**Contact Form:**
- Location: `#contato` section in `index.html`
- Fields:
  - Nome (text input)
  - E-mail (email input)
  - Telefone (tel input)
  - Mensagem (textarea)
- Current status: Non-functional (frontend only)
- Submit button: "Enviar Mensagem"
- Next steps required: Implement backend endpoint to process form submissions
  - Could integrate with: Formspree, EmailJS, custom API endpoint, etc.

## Social Media & External Links

**Social Links:**
- Location: Footer section
- Platforms: Instagram, Facebook, Pinterest
- Status: Placeholder links only (`href="#"`)
- No actual social media integration

## Google Drive File Mapping

**Images downloaded by scripts:**

`baixar_imagens.py` (initial asset set):
- 21 product photos (foto-01.png to foto-21.png)
- 3 logo/branding files
- Total: 24 files mapped with Google Drive file IDs

`baixar_novos.py` (new/updated images):
- 8 background-removed product images (sf-*.png)
- 1 brand showcase image (marca-room.PNG)
- Total: 9 files with direct Google Drive IDs

**Note:** All file IDs are embedded in Python script dictionaries for direct download access.

---

*Integration audit: 2026-04-01*
