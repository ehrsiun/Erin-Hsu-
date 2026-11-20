# erinhsu.me

Erin Hsu's portfolio. Plain HTML/CSS/JS with no build step, deployed on Vercel.

## Pages
- `index.html` (Work)
- `about/`, `play/`, `resume/`
- `work/gotgt/` (GoTgt case study)

Layouts are built 1:1 from the Figma frames (1512px wide) and scale down to fit smaller screens.

## Editing
- Text and layout: edit a page's `index.html`, or edit `tools/build.py` / `tools/casestudy.py` and run `python3 tools/build.py` to regenerate every page.
- Colors, type, spacing: `assets/css/site.css`
- Cursor, stamps, nav dot, back-to-top, contents scrollspy: `assets/js/site.js` (cursor size is `BALL`)

## Fonts
Tenso and Nexa come from Adobe Fonts (web project `pas1cwi`). Add the live domain to that web project's allowed domains or the fonts won't load.
