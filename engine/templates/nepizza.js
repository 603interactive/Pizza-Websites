/* NE Pizza: live open/closed status, mobile nav, menu tabs + search */
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


  var KEY = {
    chicken: /chicken/, beef: /steak|beef|burger|meatball|gyro|pastrami|veal/,
    pork: /\bham\b|bacon|sausage|salami|pepperoni|capicola|mortadella|genoa/, sea: /tuna|seafood|crabmeat|haddock/,
    veg: /broccoli|spinach|mushroom|peppers|eggplant|artichoke|tomato|olive|onion|lettuce|garden|salad greens/, feta: /feta|greek|gyro|tzatziki|kalamata/, sauce: /buffalo|bbq/
  };
  var MEAT = new RegExp([KEY.chicken, KEY.beef, KEY.pork, KEY.sea].map(function (r) { return r.source; }).join('|') + '|wings|fingers|meat');
  var items = $$('.m-it'), secs = $$('.m-sec'), chips = $$('#chips button'), q = $('#m-q'), px = $('#m-px'), lists = $('#lists'), clr = $('#m-clear');
  var on = {};
  function apply() {
    var v = q.value.trim().toLowerCase(), keys = Object.keys(on).filter(function (k) { return on[k]; }), c = 0;
    items.forEach(function (e) {
      var t = e.getAttribute('data-t'), sec = e.closest('.m-sec').getAttribute('data-c'), ok = !v || t.indexOf(v) > -1;
      keys.forEach(function (k) { if (!ok) return; if (k === 'nomeat') ok = sec !== 'drinks' && sec !== 'sides' && !MEAT.test(t); else ok = KEY[k].test(t); });
      e.hidden = !ok; if (ok) c++;
    });
    var shown = 0;
    secs.forEach(function (s) { var any = !!s.querySelector('.m-it:not([hidden])'); s.hidden = !any; if (any) shown++; var a = $('#rail a[data-s="' + s.getAttribute('data-c') + '"]'); a.classList.toggle('gone', !any); });
    var filtering = !!v || keys.length > 0;
    $('#m-count').textContent = filtering ? c + (c === 1 ? ' item matches' : ' items match') + ' in ' + shown + (shown === 1 ? ' section' : ' sections') : items.length + ' items across ' + secs.length + ' sections';
    $('#m-none').hidden = c > 0; clr.hidden = !filtering; $('#f-nm').hidden = !on.nomeat;
  }
  chips.forEach(function (b) { b.onclick = function () { var k = b.getAttribute('data-k'); on[k] = !on[k]; b.setAttribute('aria-pressed', on[k] ? 'true' : 'false'); apply(); }; });
  q.oninput = apply;
  clr.onclick = function () { on = {}; q.value = ''; chips.forEach(function (b) { b.setAttribute('aria-pressed', 'false'); }); apply(); q.focus(); };
  px.onchange = function () { lists.classList.toggle('nopx', !px.checked); };
  var links = $$('#rail a');
  function spy() { var cur = null; secs.forEach(function (s) { if (!s.hidden && s.getBoundingClientRect().top < 180) cur = s.getAttribute('data-c'); }); links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('data-s') === cur); }); }
  window.addEventListener('scroll', spy, { passive: true }); spy();
})();
