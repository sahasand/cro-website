#!/usr/bin/env python3
"""
Rebuild the genericized Theme 6 ("Holographic Deck") from the ORIGINAL CCS deck.

Usage:
    python3 rebuild_theme6.py <path-to-original-6-new-index.html> <output-path>
    # e.g. python3 rebuild_theme6.py 6-new/index.html 6/index.html

Re-applies the full CCS -> Tracescribe genericization that was lost when the
working file was deleted. Reports any replacement that did NOT match (count 0),
so a slightly different source can be caught and patched.
"""
import re, io, sys

SIL = ('<svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor" '
       'aria-hidden="true"><path d="M12 12.6a4.3 4.3 0 1 0 0-8.6 4.3 4.3 0 0 0 0 '
       '8.6Zm0 1.7c-4.4 0-8 2.2-8 5.2V21h16v-1.5c0-3-3.6-5.2-8-5.2Z"/></svg>')

# (label, old, new) literal replacements, applied in order on the ORIGINAL text.
LITERAL = [
 ("sub",
  '<span class="sub">Cardiovascular<br />Clinical Sciences</span>',
  '<span class="sub">Cardiovascular<br />Research</span>'),
 ("hud-coords",
  'Boston, MA · 42.3601° N / 71.0589° W',
  'Cardiovascular Clinical Research · Est. 1997'),
 ("hero-lede",
  'A physician-led cardiovascular CRO across drug and device. Konstam, Udelson, and the same senior team on every protocol from concept through database lock.',
  'A physician-led cardiovascular CRO across drug and device. The same senior cardiologists on every protocol from concept through database lock.'),
 ("hero-footer",
  'Boston, MA &nbsp;·&nbsp; Founded 1997 &nbsp;·&nbsp; Tufts Medical Center Partnership',
  'Founded 1997 &nbsp;·&nbsp; Cardiovascular Clinical Research &nbsp;·&nbsp; Drug, Device &amp; Combination'),
 ("glance-stat",
  'Founded · Boston<br />Tufts partnership',
  'Founded<br />Cardiovascular CRO'),
 ("thesis-attr",
  'Marvin Konstam, MD &nbsp;&amp;&nbsp; James Udelson, MD · Founders, Cardiovascular Clinical Sciences · Tufts Medical Center',
  'Founders · Tracescribe Research'),
 ("opmodel",
  'Konstam, Udelson, and senior cardiology staff engage',
  'Senior cardiologists engage'),
 ("corelab-jingdai",
  'Core Lab Operations are led by <strong style="color:var(--white);">Jing Dai, MD &amp; PhD</strong>.',
  'Core Lab Operations are led by our <strong style="color:var(--white);">Director of Core Laboratory Operations</strong>.'),
 ("corelab-av",
  '<div class="mono-av" aria-hidden="true">JD</div>',
  '<div class="mono-av" aria-hidden="true">' + SIL + '</div>'),
 ("founder1-av+name",
  '<div class="mono-av has-photo" aria-hidden="true"><img class="av-img" src="assets/konstam.webp" alt="" /></div>\n            <div><h3 style="font-size:1.18rem;">Marvin Konstam, MD</h3><div class="kicker" style="color:#FF8D96; margin-top:5px;">Founder · Chief Scientific Officer</div></div>',
  '<div class="mono-av" aria-hidden="true">' + SIL + '</div>\n            <div><h3 style="font-size:1.18rem;">Founder &amp; Chief Scientific Officer, M.D.</h3><div class="kicker" style="color:#FF8D96; margin-top:5px;">Heart Failure &amp; Cardiorenal</div></div>'),
 ("founder1-bio",
  '<li><span class="pill">Leadership</span> &nbsp;Chief Physician Executive Emeritus, Tufts CV Center · Past President, HFSA</li>\n            <li><span class="pill">Academic</span> &nbsp;Professor of Medicine &amp; Radiology, Tufts University School of Medicine</li>\n            <li><span class="pill">Regulatory</span> &nbsp;Multiple FDA Advisory Panels · Close work with CDER &amp; CDRH</li>',
  '<li><span class="pill">Leadership</span> &nbsp;Senior cardiology leadership at an academic medical center · Heart-failure society leadership</li>\n            <li><span class="pill">Academic</span> &nbsp;Professor of Medicine &amp; Radiology at an academic medical center</li>\n            <li><span class="pill">Regulatory</span> &nbsp;Multiple FDA advisory panels · Close work with CDER &amp; CDRH</li>'),
 ("founder2-av+name",
  '<div class="mono-av has-photo" aria-hidden="true"><img class="av-img" src="assets/udelson.webp" alt="" /></div>\n            <div><h3 style="font-size:1.18rem;">James Udelson, MD</h3><div class="kicker" style="color:#FF8D96; margin-top:5px;">Founder · Chief Medical Officer</div></div>',
  '<div class="mono-av" aria-hidden="true">' + SIL + '</div>\n            <div><h3 style="font-size:1.18rem;">Founder &amp; Chief Medical Officer, M.D.</h3><div class="kicker" style="color:#FF8D96; margin-top:5px;">Nuclear Cardiology &amp; Imaging</div></div>'),
 ("founder2-bio",
  '<li><span class="pill">Leadership</span> &nbsp;Chief of Cardiology &amp; Director of Nuclear Cardiology, Tufts · Past President, ASNC · ACC Board</li>\n            <li><span class="pill">Academic</span> &nbsp;Professor of Medicine &amp; Radiology · Associate Editor, JAMA Cardiology</li>\n            <li><span class="pill">Regulatory</span> &nbsp;Past member, FDA Medical Imaging Drugs AC · Ad-hoc Cardio-Renal panels</li>',
  '<li><span class="pill">Leadership</span> &nbsp;Chief of Cardiology &amp; Director of Nuclear Cardiology at an academic medical center · Nuclear cardiology society leadership</li>\n            <li><span class="pill">Academic</span> &nbsp;Professor of Medicine &amp; Radiology · Associate Editor, a leading cardiology journal</li>\n            <li><span class="pill">Regulatory</span> &nbsp;Former member, FDA medical imaging advisory committee · Ad-hoc cardio-renal panels</li>'),
 ("team-konstam",
  '<div class="mono-av has-photo" style="margin:0 auto 16px;"><img class="av-img" src="assets/konstam.webp" alt="" /></div><h3 style="font-size:1.03rem;">Marvin Konstam, MD</h3><div class="kicker" style="margin-top:6px;">Founder &amp; Chief Scientific Officer</div>',
  '<div class="mono-av" style="margin:0 auto 16px;">' + SIL + '</div><h3 style="font-size:1.03rem;">Founder &amp; Chief Scientific Officer, M.D.</h3><div class="kicker" style="margin-top:6px;">Heart Failure &amp; Cardiorenal</div>'),
 ("team-udelson",
  '<div class="mono-av has-photo" style="margin:0 auto 16px;"><img class="av-img" src="assets/udelson.webp" alt="" /></div><h3 style="font-size:1.03rem;">James Udelson, MD</h3><div class="kicker" style="margin-top:6px;">Founder &amp; Chief Medical Officer</div>',
  '<div class="mono-av" style="margin:0 auto 16px;">' + SIL + '</div><h3 style="font-size:1.03rem;">Founder &amp; Chief Medical Officer, M.D.</h3><div class="kicker" style="margin-top:6px;">Nuclear Cardiology &amp; Imaging</div>'),
 ("team-rusch",
  '<div class="mono-av has-photo" style="margin:0 auto 16px;"><img class="av-img" src="assets/rusch.webp" alt="" /></div><h3 style="font-size:1.03rem;">Lorraine Rusch, PhD</h3><div class="kicker" style="margin-top:6px;">CEO &amp; President</div>',
  '<div class="mono-av" style="margin:0 auto 16px;">' + SIL + '</div><h3 style="font-size:1.03rem;">Chief Executive Officer, Ph.D.</h3><div class="kicker" style="margin-top:6px;">Operations &amp; Delivery</div>'),
 ("team-patel",
  '<div class="mono-av has-photo" style="margin:0 auto 16px;"><img class="av-img" src="assets/patel.webp" alt="" /></div><h3 style="font-size:1.03rem;">Ayan Patel, MD</h3><div class="kicker" style="margin-top:6px;">Medical Director</div>',
  '<div class="mono-av" style="margin:0 auto 16px;">' + SIL + '</div><h3 style="font-size:1.03rem;">Medical Director, M.D.</h3><div class="kicker" style="margin-top:6px;">Clinical &amp; Core Lab</div>'),
 ("team-dibattista",
  '<div class="mono-av" style="margin:0 auto 16px;">MD</div><h3 style="font-size:1.03rem;">Michael DiBattista</h3><div class="kicker" style="margin-top:6px;">Director, Project Delivery</div>',
  '<div class="mono-av" style="margin:0 auto 16px;">' + SIL + '</div><h3 style="font-size:1.03rem;">Director, Project Delivery</h3><div class="kicker" style="margin-top:6px;">Clinical Operations</div>'),
 ("team-jingdai",
  '<div class="mono-av" style="margin:0 auto 16px;">JD</div><h3 style="font-size:1.03rem;">Jing Dai, MD &amp; PhD</h3><div class="kicker" style="margin-top:6px;">Director, Core Lab Operations</div>',
  '<div class="mono-av" style="margin:0 auto 16px;">' + SIL + '</div><h3 style="font-size:1.03rem;">Director, Core Laboratory Operations</h3><div class="kicker" style="margin-top:6px;">Imaging &amp; Core Lab</div>'),
 ("synth-core-mk",
  '<span class="synth-core-mk">CCS</span>',
  '<span class="synth-core-mk" style="font-size:1.6rem;">Tracescribe</span>'),
 ("footer-affil",
  'Boston, MA · Founded 1997 · Tufts Medical Center Partnership',
  'Founded 1997 · Cardiovascular Clinical Research'),
]

NEW_EVENTS = '''var events = [
      { name: "Cardiovascular Clinical Research Forum",     start: "2026-07-15", end: "2026-07-17", loc: "Chicago, IL" },
      { name: "Heart Failure Therapeutics Summit",          start: "2026-08-26", end: "2026-08-29", loc: "Berlin, Germany" },
      { name: "Structural Heart & Imaging Symposium",       start: "2026-09-18", end: "2026-09-20", loc: "Denver, CO" },
      { name: "Global Cardiology Trials Congress",          start: "2026-10-08", end: "2026-10-11", loc: "Madrid, Spain" },
      { name: "Interventional Cardiovascular Meeting",      start: "2026-10-30", end: "2026-11-02", loc: "San Francisco, CA" },
      { name: "Cardiac Endpoints & Adjudication Workshop",  start: "2026-11-12", end: "2026-11-13", loc: "London, UK" },
      { name: "Cardiovascular Innovation Sessions",         start: "2026-12-04", end: "2026-12-06", loc: "Singapore" }
    ];'''

SWITCHER_CSS = '''
  /* ---------- theme switcher ---------- */
  #themeSwitcher{position:fixed;right:1.25rem;top:50%;transform:translateY(-50%);z-index:10001;display:flex;flex-direction:column;align-items:center;gap:0.4rem;padding:0.75rem 0.5rem;background:rgba(4,13,29,0.78);backdrop-filter:blur(18px) saturate(150%);-webkit-backdrop-filter:blur(18px) saturate(150%);border:1px solid rgba(230,57,70,0.18);border-radius:100px;box-shadow:0 8px 36px rgba(0,0,0,0.5)}
  #themeSwitcher a{text-decoration:none;display:flex;align-items:center;justify-content:center}
  #themeSwitcher .ts-home{width:28px;height:28px;color:rgba(159,182,218,0.55);transition:color .3s ease,transform .3s cubic-bezier(0.34,1.56,0.64,1)}
  #themeSwitcher .ts-home:hover{color:#E63946;transform:scale(1.1)}
  #themeSwitcher .ts-home svg{width:14px;height:14px}
  #themeSwitcher .ts-sep{width:14px;height:1px;background:rgba(230,57,70,0.28)}
  #themeSwitcher .ts-dot{width:28px;height:28px;position:relative;transition:transform .3s cubic-bezier(0.34,1.56,0.64,1)}
  #themeSwitcher .ts-dot:hover{transform:scale(1.15)}
  #themeSwitcher .ts-dot-inner{width:10px;height:10px;border-radius:50%;border:1px solid rgba(159,182,218,0.18);transition:transform .3s cubic-bezier(0.34,1.56,0.64,1),box-shadow .3s}
  #themeSwitcher .ts-dot:hover .ts-dot-inner{transform:scale(1.4)}
  #themeSwitcher .ts-dot.active .ts-dot-inner{transform:scale(1.5);box-shadow:0 0 0 3px rgba(230,57,70,0.5),0 0 14px rgba(230,57,70,0.6)}
  #themeSwitcher .ts-tip{position:absolute;right:38px;top:50%;transform:translateY(-50%) translateX(6px);white-space:nowrap;background:rgba(4,13,29,0.95);color:#E9EEF7;font-family:var(--mono);font-size:10px;letter-spacing:0.08em;text-transform:uppercase;padding:5px 10px;border-radius:7px;border:1px solid rgba(230,57,70,0.25);opacity:0;pointer-events:none;transition:opacity .25s ease,transform .25s ease}
  #themeSwitcher .ts-dot:hover .ts-tip{opacity:1;transform:translateY(-50%) translateX(0)}
  @media (max-width:768px){#themeSwitcher{right:0.6rem;padding:0.55rem 0.4rem;gap:0.3rem}#themeSwitcher .ts-tip{display:none}}
'''

SWITCHER_NAV = '''
<!-- theme switcher -->
<nav id="themeSwitcher" aria-label="Theme navigation">
  <a href="../index.html" class="ts-home" title="Gallery" aria-label="Back to gallery">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect>
      <rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>
    </svg>
  </a>
  <div class="ts-sep"></div>
  <a href="../theme1-corporate.html" class="ts-dot" aria-label="Theme 1: Precision & Prestige"><span class="ts-dot-inner" style="background:linear-gradient(135deg,#1e3a5f 50%,#c9a84c 50%);"></span><span class="ts-tip">Precision &amp; Prestige</span></a>
  <a href="../2/index.html" class="ts-dot" aria-label="Theme 2: Clinical Evidence"><span class="ts-dot-inner" style="background:linear-gradient(135deg,#0A1628 50%,#C41E3A 50%);"></span><span class="ts-tip">Clinical Evidence</span></a>
  <a href="../theme3-warm.html" class="ts-dot" aria-label="Theme 3: Organic Flow"><span class="ts-dot-inner" style="background:linear-gradient(135deg,#faf8f5 50%,#e8634a 50%);"></span><span class="ts-tip">Organic Flow</span></a>
  <a href="../theme4-brutalist.html" class="ts-dot" aria-label="Theme 4: Raw & Bold"><span class="ts-dot-inner" style="background:linear-gradient(135deg,#0a0a0a 50%,#ff2d2d 50%);"></span><span class="ts-tip">Raw &amp; Bold</span></a>
  <a href="../5/index.html" class="ts-dot" aria-label="Theme 5: Natural Authority"><span class="ts-dot-inner" style="background:linear-gradient(135deg,#f3efe5 50%,#0a8d80 50%);"></span><span class="ts-tip">Natural Authority</span></a>
  <a href="../6/index.html" class="ts-dot active" aria-label="Theme 6: Holographic Deck" aria-current="page"><span class="ts-dot-inner" style="background:linear-gradient(135deg,#02060F 50%,#E63946 50%);"></span><span class="ts-tip">Holographic Deck</span></a>
</nav>
'''

def main():
    src, dst = sys.argv[1], sys.argv[2]
    s = io.open(src, encoding="utf-8").read()
    problems = []

    for label, old, new in LITERAL:
        if old in s:
            s = s.replace(old, new)
        else:
            problems.append(label)

    s, n = re.subn(r'var events = \[.*?\];', NEW_EVENTS, s, count=1, flags=re.DOTALL)
    if n != 1: problems.append("events-array")

    s = s.replace('Cardiovascular Clinical Sciences', 'Tracescribe Research')
    s = re.sub(r'\bCCS\b', 'Tracescribe', s)
    s = s.replace('ccstrials.com', 'tracescribe.com')
    s = s.replace('__ccs3dReady', '__ts3dReady')
    s = s.replace('lCcs', 'lOneTeam')

    # description / header cleanup after the global passes
    s = s.replace('Tracescribe Research (Tracescribe): a cardiovascular',
                  'Tracescribe Research: a cardiovascular')
    s = s.replace('database lock. Boston · Founded 1997.',
                  'database lock. Founded 1997.')
    s = s.replace('Founders · Founded 1997 · Tufts Medical Center',
                  'Founders · Founded 1997')

    # theme switcher: CSS before first </style>, markup after #progress
    css_anchor = '    .tl-track.on .tl-fill, .tl-track .tl-fill { width: 100%; }\n  }\n</style>'
    if css_anchor in s:
        s = s.replace(css_anchor,
                      '    .tl-track.on .tl-fill, .tl-track .tl-fill { width: 100%; }\n  }\n' + SWITCHER_CSS + '</style>', 1)
    else:
        problems.append("switcher-css-anchor")
    nav_anchor = '<div id="progress" aria-hidden="true"></div>\n\n<!-- HUD instrument frame -->'
    if nav_anchor in s:
        s = s.replace(nav_anchor,
                      '<div id="progress" aria-hidden="true"></div>\n' + SWITCHER_NAV + '\n<!-- HUD instrument frame -->', 1)
    else:
        problems.append("switcher-nav-anchor")

    io.open(dst, "w", encoding="utf-8").write(s)

    for tok in ["CCS", "Konstam", "Udelson", "Rusch", "Patel", "DiBattista",
                "Jing Dai", "Tufts", "Boston", "ccstrials", ".webp", "assets/"]:
        c = s.count(tok)
        if c: problems.append(f"RESIDUE {tok}={c}")
    print("UNMATCHED/RESIDUE:", problems if problems else "none — clean")
    print("Tracescribe count:", s.count("Tracescribe"), "| themeSwitcher:", s.count('id="themeSwitcher"'))

if __name__ == "__main__":
    main()
