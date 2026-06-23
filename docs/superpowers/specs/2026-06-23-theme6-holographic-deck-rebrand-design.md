# Theme 6 Replacement — "Holographic Deck" (Tracescribe rebrand)

**Date:** 2026-06-23
**Status:** Approved (design Q&A complete)

## Goal

Replace the current Theme 6 ("Visceral Science" — Arteris Therapeutics 3D beating
heart) with the new `6-new/` deck, rebranded from **CCS / Cardiovascular Clinical
Sciences** to **Tracescribe Research** and fully de-identified (no real people,
affiliations, photos, or conference links).

## Source

`6-new/index.html` — untracked, 2,406 lines. A dark "instrument-room" capabilities
deck: a Three.js holographic WebGL scene behind frosted-glass content panels, 15
sections. Already handles `prefers-reduced-motion` and WebGL failure gracefully
(DOM/content layer runs independently of the 3D layer). Assets in `6-new/assets/`:
4 cardiologist photos (referenced) + 3 logos + 1 ChatGPT image (all unreferenced).

## Genericization (CCS → Tracescribe Research)

1. **Brand text** — all "CCS" / "Cardiovascular Clinical Sciences" → "Tracescribe
   Research" / "Tracescribe" across 28 HTML refs + visible JS strings (the in-scene
   3D label `CCS · ONE TEAM`, HUD readouts, nav links "Why CCS", section titles).
   Footer domain `ccstrials.com` → `tracescribe.com`. Internal JS identifiers
   (`__ccs3dReady`, `lCcs`) renamed for cleanliness.
2. **People → role-only titles** (matching themes 2 & 5, which use names-free roles):
   - Konstam → Founder & Chief Scientific Officer, M.D.
   - Udelson → Founder & Chief Medical Officer, M.D.
   - Rusch → Chief Executive Officer, Ph.D.
   - Patel → Medical Director, M.D.
   - DiBattista → Director, Project Delivery
   - Jing Dai → Director, Core Laboratory Operations
   - Inline name-drops (hero lede, thesis attribution, operating model, core-lab
     marquee) → generic ("our founders", "senior cardiologists").
3. **Affiliations** — Tufts Medical Center / Tufts University / Boston, and named
   societies/journals (HFSA, ASNC, ACC, JAMA) → generic credential phrasing
   ("academic medical center", "heart-failure society leadership", "FDA
   advisory-panel experience"). **"Founded 1997" retained** (showcase-consistent).
4. **Photos** — 4 headshots → neutral silhouette avatars reusing the page's
   `.mono-av` style. The entire `6-new/assets/` folder is then unused and dropped.
5. **Events** — 10 real congresses + external URLs → ~7 generic placeholder
   cardiovascular events (Jul–Dec 2026, generic names/locations, no external
   links). Auto-drop-past-events JS retained.

## Mechanical replacement

- Edited file **becomes `6/index.html`** (gallery link `6/index.html` unchanged).
- Delete old `6/index.html`, `6/heart_b64.js` (9.6 MB), `6/realistic_human_heart.glb`
  (7.2 MB) — frees ~16.8 MB.
- Delete the `6-new/` folder entirely (including unused `assets/`).
- Add the floating **theme switcher** (present on every other theme page) to the new
  `6/index.html`: `../` paths, active dot on theme 6, styled to the theme's dark
  glassmorphism.

## Showcase integration (scope = "update everything")

- **Theme name:** "Holographic Deck". Switcher dot gradient: `#02060F` → `#E63946`
  (navy → red).
- **`index.html` gallery card** for theme 6 — rewrite copy from "Visceral Science /
  Arteris / 3D heart" to the new holographic-deck design.
- **Theme switcher on all 7 pages** (index, theme1/3/4, 2/, 5/, 6/) — update the
  theme-6 dot color + label to "Holographic Deck".
- **CLAUDE.md** — rewrite the Theme 6 section (and the relevant constraint/notes
  bullets) to describe the new theme.

## Verification

- `grep -i "ccs\|cardiovascular clinical sciences\|konstam\|udelson\|rusch\|patel\|
  dibattista\|jing dai\|tufts\|ccstrials"` over `6/` returns nothing.
- No references to `6-new/`, `assets/`, `heart_b64`, or `.glb` remain anywhere.
- Theme switcher present on new `6/index.html`, active on 6, all `../` links resolve.
- Page renders: hero reveals, WebGL scene (or graceful fallback), events list
  populates with generic 2026 events, contact form gives feedback.
