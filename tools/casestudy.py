"""GoTgt case study — Figma frame 'MacBook Pro 14" - 2' (1512 x 19567).

Every element is placed at its exact Figma page coordinate, so text, images
and doodles always line up the way they do in the design."""
from common import head, foot

V = "/assets/video/"
I = "/assets/img/cs/"
S = "/assets/svg/"
G = "/assets/gif/"

PAGE_H = 19567


def at(x, y, w=None, h=None, extra=""):
    st = f"position:absolute;left:{x}px;top:{y}px;"
    if w is not None:
        st += f"width:{w}px;"
    if h is not None:
        st += f"height:{h}px;"
    return st + extra


def P(x, y, w, cls, html, tag="p", extra=""):
    return f'<{tag} class="{cls}" style="{at(x, y, w, extra=extra)}">{html}</{tag}>\n'


def HL(x, y, w, h, r=None):
    rr = f"border-radius:{r}px;" if r else ""
    return f'<div class="hl" data-sweep style="{at(x, y, w, h, rr)}"></div>\n'


def IMG(src, x, y, w, h, alt="", border=False, fit="cover"):
    b = '<span style="position:absolute;inset:0;box-shadow:inset 0 0 0 1.6px #EAE6D8"></span>' if border else ""
    return (f'<div class="media" style="{at(x, y, w, h)}"><img src="{src}" alt="{alt}" loading="lazy" decoding="async" '
            f'style="object-fit:{fit}">{b}</div>\n')


def VID(name, x, y, w, h, alt, inner=None):
    style = ' style="' + inner + '"' if inner else ""
    return (f'<div class="media" style="{at(x, y, w, h)}"><video src="{V}{name}.mp4" poster="{V}{name}-poster.jpg" '
            f'autoplay muted loop playsinline preload="metadata" aria-label="{alt}"{style}></video></div>\n')


def SVG(name, x, y, w, h, alt=""):
    return f'<img src="{S}{name}" alt="{alt}" style="{at(x, y, w, h)}">\n'


def FACE(kind, x, y, w, h):
    # case-study doodles are the light lime (#DDF396) in Figma
    return f'<div class="doodle" data-face="{kind}" data-color="#DDF396" style="{at(x, y, w, h)}"></div>\n'


def DOODLE(name, x, y, w, h):
    return f'<img class="doodle" src="{S}{name}" alt="" style="{at(x, y, w, h)}">\n'


def RULE(y):
    return f'<div class="rule" style="{at(310, y, 891)}"></div>\n'


def SECTION(id_, y, label, statement, hl=None):
    out = f'<span id="{id_}" class="anchor" style="{at(310, y)}"></span>\n'
    out += P(310, y, 1009, "t-label ink", label)
    if hl:
        out += HL(*hl)
    out += P(310, y + 43, 891, "t-title ink over", statement, tag="h2")
    return out


TOC = [("overview", "Overview", 0, 0), ("context", "Context &amp; Constraints", 40, 0), ("concept", "Concept", 80, 0),
       ("pitch-1", "1st Pitch", 120, 0), ("mvp", "MVP Testing", 160, 0), ("pitch-2", "2nd Pitch", 200, 0),
       ("solo", "Solo Designing", 240, 0), ("character", "Character design", 280, 20),
       ("system", "Design system", 320, 20), ("motion", "Motion &amp; Animation", 360, 20),
       ("reflections", "Reflections", 400, 0)]


def build():
    h = head("GoTgt — Erin Hsu", "Designing spontaneous connection within busy routines. A case study by Erin Hsu.", PAGE_H)

    # ---------------- fixed sidebar: back arrow + contents (no top nav on case studies)
    toc = "".join(f'<a href="#{i}" class="t-nav" style="position:absolute;left:{ind}px;top:{y}px;white-space:nowrap">{t}</a>'
                  for i, t, y, ind in TOC)
    h += f"""<aside style="position:absolute;left:0;top:0;width:280px;height:{PAGE_H}px">
  <div style="position:sticky;top:0;height:var(--vhd)">
    <a href="/" data-nav aria-label="Back to work" class="back" style="position:absolute;left:78px;top:140px;width:42px;height:29px"><img src="{S}back.svg" alt="" style="width:100%;height:100%"></a>
    <nav class="toc" aria-label="Contents" style="position:absolute;left:80px;top:250px;width:200px;height:420px">
      <span class="toc-dot" aria-hidden="true" style="position:absolute;left:-24px;top:0;width:10px;height:10px;border-radius:50%;background:var(--lime)"></span>
      {toc}
    </nav>
  </div>
</aside>
"""
    m = ""
    # ---------------- intro
    m += VID("gotgt-wordmark-motion", 310, 155, 1009, 618, "GoTgt wordmark animation")
    m += P(310, 813, 638, "t-title ink", "GoTgt", tag="h1")
    m += P(310, 857, 638, "t-sub ink", "Designing spontaneous connection within busy routines")
    m += P(1001, 813, 200, "t-20 ink", "Lead Designer")
    m += P(1001, 838, 200, "t-20l", "Jan-May 2026")
    m += (f'<a href="https://go-tgt.vercel.app" target="_blank" rel="noopener" class="t-20l link" '
          f'style="{at(1001, 873)}color:var(--deep);white-space:nowrap">Prototype Link</a>\n')
    m += f'<div data-top-after style="{at(310, 813, 891, 85)}pointer-events:none"></div>\n'
    m += RULE(978)

    # ---------------- Overview
    m += SECTION("overview", 1058, "Overview",
                 "A social app that makes it so easy to see your friends that it is a net positive to initiate, even when you’re busy",
                 hl=(336, 1167, 150, 22))
    for name, cap, y, cx in [("gotgt-post-activity", "3-Step post of an activity that was already part of your day", 1249, 884),
                             ("gotgt-friends-notified", "Friends in that activity circle get notified &amp; can choose to ignore or join in", 1960, 885),
                             ("gotgt-active-events", "See all the active events before the time runs out &amp; choose if you want to join", 2671, 885)]:
        m += VID(name, 310, y, 545, 631, cap.replace("&amp;", "&"))
        m += P(cx, y + 30, 316, "t-24-32", cap)
    m += RULE(3382)

    # ---------------- Context & Constraints
    m += SECTION("context", 3462, "Context &amp; Constraints", "Semester-long competition in a digital service innovation class")
    m += SVG("steps.svg", 439, 3625, 647, 63)
    for x, t in [(310, "Generate a product idea &amp; compete with ~20 other students"),
                 (540, "Winning 4 ideas move to 2nd round with a team of 4"),
                 (770, "Team must prove the business &amp; user value through a MVP test"),
                 (1000, "Final deliverable is a presentation pitch to investors")]:
        m += P(x, 3707, 200, "t-24l", t, extra="color:#5B5B5B;")
    m += RULE(3907)

    # ---------------- Concept
    m += SECTION("concept", 3987, "Concept", "How do I create a winning product? ")
    m += DOODLE("curl2.svg", 838, 4045, 87, 110)
    for i, t in enumerate(["Real &amp; relevant problem that I believe in", "Really busy &amp; stressed during this time",
                           "Hanging out with friends makes it better", "Coordinating schedules is stressful",
                           "Busy &amp; stressed &amp; lonely"]):
        m += P(390, 4134 + i * 50, 698, "t-24l", t, extra="white-space:nowrap;")
    m += P(390, 4384, 698, "t-24 ink", "A product that would make it so easy to hang out that it is a net positive even when busy")
    m += DOODLE("bigarrow.svg", 428, 4202, 56, 264)
    m += FACE("frown", 794, 4383, 44, 37)
    m += FACE("smile", 1173, 4473, 43, 28)
    m += RULE(4524)

    # ---------------- 1st Pitch
    m += SECTION("pitch-1", 4604, "1st Pitch", "Introducing... Shared Solitude")
    m += IMG(I + "pitch-slides.png", 310, 4751, 893, 789, alt="Shared Solitude pitch slides: research, problem, solution, storyboard, MVP, existing services")
    m += HL(776, 5642, 161, 22, r=38.6)
    m += P(310, 5619, 893, "over ink", "Class vote... Tied for 1st!",
           extra="font-family:var(--serif);font-style:italic;font-weight:400;font-size:32px;line-height:44px;text-align:center;")
    m += FACE("smile", 1074, 5328, 43, 28)
    m += RULE(5743)

    # ---------------- MVP Testing
    m += SECTION("mvp", 5823, "MVP Testing", "Validating the value of reducing barriers to shared routine activities")
    m += P(310, 6014, 426, "t-24-32", "Mapping out user journey ")
    m += IMG(I + "mvp-journey.png", 310, 6056, 426, 327, alt="User journey map")
    m += P(766, 6014, 430, "t-24-32", "Finding key stakeholders")
    m += IMG(I + "mvp-stakeholders.png", 766, 6056, 430, 327, alt="Stakeholder map")
    m += P(426, 6483, 655, "t-24-32", "Selected quote from over 20 interviews")
    m += HL(850, 6553, 163.3, 27) + HL(436.5, 6608, 200.5, 27) + HL(648.3, 6718, 212.9, 27)
    m += P(426, 6525, 654, "over",
           "\"I actually would want to add more socialization into my routine, but I don't because I don't know if it will end up being a waste of time\"",
           extra="font-family:var(--serif);font-style:italic;font-weight:400;font-size:40px;line-height:55px;color:#000;")
    m += P(426, 6785, 655, "t-24l", "CMU student, 20 y/o")
    m += P(310, 6895, 1009, "t-24-32", "Minimum Viable Product")
    m += IMG(I + "mvp.png", 310, 6937, 431, 491, alt="Friends meeting up during MVP testing")
    m += P(771, 6938, 431, "t-24l-32", "Testing the MVP to see if friends who have busy schedules would actually respond to a spontaneous system of doing mundane activities together")
    m += P(771, 7364, 431, "t-24-32 ink", "Found that almost every single 1-1 invitation of ~20 happened!")
    m += RULE(7508)

    # ---------------- 2nd Pitch
    m += SECTION("pitch-2", 7588, "2nd Pitch", "We gathered our findings &amp; pitched GoTgt to investors")
    m += IMG(I + "pitch-day.png", 310, 7735, 545, 440, alt="The team pitching GoTgt")
    m += P(885, 7735, 316, "t-24l-32", "Day of the presentation, we pitched with a prepared poster, slide deck, &amp; matching fits...")
    m += P(885, 8111, 316, "t-24-32 ink", "And we did not win, but tied for second place!")
    m += FACE("frown", 1109, 8108, 44, 37)
    m += RULE(8255)

    # ---------------- still hungry
    big = "font-family:var(--serif);font-weight:400;font-size:36px;line-height:49px;color:var(--ink);"
    m += HL(379, 8409, 306, 24)
    m += P(310, 8335, 430, "over", "The course was now over, but I was still hungry...", extra=big)
    m += HL(795, 8556, 338, 24)
    m += P(770, 8433, 431, "over", "We never got to work on the design aspect, <em>what if I designed it on my own?</em>", extra=big)
    m += RULE(8660)

    # ---------------- Solo Designing
    m += SECTION("solo", 8740, "Solo Designing", "Started with the framework we already had")
    m += f'<img src="{I}solo-wordmark.png" alt="Early GoTgt home screen next to the GoTgt wordmark" style="{at(308, 8887, 889, 505)}">\n'
    m += P(310, 9507, 545, "t-24l-32", "I took notice something in the way the words fit together in GoTgt &amp; an idea was born...")
    m += SVG("wordmark-guys.svg", 450, 9631, 607, 603, "The GoTgt wordmark with the o’s turned into lil guys")
    m += DOODLE("curl1.svg", 424, 9920, 103, 130)
    m += RULE(10314)

    # ---------------- Character Design
    m += SECTION("character", 10394, "Character Design", "“lil guys” as the mascot for a spontaneous social app")
    m += P(310, 10541, 548, "t-24l-32", "The circles from GoTgt inspired life into the “lil guys”")
    m += SVG("guy.svg", 310, 10653, 890, 518, "A yellow lil guy walking")
    m += P(310, 11321, 429, "t-24l-32", "The lil guys could hold hands &amp; GoTgt!")
    m += SVG("guys.svg", 310, 11433, 891, 361, "Two lil guys holding hands")
    m += RULE(11954)

    # ---------------- Design System
    m += SECTION("system", 12034, "Design System", "Creating the brand around the character")
    m += P(310, 12181, 544, "t-24l-32", "I had to go with a playful typeface to match the concept of the app &amp; the energy of the lil guys")
    m += P(310, 12285, 544, "t-24l-32", "Not to mention also a geometric typeface that would serve the circles nicely...")
    m += P(1001, 12389, 199, "t-24l-32", "Nexa Book")
    m += P(310, 12421, 890, "", "GoTgt",
           extra="font-family:nexa,sans-serif;font-weight:400;font-size:328.15px;line-height:135%;color:var(--ink);white-space:nowrap;")
    m += P(310, 13004, 545, "t-24l-32", "And the rest of the design system followed pretty easily once the wordmark and mascot were down")
    lab = "font-family:'Open Sans',sans-serif;font-size:13.1px;line-height:18.2px;color:#6E6E6E;"
    for top, lo, l, s, css, so in [
            (0, 48, "Display XL", "ramen?", "font-family:nexa,sans-serif;font-weight:400;font-size:72.6px;line-height:72.6px", 0),
            (97.2, 29, "Display L", "ready to Tgt?", "font-family:nexa,sans-serif;font-weight:400;font-size:48.4px;line-height:52.4px", 0),
            (184.2, 14, "Title", "Costco run", "font-family:nexa,sans-serif;font-weight:400;font-size:30.25px;line-height:34.3px", 0),
            (243.4, 8, "Heading", "out right now", "font-family:nexa,sans-serif;font-weight:400;font-size:22.18px;line-height:28.2px", 0),
            (296.6, 6, "Body L", "She's going either way.", "font-family:'Open Sans',sans-serif;font-size:17.14px;line-height:26.2px", 0),
            (347.8, 3, "Body", "Tsukiya, 6 min walk", "font-family:'Open Sans',sans-serif;font-size:15.13px;line-height:22.2px", 0),
            (394.9, 3, "Body strong", "14 min", "font-family:'Open Sans',sans-serif;font-weight:600;font-size:15.13px;line-height:22.2px", 0),
            (442.1, 0, "Caption", "posted 4 min ago", "font-family:'Open Sans',sans-serif;font-size:13.1px;line-height:18.2px", 0),
            (485.3, 0, "Label", "out right now", "font-family:nexa,sans-serif;font-weight:700;font-size:12.1px;line-height:16.1px", 2)]:
        m += P(310, round(13168 + top + lo, 1), 111, "", l, extra=lab)
        m += P(423.9, round(13168 + top + so, 1), None, "", s, extra=f"white-space:nowrap;color:#252525;{css};")
    cl = "font-family:'Open Sans',sans-serif;font-size:16.63px;line-height:23px;color:#6E6E6E;white-space:nowrap;"
    for n, c, x, y, b in [("ink", "#252525", 0, 0, False), ("muted", "#6E6E6E", 148.4, 0, False), ("line", "#ECECEA", 307.2, 0, True),
                          ("mist", "#F7F7F5", 0, 185.2, True), ("yellow", "#FFD95C", 148.4, 185.2, False), ("blue", "#83C7FF", 307.2, 185.2, False),
                          ("pink", "#FF83E6", 0, 370.3, False), ("green", "#43F697", 148.4, 370.3, False)]:
        ring = "box-shadow:inset 0 0 0 1.28px #ECECEA;" if b else ""
        m += f'<div style="{at(round(770 + x, 1), round(13168 + y, 1), 112.55, 112.55)}border-radius:50%;background:{c};{ring}"></div>\n'
        m += P(round(770 + x, 1), round(13168 + y + 125.3, 1), None, "", f"{n} {c}", extra=cl)
    m += P(310, 13808, 545, "t-24l-32", "Which made it really exciting to jump into establishing components")
    m += IMG(I + "components-1.png", 310, 13932, 429, 481, alt="GoTgt components")
    m += IMG(I + "components-2.png", 769, 13932, 429, 193, alt="GoTgt components")
    m += P(769, 14291, 429, "t-24l-32", "Anytime there is a circle, there is opportunity to make it a lil guy with 2 simple dots")
    m += RULE(14493)

    # ---------------- Motion & Animation
    m += SECTION("motion", 14573, "Motion &amp; Animation", "Bringing life to the lil guys &amp; interactions through motion")
    m += P(310, 14720, 545, "t-24l-32", "From the birth of the lil guys, I had always seen them very clearly walking")
    m += P(310, 14824, 545, "t-24l-32", "It could be used for loading states, splash screen, wordmark motion... endless possibilities!")
    m += P(310, 14928, 545, "t-24l", "Drawing out individual frames to show to Claude")
    m += SVG("walk-frames.svg", 305, 15038, 902, 326, "Three hand-drawn walk cycle frames")
    m += P(310, 15443, 545, "t-24l", "Which initially did not work super well...")
    m += f'<img src="{G}walk_preview.gif" alt="An early, wobbly walk cycle" loading="lazy" style="{at(474, 15513, 682, 606)}object-fit:cover">\n'
    m += P(310, 16199, 545, "t-24l", "But then I iterated through it, working between Claude &amp; Figma Motion!")
    m += f'<img src="{G}walk-cycle.gif" alt="The finished lil guy walk cycle" loading="lazy" style="{at(484.3, 16299, 660.3, 638)}object-fit:cover">\n'
    m += P(310, 17017, 545, "t-24l", "This also meant I could bring the workmark motion vision to life!")
    m += VID("gotgt-wordmark-motion", 310, 17137, 1009, 1039, "GoTgt wordmark motion",
             inner="position:absolute;left:-418px;top:0;width:1728px;height:1038px;max-width:none")
    m += FACE("frown", 1250, 15247, 44, 37)
    m += FACE("smile", 1229, 16166, 43, 28)
    m += RULE(18297)

    # ---------------- Reflections
    m += SECTION("reflections", 18377, "Reflections", "Just how far can someone take an idea they’re passionate about?")
    paras = ["GoTgt was created for the purpose of winning, yet that ended up catapulting a journey in product thinking &amp; design that I have never been so invested in. Finding a real problem space that I genuinely cared about in the beginning made every step of this process not just more intentional, but easy.",
             "To be very honest, a lot of the courses at CMU within HCI are not very design focused, and I was once again disappointed when there was no opportunity to learn how to “properly” do the product designing.",
             "However, this project showed me that I am more than capable of applying my skills across disciplines as long as I actually sit down to do it. The entire design section of the project was done on my own, and it was probably the first time I felt actually connected to a product design work.",
             "And I am not yet done.",
             "From here, I have been thinking about taking it another step further to fully develop this app with the help of a engineering friend. I’m all about asking the “whys” and “why nots” and if this is genuinely a product that I believe in, which it has since the beginning, why shouldn’t it be a real solution that touches people’s lives?"]
    m += (f'<div class="t-24l" style="{at(310, 18518, 545)}display:flex;flex-direction:column;gap:30px">'
          + "".join(f"<p>{t}</p>" for t in paras) + "</div>\n")

    h += f'<main>\n{m}</main>\n'
    h += foot(PAGE_H)
    return h
