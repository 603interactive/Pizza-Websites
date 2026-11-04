/* Upper Crust: Week Board slider (split shifts), menu tabs + search, mobile nav */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var H = window.__HOURS__ || [], NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function tm(s) { var a = s.split(':'); return +a[0] * 60 + +a[1]; }
  function f12(m) { var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  function nyNow() { var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {}; p.forEach(function (x) { o[x.type] = x.value; }); return { dow: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: (+o.hour % 24) * 60 + +o.minute }; }
  var now = nyNow();
  $$('.hours tr, .wb-row').forEach(function (r) { if (+r.getAttribute('data-dow') === now.dow) r.classList.add('today'); });
  $$('.wb-row').forEach(function (r) { r.querySelector('.wb-d').setAttribute('data-d', ''); if (r.querySelectorAll('.bar').length > 1) r.setAttribute('data-g', '1'); });
  /* nav */
  var bg = $('.burger'), nav = $('#nav');
  function closeNav() { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); }
  bg.onclick = function () { var o = nav.classList.toggle('open'); bg.setAttribute('aria-expanded', o ? 'true' : 'false'); };
  nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') closeNav(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { closeNav(); bg.focus(); } });
  /* week board */
  var wb = $('#wb'), rng = $('#wb-range'), out = $('#wb-time'), say = $('#wb-say'), cur = $('#wb-cur'), grid = $('.wb-grid');
  var T0 = +wb.dataset.t0, T1 = +wb.dataset.t1;
  function openAt(d, m) { var c = null; H.forEach(function (r) { if (r.dow.indexOf(d) > -1 && m >= tm(r.open) && m < tm(r.close)) c = r; }); return c; }
  function nextOpen(d, m) { for (var i = 0; i < 8; i++) { var dd = (d + i) % 7, best = null; H.forEach(function (r) { if (r.dow.indexOf(dd) > -1 && (i > 0 || tm(r.open) > m)) { if (!best || tm(r.open) < tm(best.open)) best = r; } }); if (best) return { day: i === 0 ? 'later today' : i === 1 ? 'tomorrow' : NAMES[dd], at: tm(best.open) }; } return null; }
  function place() {
    var t = $('.wb-row .wb-t'), g = grid.getBoundingClientRect(), r = t.getBoundingClientRect();
    if (!r.width) return;
    var pct = (+rng.value - T0) / (T1 - T0); cur.style.left = (r.left - g.left + pct * r.width) + 'px';
    var last = $$('.wb-row').pop().getBoundingClientRect(); cur.style.top = (r.top - g.top - 4) + 'px'; cur.style.height = (last.bottom - r.top + 8) + 'px'; cur.style.bottom = 'auto';
  }
  function upd() {
    var m = +rng.value; out.textContent = f12(m); var openDays = [];
    $$('.wb-row').forEach(function (r) { var d = +r.dataset.dow, o = openAt(d, m); r.classList.toggle('on', !!o); r.querySelector('[data-st]').textContent = o ? 'Open' : 'Closed'; if (o) openDays.push(NAMES[d]); });
    var td = now.dow, o = openAt(td, m), t = 'At ' + f12(m) + ' today (' + NAMES[td] + '): ';
    if (o) t += 'open, until ' + f12(tm(o.close)) + '.';
    else { var n = nextOpen(td, m); t += 'closed' + (n ? ', next open ' + n.day + ' at ' + f12(n.at) + '.' : '.'); }
    say.textContent = t + ' ' + openDays.length + ' of 7 days are open at this time.'; place();
  }
  function useNow() { var m = Math.round(now.min / 15) * 15; if (m < T0 || m > T1 - 15) m = 18 * 60; rng.value = m; upd(); }
  rng.addEventListener('input', upd); $('#wb-now').onclick = useNow; window.addEventListener('resize', place); useNow(); setTimeout(place, 300);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(place);
  /* menu */
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); t.tabIndex = k === i ? 0 : -1; }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) {
    t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); };
    t.onkeydown = function (e) { var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : -1; if (n >= 0 && n < tabs.length) { e.preventDefault(); tabs[n].focus(); tabs[n].click(); } };
  });
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var c = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(c < 0 ? 0 : c); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
})();
