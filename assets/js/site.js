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

  // ------------------------------------------------------------------ faces (Erin's drawings)
  const SMILE = `<svg viewBox="0 0 102 66" fill="none"><path d="M96.5007 22.7695C96.5007 22.7695 95.7299 33.7359 90.1612 40.4224C84.7389 46.9332 80.6816 51.3314 69.6481 55.5333C44.9541 64.9378 22.0538 53.5685 10.347 41.5574C7.39131 38.5249 5.0013 33.0851 5.0013 33.0851" stroke="#B1D43A" stroke-width="10" stroke-linecap="round"/><path d="M29.1873 7C29.2003 8.16576 29.626 11.2044 30.2946 12.0939C30.4596 12.3133 30.852 12.384 30.8915 12.2354C30.9311 12.0867 30.6693 11.6503 30.3327 10.7695C29.996 9.88881 29.5925 8.57705 29.0012 7.14257" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M53.0012 8.99939C53.0012 9.01689 53.0012 9.03438 53.0012 9.54371C53.0012 10.053 53.0012 11.0537 53.3091 11.6673" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  const FROWN = `<svg viewBox="0 0 102 86" fill="none"><path d="M96.5945 50.137C96.5945 50.137 91.0954 40.6178 83.1594 37.0483C75.4321 33.5726 69.8576 31.3976 58.0987 32.4564C31.781 34.8262 16.1802 55.0821 10.9219 71.0089C9.59425 75.0301 9.83013 80.9671 9.83013 80.9671" stroke="#B1D43A" stroke-width="10" stroke-linecap="round"/><path d="M8.18607 10C8.19909 11.1658 8.62478 14.2044 9.29342 15.0939C9.45834 15.3133 9.85075 15.384 9.89032 15.2354C9.92989 15.0867 9.66807 14.6503 9.33144 13.7695C8.99482 12.8888 8.59132 11.577 8 10.1426" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M32 7C32 7.0175 32 7.03499 32 7.54432C32 8.05364 32 9.05427 32.3078 9.66793" stroke="#B1D43A" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  const FACE = { smile: { svg: SMILE, w: 39, h: 25 }, frown: { svg: FROWN, w: 40, h: 34 } };
  window.__faces = FACE;

  // fill any [data-face] placeholders (doodles, picker)
  $$("[data-face]").forEach((el) => { el.innerHTML = FACE[el.dataset.face].svg; });

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
    const anchor = $("[data-top-after]");
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
      const y = secs[i].getBoundingClientRect().top + scrollY - 155 * Z;
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
    el.style.cssText = `left:${pageX}px;top:${pageY}px;width:${f.w * Z}px;height:${f.h * Z}px`;
    el.innerHTML = f.svg;
    stamps.appendChild(el);
    const rot = -14;
    const s = new Spring(0, (p) => (el.style.transform = `translate(-50%,-50%) scale(${Math.max(0, p)}) rotate(${(1 - p) * rot}deg)`));
    s.set(1);
  }

  const picker = $(".picker");
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
  let cursorMode = null;

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

    function setSoon(on) {
      if (on === soon) return; soon = on;
      clearTimeout(labelTimer);
      if (on) { bw.set(label.scrollWidth + 16); bh.set(BALL); labelTimer = setTimeout(() => tl.set(1), 90); }
      else { tl.set(0, { instant: true }); bw.set(BALL); bh.set(BALL); }
    }
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
      setSoon(mode === "ball" && !!e.target.closest?.(SOON));
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
    addEventListener("pointerup", () => mode === "ball" && bs.set(1));

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
        ghost.style.cssText = `position:fixed;left:${e.clientX}px;top:${e.clientY}px;width:${f.w * Z * 1.25}px;height:${f.h * Z * 1.25}px;z-index:9999`;
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

  // hover lift on picker options
  pickerBtns.forEach((b) => {
    const s = new Spring(0, (y) => (b.style.transform = `translateY(${y}px) scale(${1 + -y * 0.03})`));
    b.addEventListener("mouseenter", () => s.set(-3));
    b.addEventListener("mouseleave", () => s.set(0));
  });
})();
