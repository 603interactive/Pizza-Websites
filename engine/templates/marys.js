/* Mary's Pizza: live status with split lunch/dinner shifts, today's deal, menu tabs + search, pizza price builder, mobile nav */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var H = window.__HOURS__ || [], DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function tm(s) { var a = s.split(':'); return +a[0] * 60 + +a[1]; }
  function f12(m) { var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  var shifts = []; H.forEach(function (r) { r.dow.forEach(function (d) { shifts.push({ d: d, o: tm(r.open), c: tm(r.close) }); }); });
  shifts.sort(function (a, b) { return a.d - b.d || a.o - b.o; });
  function ny() {
    var o = {}; new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()).forEach(function (x) { o[x.type] = x.value; });
    return { dow: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: (+o.hour % 24) * 60 + +o.minute };
  }
  function status(n) {
    var cur = shifts.filter(function (s) { return s.d === n.dow && n.min >= s.o && n.min < s.c; })[0];
    if (cur) { var left = cur.c - n.min; return { open: true, text: 'Open now · until ' + f12(cur.c) + (left <= 60 ? ' (' + left + ' min left)' : '') }; }
    for (var i = 0; i < 8; i++) {
      var d = (n.dow + i) % 7, nx = shifts.filter(function (s) { return s.d === d && (i > 0 || s.o > n.min); })[0];
      if (nx) return { open: false, text: 'Closed · opens ' + (i === 0 ? 'today' : i === 1 ? 'tomorrow' : DAYS[d]) + ' at ' + f12(nx.o) };
    }
    return { open: false, text: 'Closed' };
  }
  var now = ny(), st = status(now); document.documentElement.classList.toggle('is-open', st.open);
  $$('[data-status]').forEach(function (e) { e.textContent = st.text; });
  $$('.hours tr').forEach(function (r) { if (+r.getAttribute('data-dow') === now.dow) r.classList.add('tnow'); });
  var rb = $('[data-ribbon-x]'); if (rb) rb.onclick = function () { $('.ribbon').hidden = true; };

  // today's deal
  (function () {
    var d = now.dow, big, sub;
    if (d === 0) { big = 'Closed Sundays'; sub = 'We open again Monday at 11 AM. Everyday Lunch Special: 1 Large Cheese Pizza, $10.'; }
    else if (d === 2) { big = 'Tuesday: Large 1-Topping Pizza, 4 Breadsticks & a 2 liter of Soda, $19.99'; sub = 'Plus the Everyday Lunch Special: 1 Large Cheese Pizza, $10.00.'; }
    else if (d === 4) { big = 'Thursday: 2 Large 3-Topping Pizzas, $32.99'; sub = 'Plus the Everyday Lunch Special: 1 Large Cheese Pizza, $10.00.'; }
    else { big = 'Everyday Lunch Special: 1 Large Cheese Pizza, $10.00'; sub = 'Tuesdays: pizza, breadsticks and soda for $19.99. Thursdays: 2 large 3-topping pizzas for $32.99.'; }
    $('#t-lab').textContent = DAYS[d]; $('#t-big').textContent = big; $('#t-sub').textContent = sub;
    $$('.dcards li').forEach(function (li) { var k = li.getAttribute('data-d'); if ((k === 'all' && d !== 0) || +k === d) li.classList.add('on'); });
  })();

  // mobile nav
  var bg = $('.burger'), nav = $('#nav');
  bg.onclick = function () { var o = nav.classList.toggle('open'); bg.setAttribute('aria-expanded', o); };
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); } });

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

  // pizza builder
  var C = window.__CALC__, form = $('#bld');
  if (C && form) {
    var val = function (n) { return form.querySelector('input[name=' + n + ']:checked').value; };
    var money = function (x) { return '$' + x.toFixed(2); };
    function calc() {
      var size = val('size'), crust = val('crust'), tops = $$('input[name=top]:checked').length;
      var gfOff = crust === 'gf' && size === 'L';
      $$('input[name=size]').forEach(function (r) { if (r.value === 'L') { r.disabled = false; } });
      var note = $('#crust-note');
      if (crust === 'gf') { note.textContent = 'Gluten-free is available in small only.'; if (size === 'L') { form.querySelector('input[name=size][value=S]').checked = true; size = 'S'; } $$('input[name=size][value=L]').forEach(function (r) { r.disabled = true; }); }
      else note.textContent = crust === 'pan' ? 'Pan is the thick crust.' : crust === 'thin' ? 'Thin is the crispy crust, cooked on a screen for a soft center.' : 'Regular is the original crust, cooked on a screen for a soft center.';
      var pan = crust === 'pan' || crust === 'gf', key = (pan ? 'P' : '') + size, rows = C[key], n = Math.min(tops, 4);
      var p = rows[n] + (tops > 4 ? (tops - 4) * C.add[size] : 0);
      var ex = []; if ($('#x-cheese').checked) { p += C.cheese[size]; ex.push('extra cheese'); } if ($('#x-sauce').checked) { p += C.sauce[size]; ex.push('extra sauce'); }
      $('#b-cnt').textContent = tops + ' chosen';
      var names = $$('input[name=top]:checked').map(function (c) { return c.value.toLowerCase(); });
      $('#tk-d').textContent = (size === 'S' ? 'Small' : 'Large') + ' ' + { reg: 'regular', thin: 'thin', pan: 'pan', gf: 'gluten-free' }[crust] + ' crust, ' + (tops ? names.join(', ') : 'cheese only') + (ex.length ? ', ' + ex.join(' and ') : '') + '.';
      $('#tk-p').textContent = money(p);
    }
    form.addEventListener('change', calc);
    $('#x-cheese').addEventListener('change', calc); $('#x-sauce').addEventListener('change', calc); calc();
  }
})();
