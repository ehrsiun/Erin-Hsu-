/* Erin Hsu — portfolio interactions.
   One spring for everything so all motion feels the same: quick, a little bouncy. */
(() => {
  "use strict";

  // ------------------------------------------------------------------ spring
  const SPRING = { k: 520, c: 32, m: 0.7 };
  class Spring {
    constructor(value, onUpdate, opts = {}) {
      Object.assign(this, SPRING, opts);
      this.x = value; this.v = 0; this.target = value; this.onUpdate = onUpdate; this.raf = 0;
      onUpdate(value);
    }
    set(target, { instant = false } = {}) {
      this.target = target;
      if (instant || reduceMotion) { this.x = target; this.v = 0; this.onUpdate(target); return; }
      if (!this.raf) { this.last = performance.now(); this.raf = requestAnimationFrame(this.step); }
    }
    step = (now) => {
      let dt = Math.min(0.064, (now - this.last) / 1000); this.last = now;
      // sub-step for stability
      const n = Math.ceil(dt / 0.008); dt /= n;
      for (let i = 0; i < n; i++) {
        const a = (-this.k * (this.x - this.target) - this.c * this.v) / this.m;
        this.v += a * dt; this.x += this.v * dt;
      }
      this.onUpdate(this.x);
      if (Math.abs(this.v) < 0.01 && Math.abs(this.x - this.target) < 0.01) {
        this.x = this.target; this.v = 0; this.onUpdate(this.x); this.raf = 0; return;
      }
      this.raf = requestAnimationFrame(this.step);
    };
  }
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const touch = matchMedia("(hover: none), (pointer: coarse)").matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // ------------------------------------------------------------------ fit 1512 design to screen
  const root = document.documentElement;
  let Z = 1;
  function fit() {
    Z = Math.min(1, innerWidth / 1512);
    root.style.setProperty("--z", Z);
    root.style.setProperty("--vhd", innerHeight / Z + "px");
  }
  fit();
  addEventListener("resize", fit);
  // phones get their own single-column layout (.m) instead of the zoomed desktop canvas
  const isM = () => innerWidth <= 700;
  const SZ = () => (isM() ? 1 : Z); // stamp size factor
  const shown = (el) => el && el.getClientRects().length > 0;
  const firstShown = (sel) => $$(sel).find(shown) || null;

  // ------------------------------------------------------------------ faces (Erin's drawings)
  const SMILE = `<svg viewBox="0 0 102 66" fill="none"><path d="M96.5007 22.7695C96.5007 22.7695 95.7299 33.7359 90.1612 40.4224C84.7389 46.9332 80.6816 51.3314 69.6481 55.5333C44.9541 64.9378 22.0538 53.5685 10.347 41.5574C7.39131 38.5249 5.0013 33.0851 5.0013 33.0851" stroke="#B1D43A" stroke-width="10" stroke-linecap="round"/><path d="M29.1873 7C29.2003 8.16576 29.626 11.2044 30.2946 12.0939C30.4596 12.3133 30.852 12.384 30.8915 12.2354C30.9311 12.0867 30.6693 11.6503 30.3327 10.7695C29.996 9.88881 29.5925 8.57705 29.0012 7.14257" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M53.0012 8.99939C53.0012 9.01689 53.0012 9.03438 53.0012 9.54371C53.0012 10.053 53.0012 11.0537 53.3091 11.6673" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  const FROWN = `<svg viewBox="0 0 102 86" fill="none"><path d="M96.5945 50.137C96.5945 50.137 91.0954 40.6178 83.1594 37.0483C75.4321 33.5726 69.8576 31.3976 58.0987 32.4564C31.781 34.8262 16.1802 55.0821 10.9219 71.0089C9.59425 75.0301 9.83013 80.9671 9.83013 80.9671" stroke="#B1D43A" stroke-width="10" stroke-linecap="round"/><path d="M8.18607 10C8.19909 11.1658 8.62478 14.2044 9.29342 15.0939C9.45834 15.3133 9.85075 15.384 9.89032 15.2354C9.92989 15.0867 9.66807 14.6503 9.33144 13.7695C8.99482 12.8888 8.59132 11.577 8 10.1426" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M32 7C32 7.0175 32 7.03499 32 7.54432C32 8.05364 32 9.05427 32.3078 9.66793" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  const FACE = { smile: { svg: SMILE, w: 39, h: 25 }, frown: { svg: FROWN, w: 40, h: 34 } };
  window.__faces = FACE;

  // fill any [data-face] placeholders (doodles, picker)
  $$("[data-face]").forEach((el) => {
    let svg = FACE[el.dataset.face].svg;
    if (el.dataset.color) svg = svg.split("#B1D43A").join(el.dataset.color);
    el.innerHTML = svg;
  });

  // ------------------------------------------------------------------ match Figma line breaks
  // Each multi-line text carries its Figma box height (data-fh). Browsers measure type a hair
  // differently from Figma, so a line can break one word early or late. Nudge the box width a few
  // px (never more than 24) until the text takes the same number of lines as in Figma.
  function fitLines() {
    $$("[data-fh]").forEach((el) => {
      if (!shown(el)) return;
      const target = +el.dataset.fh;
      const base = el.__w || (el.__w = parseFloat(getComputedStyle(el).width));
      if (!base) return;
      let d = 0;
      el.style.width = base + "px";
      const lh = parseFloat(getComputedStyle(el).lineHeight) || 30;
      while (el.offsetHeight > target + lh / 2 && d < 24) { d += 2; el.style.width = base + d + "px"; }
      while (el.offsetHeight < target - lh / 2 && d > -24) { d -= 2; el.style.width = base + d + "px"; }
    });
  }
  fitLines();
  document.fonts && document.fonts.ready.then(fitLines);
  addEventListener("load", fitLines);

  // ------------------------------------------------------------------ nav dot (slides from last page)
  const nav = $(".nav");
  if (nav) {
    const links = $$("a", nav);
    const dot = $(".dot", nav);
    const active = +nav.dataset.active;
    const cx = (i) => links[i].offsetLeft + links[i].offsetWidth / 2 - 5;
    let prev = active;
    try { const p = sessionStorage.getItem("navdot"); if (p !== null) prev = +p; } catch {}
    const s = new Spring(cx(prev), (x) => (dot.style.transform = `translateX(${x}px)`));
    requestAnimationFrame(() => s.set(cx(active)));
    try { sessionStorage.setItem("navdot", active); } catch {}
    // fonts can shift widths after load
    document.fonts && document.fonts.ready.then(() => s.set(cx(active)));
    links.forEach((a, i) => a.addEventListener("click", (e) => {
      if (mode !== "ball" || e.metaKey || e.ctrlKey) return;
      if (i === active) { e.preventDefault(); scrollTo({ top: 0, behavior: "smooth" }); return; }
      e.preventDefault();
      try { sessionStorage.setItem("navdot", i); } catch {}
      s.set(cx(i));
      setTimeout(() => (location.href = a.href), 260);
    }));
    // other in-site links remember the dot too
    $$("a[data-nav]").forEach((a) => a.addEventListener("click", () => {
      try { sessionStorage.setItem("navdot", active); } catch {}
    }));
  }

  // ------------------------------------------------------------------ Home: bottom nav slides in once the top nav is gone
  const reveal = $(".side-nav.reveal");
  if (reveal && nav) {
    const rs = new Spring(0, (p) => { reveal.style.opacity = Math.max(0, Math.min(1, p)); reveal.style.transform = `translateY(${(1 - p) * 24}px)`; });
    let on = false;
    const check = () => {
      const want = nav.getBoundingClientRect().bottom <= 0;
      if (want !== on) { on = want; reveal.classList.toggle("on", want); rs.set(want ? 1 : 0); }
    };
    addEventListener("scroll", check, { passive: true }); check();
  }

  // ------------------------------------------------------------------ highlight sweeps
  const sweep = (el) => {
    const s = new Spring(0, (x) => (el.style.transform = `scaleX(${Math.max(0, x)})`), { k: 300, c: 24, m: 0.9 });
    return () => s.set(1);
  };
  const io = "IntersectionObserver" in window ? new IntersectionObserver((ents) => {
    ents.forEach((en) => { if (en.isIntersecting) { en.target.__go && en.target.__go(); io.unobserve(en.target); } });
  }, { rootMargin: "0px 0px -15% 0px" }) : null;
  $$(".hl[data-sweep]").forEach((el, i) => {
    el.__go = sweep(el);
    if (el.dataset.sweep === "load") setTimeout(el.__go, 250 + i * 80);
    else if (io) io.observe(el); else el.__go();
  });

  // mobile highlights: a lime marker sweeps in under the words when they scroll into view
  $$(".mark").forEach((el) => {
    if (el.dataset.sweep === "load") setTimeout(() => el.classList.add("on"), 300);
    else if (io) { el.__go = () => el.classList.add("on"); io.observe(el); } else el.classList.add("on");
  });

  // ------------------------------------------------------------------ videos: play only when visible
  const vids = $$("video");
  vids.forEach((v) => { v.muted = true; v.playsInline = true; });
  if ("IntersectionObserver" in window) {
    const vio = new IntersectionObserver((ents) => ents.forEach((en) => {
      const v = en.target; en.isIntersecting ? v.play().catch(() => {}) : v.pause();
    }), { threshold: 0.05 });
    vids.forEach((v) => vio.observe(v));
  }

  // ------------------------------------------------------------------ back to top
  const top = $(".to-top");
  if (top) {
    const anchor = firstShown("[data-top-after]");
    const s = new Spring(0, (p) => {
      top.style.opacity = Math.min(1, Math.max(0, p));
      top.style.transform = `translateY(${(1 - p) * 60}px)`;
    });
    let shown = false;
    const check = () => {
      const limit = anchor ? (anchor.getBoundingClientRect().bottom + scrollY) : 220 * Z;
      const want = scrollY > limit;
      if (want !== shown) { shown = want; top.classList.toggle("show", want); s.set(want ? 1 : 0); }
    };
    addEventListener("scroll", check, { passive: true }); check();
    top.addEventListener("click", () => scrollTo({ top: 0, behavior: "smooth" }));
    const hov = new Spring(0, (y) => (top.firstElementChild.style.transform = `translateY(${y}px)`));
    top.addEventListener("mouseenter", () => hov.set(-6));
    top.addEventListener("mouseleave", () => hov.set(0));
  }

  // ------------------------------------------------------------------ case study contents: dot follows the section you're reading
  const toc = $(".toc");
  if (toc) {
    const items = $$("a", toc);
    const dot = $(".toc-dot", toc);
    const secs = items.map((a) => document.getElementById(a.getAttribute("href").slice(1)));
    const ty = (i) => items[i].offsetTop + 5;
    const s = new Spring(ty(0), (y) => (dot.style.transform = `translateY(${y}px)`));
    let cur = -1;
    const spy = () => {
      const line = innerHeight * 0.35;
      let idx = 0;
      secs.forEach((sec, i) => { if (sec && sec.getBoundingClientRect().top <= line) idx = i; });
      if (idx !== cur) {
        cur = idx; s.set(ty(idx));
        items.forEach((a, i) => a.classList.toggle("on", i === idx));
      }
    };
    addEventListener("scroll", spy, { passive: true }); spy();
    items.forEach((a, i) => a.addEventListener("click", (e) => {
      if (mode !== "ball") return;
      e.preventDefault();
      const y = secs[i].getBoundingClientRect().top + scrollY - (155 - (parseFloat(getComputedStyle(document.querySelector(".page")).getPropertyValue("--shift")) || 0)) * Z;
      scrollTo({ top: y, behavior: "smooth" });
    }));
  }

  // ------------------------------------------------------------------ cursor, coming soon, stamps
  let mode = "ball"; // ball | smile | frown
  const SOON = "[data-soon]";
  const stamps = document.createElement("div");
  stamps.className = "stamps";
  document.body.appendChild(stamps);

  function addStamp(kind, pageX, pageY) {
    const f = FACE[kind];
    const el = document.createElement("div");
    el.className = "stamp";
    el.style.cssText = `left:${pageX}px;top:${pageY}px;width:${f.w * SZ()}px;height:${f.h * SZ()}px`;
    el.innerHTML = f.svg;
    stamps.appendChild(el);
    const rot = -14;
    const s = new Spring(0, (p) => (el.style.transform = `translate(-50%,-50%) scale(${Math.max(0, p)}) rotate(${(1 - p) * rot}deg)`));
    s.set(1);
  }

  const picker = firstShown(".picker");
  const pickerBtns = picker ? $$("button", picker) : [];
  const pickerSprings = pickerBtns.map((b) => new Spring(b.dataset.mode === "ball" ? 1 : 0.35, (o) => (b.style.opacity = o)));
  function setMode(m) {
    mode = m;
    pickerBtns.forEach((b, i) => {
      b.setAttribute("aria-pressed", b.dataset.mode === m);
      pickerSprings[i].set(touch || b.dataset.mode === m ? 1 : 0.35);
    });
    cursorMode && cursorMode(m);
  }
  let cursorMode = null, cursorHide = () => {}, holding = false;

  if (!touch) {
    // --- desktop cursor ---
    root.classList.add("has-cursor");
    const cur = document.createElement("div");
    cur.className = "cursor";
    cur.innerHTML = `<div class="ball"><span>Coming soon!</span></div><div class="face"></div>`;
    document.body.appendChild(cur);
    const ball = $(".ball", cur), label = $("span", cur), face = $(".face", cur);

    // position follows the pointer 1:1 (no lag) so it's easy to control
    let cx = -100, cy = -100;
    const place = () => (cur.style.transform = `translate(${cx}px, ${cy}px)`);

    const BALL = 20; // cursor ball size (px)
    const bw = new Spring(BALL, (w) => (ball.style.width = w + "px"));
    const bh = new Spring(BALL, (h) => (ball.style.height = h + "px"));
    const bs = new Spring(1, (s) => (ball.style.transform = `translate(-50%,-50%) scale(${Math.max(0, s)})`));
    const tl = new Spring(0, (o) => { label.style.opacity = Math.max(0, Math.min(1, o)); label.style.transform = `translateY(${(1 - o) * 6}px)`; });
    const fs = new Spring(0, (s) => (face.style.transform = `translate(-50%,-50%) scale(${Math.max(0, s)})`));
    let soon = false, labelTimer;

    // the ball stretches into a pill that says `text` (null = back to a ball)
    function setSoon(text) {
      text = text || false;
      if (text === soon) return; soon = text;
      clearTimeout(labelTimer);
      if (text) { label.textContent = text; tl.set(0, { instant: true }); bw.set(label.scrollWidth + 16); bh.set(BALL); labelTimer = setTimeout(() => tl.set(1), 90); }
      else { tl.set(0, { instant: true }); bw.set(BALL); bh.set(BALL); }
    }
    cursorHide = (hide) => bs.set(hide ? 0 : 1);
    cursorMode = (m) => {
      if (m === "ball") { fs.set(0); bs.set(1); }
      else {
        setSoon(false);
        const f = FACE[m];
        face.innerHTML = f.svg; face.style.width = f.w * Z + "px"; face.style.height = f.h * Z + "px";
        bs.set(0); fs.set(0, { instant: true }); fs.set(1);
      }
    };

    addEventListener("pointermove", (e) => {
      if (e.pointerType === "touch") return;
      cx = e.clientX; cy = e.clientY; place();
      cur.classList.add("on");
      setSoon(mode !== "ball" || holding ? null
        : e.target.closest?.(SOON) ? "Coming soon!"
        : e.target.closest?.("[data-hold]") ? "Hold to look" : null);
    }, { passive: true });
    document.documentElement.addEventListener("mouseleave", () => cur.classList.remove("on"));
    addEventListener("blur", () => cur.classList.remove("on"));

    addEventListener("click", (e) => {
      if (e.target.closest?.(".picker")) return;
      if (mode !== "ball") { e.preventDefault(); e.stopPropagation(); addStamp(mode, e.pageX, e.pageY); return; }
      if (e.target.closest?.(SOON)) { e.preventDefault(); e.stopPropagation(); }
    }, true);
    addEventListener("keydown", (e) => { if (e.key === "Escape") setMode("ball"); });

    // press feedback: ball squishes a little
    addEventListener("pointerdown", () => mode === "ball" && !soon && bs.set(0.82));
    addEventListener("pointerup", () => mode === "ball" && !holding && bs.set(1));

    pickerBtns.forEach((b) => b.addEventListener("click", () => setMode(b.dataset.mode)));
  } else {
    // --- touch: tap an unfinished case study -> pill pops up where you tapped ---
    let popEl = null, popTimer;
    addEventListener("click", (e) => {
      const card = e.target.closest?.(SOON);
      if (!card) return;
      e.preventDefault(); e.stopPropagation();
      if (popEl) popEl.remove();
      popEl = document.createElement("div");
      popEl.className = "pop"; popEl.textContent = "Coming soon!";
      popEl.style.left = e.clientX + "px"; popEl.style.top = e.clientY + "px";
      document.body.appendChild(popEl);
      const el = popEl;
      const s = new Spring(0, (p) => (el.style.transform = `translate(-50%, calc(-50% - ${p * 40}px)) scale(${Math.max(0, p)})`));
      s.set(1);
      clearTimeout(popTimer);
      popTimer = setTimeout(() => { s.set(0); setTimeout(() => el.remove(), 400); }, 1400);
    }, true);

    // --- touch: drag a face out of the picker and drop it ---
    pickerBtns.forEach((b) => {
      if (b.dataset.mode === "ball") { b.style.display = "none"; return; }
      b.addEventListener("pointerdown", (e) => {
        e.preventDefault();
        const kind = b.dataset.mode, f = FACE[kind];
        const ghost = document.createElement("div");
        ghost.className = "stamp";
        ghost.style.cssText = `position:fixed;left:${e.clientX}px;top:${e.clientY}px;width:${f.w * SZ() * 1.25}px;height:${f.h * SZ() * 1.25}px;z-index:9999`;
        ghost.innerHTML = f.svg;
        document.body.appendChild(ghost);
        const gs = new Spring(0, (p) => (ghost.style.transform = `translate(-50%,-50%) scale(${Math.max(0, p)})`)); gs.set(1);
        const move = (ev) => { ev.preventDefault(); ghost.style.left = ev.clientX + "px"; ghost.style.top = ev.clientY + "px"; };
        const up = (ev) => {
          removeEventListener("pointermove", move); removeEventListener("pointerup", up); removeEventListener("pointercancel", up);
          ghost.remove();
          if (ev.type === "pointerup") addStamp(kind, ev.clientX + scrollX, ev.clientY + scrollY);
        };
        addEventListener("pointermove", move, { passive: false });
        addEventListener("pointerup", up); addEventListener("pointercancel", up);
      });
    });
  }
  if (picker) setMode("ball");

  // ------------------------------------------------------------------ Play: press & hold a piece to see it big
  const holdables = $$("[data-hold]");
  if (holdables.length) {
    const veil = document.createElement("div");
    veil.className = "hold-veil";
    document.body.appendChild(veil);
    let big = null, src = null, sp = null, timer = 0, startX = 0, startY = 0;

    const open = (box) => {
      const img = $("img", box), r = box.getBoundingClientRect();
      const nw = img.naturalWidth || r.width, nh = img.naturalHeight || r.height;
      const fit = Math.min((innerWidth * 0.88) / nw, (innerHeight * 0.88) / nh);
      const w = nw * fit, h = nh * fit;
      big = img.cloneNode(); big.removeAttribute("loading"); big.className = "hold-big";
      big.style.cssText = `left:${(innerWidth - w) / 2}px;top:${(innerHeight - h) / 2}px;width:${w}px;height:${h}px`;
      document.body.appendChild(big);
      src = box; box.style.visibility = "hidden";
      holding = true; cursorHide(true);
      // spring from the thumbnail's spot to the middle of the screen
      const sx = r.width / w, sy = r.height / h;
      const dx = r.left + r.width / 2 - innerWidth / 2, dy = r.top + r.height / 2 - innerHeight / 2;
      const el = big;
      sp = new Spring(0, (p) => {
        const q = Math.max(0, p);
        el.style.transform = `translate(${dx * (1 - p)}px, ${dy * (1 - p)}px) scale(${sx + (1 - sx) * p}, ${sy + (1 - sy) * p})`;
        el.style.clipPath = `inset(0 round ${8 * (1 - Math.min(1, q))}px)`;
        veil.style.opacity = Math.min(1, q);
      });
      sp.set(1);
    };
    const close = () => {
      clearTimeout(timer); timer = 0;
      if (!big) return;
      const el = big, box = src, s = sp;
      big = null; src = null; sp = null; holding = false; cursorHide(false);
      s.onUpdate = ((f) => (p) => { f(p); if (Math.abs(p) < 0.02 && s.target === 0) { el.remove(); box.style.visibility = ""; } })(s.onUpdate);
      s.set(0);
    };
    holdables.forEach((box) => {
      box.addEventListener("contextmenu", (e) => e.preventDefault());
      box.addEventListener("pointerdown", (e) => {
        if (mode !== "ball" || e.button > 0) return;
        startX = e.clientX; startY = e.clientY;
        clearTimeout(timer);
        timer = setTimeout(() => open(box), 140);
      });
    });
    addEventListener("pointermove", (e) => {
      // a finger that moves before the hold kicks in is scrolling, not holding
      if (timer && !big && Math.hypot(e.clientX - startX, e.clientY - startY) > 8) { clearTimeout(timer); timer = 0; }
    }, { passive: true });
    addEventListener("touchmove", (e) => { if (big) e.preventDefault(); }, { passive: false });
    ["pointerup", "pointercancel", "blur"].forEach((t) => addEventListener(t, close));
    addEventListener("keydown", (e) => e.key === "Escape" && close());
  }

  // hover lift on picker options
  pickerBtns.forEach((b) => {
    const s = new Spring(0, (y) => (b.style.transform = `translateY(${y}px) scale(${1 + -y * 0.03})`));
    b.addEventListener("mouseenter", () => s.set(-3));
    b.addEventListener("mouseleave", () => s.set(0));
  });
})();
