(() => {
  const S = window.SITE || {};
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');

  /* ---------- open / closed status (shop time zone) ---------- */
  const fmt12 = t => { let [h, m] = t.split(':').map(Number); if (h === 24) h = 0; const ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return m ? `${h}:${String(m).padStart(2, '0')} ${ap}` : `${h} ${ap}`; };
  const nowInTZ = () => {
    const p = new Intl.DateTimeFormat('en-US', { timeZone: S.tz || 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    const g = k => p.find(x => x.type === k).value;
    const dow = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(g('weekday'));
    return { dow, min: (+g('hour') % 24) * 60 + +g('minute') };
  };
  const toMin = t => { const [h, m] = t.split(':').map(Number); return h * 60 + m; };
  function statusFor(loc) {
    const { dow, min } = nowInTZ();
    const today = loc.hours.find(r => r.dow.includes(dow));
    if (today && min >= toMin(today.open) && min < toMin(today.close)) return { open: true, text: `Open now · until ${fmt12(today.close)}`, short: `Open until ${fmt12(today.close)}` };
    if (today && min < toMin(today.open)) return { open: false, text: `Opens today at ${fmt12(today.open)}`, short: `Opens ${fmt12(today.open)}` };
    for (let i = 1; i <= 7; i++) {
      const d = (dow + i) % 7, r = loc.hours.find(x => x.dow.includes(d));
      if (r) { const name = i === 1 ? 'tomorrow' : ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][d]; return { open: false, text: `Closed · opens ${name} at ${fmt12(r.open)}`, short: `Opens ${name} ${fmt12(r.open)}` }; }
    }
    return { open: false, text: 'Call for hours', short: 'Call for hours' };
  }
  function paintStatus() {
    const { dow } = nowInTZ();
    (S.locations || []).forEach(loc => {
      const st = statusFor(loc);
      $$(`[data-loc="${loc.id}"]`).forEach(el => {
        const dot = $('.dot', el); if (dot) dot.className = 'dot ' + (st.open ? 'open' : 'closed');
        const full = $('[data-status-text] span', el); if (full) full.textContent = st.text;
        const short = $('[data-status-short]', el); if (short) short.textContent = st.short;
        if (el.matches('.status li')) $('span', el).textContent = `${loc.name} · ${st.short}`;
        $$('tr[data-dow]', el).forEach(tr => tr.classList.toggle('today', +tr.dataset.dow === dow));
      });
    });
  }
  paintStatus(); setInterval(paintStatus, 60000);

  /* ---------- header + mobile nav ---------- */
  const top = $('.top'), nav = $('#nav'), mb = $('.menu-btn');
  const onScroll = () => top && top.classList.toggle('scrolled', scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  if (mb) {
    mb.addEventListener('click', () => { const o = mb.getAttribute('aria-expanded') !== 'true'; mb.setAttribute('aria-expanded', o); nav.classList.toggle('open', o); mb.setAttribute('aria-label', o ? 'Close menu' : 'Open menu'); });
    $$('a', nav).forEach(a => a.addEventListener('click', () => { mb.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }));
  }

  /* ---------- order chooser (multi-location) ---------- */
  const sheet = $('#order-sheet');
  if (sheet) {
    let last;
    const open = e => { last = e.currentTarget; sheet.hidden = false; requestAnimationFrame(() => { sheet.classList.add('open'); $('.pick', sheet).focus(); }); };
    const close = () => { sheet.classList.remove('open'); setTimeout(() => { sheet.hidden = true; last && last.focus(); }, reduce ? 0 : 250); };
    $$('[data-order]').forEach(b => b.addEventListener('click', open));
    sheet.addEventListener('click', e => { if (e.target === sheet || e.target.closest('[data-close]')) close(); });
    addEventListener('keydown', e => { if (e.key === 'Escape' && !sheet.hidden) close(); });
    $$('.pick', sheet).forEach(p => p.addEventListener('click', () => setTimeout(close, 150)));
  }

  /* ---------- copy phone ---------- */
  $$('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    const txt = b.dataset.copy;
    try { await navigator.clipboard.writeText(txt); b.textContent = 'Copied'; }
    catch { const r = document.createRange(); r.selectNodeContents(b.previousElementSibling); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Selected'; }
    setTimeout(() => (b.textContent = 'Copy number'), 1800);
  }));

  /* ---------- menu: chips, search ---------- */
  const chips = $$('.chips a'), cats = $$('[data-cat]');
  if ('IntersectionObserver' in window && cats.length) {
    const vis = new Map();
    const io = new IntersectionObserver(es => {
      es.forEach(e => vis.set(e.target.id, e.isIntersecting ? e.intersectionRect.top : null));
      const cur = cats.find(c => vis.get(c.id) != null);
      if (cur) chips.forEach(a => { const on = a.hash === '#' + cur.id; a.setAttribute('aria-current', on); if (on) a.scrollIntoView({ block: 'nearest', inline: 'center', behavior: reduce ? 'auto' : 'smooth' }); });
    }, { rootMargin: '-45% 0px -50% 0px' });
    cats.forEach(c => io.observe(c));
  }
  const q = $('#menu-search'), empty = $('#menu-empty');
  if (q) q.addEventListener('input', () => {
    const v = q.value.trim().toLowerCase(); let shown = 0;
    cats.forEach(c => {
      let n = 0; $$('[data-item]', c).forEach(it => { const ok = !v || it.dataset.q.includes(v); it.classList.toggle('hide', !ok); if (ok) n++; });
      c.classList.toggle('hide', n === 0); shown += n;
      $$('.tiles,.rows', c).forEach(g => g.classList.toggle('hide', !$$('[data-item]:not(.hide)', g).length));
    });
    empty.style.display = shown ? 'none' : 'block';
  });

  /* ---------- favorites: pinned horizontal scroll on wide screens ---------- */
  const fav = $('.fav'), track = fav && $('.fav-track', fav), bar = fav && $('.fav-progress i', fav);
  function setupFav() {
    if (!fav) return;
    const wide = innerWidth >= 900 && innerHeight >= 680 && !reduce;
    fav.classList.toggle('pinned', wide);
    track.style.transform = '';
    if (!wide) { fav.style.height = ''; return; }
    const dist = Math.max(0, track.scrollWidth - innerWidth);
    fav.style.height = `calc(100vh + ${dist}px)`;
    fav.dataset.dist = dist;
  }
  function favScroll() {
    if (!fav) return;
    if (fav.classList.contains('pinned')) {
      const dist = +fav.dataset.dist || 0, r = fav.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, -r.top / Math.max(1, dist)));
      track.style.transform = `translate3d(${-p * dist}px,0,0)`;
      bar && bar.parentElement.style.setProperty('--p', p.toFixed(3));
    } else {
      const max = track.scrollWidth - track.clientWidth;
      bar && bar.parentElement.style.setProperty('--p', max > 0 ? (track.scrollLeft / max).toFixed(3) : 1);
    }
  }
  if (fav) {
    setupFav(); favScroll();
    addEventListener('resize', () => { setupFav(); favScroll(); });
    addEventListener('scroll', favScroll, { passive: true });
    track.addEventListener('scroll', favScroll, { passive: true });
    $$('[data-fav]', fav).forEach(b => b.addEventListener('click', () => {
      const card = $('.card', track); const step = card ? card.getBoundingClientRect().width + 20 : 300;
      track.scrollBy({ left: step * +b.dataset.fav, behavior: reduce ? 'auto' : 'smooth' });
    }));
  }

  /* ---------- card tilt + glare ---------- */
  if (!reduce && matchMedia('(hover:hover) and (pointer:fine)').matches) {
    $$('.card').forEach(c => {
      c.addEventListener('pointermove', e => {
        const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        c.style.transform = `perspective(900px) rotateY(${(x - .5) * 8}deg) rotateX(${(.5 - y) * 8}deg) translateY(-4px)`;
        c.style.setProperty('--mx', x * 100 + '%'); c.style.setProperty('--my', y * 100 + '%');
      });
      c.addEventListener('pointerleave', () => (c.style.transform = ''));
    });
  }

  /* ---------- hero parallax + ticker speed ---------- */
  const parImg = $('[data-par-img]'), stage = $('[data-parallax]'), ticker = $('.ticker-track');
  let lastY = scrollY, vel = 0, ticking = false;
  function frame() {
    ticking = false;
    const y = scrollY;
    if (!reduce && parImg && y < innerHeight * 1.4) {
      parImg.style.transform = `translate3d(0,${y * 0.12}px,0) scale(${1.06 + y * 0.00012})`;
      if (stage && S.heroLayout === 'split') stage.style.transform = `translate3d(0,${y * -0.06}px,0)`;
    }
    vel = vel * 0.85 + Math.abs(y - lastY) * 0.15; lastY = y;
    if (ticker && !reduce) ticker.style.setProperty('--marq', Math.max(9, 38 - vel * 1.4) + 's');
  }
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }, { passive: true });

  /* ---------- reveal (position only; content never hidden) ---------- */
  const rv = $$('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io2.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(el => { if (el.getBoundingClientRect().top < innerHeight) el.classList.add('in'); else io2.observe(el); });
  } else rv.forEach(el => el.classList.add('in'));

  /* ---------- count-up numbers ---------- */
  if (!reduce && 'IntersectionObserver' in window) {
    const io3 = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return; io3.unobserve(e.target);
      const el = e.target, end = parseFloat(el.dataset.count), sup = el.querySelector('sup'), t0 = performance.now(), dur = 900;
      const tick = t => { const k = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
        el.textContent = v; if (sup) el.prepend(sup); if (k < 1) requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
    }), { threshold: .6 });
    $$('[data-count]').forEach(el => io3.observe(el));
  }

  /* ---------- hero particles: steam / embers ---------- */
  const cv = $('.hero-fx');
  if (cv && !reduce) {
    const ctx = cv.getContext('2d'), hero = cv.parentElement, kind = S.fx || 'steam';
    let W, H, dpr, parts = [], run = true;
    const size = () => { dpr = Math.min(2, devicePixelRatio || 1); W = hero.clientWidth; H = hero.clientHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); };
    size(); addEventListener('resize', size);
    const N = kind === 'embers' ? Math.min(70, Math.round(W / 18)) : Math.min(26, Math.round(W / 50));
    const spawn = (init) => {
      if (kind === 'embers') return { x: Math.random() * W, y: init ? Math.random() * H : H + 10, r: Math.random() * 2.2 + .6, vy: -(Math.random() * .7 + .35), vx: (Math.random() - .5) * .3, life: 0, max: 400 + Math.random() * 400, hue: 18 + Math.random() * 26, wob: Math.random() * 6.28 };
      const sx = S.heroLayout === 'split' ? W * (innerWidth >= 960 ? .55 : .1) + Math.random() * W * (innerWidth >= 960 ? .4 : .8) : Math.random() * W;
      return { x: sx, y: init ? H * (.3 + Math.random() * .7) : H * (.75 + Math.random() * .3), r: 30 + Math.random() * 60, vy: -(Math.random() * .35 + .2), vx: (Math.random() - .5) * .2, life: 0, max: 420 + Math.random() * 380, wob: Math.random() * 6.28 };
    };
    for (let i = 0; i < N; i++) parts.push(spawn(true));
    const vis = new IntersectionObserver(es => { run = es[0].isIntersecting; if (run) requestAnimationFrame(loop); });
    vis.observe(hero);
    function loop() {
      if (!run || document.hidden) return;
      ctx.clearRect(0, 0, W, H);
      for (let i = 0; i < parts.length; i++) {
        const p = parts[i]; p.life++; p.wob += .02; p.x += p.vx + Math.sin(p.wob) * (kind === 'embers' ? .35 : .25); p.y += p.vy;
        const k = p.life / p.max, a = Math.sin(Math.PI * Math.min(1, k));
        if (kind === 'embers') {
          ctx.fillStyle = `hsla(${p.hue},95%,${55 + 15 * a}%,${.85 * a})`; ctx.shadowColor = `hsla(${p.hue},100%,55%,${a})`; ctx.shadowBlur = 8;
          ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.283); ctx.fill();
        } else {
          const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * (1 + k));
          g.addColorStop(0, `rgba(255,248,236,${.075 * a})`); g.addColorStop(1, 'rgba(255,248,236,0)');
          ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, p.y, p.r * (1 + k), 0, 6.283); ctx.fill();
        }
        if (p.life >= p.max || p.y < -80) parts[i] = spawn(false);
      }
      ctx.shadowBlur = 0;
      requestAnimationFrame(loop);
    }
    document.addEventListener('visibilitychange', () => { if (!document.hidden && run) requestAnimationFrame(loop); });
  }

  /* ---------- careers form ---------- */
  const form = $('#job-form'), msg = $('#form-msg');
  if (form) form.addEventListener('submit', e => {
    if (!form.checkValidity()) { e.preventDefault(); form.reportValidity(); return; }
    if (form.hasAttribute('data-preview')) {
      e.preventDefault();
      msg.hidden = false;
      msg.textContent = 'This is a design preview, so nothing was sent. On the live site this button sends the application to the shop.';
    }
  });
})();
