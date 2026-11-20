"""Shared page chrome. Run build.py to regenerate the static HTML in ../site."""

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;1,8..60,300;1,8..60,400&family=Open+Sans:wght@400;600&display=swap">\n'
    '<link rel="stylesheet" href="https://use.typekit.net/pas1cwi.css">'
)

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Ccircle cx='16' cy='16' r='14' fill='%23DDF396'/%3E%3C/svg%3E")


def head(title, desc, height):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="/assets/css/site.css">
<script>/* set zoom before first paint so nothing jumps */(function(){{var z=Math.min(1,innerWidth/1512);var r=document.documentElement.style;r.setProperty('--z',z);r.setProperty('--vhd',innerHeight/z+'px')}})();</script>
</head>
<body>
<div class="page" style="height:{height}px">
"""


def nav(active):
    items = [("Work", "/"), ("About", "/about/"), ("Play", "/play/"), ("Resume", "/resume/")]
    links = "".join(f'<a data-i="{i}" href="{h}"{" aria-current=\"page\"" if i == active else ""}>{t}</a>'
                    for i, (t, h) in enumerate(items))
    return f'<nav class="nav t-nav" data-active="{active}" aria-label="Main"><span class="dot" aria-hidden="true"></span>{links}</nav>\n'


UP_ARROW = ('<svg viewBox="0 0 30 42" fill="none" aria-hidden="true"><path d="M12.728 40C12.728 41.1046 13.6235 42 14.728 42C15.8326 42 16.728 41.1046 16.728 40L14.728 40L12.728 40ZM14.728 40L16.728 40L16.728 2L14.728 2L12.728 2L12.728 40L14.728 40ZM16.1422 0.585785C15.3612 -0.195263 14.0949 -0.195263 13.3138 0.585785L0.585892 13.3137C-0.195157 14.0948 -0.195157 15.3611 0.585892 16.1421C1.36694 16.9232 2.63327 16.9232 3.41432 16.1421L14.728 4.82843L26.0417 16.1421C26.8228 16.9232 28.0891 16.9232 28.8702 16.1421C29.6512 15.3611 29.6512 14.0948 28.8702 13.3137L16.1422 0.585785Z" fill="#DDF396"/></svg>')


FOOTER = """<footer class="t-nav site-foot" style="position:absolute;left:1001px;top:{top}px">
  <a href="mailto:erinhsu@andrew.cmu.edu" style="position:absolute;left:0;white-space:nowrap">erinhsu@andrew.cmu.edu</a>
  <a href="https://www.linkedin.com/in/erinhsuu" target="_blank" rel="noopener" style="position:absolute;left:231px">linkedin</a>
  <a href="https://www.instagram.com/ernhsu/" target="_blank" rel="noopener" style="position:absolute;left:346px">instagram</a>
</footer>
"""


def foot(height, to_top=True, raised=False):
    """Closes the page. The footer sits 52px above the page bottom, as on the Home frame (2766 of 2818)."""
    tt = (f'<button class="to-top{" raised" if raised else ""}" aria-label="Back to top">{UP_ARROW}</button>\n'
          if to_top else "")
    return FOOTER.format(top=height - 52) + f"""</div>
{tt}<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def media(src, w, h, x=None, y=None, kind="img", alt="", pos=None, extra="", style=""):
    """A clipped media box. kind: img | video."""
    st = f"width:{w}px;height:{h}px;"
    if x is not None:
        st += f"position:absolute;left:{x}px;top:{y}px;"
    st += style
    op = f' style="object-position:{pos}"' if pos else ""
    if kind == "video":
        poster = src.replace(".mp4", "-poster.jpg")
        inner = (f'<video src="{src}" poster="{poster}" autoplay muted loop playsinline preload="metadata"{op}'
                 f' aria-label="{alt}"></video>')
    else:
        inner = f'<img src="{src}" alt="{alt}" loading="lazy" decoding="async"{op}>'
    return f'<div class="media" {extra} style="{st}">{inner}</div>'
