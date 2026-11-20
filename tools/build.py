"""Generates the static pages in ../site from the Figma measurements.
All numbers are Figma pixels on the 1512-wide MacBook Pro 14" frames."""
import os
import json
import mobile
from common import head, nav, foot, media

SITE = ".."
V = "/assets/video/"
I = "/assets/img/"
S = "/assets/svg/"


FH = json.load(open(os.path.join(os.path.dirname(__file__), "fh.json")))


def tag_figma_heights(html):
    """Add data-fh="<Figma box height>" to each multi-line text so site.js can match Figma's line breaks."""
    import re
    for key, h in FH.items():
        k = key.replace("&", "&amp;").strip()
        i = html.find(">" + k, html.find("<body"))
        while i != -1:
            j = html.rfind("<", 0, i)
            tag = html[j:i]
            if tag.startswith("<span"):            # text starts with a bold span: tag its parent instead
                i = j - 1; j = html.rfind("<", 0, i)   # i now points at the parent's ">"
                tag = html[j:i]
            if not tag.startswith("</") and "data-fh" not in tag:
                html = html[:i] + f' data-fh="{h}"' + html[i:]
                break
            i = html.find(">" + k, i + 1)
    return html


def write(path, html):
    html = tag_figma_heights(html)
    depth = path.count("/")
    pre = "../" * depth
    html = html.replace('"/assets/', '"' + pre + 'assets/').replace("'/assets/", "'" + pre + "assets/")
    for a, b in [('"/about/"', 'about/index.html'), ('"/play/"', 'play/index.html'), ('"/resume/"', 'resume/index.html'),
                 ('"/work/gotgt/"', 'work/gotgt/index.html'), ('"/"', 'index.html')]:
        html = html.replace('href=' + a, 'href="' + pre + b + '"')
    p = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)


def doodle(kind, x, y, w, h, svg=None):
    if kind in ("smile", "frown"):
        return f'<div class="doodle" data-face="{kind}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
    return f'<img class="doodle" src="{S}{svg}" alt="" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'


# ============================================================== HOME
def card(i, title, sub, role, date, media_html, soon, sub_w=578, last=False):
    tag = "div" if soon else "a"
    attr = ' data-soon' if soon else ' href="/work/gotgt/" data-nav'
    label = f' aria-label="{title} — case study coming soon"' if soon else ""
    return f"""
  <{tag} class="card"{attr}{label} style="display:block;width:1006px">
    {media_html}
    <div style="position:relative;margin-top:30px;height:{108 if sub_w > 600 else 76}px">
      <div style="position:absolute;left:30px;top:0;width:{sub_w}px">
        <h2 class="t-title ink">{title}</h2>
        <p class="t-sub ink">{sub}</p>
      </div>
      <div style="position:absolute;left:806px;top:0;white-space:nowrap">
        <p class="t-20 ink">{role}</p>
        <p class="t-20l">{date}</p>
      </div>
    </div>
    <div class="rule" style="margin-top:60px;{'visibility:hidden' if last else ''}"></div>
  </{tag}>"""


home = head("Erin Hsu — visual experience designer",
            "Erin Hsu is a product designer studying Human-Computer Interaction, Design & Art at Carnegie Mellon University.",
            2818)
home += nav(0)
home += """<div class="hl" data-sweep="load" style="left:300px;top:137px;width:210px;height:32px"></div>
<h1 class="t-display over" data-top-after style="position:absolute;left:80px;top:96px;white-space:nowrap">Erin Hsu is hungry.</h1>

<aside style="position:absolute;left:0;top:169px;width:396px;height:2649px">
  <!-- Figma "Frame 45": scrolls up with the page, then stays put once it reaches the top -->
  <div class="side-fixed" style="position:sticky;top:0;height:var(--vhd)">
    <div class="t-20l" style="position:absolute;left:80px;top:82px;width:308px">
      <p>Hi! I’m a product designer studying Human-Computer Interaction, Design, &amp; Art @ Carnegie Mellon University.</p>
      <p style="margin-top:25px">I am interested in how design can translate complexity into delightful, human experiences.</p>
      <p style="margin-top:25px">But most of the time, I am just <a href="/about/" class="link" style="color:var(--deep)">hungry...</a></p>
    </div>
    <div class="picker" role="group" aria-label="Pick a cursor: stamp a smiley, stamp a frown, or the normal cursor" style="position:absolute;left:0;top:0">
      <button data-mode="smile" aria-label="Smiley stamp" style="left:81px;top:409px;width:41.5px;height:26.9px" data-face="smile"></button>
      <button data-mode="frown" aria-label="Frowny stamp" style="left:150px;top:408px;width:41.8px;height:35.2px" data-face="frown"></button>
      <button data-mode="ball" aria-label="Normal cursor" class="ball-opt" style="left:218px;top:408px;width:33px;height:33px"></button>
    </div>
    <nav class="t-nav side-nav reveal" aria-label="More" style="position:absolute;left:0;top:calc(var(--vhd) - 63px);width:396px;height:20px">
      <a href="/about/" style="position:absolute;left:80px">About</a>
      <a href="/play/" style="position:absolute;left:195px">Play</a>
      <a href="/resume/" style="position:absolute;left:310px">Resume</a>
    </nav>
  </div>
</aside>

<main style="position:absolute;left:426px;top:252px;width:1006px;display:flex;flex-direction:column;gap:80px">"""
home += card(0, "GoTgt", "Designing spontaneous connection within busy routines", "Lead Designer", "Jan-May 2026",
             media(V + "gotgt-wordmark-motion.mp4", 1006, 615.8, kind="video", alt="GoTgt wordmark animation"), False)
home += card(1, "Wild Font Finder", "Whimsical tool for designers to collect fonts in the wild", "Solo Designer", "Oct 2026",
             media(V + "wild-font-finder.mp4", 1006, 566, kind="video", alt="Wild Font Finder app on a phone"), True)
home += card(2, "Lunar Gala", "Reshaping the direction of photography of the largest fashion organization in Pennsylvania",
             "Head of Photography", "Aug 2024-May 2026",
             media(V + "lunar-gala-thumbnail.mp4", 1006, 566, kind="video", alt="Lunar Gala runway"), True, sub_w=716, last=True)
home += """
</main>

"""
home += foot(2818, raised=True, mobile=mobile.home())
write("index.html", home)

# ============================================================== ABOUT
about = head("About — Erin Hsu", "So, why is Erin Hsu hungry?", 1104)
about += nav(1)
about += f"""
{media(I + "about-erin.jpg", 491, 691, 165, 250, alt="Erin holding a knife, about to cut a cake she made")}
<p class="t-label ink" style="position:absolute;left:165px;top:955px;width:491px">Me holding a knife, about to cut a cake I made</p>

<div style="position:absolute;left:741px;top:250px;width:576px">
  <h1 class="t-h2" data-top-after>So, why is Erin Hsu hungry?</h1>
  <p class="t-24l ink" style="position:absolute;left:0;top:64px;width:576px">I am a designer who leads with gluttony &amp; greed. I see inefficiency &amp; incompetency in everything &amp; want it to be better. And then I think, <em>what is stopping me from making that happen?</em></p>
</div>
<div class="t-20l about-copy" style="position:absolute;left:741px;top:531px;width:576px">
  <p style="position:absolute;left:0;top:0">I use hunger as the primary way to describe myself because nothing else quite captures who I am so holistically. Yes, I am literally hungry in the sense that I am always eating &amp; cooking, but the very same ambition I have for food spans into the other areas of interest in my life, especially my work.</p>
  <p style="position:absolute;left:0;top:155px">I get hungry where there is friction to resolve and systems to string together. Where there is potential for clarity, whimsy, or efficiency, there is me, hungry, greedy, gluttonous to make it happen.</p>
  <p style="position:absolute;left:0;top:285px">Please note that while I am greedy, my core values stem from <span class="strong">empathy &amp; curiosity</span>. As much as I care about pushing beyond the limits, I care equally as much for how I get there. I believe it would be pointless to be hungry without also carefully making effort to understand &amp; connect with the peers, users, humans, involved.</p>
</div>
"""
about += foot(1104, mobile=mobile.about())
write("about/index.html", about)

# ============================================================== PLAY
cols = [
    (195, 318, [424, 424, 212, 222.5]),
    (543, 201, [268.9, 268, 269.8, 287]),
    (774, 320, [213, 99.8, 241.6, 347.9, 165.6]),
    (1124, 201, [186, 281.4, 310, 260.9, 268]),
]
play = head("Play — Erin Hsu", "Paintings, photography, illustration and other things Erin makes for fun.", 1804)
play += nav(2)
play += '<div data-top-after style="position:absolute;left:0;top:156px;width:1px;height:1px"></div>\n'
n = 0
for x, w, hs in cols:
    play += f'<div style="position:absolute;left:{x}px;top:246px;width:{w}px;display:flex;flex-direction:column;gap:30px">\n'
    for h in hs:
        n += 1
        play += "  " + media(f"{I}play/{n:02d}.webp", w, h, alt="").replace('class="media"', 'class="media" data-hold', 1) + "\n"
    play += "</div>\n"
play += foot(1804, mobile=mobile.play())
write("play/index.html", play)

# ============================================================== RESUME
def rrow(left, right, right_w=546, right_x=344.6):
    lw = 315 if 'Coalition' in left else 266.6
    return f"""<div style="display:flex;align-items:flex-start">
      <div style="width:{lw}px;flex:none">{left}</div>
      <div class="t-20l" style="margin-left:{right_x - lw:.1f}px;width:{right_w}px;flex:none">{right}</div>
    </div>"""


def job(title, org, when, where):
    return (f'<p class="t-24 ink">{title}</p><p class="t-20 muted">{org}</p>'
            f'<div style="margin-top:8px"><p class="t-20l">{when}</p><p class="t-20l">{where}</p></div>')


B = lambda s: f'<span class="strong">{s}</span>'
resume = head("Resume — Erin Hsu", "Education, experience, expertise and achievements.", 1703)
resume += nav(3)
resume += f"""
<div data-top-after style="position:absolute;left:0;top:156px;width:1px;height:1px"></div>
<div style="position:absolute;left:195px;top:242px;width:1122px;display:flex;flex-direction:column;gap:100px">

  <section style="position:relative;height:88px">
    <h2 class="t-label ink">Education</h2>
    <div style="position:absolute;left:231px;top:0">
      <div style="width:315px">
        <p class="t-24 ink">Carnegie Mellon University</p>
        <div style="margin-top:8px"><p class="t-20l">Aug 2023 - May 2027</p><p class="t-20l">Pittsburgh, PA</p></div>
      </div>
      <div style="position:absolute;left:345px;top:0;width:430px">
        <p class="t-20 ink">B.S. Human-Computer Interaction (HCI)</p>
        <p class="t-20 ink" style="margin-top:5px;height:22.6px">B.A. Visual Experience Design</p>
        <p class="t-20l" style="margin-top:5px">3.83 GPA</p>
      </div>
    </div>
  </section>

  <section style="position:relative">
    <h2 class="t-label ink" style="position:absolute;left:0;top:0">Experience</h2>
    <div style="margin-left:231px;display:flex;flex-direction:column;gap:49px">
      {rrow(job("Product Design Intern", "Empyrean Technology", "May – July 2026", "San Jose, CA"),
            B("Designed and prototyped") + " a license request portal to replace an email-only process; Turned a software requirements spec into " + B("2 user flows") + " using Figma and Claude; Conducted user testing &amp; packaged the prototype to ship")}
      {rrow(job("Digital Media Design Intern", "Chinese American Coalition for Compassionate Care", "May – August 2026", "Cupertino, CA"),
            B("Built and shipped 2") + " custom CSS plugins using Claude Code; Redesigned the nonprofit’s homepage from a WordPress template into a readable, structured experience for Chinese American elders and caregivers", right_x=345)}
      {rrow(job("Executive Director", "Lunar Gala", "May 2026 – Present", "Pittsburgh, PA"),
            "Producing Pennsylvania's largest annual fashion show for " + B("1,500+ attendees") + ", managing of " + B("200 members") + " across " + "8 departments &amp; 13 subdepartments; Previously " + B("Director of Production") + ", overseeing lighting, sound, stage management, &amp; livestream, &amp; " + B("Director of Photography") + " over 15 photographers")}
      {rrow(job("Teaching Assistant", "CMU School of Design", "Jan – May 2026", "Pittsburgh, PA"),
            "Supported " + B("20 students in Information Design course") + " through critiques on communication design and data visualization, guiding their design reasoning across iterations")}
    </div>
  </section>

  <section style="position:relative">
    <h2 class="t-label ink" style="position:absolute;left:0;top:0">Expertise</h2>
    <div style="margin-left:231px;display:flex;flex-direction:column;gap:40px">
      {rrow('<p class="t-24 ink">Skills</p>', "Visual design, Product thinking, Prototyping, Design systems, Branding, Illustration, User research, Usability testing, User flow, English (native), Mandarin (native)")}
      {rrow('<p class="t-24 ink">Software</p>', "Figma (Make, Motion, Jam), Adobe Creative Cloud, Claude (Code, Design), WordPress, CSS, Python, Miro")}
    </div>
  </section>

  <section style="position:relative">
    <h2 class="t-label ink" style="position:absolute;left:0;top:0">Achievements</h2>
    <div style="margin-left:231px;display:flex;flex-direction:column;gap:8px">
      {rrow('<p class="t-24 ink">xHacks 2026</p>', B("1st place ") + "with a team of 4, among ~120 participants", right_w=429.8)}
      {rrow('<p class="t-24 ink">Lemon Publication 2026</p>', "Featured print work, The Baby and the House", right_w=429.8)}
      {rrow('<p class="t-24 ink">Lemon Publication 2025</p>', "Featured 2 paintings, 婆 [pó] and On a Hike", right_w=429.8)}
    </div>
  </section>
</div>
"""
resume += foot(1703, mobile=mobile.resume())
write("resume/index.html", resume)

import casestudy  # noqa: E402  (GoTgt page lives in its own file)
write("work/gotgt/index.html", casestudy.build())
print("built")
