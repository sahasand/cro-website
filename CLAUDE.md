# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Tracescribe Research — a cardiovascular CRO (Contract Research Organization) marketing website presented as a **4-theme design showcase** that sells web design services. Each theme explores a radically different aesthetic direction over shared cardiovascular CRO content. The index page positions the showcase around modern SEO, GEO (Generative Engine Optimization), and AI search visibility.

## Tech Stack

- **Static HTML** — no build tools, no bundler, no package manager
- **Tailwind CSS v3** via CDN (`cdn.tailwindcss.com`) with per-file inline config
- **Vanilla JavaScript** — no frameworks
- **Google Fonts** — each theme has its own font pairing
- Deploy anywhere as static files (no build step)
- **Live site**: https://sites.tracescribe.com (hosted on Vercel, GitHub repo: `sahasand/cro-website`)

## File Structure

- `index.html` — Sales-oriented gallery landing page linking to all 4 themes (Fraunces + Darker Grotesque fonts, dark editorial aesthetic, copy focused on AI search era / GEO / SEO)
- `2/` — **"Clinical Evidence"** (multi-file architecture)
  - `2/index.html` — Main HTML (610+ lines)
  - `2/styles.css` — Complete stylesheet (~2,350 lines)
  - `2/script.js` — JavaScript interactions (271 lines)
  - `2/CLAUDE.md` — Comprehensive documentation
  - **Design**: Deep navy #0A1628 + crimson #C41E3A + green #00FF88, Cormorant Garamond + IBM Plex Mono
  - **Features**: Cardiac lattice visualization, data timeline, core lab services, glassmorphism
  - **Content**: Uses Tracescribe Research branding (founded 1997) for this specific implementation
- `theme3-warm.html` — "Organic Flow" (coral #e8634a + amber #f2cc8f + sage #81b29a on cream #faf8f5, DM Sans only). **Content: the de-identified "Data-First" narrative promoted from the original theme1** — hero "Data integrity from protocol concept to FDA approval", "The Problem We Solve" + "Three Commitments" sections, the six Data-First services, role-only leadership titles with silhouette avatars, anonymized testimonials, founded 1997. Aesthetic: morphing blobs with SVG-filter turbulence, 3-layer parallax, magnetic buttons (90px pull), 3D card tilt, smooth cursor glow (rAF lerp), spring easing, stagger reveals, paper texture, glassmorphism nav, floating particles, gradient section bars, pull-quote + commitment-number components. **Bug fixes:** reveal-on-load (no longer blank above the fold — fixes the IntersectionObserver vs Tailwind-CDN race), `prefers-reduced-motion` support, `scroll-padding-top` for anchored nav, carousel pause-on-hover/focus, parallax/particles/cursor/magnetic/tilt gated to fine-pointer + non-reduced-motion. Polished to match execution quality of themes 2 & 5.)
- `5/` — **"Natural Authority"** (multi-file architecture)
  - `5/index.html` — Main HTML (490+ lines)
  - `5/styles.css` — Complete stylesheet (~1,440 lines)
  - `5/script.js` — JavaScript interactions (259 lines)
  - `5/website-copy-revised.md` — Content documentation
  - **Design**: Warm cream canvas #f3efe5 + teal #0a8d80 + terracotta #ae4d2f, DM Serif Display + Manrope + IBM Plex Mono
  - **Features**: 3D tilt cards, magnetic buttons, parallax mesh, floating panel, paper texture, "Since 1997" watermark
  - **Content**: Uses Tracescribe Research branding (founded 1997) for this specific implementation
- `6/` — **"Holographic Deck"** (single self-contained file in a subfolder)
  - `6/index.html` — Main HTML (~2,440 lines, ~138KB; all CSS + JS inline, no external assets)
  - **Design**: Deep navy/near-black (#02060F / #040D1D / navy #0A2A5E) + red #E63946, Plus Jakarta Sans + JetBrains Mono + Playfair Display
  - **Features**: Three.js (via importmap `three@0.184.0`) procedural holographic WebGL scene behind frosted-glass panels — no model file; instrument-room HUD frame (corner brackets + live BPM/scroll readouts); 15 capability sections; IntersectionObserver reveals; tabbed trial portfolio; animated counters; self-updating events list (past events auto-drop); reduced-motion + `<noscript>` fallbacks; graceful no-WebGL degradation (content layer is independent of the 3D layer, `no3d` body class). No GSAP, no Tailwind.
  - **Content**: Tracescribe Research, fully de-identified (role-only leadership titles, silhouette avatars, generic placeholder events). Founded 1997.


## Architecture

Each theme file is **fully self-contained** (~40-66KB) with all CSS, HTML, and JS inline. They share no external stylesheets or scripts.

**Exceptions**: Theme 2 ("Clinical Evidence") and Theme 5 ("Natural Authority") use **multi-file architecture**:
- Separate `index.html`, `styles.css`, and `script.js` files
- Organized folder structures: `/2/` and `/5/`
- Own documentation files
- Theme 3 (`theme3-warm.html`) is the only root-level single-file theme
- Theme 6 ("Holographic Deck") is a **single self-contained `index.html` inside `/6/`** (all CSS + JS inline, Three.js loaded from CDN via importmap)

**Consistent section order across all themes:** Nav → Hero (100vh) → Stats → Services (6 cards) → About → Testimonials → Team (4 members) → Contact Form → Footer
- **Theme3 exception:** Adds "The Problem We Solve" (#approach, with a pull-quote) and "Three Commitments" between Stats and Services. Carries the de-identified Data-First copy.
- **Theme6 exception:** Uses its own capabilities-deck section structure (Hero → At a Glance → Thesis → Why → Positioning (ARO+CRO) → Operating Model → Capabilities → Differentiators → Founders → Case Study → Engagements → Experience → Team → Events → Contact), not the standard layout. Tracescribe-branded.

**Common JS patterns in every theme:**
- `IntersectionObserver` for scroll-triggered fade/bounce animations
- Mobile nav toggle with `aria-expanded`
- Contact form with `preventDefault`, validation, button text feedback, and reset
- `requestAnimationFrame` loops for continuous animations (cursor glow in theme3, theme5; parallax in theme3)
- **Theme3 & Theme5 specific**: magnetic button effects (cursor distance tracking with strength-based pull), enhanced 3D card tilt (mousemove perspective rotation with rotateX/rotateY), smooth cursor glow interpolation (lerp-based tracking)

**Theme Switcher (`#themeSwitcher`)** — a floating vertical nav fixed to the right edge of every theme page:
- Grid icon links back to `index.html` (or `../index.html` for themes in subfolders), 4 split-gradient dots link to each theme
- Active theme dot is scaled up with a glowing ring; hover shows tooltip with theme name
- Styled natively per theme (e.g., theme2 gets crimson ring, theme5 gets teal ring + paper texture shadow, warm gets bouncy spring easing, theme6 gets dark navy glassmorphism with a red glow ring (#E63946))
- `z-index: 10001` (above noise overlays at 9999), responsive (shrinks on mobile, tooltips hidden)
- CSS class names: `.ts-home`, `.ts-sep`, `.ts-dot`, `.ts-dot-inner`, `.ts-tip`, `.ts-dot.active`
- **Subfolder themes (2, 5, 6)**: Use relative paths `../` since they're in subfolders

## Design Constraints

- Each theme must have distinct: font pairing, color palette, layout structure, animation style, spatial composition
- All themes use inline SVG icons (no icon libraries)
- **Theme2 ("Clinical Evidence")**: Multi-file structure in `/2/` folder, deep navy + crimson + green, Cormorant Garamond serif + IBM Plex Mono, cardiac lattice visualization, data timeline section, grain texture overlay. Uses Tracescribe Research branding in content.
- **Theme5 ("Natural Authority")**: Multi-file structure in `/5/` folder, warm cream canvas + teal + terracotta, DM Serif Display + Manrope + IBM Plex Mono, 3D tilt cards, magnetic button effects, parallax mesh animations, paper texture grain overlay, floating hero panel. Uses Tracescribe Research branding in content.
- **Theme3 ("Organic Flow")**: Single-file architecture, warm cream canvas #faf8f5 + coral #e8634a + amber #f2cc8f + sage #81b29a, DM Sans only. **Carries the de-identified Data-First copy** (hero "Data integrity from protocol concept to FDA approval", Problem We Solve + Three Commitments, role-only leadership + silhouette avatars, anonymized testimonials, founded 1997). Morphing blobs with SVG-filter turbulence and organic border-radius keyframes, 3-layer parallax (0.15x/0.25x/0.4x), paper texture overlay (body::before, mix-blend-mode multiply), glassmorphism nav (24px backdrop-blur + saturate(160%)), magnetic buttons (90px pull, 0.35 strength), 3D card tilt (perspective 1000px), cursor glow (rAF 0.18 lerp), spring easing (cubic-bezier 0.34, 1.56, 0.64, 1), stagger reveals, stat pulse, testimonial carousel, ~16 floating particles, gradient section bars, plus `.eyebrow` / `.pull-quote` / `.commit-num` components. **Reveal is robust on load** (on-load in-viewport pass + safety-net timeout fixes the prior blank-hero race against the CDN Tailwind compiler). Honors `prefers-reduced-motion` (CSS block + JS gating: reveals everything, drops particles/parallax/cursor/magnetic/tilt); `scroll-padding-top: 96px` offsets anchored nav; carousel pauses on hover/focus; parallax/particles/cursor/magnetic/tilt gated on `(hover:hover) and (pointer:fine)`.
- **Theme6 ("Holographic Deck")**: Single self-contained `index.html` in `/6/` folder, deep navy/near-black (#02060F / #040D1D / navy #0A2A5E) + red #E63946, Plus Jakarta Sans + JetBrains Mono + Playfair Display. Three.js (importmap, `three@0.184.0`) procedural holographic WebGL scene behind frosted-glass capability panels — no model file. Instrument-room HUD frame (corner brackets + live BPM/scroll readouts), mouse-parallax camera, dynamic lighting, ambient crimson radial glow. 15-section capabilities deck with IntersectionObserver reveals, a tabbed trial portfolio, animated counters, and a self-updating events list (past events auto-drop). Two-layer architecture: a dependency-free DOM/content layer that always runs, plus a Three.js layer that degrades gracefully (no-WebGL / `<noscript>` → `no3d` body class hides the canvas + HUD, content intact). Honors `prefers-reduced-motion`. No GSAP, no Tailwind. Tracescribe-branded, fully de-identified (role-only titles, silhouette avatars, generic events).
- Section IDs available: `services`, `about`, `testimonials`, `team`, `contact`. Theme2 has `id="hero"`, `id="leadership"`, `id="core-lab"`, `id="data-timeline"`, `id="quality"`, `id="contact-form"`, `id="stats"`.
- Noise/grain overlays in theme2 & theme5 use `z-index: 9999` with `pointer-events: none` — new floating UI needs `z-index: 10001+`
- Theme3's Data-First copy (promoted from the original theme1) is sourced from `design.md` CRO copywriting framework — uses "Data-First" positioning, published metrics (94% team continuity, 97% on-time DB lock), Three Commitments structure

## Responsive Design

All pages are mobile-responsive with progressive breakpoints:
- **Theme2 ("Clinical Evidence")**: Vanilla CSS with breakpoints at 768px, 640px, 480px. Mobile menu slides in from right, hero grid collapses to single column, timeline switches from 6-col to 3-col to 2-col, metrics grid responsive. Theme switcher scales down on mobile.
- **Theme3 ("Organic Flow")**: Full responsive coverage with `sm:` / `md:` / `lg:` breakpoints. Hero text scaling, stats/services/team/commitments grids responsive, mobile blob sizing (320px/280px/300px with 60px blur). Cursor glow, parallax, magnetic/tilt, and particles disabled on touch/coarse-pointer **and** under `prefers-reduced-motion` (actually gated now, not just documented); `scroll-padding-top` offsets the fixed nav for anchor jumps.
- **Theme5 ("Natural Authority")**: Vanilla CSS with breakpoints at 1120px, 920px, 680px. Hero grid collapses at 920px, metrics/leadership/commitments go 6→3→2→1 col, mobile menu dropdown at 920px, 3D tilt effects disabled on coarse pointers. Theme switcher scales down on mobile.
- **Theme6 ("Holographic Deck")**: Vanilla CSS media queries (no Tailwind). Instrument HUD frame hidden ≤1080px; grids (stats, capabilities, founders, team) collapse via `auto-fit`/`minmax`; mobile nav menu; theme switcher shrinks and hides tooltips ≤768px.
- **Index**: Vanilla CSS (no Tailwind) with three breakpoints: 1024px (tablet), 768px (mobile), 400px (small phones). Cursor glow disabled on touch devices.
- All themes disable cursor glow on mobile/touch devices
- Nav switches to hamburger at `md:` (768px) across all themes
