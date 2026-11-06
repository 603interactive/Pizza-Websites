/* THOP: open/closed status, mobile nav, menu tabs + search, guest-check builder */
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
    if (cur) return { open: true, text: 'Open now · until ' + f12(cur.c) };
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
    $$('.m-sec').forEach(function (s) { s.hidden = !s.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };

  /* guest check */
  var lines = [], list = $('#ck-lines'), box = $('#check'), dock = $('#dock-check');
  function money(n) { return '$' + n.toFixed(2); }
  function total() { return lines.reduce(function (s, l) { return s + Math.round(l.p * 100) * l.q; }, 0) / 100; }
  function count() { return lines.reduce(function (s, l) { return s + l.q; }, 0); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
  function render() {
    list.innerHTML = lines.map(function (l, i) {
      return '<li><span class="nm">' + esc(l.n) + (l.l ? '<small>' + esc(l.l) + ' · ' + money(l.p) + ' each</small>' : '<small>' + money(l.p) + ' each</small>') + '</span><span class="pr">' + money(Math.round(l.p * 100) * l.q / 100) + '</span>' +
        '<span class="q"><button type="button" data-i="' + i + '" data-d="-1" aria-label="One less ' + esc(l.n) + '">−</button><output aria-label="Quantity">' + l.q + '</output><button type="button" data-i="' + i + '" data-d="1" aria-label="One more ' + esc(l.n) + '">+</button></span></li>';
    }).join('');
    $('#ck-empty').hidden = lines.length > 0; $('#ck-total').textContent = money(total());
    var n = count(); $('#dock-n').textContent = n ? 'Your check (' + n + ')' : 'Your check'; $('#dock-t').textContent = money(total());
  }
  $$('.add').forEach(function (b) {
    b.onclick = function () {
      var n = b.dataset.n, l = b.dataset.l, p = parseFloat(b.dataset.p), f = lines.filter(function (x) { return x.n === n && x.l === l && x.p === p; })[0];
      if (f) f.q++; else lines.push({ n: n, l: l, p: p, q: 1 });
      render(); b.classList.remove('bump'); void b.offsetWidth; b.classList.add('bump');
    };
  });
  list.onclick = function (e) {
    var b = e.target.closest('button'); if (!b) return; var i = +b.dataset.i; lines[i].q += +b.dataset.d; if (lines[i].q < 1) lines.splice(i, 1);
    render(); var nb = list.querySelector('button[data-i="' + i + '"][data-d="' + b.dataset.d + '"]') || list.querySelector('button'); if (nb) nb.focus(); else dock.focus();
  };
  $('#ck-clear').onclick = function () { lines = []; $('#ck-notes').value = ''; render(); $('#ck-copy').textContent = 'Copy my check'; };
  function slip() {
    var t = ['Tilton House of Pizza - call-in order', ''];
    lines.forEach(function (l) { t.push(l.q + ' x ' + l.n + (l.l ? ', ' + l.l : '') + ' - ' + money(Math.round(l.p * 100) * l.q / 100)); });
    t.push('', 'Estimated subtotal (before tax): ' + money(total())); var nt = $('#ck-notes').value.trim(); if (nt) t.push('Notes: ' + nt);
    return t.join('\n');
  }
  $('#ck-copy').onclick = function () {
    var btn = this, txt = slip(), done = function (ok) { btn.textContent = ok ? 'Copied. Now call us' : 'Select and copy from the notes box'; if (!ok) { $('#ck-notes').value = txt; } };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () { done(true); }, function () { done(false); }); else done(false);
  };
  function setOpen(o) { box.classList.toggle('open', o); dock.setAttribute('aria-expanded', o); if (o) $('#ck-close').focus(); else dock.focus(); }
  dock.onclick = function () { setOpen(!box.classList.contains('open')); };
  $('#ck-close').onclick = function () { setOpen(false); };
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (box.classList.contains('open')) setOpen(false); else if (nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); }
  });
  render();
})();
