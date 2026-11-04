/* Pizza Haven: pizza finder (filters + surprise me), menu tabs + search, weekend-aware status */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  /* status: only Mon-Fri hours are known, so say so on weekends */
  var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
  p.forEach(function (x) { o[x.type] = x.value; });
  var dow = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min = (+o.hour % 24) * 60 + +o.minute;
  var wkend = dow === 0 || dow === 6 || (dow === 5 && min >= 21 * 60);
  if (wkend) { document.documentElement.classList.remove('is-open'); $$('[data-status]').forEach(function (e) { e.textContent = dow === 5 ? 'Closed for tonight · weekend hours not confirmed, call' : 'Weekend hours not confirmed · call to check'; }); }
  $$('.hours tr').forEach(function (r) { if (+r.getAttribute('data-dow') === dow) r.classList.add('today'); });
  /* finder */
  var chips = $$('#pf-chips button'), cards = $$('.pf-card'), cnt = $('#pf-count'), spot = $('#pf-spot'), cur = 'all';
  function apply() {
    var n = 0; cards.forEach(function (c) { var m = cur === 'all' || c.getAttribute('data-tags').split(' ').indexOf(cur) > -1; c.hidden = !m; if (m) n++; });
    cnt.textContent = n + (n === 1 ? ' pizza' : ' pizzas') + (cur === 'all' ? ' on the menu' : ' match');
  }
  chips.forEach(function (b) { b.onclick = function () { cur = b.getAttribute('data-f'); chips.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); spot.hidden = true; apply(); }; });
  var last = -1;
  $('#pf-surprise').onclick = function () {
    var vis = cards.filter(function (c) { return !c.hidden; }); if (!vis.length) return;
    var k; do { k = Math.floor(Math.random() * vis.length); } while (vis.length > 1 && vis[k] === cards[last]);
    var c = vis[k]; last = cards.indexOf(c);
    $('#sp-name').textContent = c.getAttribute('data-name'); $('#sp-desc').textContent = c.getAttribute('data-desc') || 'Ask the shop how this one is built.';
    $('#sp-price').textContent = c.getAttribute('data-price'); var cz = c.getAttribute('data-calz');
    $('#sp-calz').textContent = cz ? 'Also a calzone for ' + cz : ''; spot.hidden = false;
    cards.forEach(function (x) { x.classList.toggle('pick', x === c); });
  };
  apply();
  /* menu */
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); panels.forEach(function (x, k) { x.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) { t.onclick = function () { q.value = ''; $$('.m-it,.m-sub').forEach(function (e) { e.hidden = false; }); show(i); }; });
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var c0 = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it,.m-sub').forEach(function (e) { e.hidden = false; }); show(c0 < 0 ? 0 : c0); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    $$('.m-sub').forEach(function (s) { s.hidden = !s.querySelector('.m-it:not([hidden])'); });
    panels.forEach(function (x) { x.hidden = !x.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
})();
