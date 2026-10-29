(() => {
  const S = window.SITE || {};
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const ease = t => t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  const easeOut = t => 1 - Math.pow(1 - t, 3);
  const bounce = t => { if (t < 1 / 2.75) return 7.5625 * t * t; if (t < 2 / 2.75) return 7.5625 * (t -= 1.5 / 2.75) * t + .75; if (t < 2.5 / 2.75) return 7.5625 * (t -= 2.25 / 2.75) * t + .9375; return 7.5625 * (t -= 2.625 / 2.75) * t + .984375; };
  const lerp = (a, b, t) => a + (b - a) * t;
  const mix = (c1, c2, t) => { const a = c1.match(/\d+/g).map(Number), b = c2.match(/\d+/g).map(Number); return `rgb(${Math.round(lerp(a[0], b[0], t))},${Math.round(lerp(a[1], b[1], t))},${Math.round(lerp(a[2], b[2], t))})`; };
  let seed = 7; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };

  /* ---------- open / closed ---------- */
  const fmt12 = t => { let [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return m ? `${h}:${String(m).padStart(2, '0')} ${ap}` : `${h} ${ap}`; };
  const toMin = t => { const [h, m] = t.split(':').map(Number); return h * 60 + m; };
  const nowInTZ = () => { const p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()); const g = k => p.find(x => x.type === k).value; return { dow: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(g('weekday')), min: (+g('hour') % 24) * 60 + +g('minute') }; };
  function status() {
    const { dow, min } = nowInTZ(), H = S.hours || [];
    const today = H.find(r => r.dow.includes(dow));
    if (today && min >= toMin(today.open) && min < toMin(today.close)) return { open: true, text: `Open now · until ${fmt12(today.close)}` };
    if (today && min < toMin(today.open)) return { open: false, text: `Opens today at ${fmt12(today.open)}` };
    for (let i = 1; i <= 7; i++) { const d = (dow + i) % 7, r = H.find(x => x.dow.includes(d)); if (r) return { open: false, text: `Closed · opens ${i === 1 ? 'tomorrow' : ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][d]} at ${fmt12(r.open)}` }; }
    return { open: false, text: 'Call for hours' };
  }
  function paint() {
    const st = status(), { dow } = nowInTZ();
    $$('[data-status],[data-loc]').forEach(el => { const d = $('.dot', el); if (d) d.className = 'dot ' + (st.open ? 'open' : 'closed'); const s = $('span', el); if (s) s.textContent = st.text; });
    $$('tr[data-dow]').forEach(tr => tr.classList.toggle('today', +tr.dataset.dow === dow));
  }
  paint(); setInterval(paint, 60000);

  /* ---------- header, nav, copy, search, chips, reveal ---------- */
  const top = $('.top'), nav = $('#nav'), mb = $('.menu-btn');
  addEventListener('scroll', () => top.classList.toggle('scrolled', scrollY > 10), { passive: true });
  mb.addEventListener('click', () => { const o = mb.getAttribute('aria-expanded') !== 'true'; mb.setAttribute('aria-expanded', o); nav.classList.toggle('open', o); });
  $$('a', nav).forEach(a => a.addEventListener('click', () => { mb.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }));
  $$('[data-copy]').forEach(b => b.addEventListener('click', async () => { try { await navigator.clipboard.writeText(b.dataset.copy); b.textContent = 'Copied'; } catch { const r = document.createRange(); r.selectNodeContents(b.previousElementSibling); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Selected'; } setTimeout(() => (b.textContent = 'Copy number'), 1800); }));
  const chips = $$('.chips a'), cats = $$('[data-cat]');
  if ('IntersectionObserver' in window) {
    const vis = new Map(); const io = new IntersectionObserver(es => { es.forEach(e => vis.set(e.target.id, e.isIntersecting)); const cur = cats.find(c => vis.get(c.id)); if (cur) chips.forEach(a => a.setAttribute('aria-current', a.hash === '#' + cur.id)); }, { rootMargin: '-40% 0px -50% 0px' });
    cats.forEach(c => io.observe(c));
  }
  const q = $('#menu-search'), empty = $('#menu-empty');
  q.addEventListener('input', () => { const v = q.value.trim().toLowerCase(); let shown = 0; cats.forEach(c => { let n = 0; $$('[data-item]', c).forEach(it => { const ok = !v || it.dataset.q.includes(v) || c.id.includes(v.replace(/\s+/g, '-')); it.classList.toggle('hide', !ok); if (ok) n++; }); c.classList.toggle('hide', n === 0); shown += n; }); empty.style.display = shown ? 'none' : 'block'; });
  const rv = $$('.rv');
  if ('IntersectionObserver' in window && !reduce) { const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io2.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' }); rv.forEach(el => { if (el.getBoundingClientRect().top < innerHeight) el.classList.add('in'); else io2.observe(el); }); } else rv.forEach(el => el.classList.add('in'));

  /* =====================================================================
     THE SCENE. Scroll progress p in [0,1] runs six stages:
     0 dough  1 sauce  2 cheese  3 toppings  4 oven  5 slice
     Everything is drawn from code; nothing here is a photo.
     ===================================================================== */
  const cv = $('#scene'), story = $('#story'), stage = $('.stage'), caps = $$('.cap'), steps = $$('.steps li');
  const ctx = cv.getContext('2d', { alpha: false });
  const N_ST = 6, B = [0, .16, .32, .49, .66, .84, 1];  // stage boundaries in p
  let W = 0, H = 0, dpr = 1, cx = 0, cy = 0, R = 0, mobile = false, mx = 0, my = 0, tmx = 0, tmy = 0;
  let wood, flourTex;

  function size() {
    dpr = Math.min(reduce ? 1 : 1.75, devicePixelRatio || 1);
    W = stage.clientWidth; H = stage.clientHeight; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    mobile = W < 1000;
    R = mobile ? Math.min(W * .34, H * .19) : Math.min(W * .21, H * .33);
    cx = mobile ? W * .5 : W * .69; cy = mobile ? H * .7 : H * .54;
    wood = makeWood(); flourTex = makeFlour();
  }
  function makeWood() {
    const c = document.createElement('canvas'); c.width = Math.round(W * dpr); c.height = Math.round(H * dpr); const g = c.getContext('2d'); g.scale(dpr, dpr);
    const base = g.createLinearGradient(0, 0, 0, H); base.addColorStop(0, '#5A3A22'); base.addColorStop(.5, '#6B4529'); base.addColorStop(1, '#3E2616'); g.fillStyle = base; g.fillRect(0, 0, W, H);
    seed = 11; const planks = Math.ceil(H / 110) + 1;
    for (let i = 0; i < planks; i++) { const y = i * 110 + (rnd() - .5) * 10; g.fillStyle = `rgba(0,0,0,${.12 + rnd() * .1})`; g.fillRect(0, y, W, 3); g.strokeStyle = 'rgba(255,220,170,.06)'; g.lineWidth = 1; for (let k = 0; k < 14; k++) { g.beginPath(); let x = -20, yy = y + 8 + rnd() * 96; g.moveTo(x, yy); for (; x < W + 40; x += 60) { yy += (rnd() - .5) * 6; g.lineTo(x, yy); } g.stroke(); } }
    const vig = g.createRadialGradient(W * .5, H * .5, Math.min(W, H) * .3, W * .5, H * .5, Math.max(W, H) * .8); vig.addColorStop(0, 'rgba(0,0,0,0)'); vig.addColorStop(1, 'rgba(0,0,0,.65)'); g.fillStyle = vig; g.fillRect(0, 0, W, H);
    return c;
  }
  function makeFlour() {
    const c = document.createElement('canvas'); c.width = Math.round(W * dpr); c.height = Math.round(H * dpr); const g = c.getContext('2d'); g.scale(dpr, dpr);
    const fg = g.createRadialGradient(cx, cy, R * .6, cx, cy, R * 2.2); fg.addColorStop(0, 'rgba(246,231,200,.42)'); fg.addColorStop(.6, 'rgba(246,231,200,.12)'); fg.addColorStop(1, 'rgba(246,231,200,0)'); g.fillStyle = fg; g.fillRect(0, 0, W, H);
    seed = 5; g.fillStyle = 'rgba(255,245,225,.55)'; for (let i = 0; i < 900; i++) { const a = rnd() * 6.283, d = R * (.7 + rnd() * rnd() * 1.8); g.beginPath(); g.arc(cx + Math.cos(a) * d * 1.3, cy + Math.sin(a) * d, rnd() * 1.4 + .2, 0, 6.283); g.fill(); }
    return c;
  }

  // deterministic layout of cheese shreds and toppings
  seed = 3;
  const shreds = Array.from({ length: 320 }, (_, i) => { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * .82; return { a, d, rot: rnd() * 6.283, len: .07 + rnd() * .08, hue: rnd(), i }; });
  seed = 9;
  const tops = [];
  for (let i = 0; i < 13; i++) { const a = (i / 13) * 6.283 + rnd() * .5, d = (i % 2 ? .62 : .33) + rnd() * .14; tops.push({ k: 'pep', a, d, r: .11 + rnd() * .02, rot: rnd() * 6.283, i }); }
  for (let i = 0; i < 7; i++) { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * .7; tops.push({ k: 'pepper', a, d, r: .09 + rnd() * .03, rot: rnd() * 6.283, i: 13 + i }); }
  for (let i = 0; i < 9; i++) { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * .72; tops.push({ k: 'olive', a, d, r: .045 + rnd() * .012, rot: rnd() * 6.283, i: 20 + i }); }
  for (let i = 0; i < 5; i++) { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * .6; tops.push({ k: 'basil', a, d, r: .1 + rnd() * .03, rot: rnd() * 6.283, i: 29 + i }); }
  seed = 21;
  const blisters = Array.from({ length: 26 }, () => { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * .8; return { a, d, r: .02 + rnd() * .035 }; });
  const dents = Array.from({ length: 64 }, () => rnd());
  const particles = [];  // flour / shreds / embers / steam, time based
  const spawnP = (k, init) => {
    const p = { k, life: 0 };
    if (k === 'flour') Object.assign(p, { x: cx + (rnd() - .5) * R * 4, y: init ? rnd() * H : H + 10, r: .6 + rnd() * 1.6, vx: (rnd() - .5) * .25, vy: -(.15 + rnd() * .3), max: 500 + rnd() * 500 });
    else if (k === 'ember') Object.assign(p, { x: cx + (rnd() - .5) * R * 3.2, y: init ? rnd() * H : H * .9 + rnd() * H * .1, r: .8 + rnd() * 2, vx: (rnd() - .5) * .4, vy: -(.5 + rnd() * .9), max: 260 + rnd() * 320, hue: 14 + rnd() * 30 });
    else if (k === 'steam') Object.assign(p, { x: cx + (rnd() - .5) * R * 1.6, y: cy - R * .2 + (rnd() - .5) * R * .6, r: 18 + rnd() * 30, vx: (rnd() - .5) * .3, vy: -(.3 + rnd() * .4), max: 240 + rnd() * 240 });
    return p;
  };
  for (let i = 0; i < 70; i++) particles.push(spawnP('flour', true));

  const stageT = (p, i) => clamp((p - B[i]) / (B[i + 1] - B[i]));

  function pieEdge(ctx, rad, wob) {
    ctx.beginPath();
    for (let i = 0; i <= 64; i++) { const a = (i / 64) * 6.283, w = 1 + (dents[i % 64] - .5) * wob; const x = cx + Math.cos(a) * rad * w, y = cy + Math.sin(a) * rad * w; i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }
    ctx.closePath();
  }

  function draw(p, time) {
    const t0 = stageT(p, 0), t1 = stageT(p, 1), t2 = stageT(p, 2), t3 = stageT(p, 3), t4 = stageT(p, 4), t5 = stageT(p, 5);
    const bake = easeOut(t4);               // 0 raw → 1 baked
    const inOven = clamp((p - B[4] + .04) / .14);   // darkening into the oven stage
    const outOven = easeOut(t5);           // back onto the counter for the slice
    const ovenMix = inOven * (1 - outOven * .85);
    // parallax
    tmx += (mx - tmx) * .06; tmy += (my - tmy) * .06;
    const px = tmx * 14, py = tmy * 10;

    // ---- background: counter, then oven
    ctx.save(); ctx.translate(px * .4, py * .4);
    ctx.drawImage(wood, -10, -10, W + 20, H + 20);
    ctx.drawImage(flourTex, -10, -10, W + 20, H + 20);
    ctx.restore();
    if (ovenMix > 0) {
      ctx.fillStyle = `rgba(14,7,4,${ovenMix * .8})`; ctx.fillRect(0, 0, W, H);
      // brick arch + firebox behind the pie
      ctx.save(); ctx.globalAlpha = ovenMix; ctx.translate(px * .2, py * .2);
      const ar = R * 1.75;
      ctx.fillStyle = '#4A2A1A'; ctx.beginPath(); ctx.arc(cx, cy + R * .15, ar, Math.PI, 0); ctx.lineTo(cx + ar, H); ctx.lineTo(cx - ar, H); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#7A4A2C'; ctx.lineWidth = 2; for (let i = 0; i < 22; i++) { const a = Math.PI + (i / 22) * Math.PI; ctx.beginPath(); ctx.moveTo(cx + Math.cos(a) * ar * .86, cy + R * .15 + Math.sin(a) * ar * .86); ctx.lineTo(cx + Math.cos(a) * ar, cy + R * .15 + Math.sin(a) * ar); ctx.stroke(); }
      ctx.strokeStyle = '#8E5A36'; ctx.lineWidth = 4; ctx.beginPath(); ctx.arc(cx, cy + R * .15, ar * .86, Math.PI, 0); ctx.stroke(); ctx.beginPath(); ctx.arc(cx, cy + R * .15, ar, Math.PI, 0); ctx.stroke();
      // fire
      const fg = ctx.createRadialGradient(cx, cy + R * .1, R * .1, cx, cy + R * .1, ar * .85); const fl = .9 + Math.sin(time / 90) * .06 + Math.sin(time / 37) * .04;
      fg.addColorStop(0, `rgba(255,215,120,${.95 * fl})`); fg.addColorStop(.35, `rgba(255,120,30,${.75 * fl})`); fg.addColorStop(.7, 'rgba(160,40,10,.35)'); fg.addColorStop(1, 'rgba(60,10,0,0)');
      ctx.fillStyle = fg; ctx.beginPath(); ctx.arc(cx, cy + R * .15, ar * .86, Math.PI, 0); ctx.closePath(); ctx.fill();
      // flames
      for (let i = 0; i < 9; i++) { const fx = cx + (i - 4) * R * .3, hgt = R * (.55 + Math.sin(time / 110 + i * 1.7) * .18 + Math.sin(time / 53 + i) * .1), base = cy + R * .12; ctx.fillStyle = `rgba(255,${150 + Math.round(Math.sin(time / 70 + i) * 40)},40,.55)`; ctx.beginPath(); ctx.moveTo(fx - R * .14, base); ctx.quadraticCurveTo(fx - R * .18, base - hgt * .5, fx + Math.sin(time / 80 + i) * R * .06, base - hgt); ctx.quadraticCurveTo(fx + R * .18, base - hgt * .5, fx + R * .14, base); ctx.closePath(); ctx.fill(); }
      ctx.restore();
      // floor glow
      const gl = ctx.createRadialGradient(cx, cy + R * .8, R * .2, cx, cy + R * .8, R * 2.6); gl.addColorStop(0, `rgba(255,120,30,${.35 * ovenMix})`); gl.addColorStop(1, 'rgba(255,120,30,0)'); ctx.fillStyle = gl; ctx.fillRect(0, 0, W, H);
    }

    // ---- the pie (with parallax opposite the counter)
    ctx.save(); ctx.translate(-px * .5, -py * .5);
    const grow = easeOut(t0), rad = R * (.55 + .45 * grow);
    const liftY = -Math.sin(t0 * Math.PI) * R * .18;  // tossed up while stretching
    ctx.translate(0, liftY);
    // shadow
    ctx.fillStyle = `rgba(0,0,0,${.35 + ovenMix * .3})`; ctx.beginPath(); ctx.ellipse(cx + 6, cy + 14 - liftY * .6, rad * 1.02, rad * .98, 0, 0, 6.283); ctx.fill();
    // dough
    const raw = 'rgb(240,218,170)', baked = 'rgb(214,150,74)', rawEdge = 'rgb(230,200,150)', bakedEdge = 'rgb(176,104,40)';
    const dg = ctx.createRadialGradient(cx - rad * .2, cy - rad * .25, rad * .1, cx, cy, rad); dg.addColorStop(0, mix('rgb(248,230,190)', 'rgb(226,166,90)', bake)); dg.addColorStop(.8, mix(raw, baked, bake)); dg.addColorStop(1, mix(rawEdge, bakedEdge, bake));
    pieEdge(ctx, rad, .05 + .03 * (1 - grow)); ctx.fillStyle = dg; ctx.fill();
    // crust ring
    ctx.lineWidth = rad * .07; ctx.strokeStyle = mix('rgb(232,205,158)', 'rgb(190,118,48)', bake); pieEdge(ctx, rad * .965, .04); ctx.stroke();
    // char spots on crust when baked
    if (bake > .2) { ctx.fillStyle = `rgba(70,30,10,${.5 * bake})`; for (let i = 0; i < 18; i++) { const a = (i / 18) * 6.283 + dents[i] * .3; ctx.beginPath(); ctx.ellipse(cx + Math.cos(a) * rad * .96, cy + Math.sin(a) * rad * .96, rad * .035 * (.6 + dents[i + 20]), rad * .02, a, 0, 6.283); ctx.fill(); } }
    // sauce
    const sr = rad * .86 * easeOut(t1);
    if (sr > 0) {
      const sg = ctx.createRadialGradient(cx, cy, 0, cx, cy, sr); sg.addColorStop(0, mix('rgb(205,42,30)', 'rgb(170,38,24)', bake)); sg.addColorStop(1, mix('rgb(176,30,22)', 'rgb(140,28,18)', bake));
      ctx.fillStyle = sg; pieEdge(ctx, sr, .06); ctx.fill();
      // ladle spiral highlight while spreading
      if (t1 < 1) { ctx.strokeStyle = 'rgba(255,120,100,.35)'; ctx.lineWidth = rad * .07; ctx.beginPath(); const turns = 3.5 * t1; for (let i = 0; i <= 120; i++) { const k = i / 120, a = k * turns * 6.283, d = k * sr * .95; i ? ctx.lineTo(cx + Math.cos(a) * d, cy + Math.sin(a) * d) : ctx.moveTo(cx, cy); } ctx.stroke(); }
    }
    // cheese shreds (fall in during stage 2, melt into a blanket when baked)
    const shown = t2 * (shreds.length + 60);
    if (bake > 0) { const cg = ctx.createRadialGradient(cx, cy, 0, cx, cy, rad * .84); cg.addColorStop(0, `rgba(255,224,150,${.9 * bake})`); cg.addColorStop(1, `rgba(238,190,110,${.85 * bake})`); ctx.fillStyle = cg; pieEdge(ctx, rad * .83, .08); ctx.fill(); }
    for (const s of shreds) {
      const local = clamp((shown - s.i) / 60); if (local <= 0) continue;
      const fall = (1 - easeOut(local)) * -H * .5, x = cx + Math.cos(s.a) * s.d * rad, y = cy + Math.sin(s.a) * s.d * rad + fall, L = s.len * rad * (1 - bake * .4);
      ctx.save(); ctx.translate(x, y); ctx.rotate(s.rot + (1 - local) * 2); ctx.fillStyle = `rgba(${255},${228 - s.hue * 30},${150 - s.hue * 40},${(.95 - bake * .5) * Math.min(1, local * 3)})`; ctx.beginPath(); ctx.roundRect(-L / 2, -L * .17, L, L * .34, L * .17); ctx.fill(); ctx.restore();
    }
    // blisters / browned cheese
    if (bake > .3) for (const b of blisters) { const x = cx + Math.cos(b.a) * b.d * rad, y = cy + Math.sin(b.a) * b.d * rad, r = b.r * rad; const bg = ctx.createRadialGradient(x, y, 0, x, y, r); bg.addColorStop(0, `rgba(150,70,20,${.55 * (bake - .3)})`); bg.addColorStop(.6, `rgba(200,110,40,${.35 * (bake - .3)})`); bg.addColorStop(1, 'rgba(200,110,40,0)'); ctx.fillStyle = bg; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.283); ctx.fill(); }
    // toppings drop in
    const dropN = t3 * (tops.length + 10);
    for (const o of tops) {
      const local = clamp((dropN - o.i) / 10); if (local <= 0) continue;
      const fall = (1 - bounce(local)) * -H * .45, x = cx + Math.cos(o.a) * o.d * rad, y = cy + Math.sin(o.a) * o.d * rad + fall, r = o.r * rad;
      ctx.save(); ctx.translate(x, y); ctx.rotate(o.rot); ctx.globalAlpha = Math.min(1, local * 4);
      if (local < 1) { ctx.shadowColor = 'rgba(0,0,0,.4)'; ctx.shadowBlur = 14; ctx.shadowOffsetY = (1 - local) * 30; }
      if (o.k === 'pep') { const g = ctx.createRadialGradient(-r * .3, -r * .3, r * .1, 0, 0, r); g.addColorStop(0, mix('rgb(204,52,44)', 'rgb(150,28,20)', bake)); g.addColorStop(1, mix('rgb(160,26,22)', 'rgb(96,18,12)', bake)); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, r, 0, 6.283); ctx.fill(); ctx.fillStyle = `rgba(255,170,150,${.35})`; for (let k = 0; k < 7; k++) { const aa = k * 2.3, dd = r * (.2 + (k % 3) * .22); ctx.beginPath(); ctx.arc(Math.cos(aa) * dd, Math.sin(aa) * dd, r * .09, 0, 6.283); ctx.fill(); } if (bake > .4) { ctx.strokeStyle = `rgba(60,10,5,${(bake - .4) * .9})`; ctx.lineWidth = r * .12; ctx.beginPath(); ctx.arc(0, 0, r * .92, 0, 6.283); ctx.stroke(); } }
      else if (o.k === 'pepper') { ctx.strokeStyle = mix('rgb(84,160,70)', 'rgb(70,120,50)', bake); ctx.lineWidth = r * .32; ctx.beginPath(); for (let k = 0; k <= 24; k++) { const aa = k / 24 * 6.283, w = 1 + Math.sin(aa * 3) * .12; k ? ctx.lineTo(Math.cos(aa) * r * w, Math.sin(aa) * r * w) : ctx.moveTo(r, 0); } ctx.closePath(); ctx.stroke(); ctx.strokeStyle = 'rgba(200,255,180,.35)'; ctx.lineWidth = r * .08; ctx.stroke(); }
      else if (o.k === 'olive') { ctx.fillStyle = '#1E1516'; ctx.beginPath(); ctx.arc(0, 0, r, 0, 6.283); ctx.fill(); ctx.fillStyle = mix('rgb(200,42,30)', 'rgb(230,190,120)', Math.min(1, t2 + bake)); ctx.beginPath(); ctx.arc(0, 0, r * .42, 0, 6.283); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,.25)'; ctx.beginPath(); ctx.arc(-r * .3, -r * .3, r * .22, 0, 6.283); ctx.fill(); }
      else { ctx.fillStyle = mix('rgb(70,140,60)', 'rgb(46,92,40)', bake); ctx.beginPath(); ctx.moveTo(-r, 0); ctx.quadraticCurveTo(-r * .2, -r * .9, r, 0); ctx.quadraticCurveTo(-r * .2, r * .9, -r, 0); ctx.fill(); ctx.strokeStyle = 'rgba(200,240,160,.5)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(-r * .9, 0); ctx.lineTo(r * .9, 0); ctx.stroke(); }
      ctx.restore();
    }
    // oven heat haze on top of the pie
    if (ovenMix > 0) { const hz = ctx.createRadialGradient(cx, cy - rad * .3, 0, cx, cy, rad * 1.3); hz.addColorStop(0, `rgba(255,160,60,${.18 * ovenMix})`); hz.addColorStop(1, 'rgba(255,120,30,0)'); ctx.fillStyle = hz; ctx.fillRect(cx - rad * 1.4, cy - rad * 1.4, rad * 2.8, rad * 2.8); }
    // slice: cut lines, then one wedge pulls out with cheese strings
    if (t5 > 0) {
      const cuts = 8, cutT = clamp(t5 / .35);
      ctx.strokeStyle = `rgba(60,25,10,${.35 + .35 * cutT})`; ctx.lineWidth = 2.5;
      for (let i = 0; i < cuts; i++) { const a = (i / cuts) * 6.283, L = rad * .98 * clamp(cutT * cuts - i + 1); if (L <= 0) continue; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(a) * L, cy + Math.sin(a) * L); ctx.stroke(); }
      const pull = easeOut(clamp((t5 - .35) / .65)), a0 = -6.283 / cuts * 1.5, a1 = a0 + 6.283 / cuts, mid = (a0 + a1) / 2, off = pull * rad * .62;
      if (pull > 0) {
        // cover the wedge's old spot with a darker tray
        ctx.save(); ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, rad * 1.01, a0, a1); ctx.closePath(); ctx.fillStyle = mix('rgb(120,80,48)', 'rgb(60,36,20)', ovenMix); ctx.fill(); ctx.fillStyle='rgba(255,220,150,.25)'; for(let k=0;k<12;k++){const aa=a0+(a1-a0)*dents[k], dd=rad*dents[k+12]*.9; ctx.beginPath(); ctx.arc(cx+Math.cos(aa)*dd, cy+Math.sin(aa)*dd, 2+dents[k+30]*3, 0, 6.283); ctx.fill();} ctx.restore();
        // cheese strings
        ctx.strokeStyle = 'rgba(255,236,170,.95)'; ctx.lineCap = 'round'; ctx.shadowColor='rgba(0,0,0,.4)'; ctx.shadowBlur=4;
        for (let k = 0; k < 5; k++) { const kk = k / 4, aa = a0 + (a1 - a0) * (.15 + kk * .7), d = rad * (.25 + kk * .5); const x1 = cx + Math.cos(aa) * d, y1 = cy + Math.sin(aa) * d, x2 = x1 + Math.cos(mid) * off, y2 = y1 + Math.sin(mid) * off; ctx.lineWidth = 2 + (1 - pull) * 3; ctx.globalAlpha = 1 - pull * .45; ctx.beginPath(); ctx.moveTo(x1, y1); ctx.quadraticCurveTo((x1 + x2) / 2, (y1 + y2) / 2 + off * .35, x2, y2); ctx.stroke(); }
        ctx.globalAlpha = 1; ctx.shadowBlur = 0;
        // the wedge, redrawn and translated
        ctx.save(); ctx.translate(Math.cos(mid) * off, Math.sin(mid) * off - pull * 8); ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, rad * .99, a0, a1); ctx.closePath(); ctx.clip();
        ctx.fillStyle = dg; pieEdge(ctx, rad, .05); ctx.fill(); ctx.lineWidth = rad * .07; ctx.strokeStyle = mix('rgb(232,205,158)', 'rgb(190,118,48)', bake); pieEdge(ctx, rad * .965, .04); ctx.stroke();
        ctx.fillStyle = mix('rgb(176,30,22)', 'rgb(140,28,18)', bake); pieEdge(ctx, rad * .86, .06); ctx.fill();
        const cg2 = ctx.createRadialGradient(cx, cy, 0, cx, cy, rad * .84); cg2.addColorStop(0, 'rgba(255,224,150,.9)'); cg2.addColorStop(1, 'rgba(238,190,110,.85)'); ctx.fillStyle = cg2; pieEdge(ctx, rad * .83, .08); ctx.fill();
        for (const o of tops) { const x = cx + Math.cos(o.a) * o.d * rad, y = cy + Math.sin(o.a) * o.d * rad, r = o.r * rad; if (o.k === 'pep') { ctx.fillStyle = 'rgb(130,24,18)'; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.283); ctx.fill(); } else if (o.k === 'olive') { ctx.fillStyle = '#1E1516'; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.283); ctx.fill(); } else if (o.k === 'pepper') { ctx.strokeStyle = 'rgb(70,120,50)'; ctx.lineWidth = r * .32; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.283); ctx.stroke(); } }
        ctx.restore();
      }
    }
    ctx.restore();

    // ---- particles (time based)
    const want = inOven > .3 && outOven < .9 ? 'ember' : (t5 > .3 ? 'steam' : 'flour');
    for (let i = 0; i < particles.length; i++) {
      const q = particles[i]; q.life++; q.x += q.vx; q.y += q.vy; const k = q.life / q.max, a = Math.sin(Math.PI * Math.min(1, k));
      if (q.k === 'flour') { ctx.fillStyle = `rgba(255,245,225,${.55 * a})`; ctx.beginPath(); ctx.arc(q.x, q.y, q.r, 0, 6.283); ctx.fill(); }
      else if (q.k === 'ember') { ctx.fillStyle = `hsla(${q.hue},95%,60%,${.9 * a})`; ctx.beginPath(); ctx.arc(q.x + Math.sin(q.life / 9) * .6, q.y, q.r, 0, 6.283); ctx.fill(); }
      else { const g = ctx.createRadialGradient(q.x, q.y, 0, q.x, q.y, q.r * (1 + k)); g.addColorStop(0, `rgba(255,248,236,${.08 * a})`); g.addColorStop(1, 'rgba(255,248,236,0)'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(q.x, q.y, q.r * (1 + k), 0, 6.283); ctx.fill(); }
      if (q.life >= q.max || q.y < -60) particles[i] = spawnP(want, false);
    }
    // vignette
    const vg = ctx.createRadialGradient(W * .5, H * .5, Math.min(W, H) * .45, W * .5, H * .5, Math.max(W, H) * .75); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, `rgba(0,0,0,${.35 + ovenMix * .3})`); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    // left-side shade so the captions read on desktop
    if (!mobile) { const sg = ctx.createLinearGradient(0, 0, W * .55, 0); sg.addColorStop(0, 'rgba(10,5,3,.78)'); sg.addColorStop(1, 'rgba(10,5,3,0)'); ctx.fillStyle = sg; ctx.fillRect(0, 0, W * .55, H); }
    else { const sg = ctx.createLinearGradient(0, 0, 0, H * .5); sg.addColorStop(0, 'rgba(10,5,3,.86)'); sg.addColorStop(1, 'rgba(10,5,3,0)'); ctx.fillStyle = sg; ctx.fillRect(0, 0, W, H * .5); }
  }

  // ---- captions and progress follow p
  let curStage = -1;
  function captions(p) {
    const i = Math.min(N_ST - 1, B.findIndex((b, k) => p >= b && p < B[k + 1]) );
    const idx = i < 0 ? N_ST - 1 : i;
    if (idx !== curStage) { curStage = idx; caps.forEach((c, k) => c.classList.toggle('on', k === idx)); steps.forEach((s, k) => { s.classList.toggle('on', k === idx); s.classList.toggle('done', k < idx); }); }
  }

  let p = 0, raf = false, running = true;
  function progress() { const r = story.getBoundingClientRect(); const total = r.height - H; return clamp(-r.top / Math.max(1, total)); }
  function frame(time) { raf = false; if (!running) return; draw(p, time); if (!reduce) requestAnimationFrame(frame); }
  function onScroll() { p = progress(); captions(p); }
  if (reduce) { size(); p = 1; draw(1, 0); caps.forEach(c => c.classList.add('on')); }
  else {
    size(); onScroll(); requestAnimationFrame(frame);
    addEventListener('scroll', onScroll, { passive: true });
    addEventListener('resize', () => { size(); onScroll(); });
    addEventListener('pointermove', e => { if (!mobile && e.pointerType === 'mouse') { mx = (e.clientX / W - .5) * 2; my = (e.clientY / H - .5) * 2; } }, { passive: true });
    new IntersectionObserver(es => { running = es[0].isIntersecting; if (running) requestAnimationFrame(frame); }).observe(stage);
    document.addEventListener('visibilitychange', () => { if (!document.hidden && running) requestAnimationFrame(frame); });
    // ticker speed follows scroll velocity
    const ticker = $('.ticker-track'); let ly = scrollY, vel = 0; addEventListener('scroll', () => { vel = vel * .85 + Math.abs(scrollY - ly) * .15; ly = scrollY; ticker.style.setProperty('--marq', Math.max(9, 40 - vel * 1.4) + 's'); }, { passive: true });
  }
})();
