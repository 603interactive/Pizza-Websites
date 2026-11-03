/* Jaffrey Pizza Barn: Same Flavor Four Ways tabs, menu tabs + search, barn doors */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var h = $('#hero'); if (h) { var rm = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches; if (rm) h.classList.add('open'); else setTimeout(function () { h.classList.add('open'); }, 350); }
  var fb = $$('#fl-pick button'), bodies = $$('.fl-body');
  fb.forEach(function (b, i) { b.onclick = function () { fb.forEach(function (x, k) { x.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); bodies.forEach(function (x, k) { x.hidden = k !== i; }); }; });
  fb.forEach(function (b, i) { b.onkeydown = function (e) { var n = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? i + 1 : e.key === 'ArrowLeft' || e.key === 'ArrowUp' ? i - 1 : -1; if (n >= 0 && n < fb.length) { e.preventDefault(); fb[n].focus(); fb[n].click(); } }; });
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) { t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); }; });
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var cur = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(cur < 0 ? 0 : cur); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $$('.m-div').forEach(function (e) { e.hidden = true; });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
  var wk = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date())];
  $$('.hours tr').forEach(function (r) { if (+r.getAttribute('data-dow') === wk) r.classList.add('today'); });
})();
