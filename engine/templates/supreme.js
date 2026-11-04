/* Supreme House of Pizza: Name Your Price budget finder + tray, menu tabs + search, season hours */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var ITEMS = window.__ITEMS__ || [], TAX = 0.09, MIN = 25, SHOW = 18, shown = SHOW, group = -1, tray = {};
  var bd = $('#bd'), out = $('#bd-o');
  function m(n) { return '$' + n.toFixed(2); }
  function key(i) { return i; }
  function sub() { var s = 0; Object.keys(tray).forEach(function (k) { s += ITEMS[k].p * tray[k]; }); return s; }
  function budget() { return +bd.value; }
  function render() {
    var B = budget(), s = sub(), tot = s * (1 + TAX), left = B - tot;
    out.textContent = '$' + B; bd.style.setProperty('--pct', ((B - 5) / 95 * 100) + '%');
    var list = [];
    ITEMS.forEach(function (it, i) { if ((group < 0 || it.g === group) && (tray[i] || it.p * (1 + TAX) <= left + 0.001)) list.push(i); });
    list.sort(function (a, b) { return ITEMS[b].p - ITEMS[a].p; });
    $('#fnd-count').textContent = list.length + (list.length === 1 ? ' thing fits' : ' things fit') + ' in ' + m(Math.max(left, 0)) + ' of budget';
    var vis = list.slice(0, shown);
    $('#tiles').innerHTML = vis.map(function (i) {
      var it = ITEMS[i], q = tray[i] || 0;
      return '<li><button type="button" class="tile' + (q ? ' on' : '') + '" data-i="' + i + '" aria-label="Add ' + it.n + (it.s ? ' ' + it.s : '') + ', ' + m(it.p) + '"><span class="t-c">' + it.c + (it.s ? ' · ' + it.s : '') + '</span><b>' + it.n + '</b><span class="t-p">' + m(it.p) + '<small>' + m(it.p * (1 + TAX)) + ' with tax</small></span>' + (q ? '<i class="t-q">×' + q + '</i>' : '') + '</button></li>';
    }).join('');
    var more = $('#more'); more.hidden = list.length <= shown; more.textContent = 'Show ' + Math.min(SHOW, list.length - shown) + ' more';
    $('#fnd-none').hidden = list.length > 0;
    var keys = Object.keys(tray);
    $('#t-lines').innerHTML = keys.length ? keys.map(function (k) {
      var it = ITEMS[k]; return '<li><span class="l-n">' + it.n + (it.s ? ' <small>' + it.s + '</small>' : '') + '</span><span class="l-q"><button type="button" data-d="-1" data-i="' + k + '" aria-label="Remove one ' + it.n + '">−</button>' + tray[k] + '<button type="button" data-d="1" data-i="' + k + '" aria-label="Add one ' + it.n + '">+</button></span><span class="l-p">' + m(it.p * tray[k]) + '</span></li>';
    }).join('') : '<li class="t-empty">Tap anything on the left to add it.</li>';
    $('#t-sub').textContent = m(s); $('#t-tax').textContent = m(s * TAX); $('#t-tot').textContent = m(tot);
    var l = $('#t-left'); l.textContent = left < 0 ? '−' + m(-left) : m(left); l.classList.toggle('over', left < 0);
    $('#dm-fill').style.width = Math.min(100, s / MIN * 100) + '%'; $('#dm-fill').classList.toggle('ok', s >= MIN);
    $('#dm-txt').textContent = !keys.length ? 'Evening delivery starts at $25 in food.' : s >= MIN ? 'Clears the $25 minimum for delivery after 4 PM (+$3 delivery charge).' : 'Add ' + m(MIN - s) + ' to reach the $25 delivery minimum, or pick it up.';
    $('#tray').classList.toggle('has', keys.length > 0);
  }
  bd.oninput = function () { shown = SHOW; render(); };
  $('#bd-m').onclick = function () { bd.value = budget() - 1; shown = SHOW; render(); }; $('#bd-p').onclick = function () { bd.value = budget() + 1; shown = SHOW; render(); };
  $$('#chips button').forEach(function (b) { b.onclick = function () { group = +b.getAttribute('data-g'); $$('#chips button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); shown = SHOW; render(); }; });
  $('#more').onclick = function () { shown += SHOW; render(); };
  $('#tiles').onclick = function (e) { var b = e.target.closest('.tile'); if (!b) return; var i = b.getAttribute('data-i'); tray[i] = (tray[i] || 0) + 1; render(); var nb = $('.tile[data-i="' + i + '"]'); if (nb) nb.focus(); };
  $('#t-lines').onclick = function (e) { var b = e.target.closest('button[data-d]'); if (!b) return; var i = b.getAttribute('data-i'); tray[i] = (tray[i] || 0) + (+b.getAttribute('data-d')); if (tray[i] <= 0) delete tray[i]; render(); };
  $('#t-clear').onclick = function () { tray = {}; render(); };
  $('#t-copy').onclick = function () {
    var keys = Object.keys(tray); if (!keys.length) return;
    var t = 'Order for Supreme House of Pizza (603-895-9500):\n' + keys.map(function (k) { return tray[k] + ' x ' + ITEMS[k].n + (ITEMS[k].s ? ' (' + ITEMS[k].s + ')' : '') + ' ' + m(ITEMS[k].p * tray[k]); }).join('\n') + '\nFood ' + m(sub()) + ' + 9% meal tax = ' + m(sub() * (1 + TAX));
    var b = $('#t-copy'); function done() { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy my order'; }, 1800); }
    try { navigator.clipboard.writeText(t).then(done, done); } catch (x) { done(); }
  };
  render();
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
