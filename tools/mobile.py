"""Phone layouts (Figma section "Mobile (390)"). One column, 24px side margins.

Each page's desktop canvas (.page) is hidden below 700px and this markup (.m) is shown instead.
The content and assets are the same as desktop; only the layout changes."""

V = "/assets/video/"
I = "/assets/img/"
S = "/assets/svg/"
G = "/assets/gif/"

BACK = ('<svg width="28" height="20" viewBox="0 0 42 30" fill="none" aria-hidden="true"><path d="M40 16.7C41.1 16.7 42 15.8 42 14.7C42 13.6 41.1 12.7 40 12.7V14.7V16.7ZM40 14.7V12.7L2 12.7V14.7V16.7L40 16.7V14.7ZM0.6 13.3C-0.2 14.1 -0.2 15.4 0.6 16.1L13.3 28.9C14.1 29.7 15.4 29.7 16.1 28.9C16.9 28.1 16.9 26.8 16.1 26L4.8 14.7L16.1 3.4C16.9 2.6 16.9 1.4 16.1 0.6C15.4 -0.2 14.1 -0.2 13.3 0.6L0.6 13.3Z" fill="#DDF396"/></svg>')

B = lambda s: f'<span class="strong">{s}</span>'


def nav(active):
    items = [("Work", "/"), ("About", "/about/"), ("Play", "/play/"), ("Resume", "/resume/")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if i == active else ""}>{t}</a>' for i, (t, h) in enumerate(items))
    return f'<nav class="m-nav" aria-label="Main">{links}</nav>\n'


FOOT = """<footer class="m-foot">
  <a href="mailto:erinhsu@andrew.cmu.edu">erinhsu@andrew.cmu.edu</a>
  <a href="https://www.linkedin.com/in/erinhsuu" target="_blank" rel="noopener">linkedin</a>
  <a href="https://www.instagram.com/ernhsu/" target="_blank" rel="noopener">instagram</a>
</footer>
"""


def vid(name, ratio, alt, pos="center"):
    return (f'<div class="m-media" style="aspect-ratio:{ratio}"><video src="{V}{name}.mp4" poster="{V}{name}-poster.jpg" '
            f'autoplay muted loop playsinline preload="metadata" aria-label="{alt}" style="object-position:{pos}"></video></div>')


def img(src, alt="", extra="", cls="m-media"):
    return f'<div class="{cls}"{extra}><img src="{src}" alt="{alt}" loading="lazy" decoding="async"></div>'


# ============================================================== HOME
def home():
    def card(title, sub, role, date, media, soon):
        tag, attr = ("div", f' data-soon aria-label="{title} — case study coming soon"') if soon else ("a", ' href="/work/gotgt/"')
        return f"""<{tag} class="m-card"{attr}>
  {media}
  <h2 class="m-card-title">{title}</h2>
  <p class="m-card-sub">{sub}</p>
  <p class="m-meta"><span class="ink">{role}</span><span>{date}</span></p>
</{tag}>
<div class="m-rule"></div>
"""
    return (nav(0) + """<h1 class="m-title" data-top-after>Erin Hsu is <span class="mark" data-sweep="load">hungry.</span></h1>
<div class="m-body">
  <p>Hi! I’m a product designer studying Human-Computer Interaction, Design, &amp; Art @ Carnegie Mellon University.</p>
  <p>I am interested in how design can translate complexity into delightful, human experiences.</p>
  <p>But most of the time, I am just <a href="/about/" class="link" style="color:var(--deep)">hungry...</a></p>
</div>
<div class="picker m-picker" role="group" aria-label="Drag a smiley or a frown onto the page">
  <button data-mode="smile" aria-label="Smiley stamp" style="width:41.5px;height:26.9px" data-face="smile"></button>
  <button data-mode="frown" aria-label="Frowny stamp" style="width:41.8px;height:35.2px" data-face="frown"></button>
  <button data-mode="ball" aria-label="Normal cursor" class="ball-opt" style="width:33px;height:33px"></button>
  <span class="m-hint">drag a face anywhere</span>
</div>
<div class="m-cards">
"""
            + card("GoTgt", "Designing spontaneous connection within busy routines", "Lead Designer", "Jan-May 2026",
                   vid("gotgt-wordmark-motion", "1006/616", "GoTgt wordmark animation"), False)
            + card("Wild Font Finder", "Whimsical tool for designers to collect fonts in the wild", "Solo Designer", "Oct 2026",
                   vid("wild-font-finder", "1006/566", "Wild Font Finder app on a phone"), True)
            + card("Lunar Gala", "Reshaping the direction of photography of the largest fashion organization in Pennsylvania",
                   "Head of Photography", "Aug 2024-May 2026", vid("lunar-gala-thumbnail", "1006/566", "Lunar Gala runway"), True)
            + "</div>\n" + FOOT)


# ============================================================== ABOUT
def about():
    return (nav(1) + f"""<div class="m-gap32"></div>
{img(I + "about-erin.jpg", "Erin holding a knife, about to cut a cake she made", ' style="aspect-ratio:491/691"')}
<p class="m-caption">Me holding a knife, about to cut a cake I made</p>
<h1 class="m-h1" data-top-after>So, why is Erin Hsu hungry?</h1>
<p class="m-lead">I am a designer who leads with gluttony &amp; greed. I see inefficiency &amp; incompetency in everything &amp; want it to be better. And then I think, <em>what is stopping me from making that happen?</em></p>
<div class="m-body m-body-15">
  <p>I use hunger as the primary way to describe myself because nothing else quite captures who I am so holistically. Yes, I am literally hungry in the sense that I am always eating &amp; cooking, but the very same ambition I have for food spans into the other areas of interest in my life, especially my work.</p>
  <p>I get hungry where there is friction to resolve and systems to string together. Where there is potential for clarity, whimsy, or efficiency, there is me, hungry, greedy, gluttonous to make it happen.</p>
  <p>Please note that while I am greedy, my core values stem from {B("empathy &amp; curiosity")}. As much as I care about pushing beyond the limits, I care equally as much for how I get there. I believe it would be pointless to be hungry without also carefully making effort to understand &amp; connect with the peers, users, humans, involved.</p>
</div>
""" + FOOT)


# ============================================================== PLAY
def play():
    # same pieces as desktop (01-18), poured into two columns, each piece going to the shorter column
    heights = [424, 424, 212, 222.5, 268.9, 268, 269.8, 287, 213, 99.8, 241.6, 347.9, 165.6, 186, 281.4, 310, 260.9, 268]
    widths = [318] * 4 + [201] * 4 + [320] * 5 + [201] * 5
    cols, hs = [[], []], [0.0, 0.0]
    for n, (h, w) in enumerate(zip(heights, widths), 1):
        r = h / w
        c = 0 if hs[0] <= hs[1] else 1
        cols[c].append(f'<div class="m-media" data-hold style="aspect-ratio:{w}/{h}"><img src="{I}play/{n:02d}.webp" alt="" loading="lazy" decoding="async"></div>')
        hs[c] += r + 0.1
    return (nav(2) + '<div class="m-gap32" data-top-after></div>\n<div class="m-play">'
            + "".join(f'<div>{"".join(c)}</div>' for c in cols) + "</div>\n" + FOOT)


# ============================================================== RESUME
def resume():
    def entry(title, org=None, when=None, where=None, desc=None):
        out = f'<div class="m-entry"><p class="m-entry-title">{title}</p>'
        if org:
            out += f'<p class="m-entry-org">{org}</p>'
        if when:
            out += f'<p class="m-meta"><span>{when}</span><span>{where}</span></p>'
        if desc:
            out += "".join(f'<p class="m-entry-desc">{d}</p>' for d in ([desc] if isinstance(desc, str) else desc))
        return out + "</div>"

    def section(label, entries):
        return f'<section class="m-section"><h2 class="m-label">{label}</h2>{"".join(entries)}</section>\n'

    return (nav(3) + '<div class="m-gap32" data-top-after></div>\n'
            + section("Education", [entry("Carnegie Mellon University", None, "Aug 2023 - May 2027", "Pittsburgh, PA",
                                          ['<span class="ink">B.S. Human-Computer Interaction (HCI)</span>',
                                           '<span class="ink">B.A. Visual Experience Design</span>', "3.83 GPA"])])
            + section("Experience", [
                entry("Product Design Intern", "Empyrean Technology", "May – July 2026", "San Jose, CA",
                      B("Designed and prototyped") + " a license request portal to replace an email-only process; Turned a software requirements spec into " + B("2 user flows") + " using Figma and Claude; Conducted user testing &amp; packaged the prototype to ship"),
                entry("Digital Media Design Intern", "Chinese American Coalition for Compassionate Care", "May – August 2026", "Cupertino, CA",
                      B("Built and shipped 2") + " custom CSS plugins using Claude Code; Redesigned the nonprofit’s homepage from a WordPress template into a readable, structured experience for Chinese American elders and caregivers"),
                entry("Executive Director", "Lunar Gala", "May 2026 – Present", "Pittsburgh, PA",
                      "Producing Pennsylvania's largest annual fashion show for " + B("1,500+ attendees") + ", managing of " + B("200 members") + " across 8 departments &amp; 13 subdepartments; Previously " + B("Director of Production") + ", overseeing lighting, sound, stage management, &amp; livestream, &amp; " + B("Director of Photography") + " over 15 photographers"),
                entry("Teaching Assistant", "CMU School of Design", "Jan – May 2026", "Pittsburgh, PA",
                      "Supported " + B("20 students in Information Design course") + " through critiques on communication design and data visualization, guiding their design reasoning across iterations")])
            + section("Expertise", [
                entry("Skills", desc="Visual design, Product thinking, Prototyping, Design systems, Branding, Illustration, User research, Usability testing, User flow, English (native), Mandarin (native)"),
                entry("Software", desc="Figma (Make, Motion, Jam), Adobe Creative Cloud, Claude (Code, Design), WordPress, CSS, Python, Miro")])
            + section("Achievements", [
                entry("xHacks 2026", desc=B("1st place ") + "with a team of 4, among ~120 participants"),
                entry("Lemon Publication 2026", desc="Featured print work, The Baby and the House"),
                entry("Lemon Publication 2025", desc="Featured 2 paintings, 婆 [pó] and On a Hike")])
            + FOOT)


# ============================================================== GoTgt case study
def gotgt():
    C = I + "cs/"

    def sec(label, statement, body):
        return (f'<div class="m-rule m-rule-sec"></div>\n<section class="m-cs-sec"><p class="m-label">{label}</p>'
                f'<h2 class="m-statement">{statement}</h2>{body}</section>\n')

    def p(t, cls="m-p"):
        return f'<p class="{cls}">{t}</p>'

    def face(kind, extra=""):
        return f'<img class="m-doodle" src="{S}doodle-{kind}.svg" alt=""{extra}>'

    ramp = [("Display XL", "ramen?", "font-family:nexa,sans-serif;font-size:36px;line-height:38px"),
            ("Display L", "ready to Tgt?", "font-family:nexa,sans-serif;font-size:26px;line-height:30px"),
            ("Title", "Costco run", "font-family:nexa,sans-serif;font-size:19px;line-height:23px"),
            ("Heading", "out right now", "font-family:nexa,sans-serif;font-size:16px;line-height:21px"),
            ("Body L", "She's going either way.", "font-family:'Open Sans',sans-serif;font-size:14px;line-height:21px"),
            ("Body", "Tsukiya, 6 min walk", "font-family:'Open Sans',sans-serif;font-size:13px;line-height:19px"),
            ("Body strong", "14 min", "font-family:'Open Sans',sans-serif;font-weight:600;font-size:13px;line-height:19px"),
            ("Caption", "posted 4 min ago", "font-family:'Open Sans',sans-serif;font-size:12px;line-height:17px"),
            ("Label", "out right now", "font-family:nexa,sans-serif;font-weight:700;font-size:11px;line-height:15px")]
    colors = [("ink", "#252525", False), ("muted", "#6E6E6E", False), ("line", "#ECECEA", True), ("mist", "#F7F7F5", True),
              ("yellow", "#FFD95C", False), ("blue", "#83C7FF", False), ("pink", "#FF83E6", False), ("green", "#43F697", False)]

    out = f'<a class="m-back" href="/" aria-label="Back to work">{BACK}</a>\n'
    out += vid("gotgt-wordmark-motion", "1009/618", "GoTgt wordmark animation")
    out += f"""<h1 class="m-card-title" data-top-after>GoTgt</h1>
<p class="m-card-sub">Designing spontaneous connection within busy routines</p>
<p class="m-meta"><span class="ink">Lead Designer</span><span>Jan-May 2026</span></p>
<p class="m-meta"><a class="link" href="https://go-tgt.vercel.app" target="_blank" rel="noopener" style="color:var(--deep)">Prototype Link</a></p>
"""
    # Overview
    body = ""
    for name, cap in [("gotgt-post-activity", "3-Step post of an activity that was already part of your day"),
                      ("gotgt-friends-notified", "Friends in that activity circle get notified &amp; can choose to ignore or join in"),
                      ("gotgt-active-events", "See all the active events before the time runs out &amp; choose if you want to join")]:
        body += vid(name, "545/631", cap.replace("&amp;", "&")) + p(cap, "m-p m-cap")
    out += sec("Overview", 'A social app that makes it so easy to see your friends that it is a <span class="mark">net positive</span> to initiate, even when you’re busy', body)
    # Context
    steps = ["Generate a product idea &amp; compete with ~20 other students", "Winning 4 ideas move to 2nd round with a team of 4",
             "Team must prove the business &amp; user value through a MVP test", "Final deliverable is a presentation pitch to investors"]
    out += sec("Context &amp; Constraints", "Semester-long competition in a digital service innovation class",
               '<ol class="m-steps">' + "".join(f"<li>{s}</li>" for s in steps) + "</ol>")
    # Concept
    items = ["Real &amp; relevant problem that I believe in", "Really busy &amp; stressed during this time",
             "Hanging out with friends makes it better", "Coordinating schedules is stressful", "Busy &amp; stressed &amp; lonely"]
    out += sec("Concept", "How do I create a winning product?",
               f'<div class="m-spiral"><img src="{S}bigarrow.svg" alt="" class="m-spiral-svg"><div>'
               + "".join(p(t, "m-p m-li") for t in items)
               + p("A product that would make it so easy to hang out that it is a net positive even when busy", "m-p m-li ink") + "</div></div>")
    # 1st pitch
    out += sec("1st Pitch", "Introducing... Shared Solitude",
               img(C + "pitch-slides.png", "Shared Solitude pitch slides", ' style="aspect-ratio:893/789"')
               + f'<p class="m-vote">Class vote... <span class="mark">Tied for 1st!</span>{face("smile")}</p>')
    # MVP
    out += sec("MVP Testing", "Validating the value of reducing barriers to shared routine activities",
               p("Mapping out user journey", "m-p m-sub") + img(C + "mvp-journey.png", "User journey map", ' style="aspect-ratio:426/327"')
               + p("Finding key stakeholders", "m-p m-sub") + img(C + "mvp-stakeholders.png", "Stakeholder map", ' style="aspect-ratio:430/327"')
               + p("Selected quote from over 20 interviews", "m-p m-sub")
               + '<blockquote class="m-quote">"I actually would want to <span class="mark">add more socialization</span> into my routine, but I don\'t because I don\'t know if it will end up being <span class="mark">a waste of time</span>"</blockquote>'
               + p("CMU student, 20 y/o")
               + p("Minimum Viable Product", "m-p m-sub") + img(C + "mvp.png", "Friends meeting up during MVP testing", ' style="aspect-ratio:431/491"')
               + p("Testing the MVP to see if friends who have busy schedules would actually respond to a spontaneous system of doing mundane activities together")
               + p("Found that almost every single 1-1 invitation of ~20 happened!", "m-p ink"))
    # 2nd pitch
    out += sec("2nd Pitch", "We gathered our findings &amp; pitched GoTgt to investors",
               img(C + "pitch-day.png", "The team pitching GoTgt", ' style="aspect-ratio:545/440"')
               + p("Day of the presentation, we pitched with a prepared poster, slide deck, &amp; matching fits...")
               + f'<p class="m-p ink">And we did not win, but tied for second place! {face("frown", " style=\"vertical-align:-6px\"")}</p>')
    # still hungry
    out += ('<div class="m-rule m-rule-sec"></div>\n<div class="m-hungry">'
            '<p>The course was now over, but <span class="mark">I was still hungry...</span></p>'
            '<p>We never got to work on the design aspect, <em><span class="mark">what if I designed it on my own?</span></em></p></div>\n')
    # Solo
    out += sec("Solo Designing", "Started with the framework we already had",
               img(C + "solo-wordmark.png", "Early GoTgt home screen next to the GoTgt wordmark", ' style="aspect-ratio:889/505"')
               + p("I took notice something in the way the words fit together in GoTgt &amp; an idea was born...")
               + f'<div class="m-curl"><img src="{S}curl1.svg" alt=""></div>'
               + f'<img class="m-ill" src="{S}wordmark-guys.svg" alt="The GoTgt wordmark with the o’s turned into lil guys" style="aspect-ratio:607/603">')
    # Character
    out += sec("Character Design", "“lil guys” as the mascot for a spontaneous social app",
               p("The circles from GoTgt inspired life into the “lil guys”")
               + f'<img class="m-ill" src="{S}guy.svg" alt="A yellow lil guy walking" style="aspect-ratio:890/518">'
               + p("The lil guys could hold hands &amp; GoTgt!")
               + f'<img class="m-ill" src="{S}guys.svg" alt="Two lil guys holding hands" style="aspect-ratio:891/361">')
    # Design system
    out += sec("Design System", "Creating the brand around the character",
               p("I had to go with a playful typeface to match the concept of the app &amp; the energy of the lil guys")
               + p("Not to mention also a geometric typeface that would serve the circles nicely...")
               + '<p class="m-p m-right">Nexa Book</p><p class="m-nexa">GoTgt</p>'
               + p("And the rest of the design system followed pretty easily once the wordmark and mascot were down")
               + '<div class="m-ramp">' + "".join(f'<span>{l}</span><span style="{css};color:#252525">{s}</span>' for l, s, css in ramp) + "</div>"
               + '<div class="m-swatches">' + "".join(
                   f'<div><i style="background:{c};{"box-shadow:inset 0 0 0 1px #ECECEA" if b else ""}"></i><span>{n} {c}</span></div>' for n, c, b in colors) + "</div>"
               + p("Which made it really exciting to jump into establishing components")
               + img(C + "components-1.png", "GoTgt nav bar states", ' style="aspect-ratio:429/481"')
               + img(C + "components-2.png", "GoTgt toggle", ' style="aspect-ratio:429/193"')
               + p("Anytime there is a circle, there is opportunity to make it a lil guy with 2 simple dots"))
    # Motion
    out += sec("Motion &amp; Animation", "Bringing life to the lil guys &amp; interactions through motion",
               p("From the birth of the lil guys, I had always seen them very clearly walking")
               + p("It could be used for loading states, splash screen, wordmark motion... endless possibilities!")
               + p("Drawing out individual frames to show to Claude")
               + f'<img class="m-ill" src="{S}walk-frames.svg" alt="Three hand-drawn walk cycle frames" style="aspect-ratio:902/326">'
               + f'<p class="m-p">Which initially did not work super well... {face("frown", " style=\"vertical-align:-8px\"")}</p>'
               + f'<img class="m-ill" src="{G}walk_preview.gif" alt="An early, wobbly walk cycle" loading="lazy" style="aspect-ratio:682/606;object-fit:cover">'
               + f'<p class="m-p">But then I iterated through it, working between Claude &amp; Figma Motion! {face("smile", " style=\"vertical-align:-4px\"")}</p>'
               + f'<img class="m-ill" src="{G}walk-cycle.gif" alt="The finished lil guy walk cycle" loading="lazy" style="aspect-ratio:660/638;object-fit:cover">'
               + p("This also meant I could bring the workmark motion vision to life!")
               + vid("gotgt-wordmark-motion", "891/1039", "GoTgt wordmark motion"))
    # Reflections
    paras = ["GoTgt was created for the purpose of winning, yet that ended up catapulting a journey in product thinking &amp; design that I have never been so invested in. Finding a real problem space that I genuinely cared about in the beginning made every step of this process not just more intentional, but easy.",
             "To be very honest, a lot of the courses at CMU within HCI are not very design focused, and I was once again disappointed when there was no opportunity to learn how to “properly” do the product designing.",
             "However, this project showed me that I am more than capable of applying my skills across disciplines as long as I actually sit down to do it. The entire design section of the project was done on my own, and it was probably the first time I felt actually connected to a product design work.",
             "And I am not yet done.",
             "From here, I have been thinking about taking it another step further to fully develop this app with the help of a engineering friend. I’m all about asking the “whys” and “why nots” and if this is genuinely a product that I believe in, which it has since the beginning, why shouldn’t it be a real solution that touches people’s lives?"]
    out += sec("Reflections", "Just how far can someone take an idea they’re passionate about?", "".join(p(t) for t in paras))
    return out + FOOT
