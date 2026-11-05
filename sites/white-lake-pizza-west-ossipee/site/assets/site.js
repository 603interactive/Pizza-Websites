/* White Lake Pizza: live open/closed status (summer vs off-season hours), season toggle, menu tabs + search, mobile nav */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var HRS = window.__HOURS__ || {}, DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function tm(s) { var a = s.split(':'); return +a[0] * 60 + +a[1]; }
  function f12(m) { var h = Math.floor(m / 60) % 24, mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  function ny() {
    var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', month: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
    p.forEach(function (x) { o[x.type] = x.value; });
    return { dow: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: (+o.hour % 24) * 60 + +o.minute, month: +o.month };
  }
  function rowFor(season, d) { var r = (HRS[season] || []).filter(function (h) { return h.dow.indexOf(d) > -1; })[0]; return r ? { o: tm(r.open), c: tm(r.close), dn: r.dine ? tm(r.dine) : null } : null; }
  function status(season) {
    var n = ny(), r = rowFor(season, n.dow);
    if (r && n.min >= r.o && n.min < r.c) {
      var t = 'Open now · until ' + f12(r.c), left = r.c - n.min;
      if (left <= 60) t += ' (' + left + ' min left)';
      else if (r.dn && n.min < r.dn) t += ' · dining room until ' + f12(r.dn);
      return { open: true, text: t };
    }
    for (var i = 0; i < 8; i++) { var d = (n.dow + i) % 7, s = rowFor(season, d); if (s && (i > 0 || s.o > n.min)) return { open: false, text: 'Closed · opens ' + (i === 0 ? 'today' : i === 1 ? 'tomorrow' : DAYS[d]) + ' at ' + f12(s.o) }; }
    return { open: false, text: 'Closed' };
  }
  // season in effect: assumed June to August = summer; the shop does not publish changeover dates
  var now = ny(), cur = (now.month >= 6 && now.month <= 8) ? 'summer' : 'off';
  function paint() {
    var st = status(cur); document.documentElement.classList.toggle('is-open', st.open);
    $$('[data-status]').forEach(function (e) { e.textContent = st.text; });
    $$('[data-season]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-season') === cur ? 'true' : 'false'); });
    $$('[data-season-table]').forEach(function (t) { t.hidden = t.getAttribute('data-season-table') !== cur; });
    $$('.hours tr').forEach(function (r) { r.classList.toggle('today', +r.getAttribute('data-dow') === now.dow); });
  }
  $$('[data-season]').forEach(function (b) { b.onclick = function () { cur = b.getAttribute('data-season'); paint(); }; });
  paint();
  var rb = $('[data-ribbon-x]'); if (rb) rb.onclick = function () { $('.ribbon').hidden = true; };

  var bg = $('.burger'), nav = $('#nav');
  bg.onclick = function () { var o = nav.classList.toggle('open'); bg.setAttribute('aria-expanded', o); };
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); } });

  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); t.tabIndex = k === i ? 0 : -1; }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) {
    t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); $$('.m-sec').forEach(function (e) { e.hidden = false; }); show(i); };
    t.onkeydown = function (e) { var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1; if (n >= 0 && n < tabs.length) { e.preventDefault(); tabs[n].focus(); tabs[n].click(); } };
  });
  show(0);
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var c0 = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); $$('.m-sec').forEach(function (e) { e.hidden = false; }); show(c0 < 0 ? 0 : c0); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    $$('.m-sec').forEach(function (s) { s.hidden = !s.querySelector('.m-it:not([hidden])'); });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
})();
