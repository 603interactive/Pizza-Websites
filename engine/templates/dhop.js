/* DHOP: live status (handles after-midnight closes), Late Shift week scrubber, menu tabs + search, mobile nav */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var H = window.__HOURS__ || [], DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function tm(s) { var a = s.split(':'); return +a[0] * 60 + +a[1]; }
  function f12(m) { m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  // each shift: day it starts, start minute, end minute in that day's frame (end > 1440 when it runs past midnight)
  var shifts = []; H.forEach(function (r) { var o = tm(r.open), c = tm(r.close); if (c <= o) c += 1440; r.dow.forEach(function (d) { shifts.push({ d: d, o: o, c: c }); }); });
  function ny() {
    var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
    p.forEach(function (x) { o[x.type] = x.value; });
    return { dow: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: (+o.hour % 24) * 60 + +o.minute };
  }
  // is the shop open on the business day d at frame-minute t (t may exceed 1440)?
  function openOn(d, t) { return shifts.some(function (s) { return s.d === d && t >= s.o && t < s.c; }); }
  function shiftOn(d) { return shifts.filter(function (s) { return s.d === d; })[0]; }
  // current position: after-midnight minutes belong to the previous day's shift
  function frame() { var n = ny(); return { d: (n.dow + 6) % 7, t: n.min + 1440, d0: n.dow, t0: n.min }; }
  function status() {
    var n = ny(), cur = null;
    if (openOn(n.dow, n.min)) cur = shiftOn(n.dow); else if (openOn((n.dow + 6) % 7, n.min + 1440)) cur = shiftOn((n.dow + 6) % 7);
    if (cur) { var left = cur.c - (openOn(n.dow, n.min) ? n.min : n.min + 1440); return { open: true, text: 'Open now · until ' + f12(cur.c) + (left <= 90 ? ' (' + left + ' min left)' : '') }; }
    for (var i = 0; i < 8; i++) { var d = (n.dow + i) % 7, s = shiftOn(d); if (s && (i > 0 || s.o > n.min)) return { open: false, text: 'Closed · opens ' + (i === 0 ? 'today' : i === 1 ? 'tomorrow' : DAYS[d]) + ' at ' + f12(s.o) }; }
    return { open: false, text: 'Closed' };
  }
  var st = status(); document.documentElement.classList.toggle('is-open', st.open);
  $$('[data-status]').forEach(function (e) { e.textContent = st.text; });
  var wk = ny().dow; $$('.hours tr').forEach(function (r) { if (+r.getAttribute('data-dow') === wk) r.classList.add('today'); });
  var rb = $('[data-ribbon-x]'); if (rb) rb.onclick = function () { $('.ribbon').hidden = true; };

  // mobile nav
  var bg = $('.burger'), nav = $('#nav');
  bg.onclick = function () { var o = nav.classList.toggle('open'); bg.setAttribute('aria-expanded', o); };
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); } });

  // Late Shift scrubber: axis 11:00 (660) .. 03:00 next day (1620)
  var MIN = 660, MAX = 1620, SPAN = MAX - MIN, rng = $('#ls-range');
  if (rng) {
    var nowMode = true, rows = $$('.ls-rows li'), line = $('.ls-line b'), read = $('#ls-read'), axis = $('.ls-axis');
    function pct(t) { return Math.max(0, Math.min(100, (t - MIN) / SPAN * 100)); }
    [[720, '12 PM'], [960, '4 PM'], [1200, '8 PM'], [1440, '12 AM'], [1560, '2 AM']].forEach(function (a) { var s = document.createElement('span'); s.style.left = pct(a[0]) + '%'; s.textContent = a[1]; axis.appendChild(s); });
    rows.forEach(function (r) { var s = shiftOn(+r.getAttribute('data-dow')), f = r.querySelector('.ls-fill'); if (!s) { f.style.display = 'none'; return; } f.style.left = pct(s.o) + '%'; f.style.width = (pct(Math.min(s.c, MAX)) - pct(s.o)) + '%'; });
    function render() {
      var t = +rng.value, hit = [], only = (nowMode && t >= 1440) ? (ny().dow + 6) % 7 : -1;
      line.parentNode.style.display = 'block'; line.style.left = pct(t) + '%';
      rows.forEach(function (r) { var d = +r.getAttribute('data-dow'), on = openOn(d, t) && (only < 0 || d === only); r.classList.toggle('hit', on); if (on) hit.push(d); });
      var late = t >= 1440, label = f12(t) + (late ? ' (after midnight)' : '');
      if (!hit.length) read.innerHTML = '<b>' + label + '</b>: <span class="cl">closed every day</span>.';
      else { var names = hit.map(function (d) { return DAYS[d].slice(0, 3) + (late ? ' night' : ''); }); read.innerHTML = '<b>' + label + '</b>: <span>open ' + (hit.length === 7 ? 'every day' : names.join(', ')) + '</span>' + (hit.length < 7 ? '. Closed other ' + (late ? 'nights' : 'days') + '.' : '.'); }
      rng.setAttribute('aria-valuetext', label + ', ' + (hit.length ? 'open ' + hit.map(function (d) { return DAYS[d]; }).join(', ') : 'closed'));
    }
    function place() {
      var n = ny(), tt = n.min < 180 ? n.min + 1440 : n.min;
      var inr = tt >= MIN && tt <= MAX, fd = tt >= 1440 ? (n.dow + 6) % 7 : n.dow; $$('.nm').forEach(function (e) { e.remove(); });
      if (inr) { var row = $('.ls-rows li[data-dow="' + fd + '"] .ls-track'), m = document.createElement('span'); m.className = 'nm'; m.style.left = pct(tt) + '%'; m.innerHTML = '<span>Now</span>'; row.appendChild(m); }
      return Math.max(MIN, Math.min(MAX, Math.round(tt / 15) * 15));
    }
    rng.oninput = function () { nowMode = false; render(); };
    $$('.ls-btns button').forEach(function (b) { b.onclick = function () { var v = b.getAttribute('data-t'); nowMode = v === 'now'; rng.value = v === 'now' ? place() : v; render(); }; });
    rng.value = place(); render();
  }

  // menu tabs + search
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); t.tabIndex = k === i ? 0 : -1; }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) {
    t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); };
    t.onkeydown = function (e) { var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1; if (n >= 0 && n < tabs.length) { e.preventDefault(); tabs[n].focus(); tabs[n].click(); } };
  });
  show(0);
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var cur = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(cur < 0 ? 0 : cur); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
})();
