/* Supreme Exeter: live open/closed, mobile nav, menu tabs + search, and the order tray (estimate, specials check, copy list) */
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

  /* menu tabs + search */
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); t.tabIndex = k === i ? 0 : -1; }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  function showById(id) { panels.forEach(function (p, k) { if (p.getAttribute('data-p') === id) { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(k); var m = $('#menu'); m.scrollIntoView(); } }); }
  tabs.forEach(function (t, i) {
    t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); };
    t.onkeydown = function (e) { var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1; if (n >= 0 && n < tabs.length) { e.preventDefault(); tabs[n].focus(); tabs[n].click(); tabs[n].scrollIntoView({ block: 'nearest', inline: 'nearest' }); } };
  });
  show(0);
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var cur = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(cur < 0 ? 0 : cur); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
  $$('[data-go]').forEach(function (b) { b.onclick = function () { showById(b.getAttribute('data-go')); }; });

  /* tray */
  var lines = [], tray = $('#tray'), fab = $('#fab');
  function money(n) { return '$' + n.toFixed(2); }
  function key(l) { return l.c + '|' + l.n + '|' + l.l; }
  function add(c, n, l, p) { var k = c + '|' + n + '|' + l, f = lines.filter(function (x) { return key(x) === k; })[0]; if (f) f.q++; else lines.push({ c: c, n: n, l: l, p: p, q: 1 }); render(); }
  function dealText(lg) {
    var out = [];
    if (lg >= 4) out.push('You have ' + lg + ' large pizzas, so both free-pizza specials apply: a free large cheese pizza (buy any four large) and a free small cheese pizza (buy any two large). Check how the shop applies them at checkout.');
    else if (lg >= 2) out.push('You have ' + lg + ' large pizzas: the free small cheese pizza special (buy any two large) applies. ' + (4 - lg) + ' more large pizza' + (4 - lg === 1 ? '' : 's') + ' would also unlock a free large cheese pizza.');
    else if (lg === 1) out.push('Add one more large pizza to unlock a free small cheese pizza (buy any two large).');
    return out.join(' ');
  }
  function render() {
    var ul = $('#tray-list'); ul.innerHTML = '';
    var total = 0, count = 0, lg = 0;
    lines.forEach(function (x, i) {
      total += x.p * x.q; count += x.q; if (x.c === 'pizza' && x.l === 'Lg') lg += x.q;
      var li = document.createElement('li');
      li.innerHTML = '<span class="tn"></span><span class="tp"></span><span class="qty"><button type="button" aria-label="One less"></button><output></output><button type="button" aria-label="One more"></button></span>';
      li.querySelector('.tn').innerHTML = ''; var nm = document.createElement('span'); nm.textContent = x.n; li.querySelector('.tn').appendChild(nm);
      if (x.l) { var sm = document.createElement('small'); sm.textContent = x.l; li.querySelector('.tn').appendChild(sm); }
      li.querySelector('.tp').textContent = money(x.p * x.q);
      var bs = li.querySelectorAll('button'); bs[0].textContent = '−'; bs[1].textContent = '+';
      bs[0].setAttribute('aria-label', 'One less ' + x.n + (x.l ? ' ' + x.l : '')); bs[1].setAttribute('aria-label', 'One more ' + x.n + (x.l ? ' ' + x.l : ''));
      li.querySelector('output').textContent = x.q;
      bs[0].onclick = function () { x.q--; if (x.q <= 0) lines.splice(i, 1); render(); };
      bs[1].onclick = function () { x.q++; render(); };
      ul.appendChild(li);
    });
    var has = lines.length > 0;
    $('#tray-empty').hidden = has; $('#tray-sum').hidden = !has; $('#tray-act').hidden = !has;
    $('#t-total').textContent = money(total); $('#t-count').textContent = count + (count === 1 ? ' item' : ' items') + ', before tax and fees';
    var dt = dealText(lg); $('#t-deals').hidden = !dt; $('#t-deals-txt').textContent = dt;
    var pts = Math.floor(total), tue = ny().dow === 2, pe = $('#t-pts'); pe.hidden = !has;
    pe.textContent = 'If you order through the shop\'s rewards program ($1 = 1 point): about ' + (tue ? pts * 2 + ' points today (double points Tuesday)' : pts + ' points. Tuesdays earn double') + '. 100 points is $5 off.';
    fab.hidden = !has; $('#fab-n').textContent = count; $('#fab-t').textContent = money(total);
    if (!has) closeTray(false);
  }
  function openTray() { tray.classList.add('open'); fab.setAttribute('aria-expanded', 'true'); $('#tray-x').focus(); }
  function closeTray(back) { tray.classList.remove('open'); fab.setAttribute('aria-expanded', 'false'); if (back) fab.focus(); }
  fab.onclick = function () { tray.classList.contains('open') ? closeTray(true) : openTray(); };
  $('#tray-x').onclick = function () { closeTray(true); };
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { if (tray.classList.contains('open')) closeTray(true); else if (nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); } }
  });
  $$('.chip').forEach(function (b) { b.onclick = function () { add(b.getAttribute('data-c'), b.getAttribute('data-n'), b.getAttribute('data-l'), +b.getAttribute('data-p')); b.classList.add('pop'); setTimeout(function () { b.classList.remove('pop'); }, 350); }; });
  $('#t-clear').onclick = function () { lines = []; render(); };
  $('#t-copy').onclick = function () {
    var total = 0, t = 'My order for Supreme House of Pizza, Exeter (603-778-8304):\n';
    lines.forEach(function (x) { total += x.p * x.q; t += x.q + ' x ' + x.n + (x.l ? ' (' + x.l + ')' : '') + ' ' + money(x.p * x.q) + '\n'; });
    t += 'Estimated subtotal ' + money(total) + ' before tax. Check prices when ordering.';
    var b = $('#t-copy'), done = function (ok) { b.textContent = ok ? 'Copied' : 'Copy not available'; setTimeout(function () { b.textContent = 'Copy my list'; }, 2200); };
    function fallback() { var ta = document.createElement('textarea'); ta.value = t; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;left:-999px'; document.body.appendChild(ta); ta.select(); var ok = false; try { ok = document.execCommand('copy'); } catch (e) {} document.body.removeChild(ta); done(ok); }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(function () { done(true); }, fallback); else fallback();
  };
  render();
})();
