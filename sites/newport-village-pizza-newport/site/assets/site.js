/* Newport: status, nav, Pie Math planner, menu tabs + search */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var H = window.__HOURS__ || [], DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function tm(s) { var a = s.split(':'); return +a[0] * 60 + +a[1]; }
  function f12(m) { m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  var shifts = []; H.forEach(function (r) { var o = tm(r.open), c = tm(r.close); if (c <= o) c += 1440; r.dow.forEach(function (d) { shifts.push({ d: d, o: o, c: c }); }); });
  function ny() {
    var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
    p.forEach(function (x) { o[x.type] = x.value; });
    return { dow: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: (+o.hour % 24) * 60 + +o.minute };
  }
  function openOn(d, t) { return shifts.some(function (s) { return s.d === d && t >= s.o && t < s.c; }); }
  function shiftOn(d) { return shifts.filter(function (s) { return s.d === d; })[0]; }
  function status() {
    var n = ny(), cur = null;
    if (openOn(n.dow, n.min)) cur = shiftOn(n.dow); else if (openOn((n.dow + 6) % 7, n.min + 1440)) cur = shiftOn((n.dow + 6) % 7);
    if (cur) { var left = cur.c - (openOn(n.dow, n.min) ? n.min : n.min + 1440); return { open: true, text: 'Open now · until ' + f12(cur.c) + (left <= 90 ? ' (' + left + ' min left)' : '') }; }
    for (var i = 0; i < 8; i++) { var d = (n.dow + i) % 7, s = shiftOn(d); if (s && (i > 0 || s.o > n.min)) return { open: false, text: 'Closed · opens ' + (i === 0 ? 'today' : i === 1 ? 'tomorrow' : DAYS[d]) + ' at ' + f12(s.o) }; }
    return { open: false, text: 'Closed' };
  }
  var st = status(); document.documentElement.classList.toggle('is-open', st.open);
  $$('[data-status]').forEach(function (e) { e.textContent = st.text; });
  var wk = ny().dow, ts = shiftOn(wk); $$('[data-today]').forEach(function (e) { e.textContent = ts ? f12(ts.o) + ' – ' + f12(ts.c) : 'Closed today'; });
  $$('.hours tr').forEach(function (r) { if (+r.getAttribute('data-dow') === wk) r.classList.add('today'); });
  var rb = $('[data-ribbon-x]'); if (rb) rb.onclick = function () { $('.ribbon').hidden = true; };

  var bg = $('.burger'), nav = $('#nav');
  bg.onclick = function () { var o = nav.classList.toggle('open'); bg.setAttribute('aria-expanded', o); };
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); } });


  /* ---- Pie Math planner ---- */
  var PL = window.__PLAN__, state = { qty: 1, lines: [] };
  var styleEl = $('#pm-style'), sizeEl = $('#pm-size');
  function val(name) { var e = document.querySelector('input[name=' + name + ']:checked'); return e ? e.value : null; }
  function money(n) { return '$' + (n % 1 ? n.toFixed(2) : n); }
  function range(a, b) { return a === b ? money(a) : money(a) + ' – ' + money(b); }
  function tbl() { var s = val('style'); return s === 'white' ? PL.sizes.white : s.indexOf('gourmet') === 0 ? PL.sizes.gourmet : PL.sizes.cheese; }
  function tops() { return $$('input[name=top]:checked').map(function (e) { return e.value; }); }
  function drawSizes() {
    var t = tbl(), keep = val('size'), keys = Object.keys(t); if (keys.indexOf(keep) < 0) keep = keys.indexOf('Small') > -1 ? 'Small' : keys[0];
    sizeEl.innerHTML = ''; keys.forEach(function (k) { var l = document.createElement('label'), i = document.createElement('input'), s = document.createElement('span'); i.type = 'radio'; i.name = 'size'; i.value = k; i.checked = k === keep; s.textContent = k + ' ' + money(t[k]); l.appendChild(i); l.appendChild(s); sizeEl.appendChild(l); });
  }
  function syncForm() {
    var s = val('style'), gour = s.indexOf('gourmet') === 0, can = s.indexOf('cheese') === 0;
    $('#pm-gwrap').hidden = !gour; $('#pm-gd').textContent = gour ? PL.gourmet_desc[$('#pm-g').value] : '';
    $$('input[name=top]').forEach(function (e) { e.disabled = !can; if (!can) e.checked = false; });
    $('#pm-hint').textContent = can ? 'Each topping is $1 to $2 on the shop’s menu, so the tape shows a range.' : (s === 'white' ? 'The white pie comes as listed: garlic oil, ricotta and the shop’s cheese blend.' : 'Gourmet pies come as listed on the menu, so toppings are for cheese pizzas and calzones.');
    var n = tops().length; $('#pm-tcount').textContent = n ? n + ' selected' : 'none';
  }
  function current() {
    var s = val('style'), size = val('size'), t = tbl(), crust = val('crust'), tp = can_tops() ? tops() : [], base = t[size] + (crust !== '0' ? PL.crust_up : 0), q = state.qty;
    var name = s === 'white' ? 'White pie' : s === 'cheese-pizza' ? 'Cheese pizza' : s === 'cheese-calzone' ? 'Cheese calzone' : $('#pm-g').value + (s === 'gourmet-calzone' ? ' calzone' : ' pizza');
    var det = size + (crust === 'gf' ? ', gluten-free' : crust === 'cf' ? ', cauliflower crust' : '') + (tp.length ? ', ' + tp.join(', ') : '');
    return { name: name, det: det, qty: q, lo: (base + tp.length * PL.top_lo) * q, hi: (base + tp.length * PL.top_hi) * q, tops: tp.length };
  }
  function can_tops() { return val('style').indexOf('cheese') === 0; }
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }
  function draw() {
    var ul = $('#tape-lines'); ul.innerHTML = '';
    if (!state.lines.length) { ul.appendChild(el('li', 'empty', 'Nothing on the tape yet.')); }
    var lo = 0, hi = 0, anyRange = false;
    state.lines.forEach(function (L, i) {
      lo += L.lo; hi += L.hi; if (L.lo !== L.hi) anyRange = true;
      var li = el('li'); li.appendChild(el('span', 'l', L.qty + ' x ' + L.name)); li.appendChild(el('span', 'r', range(L.lo, L.hi))); li.appendChild(el('span', 's', L.det));
      var x = el('button', 'x', 'remove'); x.type = 'button'; x.setAttribute('aria-label', 'Remove ' + L.name + ' from the tape'); x.onclick = function () { state.lines.splice(i, 1); draw(); }; li.appendChild(x); ul.appendChild(li);
    });
    $('#tape-total').textContent = range(lo, hi); $('#tape-note').textContent = anyRange ? 'Toppings are $1 to $2 each, so the total is a range. The shop confirms the final price.' : '';
    state.lo = lo; state.hi = hi;
  }
  function onChange(e) {
    if (e && e.target && e.target.name === 'style') drawSizes();
    syncForm();
  }
  $('#pm-form').addEventListener('change', onChange);
  $('#pm-g').addEventListener('change', syncForm);
  $('#pm-plus').onclick = function () { state.qty = Math.min(20, state.qty + 1); $('#pm-qty').textContent = state.qty; };
  $('#pm-minus').onclick = function () { state.qty = Math.max(1, state.qty - 1); $('#pm-qty').textContent = state.qty; };
  $('#pm-add').onclick = function () { state.lines.push(current()); draw(); $('#tape-msg').textContent = 'Added. Keep building, or copy the list and call.'; };
  $('#tape-feast').onclick = function () { state.lines.push({ name: 'Game Day Feast', det: 'Large cheese pizza, mozzarella sticks, bread sticks, 2 liter soda. Sunday only.', qty: 1, lo: PL.feast.price, hi: PL.feast.price }); draw(); $('#tape-msg').textContent = 'The Feast is Sunday only. Call to confirm it is available.'; };
  $('#tape-clear').onclick = function () { state.lines = []; draw(); $('#tape-msg').textContent = 'Tape cleared.'; };
  $('#tape-copy').onclick = function () {
    if (!state.lines.length) { $('#tape-msg').textContent = 'Add something to the tape first.'; return; }
    var t = 'Newport Village Pizza order (estimate)\n' + state.lines.map(function (L) { return L.qty + ' x ' + L.name + ' (' + L.det + ') ' + range(L.lo, L.hi); }).join('\n') + '\nEstimated total: ' + range(state.lo, state.hi) + ' before tax and extras';
    function ok() { $('#tape-msg').textContent = 'Copied. Paste it into a text, or read it out when you call (603) 863-2900.'; }
    function fail() { $('#tape-msg').textContent = t.replace(/\n/g, ' | '); }
    try { navigator.clipboard.writeText(t).then(ok, fail); } catch (e) { fail(); }
  };
  drawSizes(); syncForm(); draw();

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
