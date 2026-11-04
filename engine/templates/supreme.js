/* Supreme House of Pizza: menu tabs + search, season hours */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  // menu tabs + search
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) { t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); }; });
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var cur = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(cur < 0 ? 0 : cur); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var ok = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !ok; if (ok) c++; });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
  // hours: highlight current season and today
  var cur = window.__SUMMER__ ? 'summer' : 'winter';
  $$('.seas').forEach(function (s) { var on = s.getAttribute('data-season') === cur; s.classList.toggle('cur', on); s.querySelector('[data-now]').hidden = !on; });
  var wk = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date())];
  $$('.seas.cur tr').forEach(function (r) { if (+r.getAttribute('data-dow') === wk) r.classList.add('today'); });
})();
