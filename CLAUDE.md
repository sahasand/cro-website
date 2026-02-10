# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CardioVera Research — a cardiovascular CRO (Contract Research Organization) marketing website presented as a **5-theme design showcase** that sells web design services. Each theme explores a radically different aesthetic direction using identical content. The index page positions the showcase around modern SEO, GEO (Generative Engine Optimization), and AI search visibility.

## Tech Stack

- **Static HTML** — no build tools, no bundler, no package manager
- **Tailwind CSS v3** via CDN (`cdn.tailwindcss.com`) with per-file inline config
- **Vanilla JavaScript** — no frameworks
- **Google Fonts** — each theme has its own font pairing
- Deploy anywhere as static files (no build step)

## File Structure

- `index.html` — Sales-oriented gallery landing page linking to all 5 themes (Fraunces + Darker Grotesque fonts, dark editorial aesthetic, copy focused on AI search era / GEO / SEO)
- `theme1-corporate.html` — "Precision & Prestige" (dark navy #0d1b2e + gold #c9a84c, Playfair Display, dark immersive design with gold aurora, cursor glow, glassmorphism, ECG heartbeat, grain overlay, bento services grid, AI-generated hero image `img1.png`)
- `2/` — **"Clinical Evidence"** (multi-file architecture)
  - `2/index.html` — Main HTML (610+ lines)
  - `2/styles.css` — Complete stylesheet (~2,350 lines)
  - `2/script.js` — JavaScript interactions (271 lines)
  - `2/CLAUDE.md` — Comprehensive documentation
  - **Design**: Deep navy #0A1628 + crimson #C41E3A + green #00FF88, Cormorant Garamond + IBM Plex Mono
  - **Features**: Cardiac lattice visualization, data timeline, core lab services, glassmorphism
  - **Content**: Uses Tracescribe Research branding (founded 1997) for this specific implementation
- `theme3-warm.html` — "Organic Flow" (coral #e8634a on cream #faf8f5, DM Sans, floating blobs, spring animations)
- `theme4-brutalist.html` — "Raw & Bold" (black + red #ff2d2d, Instrument Serif + Azeret Mono, zero border-radius, marquee, glitch text)
- `5/` — **"Natural Authority"** (multi-file architecture)
  - `5/index.html` — Main HTML (490+ lines)
  - `5/styles.css` — Complete stylesheet (~1,440 lines)
  - `5/script.js` — JavaScript interactions (259 lines)
  - `5/website-copy-revised.md` — Content documentation
  - **Design**: Warm cream canvas #f3efe5 + teal #0a8d80 + terracotta #ae4d2f, DM Serif Display + Manrope + IBM Plex Mono
  - **Features**: 3D tilt cards, magnetic buttons, parallax mesh, floating panel, paper texture, "Since 1997" watermark
  - **Content**: Uses Tracescribe Research branding (founded 1997) for this specific implementation
- `playground.html` — Split-screen theme comparator (pick any 2 themes side by side, draggable divider, viewport presets, prompt output with copy)

## Architecture

Each theme file is **fully self-contained** (~40-66KB) with all CSS, HTML, and JS inline. They share no external stylesheets or scripts.

**Exceptions**: Theme 2 ("Clinical Evidence") and Theme 5 ("Natural Authority") use **multi-file architecture**:
- Separate `index.html`, `styles.css`, and `script.js` files
- Organized folder structures: `/2/` and `/5/`
- Own documentation files
- Themes 1, 3, 4 remain single-file for comparison

**Consistent section order across all themes:** Nav → Hero (100vh) → Stats → Services (6 cards) → About → Testimonials → Team (4 members) → Contact Form → Footer
- **Theme1 exception:** Has 2 extra sections between Stats and Services: "The Problem We Solve" → "Three Commitments"

**Common JS patterns in every theme:**
- `IntersectionObserver` for scroll-triggered fade/bounce animations
- Mobile nav toggle with `aria-expanded`
- Contact form with `preventDefault`, validation, button text feedback, and reset
- `requestAnimationFrame` loops for continuous animations (particles, cursor effects)

**Theme Switcher (`#themeSwitcher`)** — a floating vertical nav fixed to the right edge of every theme page:
- Grid icon links back to `index.html` (or `../index.html` for themes in subfolders), 5 split-gradient dots link to each theme
- Active theme dot is scaled up with a glowing ring; hover shows tooltip with theme name
- Styled natively per theme (e.g., theme2 gets crimson ring, theme5 gets teal ring + paper texture shadow, brutalist gets offset shadow, warm gets bouncy spring easing)
- `z-index: 10001` (above noise overlays at 9999), responsive (shrinks on mobile, tooltips hidden)
- CSS class names: `.ts-home`, `.ts-sep`, `.ts-dot`, `.ts-dot-inner`, `.ts-tip`, `.ts-dot.active`
- **Subfolder themes (2, 5)**: Use relative paths `../` since they're in subfolders

## Design Constraints

- ECG heartbeat animation exists **only** in theme1-corporate.html — intentionally removed from all others
- Each theme must have distinct: font pairing, color palette, layout structure, animation style, spatial composition
- All themes use inline SVG icons (no icon libraries)
- **Theme2 ("Clinical Evidence")**: Multi-file structure in `/2/` folder, deep navy + crimson + green, Cormorant Garamond serif + IBM Plex Mono, cardiac lattice visualization, data timeline section, grain texture overlay. Uses Tracescribe Research branding in content.
- **Theme5 ("Natural Authority")**: Multi-file structure in `/5/` folder, warm cream canvas + teal + terracotta, DM Serif Display + Manrope + IBM Plex Mono, 3D tilt cards, magnetic button effects, parallax mesh animations, paper texture grain overlay, floating hero panel. Uses Tracescribe Research branding in content.
- Theme1 hero uses local AI-generated image `img1.png` (dark cinematic doctor with gold lighting, no external URL)
- Theme1 team avatars use inline SVG monograms (Playfair Display initials, navy bg, gold text)
- Section IDs available: `services`, `about`, `testimonials`, `team`, `contact`. Theme2 has `id="hero"`, `id="leadership"`, `id="core-lab"`, `id="data-timeline"`, `id="quality"`, `id="contact-form"`, `id="stats"`.
- Theme4 has `*, *::before, *::after { border-radius: 0 !important; }` — any new elements inherit square corners
- Noise/grain overlays in theme1, theme2, theme4, theme5 use `z-index: 9999` with `pointer-events: none` — new floating UI needs `z-index: 10001+`
- Theme1 copy sourced from `design.md` CRO copywriting framework — uses "Data-First" positioning, published metrics (94% team continuity, 97% on-time DB lock), Three Commitments structure
- Theme1 design matches sophistication of themes 2 & 5: dark immersive bg, drifting ambient gold glow (body::before), cursor glow, glassmorphism cards, gold shimmer hovers, scanning line on stats, about section has animated cardiac data viz

## Responsive Design

All pages are mobile-responsive with progressive breakpoints:
- **Theme1**: Full `sm:` / `md:` / `lg:` stepping — nav at `md:`, hero side-by-side at `md:`, bento grid `md:grid-cols-2` → `lg:grid-cols-3`, stats `md:grid-cols-3` → `lg:grid-cols-6`
- **Theme2 ("Clinical Evidence")**: Vanilla CSS with breakpoints at 768px, 640px, 480px. Mobile menu slides in from right, hero grid collapses to single column, timeline switches from 6-col to 3-col to 2-col, metrics grid responsive. Theme switcher scales down on mobile.
- **Theme3**: Already had good `md:` coverage — no gaps
- **Theme4**: Already had good `md:` coverage — no gaps
- **Theme5 ("Natural Authority")**: Vanilla CSS with breakpoints at 1120px, 920px, 680px. Hero grid collapses at 920px, metrics/leadership/commitments go 6→3→2→1 col, mobile menu dropdown at 920px, 3D tilt effects disabled on coarse pointers. Theme switcher scales down on mobile.
- **Index**: Vanilla CSS (no Tailwind) with three breakpoints: 1024px (tablet), 768px (mobile), 400px (small phones). Cursor glow disabled on touch devices.
- All themes disable cursor glow on mobile/touch devices
- Nav switches to hamburger at `md:` (768px) across all themes
