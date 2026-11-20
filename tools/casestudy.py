"""GoTgt case study — Figma frame 'MacBook Pro 14" - 2' (1512 x 19567)."""
from common import head, nav, foot, media

V = "/assets/video/"
I = "/assets/img/cs/"
S = "/assets/svg/"
G = "/assets/gif/"


def doodle(kind, x, y, w, h, svg=None):
    if kind in ("smile", "frown"):
        return f'<div class="doodle" data-face="{kind}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
    return f'<img class="doodle" src="{S}{svg}" alt="" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'


def hdr(label, statement, hl=None, w=891):
    bar = (f'<div class="hl" data-sweep style="left:{hl[0]}px;top:{hl[1]}px;width:{hl[2]}px;height:{hl[3]}px"></div>'
           if hl else "")
    return (f'<header><p class="t-label ink">{label}</p>'
            f'<div style="position:relative;margin-top:10px;width:{w}px">{bar}<h2 class="t-title ink over">{statement}</h2></div></header>')


def img(name, w, h, x=None, y=None, alt="", style="", border=False):
    st = "box-shadow:inset 0 0 0 1.6px #EAE6D8;" if border else ""
    m = media(I + name, w, h, x, y, alt=alt, style=style)
    if border:  # border sits above the image
        m = m.replace("</div>", f'<span style="position:absolute;inset:0;{st}"></span></div>', 1)
    return m


RULE = '<div class="rule" style="width:891px"></div>'

TOC = [("overview", "Overview", 0, 0), ("context", "Context &amp; Constraints", 40, 0), ("concept", "Concept", 80, 0),
       ("pitch-1", "1st Pitch", 120, 0), ("mvp", "MVP Testing", 160, 0), ("pitch-2", "2nd Pitch", 200, 0),
       ("solo", "Solo Designing", 240, 0), ("character", "Character design", 280, 20),
       ("system", "Design system", 320, 20), ("motion", "Motion &amp; Animation", 360, 20),
       ("reflections", "Reflections", 400, 0)]


def build():
    h = head("GoTgt — Erin Hsu", "Designing spontaneous connection within busy routines. A case study by Erin Hsu.", 19567)

    # ---------------- sticky sidebar: back arrow + contents
    toc = "".join(f'<a href="#{i}" class="t-nav" style="position:absolute;left:{ind}px;top:{y}px;white-space:nowrap">{t}</a>'
                  for i, t, y, ind in TOC)
    h += f"""
<aside style="position:absolute;left:0;top:0;width:280px;height:19567px">
  <div style="position:sticky;top:0;height:var(--vhd)">
    <a href="/" data-nav aria-label="Back to work" class="back" style="position:absolute;left:78px;top:140px;width:42px;height:29px"><img src="{S}back.svg" alt="" style="width:100%;height:100%"></a>
    <nav class="toc" aria-label="Contents" style="position:absolute;left:80px;top:250px;width:200px;height:420px">
      <span class="toc-dot" aria-hidden="true" style="position:absolute;left:-24px;top:0;width:10px;height:10px;border-radius:50%;background:var(--lime)"></span>
      {toc}
    </nav>
  </div>
</aside>
"""

    # ---------------- main column
    h += f"""
<main style="position:absolute;left:310px;top:155px;width:1009px">
  {media(V + "gotgt-wordmark-motion.mp4", 1009, 618, kind="video", alt="GoTgt wordmark animation")}
  <div data-top-after style="position:relative;margin-top:40px;height:85px">
    <div style="position:absolute;left:0;top:0;width:638px">
      <h1 class="t-title ink">GoTgt</h1>
      <p class="t-sub ink">Designing spontaneous connection within busy routines</p>
    </div>
    <div style="position:absolute;left:691px;top:0;width:200px">
      <p class="t-20 ink">Lead Designer</p>
      <p class="t-20l">Jan-May 2026</p>
      <a href="#" data-todo="prototype url" target="_blank" rel="noopener" class="t-20l link" style="display:block;margin-top:10px;color:var(--deep)">Prototype Link</a>
    </div>
  </div>
  <div style="margin-top:80px">{RULE}</div>

  <div style="margin-top:80px;display:flex;flex-direction:column;gap:80px">
"""
    # Overview
    rows = [("gotgt-post-activity.mp4", "3-Step post of an activity that was already part of your day", 574),
            ("gotgt-friends-notified.mp4", "Friends in that activity circle get notified &amp; can choose to ignore or join in", 575),
            ("gotgt-active-events.mp4", "See all the active events before the time runs out &amp; choose if you want to join", 575)]
    ov = "".join(f"""
      <div style="position:relative;height:631px">
        {media(V + v, 545, 631, kind="video", alt=c.replace("&amp;", "&"))}
        <p class="t-24-32" style="position:absolute;left:{x}px;top:30px;width:316px">{c}</p>
      </div>""" for v, c, x in rows)
    h += f"""
    <section id="overview">
      {hdr("Overview", "A social app that makes it so easy to see your friends that it is a net positive to initiate, even when you’re busy", (26, 66, 150, 22))}
      <div style="margin-top:60px;display:flex;flex-direction:column;gap:80px">{ov}
      </div>
    </section>
    {RULE}
"""
    # Context & Constraints
    steps = [("Generate a product idea &amp; compete with ~20 other students", 0),
             ("Winning 4 ideas move to 2nd round with a team of 4", 230),
             ("Team must prove the business &amp; user value through a MVP test", 460),
             ("Final deliverable is a presentation pitch to investors", 690)]
    st = "".join(f'<p class="t-24l" style="position:absolute;left:{x}px;top:78px;width:200px;color:#5B5B5B">{t}</p>' for t, x in steps)
    h += f"""
    <section id="context">
      {hdr("Context &amp; Constraints", "Semester-long competition in a digital service innovation class")}
      <div style="position:relative;margin-top:80px;height:198px">
        <img src="{S}steps.svg" alt="" style="position:absolute;left:129px;top:-4px;width:647px;height:63px">
        {st}
      </div>
    </section>
    {RULE}
"""
    # Concept
    items = ["Real &amp; relevant problem that I believe in", "Really busy &amp; stressed during this time",
             "Hanging out with friends makes it better", "Coordinating schedules is stressful", "Busy &amp; stressed &amp; lonely"]
    li = "".join(f'<li class="t-24l" style="position:absolute;left:80px;top:{i*50}px;white-space:nowrap">{t}</li>' for i, t in enumerate(items))
    h += f"""
    <section id="concept" style="position:relative">
      {hdr("Concept", "How do I create a winning product? ")}
      <ul style="list-style:none;position:relative;margin-top:60px;width:778px;height:310px">
        {li}
        <li class="t-24 ink" style="position:absolute;left:80px;top:250px;width:698px">A product that would make it so easy to hang out that it is a net positive even when busy</li>
      </ul>
      {doodle(None, 528, 58, 87, 110, "curl2.svg")}
      {doodle(None, 118, 215, 56, 264, "bigarrow.svg")}
      {doodle("frown", 484, 396, 44, 37)}
      {doodle("smile", 1173 - 310, 4473 - 3987, 43, 28)}
    </section>
    {RULE}
"""
    # 1st Pitch
    grid = [("pitch-1.jpg", 0, 0), ("pitch-2.jpg", 461.5, 0), ("pitch-3.jpg", 0, 272.7),
            ("pitch-4.jpg", 461.5, 272.7), ("pitch-5.jpg", 0, 545.4), ("pitch-6.jpg", 461.5, 545.4)]
    gi = "".join(img(n, 431.5, 242.7, x, y, alt="Shared Solitude pitch slide", border=True) for n, x, y in grid)
    h += f"""
    <section id="pitch-1" style="position:relative">
      {hdr("1st Pitch", "Introducing... Shared Solitude")}
      <div style="position:relative;margin-top:60px;width:893px;height:788px">{gi}</div>
      <div style="position:relative;margin-top:80px;height:44px">
        <div class="hl" data-sweep style="left:466px;top:23px;width:161px;height:22px;border-radius:38.6px"></div>
        <p class="over ink" style="font-family:var(--serif);font-style:italic;font-weight:400;font-size:32px;line-height:44px">Class vote... Tied for 1st!</p>
      </div>
      {doodle("smile", 764, 724, 43, 28)}
    </section>
    {RULE}
"""
    # MVP Testing + Minimum Viable Product
    h += f"""
    <section id="mvp">
      {hdr("MVP Testing", "Validating the value of reducing barriers to shared routine activities")}
      <div style="margin-top:60px;display:flex;gap:30px">
        <div style="width:426px"><p class="t-24-32">Mapping out user journey </p><div style="margin-top:10px">{img("mvp-journey.jpg", 426, 327, alt="User journey map")}</div></div>
        <div style="width:430px"><p class="t-24-32">Finding key stakeholders</p><div style="margin-top:10px">{img("mvp-stakeholders.jpg", 430, 327, alt="Stakeholder map")}</div></div>
      </div>
      <div style="margin:100px 0 0 116px;width:655px">
        <p class="t-24-32">Selected quote from over 20 interviews</p>
        <div style="position:relative;margin-top:10px;width:654px">
          <div class="hl" data-sweep style="left:424.9px;top:28px;width:163.3px;height:27px"></div>
          <div class="hl" data-sweep style="left:10.5px;top:83px;width:200.5px;height:27px"></div>
          <div class="hl" data-sweep style="left:222.3px;top:193px;width:212.9px;height:27px"></div>
          <p class="over" style="font-family:var(--serif);font-style:italic;font-weight:400;font-size:40px;line-height:55px;color:#000">"I actually would want to add more socialization into my routine, but I don't because I don't know if it will end up being a waste of time"</p>
        </div>
        <p class="t-24l" style="margin-top:40px">CMU student, 20 y/o</p>
      </div>
      <div style="margin-top:80px">
        <p class="t-24-32">Minimum Viable Product</p>
        <div style="position:relative;margin-top:10px;width:892px;height:490px">
          {img("mvp-1.jpg", 430.5, 233.5, 0, 0, alt="MVP test messages")}
          {img("mvp-2.jpg", 200.1, 233.5, 0, 256.9, alt="MVP test")}
          {img("mvp-3.jpg", 199.3, 233.5, 231.2, 256.9, alt="MVP test")}
          <div style="position:absolute;left:460.5px;top:0;width:431px;height:490px">
            <p class="t-24l-32">Testing the MVP to see if friends who have busy schedules would actually respond to a spontaneous system of doing mundane activities together</p>
            <p class="t-24-32 ink" style="position:absolute;left:0;top:426px">Found that almost every single 1-1 invitation of ~20 happened!</p>
          </div>
        </div>
      </div>
    </section>
    {RULE}
"""
    # 2nd Pitch
    h += f"""
    <section id="pitch-2" style="position:relative">
      {hdr("2nd Pitch", "We gathered our findings &amp; pitched GoTgt to investors")}
      <div style="position:relative;margin-top:60px;height:440px">
        {img("pitch-day.jpg", 545, 440, 0, 0, alt="The team pitching GoTgt")}
        <div style="position:absolute;left:575px;top:0;width:316px;height:440px">
          <p class="t-24l-32">Day of the presentation, we pitched with a prepared poster, slide deck, &amp; matching fits...</p>
          <p class="t-24-32 ink" style="position:absolute;left:0;top:376px">And we did not win, but tied for second place!</p>
        </div>
      </div>
      {doodle("frown", 799, 520, 44, 37)}
    </section>
    {RULE}
"""
    # Still hungry
    big = "font-family:var(--serif);font-weight:400;font-size:36px;line-height:49px;color:var(--ink)"
    h += f"""
    <div style="position:relative;height:245px">
      <div style="position:absolute;left:0;top:0;width:430px">
        <div class="hl" data-sweep style="left:69px;top:74px;width:306px;height:24px"></div>
        <p class="over" style="{big}">The course was now over, but I was still hungry...</p>
      </div>
      <div style="position:absolute;left:460px;top:98px;width:431px">
        <div class="hl" data-sweep style="left:25px;top:123px;width:338px;height:24px"></div>
        <p class="over" style="{big}">We never got to work on the design aspect, <em>what if I designed it on my own?</em></p>
      </div>
    </div>
    {RULE}
"""
    # Solo Designing
    h += f"""
    <section id="solo" style="position:relative">
      {hdr("Solo Designing", "Started with the framework we already had")}
      <div style="position:relative;margin-top:60px;height:684px">
        <img src="{I}solo-wordmark.png" alt="Early GoTgt home screen next to the GoTgt wordmark" style="position:absolute;left:-2px;top:0;width:889px;height:505px">
        <p class="t-24l-32" style="position:absolute;left:0;top:620px;width:545px">I took notice something in the way the words fit together in GoTgt &amp; an idea was born...</p>
      </div>
      <img src="{S}wordmark-guys.svg" alt="The GoTgt wordmark with the o’s turned into lil guys" style="display:block;margin:60px 0 0 140px;width:607px;height:603px">
      {doodle(None, 114, 1180, 103, 130, "curl1.svg")}
    </section>
    {RULE}

    <section id="character">
      {hdr("Character Design", "“lil guys” as the mascot for a spontaneous social app")}
      <p class="t-24l-32" style="margin-top:60px;width:548px">The circles from GoTgt inspired life into the “lil guys”</p>
      <img src="{S}guy.svg" alt="A yellow lil guy walking" style="display:block;margin-top:80px;width:890px;height:518px">
      <p class="t-24l-32" style="margin-top:150px;width:429px">The lil guys could hold hands &amp; GoTgt!</p>
      <img src="{S}guys.svg" alt="Two lil guys holding hands" style="display:block;margin-top:80px;width:891px;height:361px">
    </section>
    {RULE}
"""
    # Design system
    type_rows = [
        (0, 48, "Display XL", "ramen?", "font-family:nexa,sans-serif;font-weight:400;font-size:72.6px;line-height:72.6px", 0),
        (97.2, 29, "Display L", "ready to Tgt?", "font-family:nexa,sans-serif;font-weight:400;font-size:48.4px;line-height:52.4px", 0),
        (184.2, 14, "Title", "Costco run", "font-family:nexa,sans-serif;font-weight:400;font-size:30.25px;line-height:34.3px", 0),
        (243.4, 8, "Heading", "out right now", "font-family:nexa,sans-serif;font-weight:400;font-size:22.18px;line-height:28.2px", 0),
        (296.6, 6, "Body L", "She's going either way.", "font-family:'Open Sans',sans-serif;font-size:17.14px;line-height:26.2px", 0),
        (347.8, 3, "Body", "Tsukiya, 6 min walk", "font-family:'Open Sans',sans-serif;font-size:15.13px;line-height:22.2px", 0),
        (394.9, 3, "Body strong", "14 min", "font-family:'Open Sans',sans-serif;font-weight:600;font-size:15.13px;line-height:22.2px", 0),
        (442.1, 0, "Caption", "posted 4 min ago", "font-family:'Open Sans',sans-serif;font-size:13.1px;line-height:18.2px", 0),
        (485.3, 0, "Label", "out right now", "font-family:nexa,sans-serif;font-weight:700;font-size:12.1px;line-height:16.1px", 2),
    ]
    lab = "font-family:'Open Sans',sans-serif;font-size:13.1px;line-height:18.2px;color:#6E6E6E"
    tr = "".join(f'<p style="position:absolute;left:0;top:{t+lo}px;{lab}">{l}</p>'
                 f'<p style="position:absolute;left:113.9px;top:{t+so}px;white-space:nowrap;color:#252525;{css}">{s}</p>'
                 for t, lo, l, s, css, so in type_rows)
    sw = [("ink", "#252525", 0, 0, False), ("muted", "#6E6E6E", 148.4, 0, False), ("line", "#ECECEA", 307.2, 0, True),
          ("mist", "#F7F7F5", 0, 185.2, True), ("yellow", "#FFD95C", 148.4, 185.2, False), ("blue", "#83C7FF", 307.2, 185.2, False),
          ("pink", "#FF83E6", 0, 370.3, False), ("green", "#43F697", 148.4, 370.3, False)]
    cl = "font-family:'Open Sans',sans-serif;font-size:16.63px;line-height:23px;color:#6E6E6E;white-space:nowrap"
    swh = "".join(f'<div style="position:absolute;left:{x}px;top:{y}px">'
                  f'<div style="width:112.55px;height:112.55px;border-radius:50%;background:{c};{"box-shadow:inset 0 0 0 1.28px #ECECEA" if b else ""}"></div>'
                  f'<p style="margin-top:12.8px;{cl}">{n} {c}</p></div>' for n, c, x, y, b in sw)
    h += f"""
    <section id="system">
      {hdr("Design System", "Creating the brand around the character")}
      <p class="t-24l-32" style="margin-top:60px;width:544px">I had to go with a playful typeface to match the concept of the app &amp; the energy of the lil guys</p>
      <p class="t-24l-32" style="margin-top:40px;width:544px">Not to mention also a geometric typeface that would serve the circles nicely...</p>
      <div style="position:relative;margin-top:40px;width:890px;height:555px">
        <p class="t-24l-32" style="position:absolute;left:691px;top:0">Nexa Book</p>
        <p style="position:absolute;left:0;top:32px;font-family:nexa,sans-serif;font-weight:400;font-size:328.15px;line-height:135%;color:var(--ink);white-space:nowrap">GoTgt</p>
      </div>
      <p class="t-24l-32" style="margin-top:60px;width:545px">And the rest of the design system followed pretty easily once the wordmark and mascot were down</p>
      <div style="position:relative;margin-top:100px;width:880px;height:520px">
        <div style="position:absolute;left:0;top:0;width:430px;height:504px">{tr}</div>
        <div style="position:absolute;left:460px;top:0;width:420px;height:520px">{swh}</div>
      </div>
      <p class="t-24l-32" style="margin-top:120px;width:545px">Which made it really exciting to jump into establishing components</p>
      <div style="position:relative;margin-top:60px;width:888px;height:481px">
        {img("components-1.png", 429, 481, 0, 0, alt="GoTgt components")}
        {img("components-2.png", 429, 193, 459, 0, alt="GoTgt components")}
        <p class="t-24l-32" style="position:absolute;left:459px;top:359px;width:429px">Anytime there is a circle, there is opportunity to make it a lil guy with 2 simple dots</p>
      </div>
    </section>
    {RULE}
"""
    # Motion & Animation
    h += f"""
    <section id="motion" style="position:relative">
      {hdr("Motion &amp; Animation", "Bringing life to the lil guys &amp; interactions through motion")}
      <p class="t-24l-32" style="margin-top:60px;width:545px">From the birth of the lil guys, I had always seen them very clearly walking</p>
      <p class="t-24l-32" style="margin-top:40px;width:545px">It could be used for loading states, splash screen, wordmark motion... endless possibilities!</p>
      <p class="t-24l" style="margin-top:40px;width:545px">Drawing out individual frames to show to Claude</p>
      <div style="position:relative;margin-top:40px;height:406px">
        <img src="{S}walk-frames.svg" alt="Three hand-drawn walk cycle frames" style="position:absolute;left:-5px;top:40px;width:902px;height:326px">
      </div>
      <p class="t-24l" style="margin-top:40px;width:545px">Which initially did not work super well...</p>
      <div style="position:relative;margin-top:40px;height:646px">
        <img src="/assets/gif/walk_preview.gif" alt="An early, wobbly walk cycle" loading="lazy" style="position:absolute;left:164px;top:0;width:682px;height:606px;object-fit:cover">
      </div>
      <p class="t-24l" style="margin-top:40px;width:545px">But then I iterated through it, working between Claude &amp; Figma Motion!</p>
      <div style="position:relative;margin-top:40px;height:678px">
        <img src="/assets/gif/walk-cycle.gif" alt="The finished lil guy walk cycle" loading="lazy" style="position:absolute;left:174.3px;top:0;width:660.3px;height:638px;object-fit:cover">
      </div>
      <p class="t-24l" style="margin-top:40px;width:545px">This also meant I could bring the workmark motion vision to life!</p>
      <div class="media" style="position:relative;margin-top:60px;width:1009px;height:1039px">
        <video src="{V}gotgt-wordmark-motion.mp4" poster="{V}gotgt-wordmark-motion-poster.jpg" autoplay muted loop playsinline preload="metadata" aria-label="GoTgt wordmark motion" style="position:absolute;left:-418px;top:0;width:1728px;height:1038px;max-width:none;object-fit:cover"></video>
      </div>
      {doodle("frown", 940, 674, 44, 37)}
      {doodle("smile", 919, 1593, 43, 28)}
    </section>
    {RULE}

    <section id="reflections">
      {hdr("Reflections", "Just how far can someone take an idea they’re passionate about?")}
      <div class="t-24l" style="margin-top:10px;width:545px;display:flex;flex-direction:column;gap:30px">
        <p>GoTgt was created for the purpose of winning, yet that ended up catapulting a journey in product thinking &amp; design that I have never been so invested in. Finding a real problem space that I genuinely cared about in the beginning made every step of this process not just more intentional, but easy.</p>
        <p>To be very honest, a lot of the courses at CMU within HCI are not very design focused, and I was once again disappointed when there was no opportunity to learn how to “properly” do the product designing.</p>
        <p>However, this project showed me that I am more than capable of applying my skills across disciplines as long as I actually sit down to do it. The entire design section of the project was done on my own, and it was probably the first time I felt actually connected to a product design work.</p>
        <p>And I am not yet done.</p>
        <p>From here, I have been thinking about taking it another step further to fully develop this app with the help of a engineering friend. I’m all about asking the “whys” and “why nots” and if this is genuinely a product that I believe in, which it has since the beginning, why shouldn’t it be a real solution that touches people’s lives?</p>
      </div>
    </section>
  </div>
</main>
"""
    h += foot(19567)
    return h
