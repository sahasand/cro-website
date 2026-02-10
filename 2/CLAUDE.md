# Tracescribe Research Website - HTML Version

## Project Overview

This is a static HTML/CSS/JavaScript website for Tracescribe Research, a cardiovascular clinical research organization (CRO) founded in 1997. The site showcases their expertise in cardiovascular endpoints, core laboratory services, and clinical trial execution.

**Technology Stack:**
- Pure HTML5, CSS3, Vanilla JavaScript
- Google Fonts: Cormorant Garamond (serif), IBM Plex Mono (monospace)
- Python HTTP server for local development (port 8080)
- No build process or dependencies

## File Structure

```
html-site/
├── index.html          # Main HTML file with all content
├── styles.css          # Complete stylesheet (~1800 lines)
├── script.js           # JavaScript for interactions and animations
└── CLAUDE.md          # This file
```

## Design System

### Color Palette

**CSS Variables:**
```css
--deep-navy: #0A1628;           /* Primary background */
--clinical-white: #F8F9FA;      /* Primary text */
--accent-crimson: #C41E3A;      /* Brand accent, CTAs */
--data-green: #00FF88;          /* Highlights, success states */
--electric-blue: #0066FF;       /* Secondary accent */
--soft-gray: #B0B8C1;           /* Secondary text */
```

**Usage Guidelines:**
- Background: Deep navy (#0A1628)
- Headings: Clinical white (#F8F9FA)
- Brand elements: Crimson (#C41E3A)
- Data/metrics: Green (#00FF88)
- Interactive elements: Blue (#0066FF)

### Typography

**Font Families:**
- **Serif (Headings):** Cormorant Garamond - Elegant, professional
  - Weights: 300 (light), 400 (regular), 600 (semibold)
  - Use for: Hero title, section headings, leadership quotes

- **Monospace (UI):** IBM Plex Mono - Technical, precise
  - Weights: 400 (regular), 500 (medium), 600 (semibold)
  - Use for: Navigation, eyebrows, data labels, metrics

**Font Sizing:**
- Hero title: `clamp(2rem, 5vw, 4rem)` - All lines uniform size
- Section headings: `clamp(2.5rem, 5vw, 4rem)`
- Body text: `1rem` (16px base)
- Small text: `0.875rem` (14px)

### Visual Effects

**Glassmorphism:**
```css
.glass-card {
  background: rgba(13, 27, 42, 0.4);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}
```

**Animations:**
- Page load: Staggered reveals with `animation-delay`
- Scroll: Intersection Observer triggers `.is-visible` class
- Hover: Transform effects (translateY, scale)
- SVG paths: stroke-dasharray/stroke-dashoffset animations

## Site Sections

### 1. Navigation Header
- **Logo:** Heartbeat icon + "Tracescribe / RESEARCH"
- **Nav Items:** Leadership, Services, Core Laboratory, Data Strategy, Quality, Contact
- **Behavior:** Fixed position, glassmorphism on scroll

### 2. Hero Section
**Title (4 lines, uniform sizing):**
- "Cardiovascular"
- "evidence" (crimson)
- "designed at protocol" (green underline)
- "delivered at submission." (green underline)

**Features:**
- Animated SVG underlines
- Cardiac lattice visualization (right side)
- Two CTA buttons
- 48-hour response guarantee note

### 3. Trust Metrics Section
**6 Glassmorphic Cards:**
- 1,997 - Founded by Cardiologists
- 2,500+ - Specialized CV Sites
- 16 - Countries
- I-III - Full Phase Range
- 94% - Team Continuity
- 0 - FDA Complete Response Letters

**Features:**
- Counter animations (animateCounter function in script.js)
- 3D tilt effect on hover
- Intersection Observer triggers

### 4. Leadership Section
**4 Leader Cards:**
- Chief Medical Officer, M.D.
- Chief Scientific Officer, M.D.
- Chief Operations Officer, Ph.D., FCP
- Medical Director, M.D.

**Features:**
- Glassmorphic cards
- Gradient left border on hover
- Blockquotes with green accent

### 5. The Execution Gap Section
**Two-Column Layout:**
- **Left:** "The Problem" (crimson bullets)
- **Right:** "The Tracescribe Difference" (green bullets)

**Visual Design:**
- Color-coded bullet points
- Clear problem/solution contrast

### 6. Operating Commitments Section
**4-Card Grid:**
- Medical Leadership on Every Call
- Core Lab Integration at Protocol
- Unified Quality Framework
- Continuity Through Submission

**Features:**
- Bottom gradient line on hover

### 7. Clinical Research Services Section
**7 Service Cards (Grid):**
1. Clinical Development Strategy
2. Trial Planning & Design
3. Clinical Operations
4. Data Management
5. Biostatistics
6. Clinical Trial Analytics
7. Pharmacovigilance & Safety

**Features:**
- Top gradient bar animation on hover

### 8. Core Laboratory Services Section
**3 Detailed Cards:**
1. Cardiac Imaging Acquisition (ECHO, MRI, CT, NUCLEAR/PET)
2. Central Reading & Adjudication (BICR)
3. Biomarker Core Services

**Features:**
- Green modality labels
- Blue bullet points
- Right gradient border on hover

### 9. Data Strategy Section
**Timeline Visualization:**
- 6 nodes: DAY 1 → DESIGN → FPI → LIVE → DBL → FINAL
- Gradient progress bar (green to crimson)
- Large heading: "Your data strategy starts at Day 1, not ~~Day 400~~."

### 10. Global Reach Section
**3 Stats + Description:**
- 2,500+ Specialized CV Sites
- 16 Countries
- 150+ Credentialed Core Lab Readers

**Features:**
- Two descriptive paragraphs
- Glassmorphic stat cards

### 11. Quality & Compliance Section
**4 Quality Cards:**
- Regulatory Compliance
- Quality Management System
- Audit Readiness
- Data Integrity

**Special Metrics (Large Green):**
- 0 - FDA Complete Response Letters
- 0 - Critical Audit Findings
- 100% - Successful Regulatory Inspections

### 12. Contact Form Section
**Form Fields:**
- Name (required)
- Email (required)
- Organization (required)
- Current Phase (dropdown)
- Program Details (textarea)
- Submit button (crimson)

**Heading:** "Start a Conversation"
**Subheading:** "Scientific leadership reviews every inquiry and responds within 48 hours."

### 13. Footer
- TSR logo
- "Tracescribe Research" heading
- Tagline: "Cardiovascular evidence, designed at protocol, delivered at submission."
- Copyright: "© 2024 Tracescribe Research. All rights reserved."

## JavaScript Functionality

### Core Features (script.js)

**1. Scroll State Management**
- Updates header with `.is-scrolled` class after 50px scroll
- Passive event listener for performance

**2. Smooth Scroll Navigation**
- Handles anchor link clicks
- Calculates offset for fixed header
- Closes mobile menu after navigation

**3. Mobile Menu Toggle**
- Hamburger menu for responsive nav
- Click outside to close
- Escape key to close
- Aria-expanded for accessibility

**4. Page Load Animation**
- Adds `.loaded` class to body after 100ms
- Triggers all staggered reveal animations

**5. Counter Animations**
```javascript
animateCounter(element)
// - Reads data-value attribute
// - 2-second duration with ease-out cubic easing
// - Supports +, %, and comma formatting
```

**6. 3D Tilt Effect**
```javascript
add3DTilt(element)
// - Applied to .metric-item cards
// - Mousemove calculates perspective transform
// - Reset on mouseleave
```

**7. Intersection Observer**
- Generic reveal observer for `[data-reveal]` elements
- Metrics observer triggers counters at 30% visibility
- Timeline observer with sequential node animations

**8. Timeline Animation**
- Progress bar animation
- Staggered node reveals (150ms delay between)

**9. Reduced Motion Support**
- Detects `prefers-reduced-motion: reduce`
- Disables animations with CSS injection
- Shows all content immediately

## Development Guidelines

### Local Development

**Start server:**
```bash
cd /Users/sanman/Documents/cro-website3/html-site
python3 -m http.server 8080
```

**Access:** http://localhost:8080

### Making Changes

**HTML Updates:**
- All content is in `index.html`
- Maintain semantic HTML structure
- Use BEM-like class naming conventions
- Add `data-reveal` to elements that should animate in

**CSS Updates:**
- All styles in `styles.css`
- Use CSS custom properties for colors
- Maintain mobile-first responsive design
- Test at: 320px, 768px, 1024px, 1440px breakpoints

**JavaScript Updates:**
- Keep vanilla JS, no dependencies
- Use passive event listeners where possible
- Support reduced motion preferences
- Test with DevTools throttling

### Performance Considerations

**Optimizations Already Implemented:**
- Passive scroll listeners
- CSS animations over JavaScript
- Intersection Observer for scroll-triggered effects
- Font preloading
- requestAnimationFrame for smooth animations
- Debounced/throttled event handlers

**Future Optimizations:**
- Lazy load images (when added)
- Minify CSS/JS for production
- Add service worker for offline support
- Implement critical CSS inline

## Design Principles

### 1. Premium Clinical Aesthetic
- Dark, sophisticated color palette
- Glassmorphism for depth without clutter
- Generous white space
- Professional typography hierarchy

### 2. Data-Driven Trust
- Prominent metrics (1997, 2,500+, 0 FDA letters)
- Specific technical details (ECHO, MRI, BICR)
- Process visualization (timeline)
- Transparent quality reporting (0, 0, 100%)

### 3. Scientific Credibility
- Physician-scientist leadership emphasized
- Technical terminology used appropriately
- Evidence-based messaging
- Regulatory compliance highlighted

### 4. Smooth, Professional Interactions
- 60fps animations
- Subtle hover effects
- Smooth scroll behavior
- Progressive enhancement

## Content Guidelines

### Voice & Tone
- **Professional but not corporate:** Technical yet accessible
- **Confident but not arrogant:** Let the data speak
- **Precise:** Use specific numbers and terminology
- **Action-oriented:** Focus on outcomes and execution

### Messaging Hierarchy
1. **Cardiovascular evidence** - Core value proposition
2. **Protocol to submission** - End-to-end capability
3. **Physician-scientist leadership** - Credibility
4. **Zero tolerance for errors** - Quality commitment
5. **48-hour response** - Responsiveness

### Writing Style
- **Headlines:** Short, impactful (3-6 words)
- **Body copy:** Clear, specific, evidence-based
- **Bullets:** Start with verbs or nouns, parallel structure
- **CTAs:** Direct imperatives ("Tell Us About Your Program")

## Deployment

### Static Hosting Options

**Recommended Platforms:**
1. **Netlify** - Drag & drop, auto HTTPS, forms support
2. **Vercel** - CLI deployment, edge network
3. **GitHub Pages** - Free, simple, version controlled
4. **Cloudflare Pages** - Fast CDN, analytics

**Deployment Steps (Netlify example):**
```bash
# 1. Install Netlify CLI
npm install -g netlify-cli

# 2. Login
netlify login

# 3. Deploy
cd /Users/sanman/Documents/cro-website3/html-site
netlify deploy --prod
```

### Pre-Deployment Checklist

- [ ] Update copyright year in footer
- [ ] Test all navigation links
- [ ] Test contact form (add form handling)
- [ ] Verify all images are optimized
- [ ] Test on mobile devices
- [ ] Run Lighthouse audit (aim for 90+ scores)
- [ ] Check browser compatibility
- [ ] Add favicon.ico
- [ ] Add meta tags for SEO
- [ ] Add Open Graph tags for social sharing

## Browser Support

**Tested & Supported:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Features Requiring Polyfills (for older browsers):**
- Intersection Observer
- CSS custom properties
- backdrop-filter (glassmorphism)
- clamp()

## Maintenance

### Regular Updates

**Content:**
- Update copyright year annually
- Review and update metrics quarterly
- Update service descriptions as offerings change

**Technical:**
- Update Google Fonts CDN links annually
- Test with latest browsers quarterly
- Review analytics and optimize based on user behavior
- Update CLAUDE.md when making structural changes

## Future Enhancements

### Phase 2 Features (Optional)
- [ ] Blog/News section for publications
- [ ] Case studies with detailed project examples
- [ ] Team member photos and bios
- [ ] Interactive capabilities assessment tool
- [ ] Client testimonials/logos
- [ ] White papers download section
- [ ] Newsletter signup integration

### Technical Improvements (Optional)
- [ ] Add favicon set (16x16, 32x32, 180x180, 512x512)
- [ ] Implement service worker for offline support
- [ ] Add structured data (JSON-LD) for rich snippets
- [ ] Integrate analytics (Plausible or Fathom)
- [ ] Add contact form backend (Formspree, Netlify Forms)
- [ ] Optimize images (WebP with fallbacks)
- [ ] Add print stylesheet
- [ ] Implement dark/light mode toggle (optional)

## Troubleshooting

### Common Issues

**Issue:** Animations not triggering
- **Solution:** Check that `body.loaded` class is added
- **Solution:** Verify Intersection Observer thresholds
- **Solution:** Check `data-reveal` attributes are present

**Issue:** Glassmorphism not showing
- **Solution:** Verify `backdrop-filter` browser support
- **Solution:** Check background elements have content behind them
- **Solution:** Add `-webkit-backdrop-filter` for Safari

**Issue:** Mobile menu not closing
- **Solution:** Check click event listeners are attached
- **Solution:** Verify `.is-open` class toggling
- **Solution:** Check z-index stacking context

**Issue:** Smooth scroll not working
- **Solution:** Verify `scroll-behavior: smooth` in CSS
- **Solution:** Check JavaScript smooth scroll polyfill
- **Solution:** Test with reduced motion preference disabled

## Contact Information

**Project Owner:** Tracescribe Research
**Website:** (Production URL to be added)
**Development Server:** http://localhost:8080
**Last Updated:** February 2026

---

## Quick Reference Commands

```bash
# Start dev server
cd /Users/sanman/Documents/cro-website3/html-site && python3 -m http.server 8080

# Stop server
# Press Ctrl+C in terminal

# Check for broken links (requires linkchecker)
linkchecker http://localhost:8080

# Validate HTML (requires html5validator)
html5validator --root /Users/sanman/Documents/cro-website3/html-site

# Minify CSS for production (requires cleancss)
cleancss -o styles.min.css styles.css

# Minify JS for production (requires uglifyjs)
uglifyjs script.js -o script.min.js -c -m
```

---

*This CLAUDE.md file provides comprehensive documentation for AI assistants working on this project. Update this file when making significant changes to structure, design system, or functionality.*
