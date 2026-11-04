/* Brookside Pizza II: Day Dial (slices / kitchen / bar by hour), menu tabs + search, today highlight */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var H = window.__HOURS__ || [], B = window.__BRK__ || {}, NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function tm(s) { var a = s.split(':'); return (+a[0] || 24 * (a[0] === '24')) * 60 + +a[1]; }
  function f12(m) { m = m % 1440; var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  function dur(m) { var h = Math.floor(m / 60), mm = m % 60; return (h ? h + ' hr ' : '') + (mm ? mm + ' min' : (h ? '' : '0 min')); }
  var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
  p.forEach(function (x) { o[x.type] = x.value; });
  var today = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], nowMin = (+o.hour % 24) * 60 + +o.minute;
  function kitchen(d) { for (var i = 0; i < H.length; i++) if (H[i].dow.indexOf(d) > -1) return [tm(H[i].open), tm(H[i].close)]; return null; }
  var SL = tm(B.slices_until || '15:00'), BARC = 1440, A0 = 10 * 60, A1 = 24 * 60, SPAN = A1 - A0;
  var k0 = kitchen(today), kopen = k0 && nowMin >= k0[0] && nowMin < k0[1];
  document.documentElement.classList.toggle('is-open', !!kopen);
  var st = kopen ? 'Kitchen open now · until ' + f12(k0[1]) : 'Kitchen closed' + (k0 && nowMin < k0[0] ? ' · opens today at ' + f12(k0[0]) : '');
  $$('[data-status]').forEach(function (e) { e.textContent = st + (nowMin >= k0[0] && nowMin < BARC ? ' · bar until midnight' : ''); });
  /* axis */
  var ax = $('.axis'); if (ax) for (var h = 10; h <= 24; h += 1) { var s = document.createElement('span'); s.style.left = ((h * 60 - A0) / SPAN * 100) + '%'; s.textContent = h === 24 ? '12 AM' : f12(h * 60).replace(':00', ''); if (h % 2) s.className = 'mb'; ax.appendChild(s); }
  function pct(m) { return Math.max(0, Math.min(100, (m - A0) / SPAN * 100)); }
  function setBar(lane, a, b, txt) {
    var l = $('[data-lane=' + lane + ']'), bar = l.querySelector('.bar'); l.classList.toggle('off', a == null);
    if (a != null) { bar.style.left = pct(a) + '%'; bar.style.width = (pct(b) - pct(a)) + '%'; }
    l.querySelector('[data-t]').textContent = txt;
  }
  var sel = today, days = $$('#days button');
  function render(d) {
    sel = d; days.forEach(function (b) { b.setAttribute('aria-pressed', +b.getAttribute('data-d') === d ? 'true' : 'false'); });
    var k = kitchen(d);
    if (k) {
      setBar('slices', k[0], Math.min(SL, k[1]), f12(k[0]) + ' – ' + f12(SL));
      setBar('kitchen', k[0], k[1], f12(k[0]) + ' – ' + f12(k[1]));
      setBar('bar', k[0] - 60 < A0 ? A0 : k[0] - 60, BARC, 'Opening time not published · until midnight');
    } else { ['slices', 'kitchen', 'bar'].forEach(function (n) { setBar(n, null, null, 'Closed'); }); }
    var nl = $('#nowline'), tr = $('.track'), dial = $('#dial');
    if (d === today && nowMin >= A0 && nowMin <= A1) {
      nl.hidden = false; var tw = tr.getBoundingClientRect(), dw = dial.getBoundingClientRect();
      nl.style.left = (tw.left - dw.left + tw.width * pct(nowMin) / 100) + 'px';
    } else nl.hidden = true;
    var msg;
    if (d !== today) {
      msg = NAMES[d] + ': kitchen ' + (k ? f12(k[0]) + ' to ' + f12(k[1]) : 'closed') + ', slices until ' + f12(SL) + ', bar until midnight.';
    } else if (!k) msg = 'Closed today.';
    else if (nowMin < k[0]) msg = 'Not open yet. Kitchen and slices start at ' + f12(k[0]) + '.';
    else {
      var parts = [];
      parts.push(nowMin < SL ? 'Slices for ' + dur(SL - nowMin) + ' more' : 'slices are done for today');
      parts.push(nowMin < k[1] ? 'kitchen open ' + dur(k[1] - nowMin) + ' more (till ' + f12(k[1]) + ')' : 'kitchen is closed');
      parts.push(nowMin < BARC ? 'the Tap is open until midnight' : 'the bar is closed');
      msg = 'Right now: ' + parts.join(' · ') + '.'; msg = msg.charAt(0).toUpperCase() + msg.slice(1);
    }
    $('#now').textContent = msg;
  }
  days.forEach(function (b) { b.onclick = function () { render(+b.getAttribute('data-d')); }; });
  if (days.length) { render(today); window.addEventListener('resize', function () { render(sel); }); }
  /* menu */
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); panels.forEach(function (x, k) { x.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; }
  tabs.forEach(function (t, i) { t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); }; });
  tabs.forEach(function (b, i) { b.onkeydown = function (e) { var n = e.key === 'ArrowDown' || e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowUp' || e.key === 'ArrowLeft' ? i - 1 : -1; if (n >= 0 && n < tabs.length) { e.preventDefault(); tabs[n].focus(); tabs[n].click(); } }; });
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var cur = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(cur < 0 ? 0 : cur); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    panels.forEach(function (x) { x.hidden = !x.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
  $$('.hours tr').forEach(function (r) { if (+r.getAttribute('data-dow') === today) r.classList.add('today'); });
})();
