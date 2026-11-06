/* ALTON: live open/closed status, mobile nav, menu tabs + search */
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

  /* Pizza Price Check: build-your-own vs. specialty math, from the shop's menu prices */
  var C = window.__CALC__, form = $('#pc');
  function m(n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); }
  function sz() { return +form.elements.size.value; }
  function picks() { return $$('#pc input[name=top]:checked').map(function (i) { return i.value; }); }
  function extras(s) { var x = 0; if (form.elements.xc.checked) x += C.xcheese[s]; if (form.elements.xs.checked) x += C.xsauce[s]; if (form.elements.gf.checked) x += C.gf; return x; }
  function build(n, s) { return C.cheese[s] + n * C.top[s]; }
  var last = '';
  function calc() {
    var s = sz(), p = picks(), n = p.length, ex = extras(s), tot = build(n, s) + ex, lines = [];
    lines.push([(s ? 'Large' : 'Small') + ' cheese pizza', C.cheese[s]]);
    if (n) lines.push([n + (n === 1 ? ' topping' : ' toppings') + ' at ' + m(C.top[s]), n * C.top[s]]);
    if (form.elements.xc.checked) lines.push(['Extra cheese', C.xcheese[s]]);
    if (form.elements.xs.checked) lines.push(['Extra sauce', C.xsauce[s]]);
    if (form.elements.gf.checked) lines.push(['Gluten free option', C.gf]);
    $('#pc-total').textContent = m(tot);
    $('#pc-n').textContent = n ? n + ' picked: ' + p.join(', ') : 'none picked';
    $('#pc-lines').innerHTML = lines.map(function (l) { return '<li><span>' + l[0] + '</span><b>' + m(l[1]) + '</b></li>'; }).join('');
    var tip = $('#pc-tip'), msg = '', best = null;
    var vs = C.veg.set.every(function (t) { return p.indexOf(t) > -1; });
    if (vs) { var a = C.veg.price[s] + (n - C.veg.set.length) * C.top[s] + ex; if (a < tot) best = { n: C.veg.name, a: a, why: 'It already includes all six of those toppings.' }; }
    if (n >= C.village.count) { var b = C.village.price[s] + (n - C.village.count) * C.top[s] + ex; if (b < tot && (!best || b < best.a)) best = { n: C.village.name, a: b, why: 'It is a set mix of 8 popular toppings chosen by the shop, so ask what is on it before you swap.' }; }
    if (best) msg = 'Cheaper way in: the ' + best.n + ' with the same extras comes to ' + m(best.a) + ', saving ' + m(tot - best.a) + '. ' + best.why;
    else if (n) msg = 'Building it is the better price for this combination.';
    tip.hidden = !msg; tip.textContent = msg;
    last = lines.map(function (l) { return l[0]; }).join(', ') + (n ? '. Toppings: ' + p.join(', ') : '') + '. Menu total ' + m(tot) + ' before tax.';
  }
  form.addEventListener('change', calc);
  $('#pc-clear').onclick = function () { form.reset(); calc(); };
  $('#pc-copy').onclick = function () {
    var b = $('#pc-copy'), done = function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy my pizza'; }, 1800); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(last).then(done, done); else done();
  };
  var rows = [[C.village, C.village.count], [C.veg, C.veg.set.length]].map(function (r) {
    var o = r[0], k = r[1], c = [0, 1].map(function (s) { return '<td><b>' + m(o.price[s]) + '</b><small>built: ' + m(build(k, s)) + ' (saves ' + m(build(k, s) - o.price[s]) + ')</small></td>'; }).join('');
    return '<tr><th scope="row">' + o.name + '<small>' + k + ' toppings</small></th>' + c + '</tr>';
  }).join('');
  $('#pc-rows').innerHTML = rows; calc();
})();
