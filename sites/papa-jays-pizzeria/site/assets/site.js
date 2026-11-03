/* shared: live open/closed in America/New_York, reveal-on-scroll, ribbon dismiss */
(function () {
  var H = window.__HOURS__ || [];
  function nyNow() {
    var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
    p.forEach(function (x) { o[x.type] = x.value; });
    return { dow: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: (+o.hour % 24) * 60 + +o.minute };
  }
  function tm(s) { var a = s.split(':'); return +a[0] * 60 + +a[1]; }
  function f12(m) { var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ' ' + ap; }
  var NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function status() {
    var n = nyNow(), cur = null;
    H.forEach(function (r) { if (r.dow.indexOf(n.dow) > -1 && n.min >= tm(r.open) && n.min < tm(r.close)) cur = r; });
    if (cur) return { open: true, text: 'Open now · until ' + f12(tm(cur.close)) };
    for (var i = 0; i < 8; i++) {
      var d = (n.dow + i) % 7;
      for (var k = 0; k < H.length; k++) {
        var r = H[k];
        if (r.dow.indexOf(d) > -1 && (i > 0 || tm(r.open) > n.min)) return { open: false, text: 'Closed · opens ' + (i === 0 ? 'today' : i === 1 ? 'tomorrow' : NAMES[d]) + ' at ' + f12(tm(r.open)) };
      }
    }
    return { open: false, text: 'Closed' };
  }
  var s = status();
  document.documentElement.classList.toggle('is-open', s.open);
  [].forEach.call(document.querySelectorAll('[data-status]'), function (e) { e.textContent = s.text; });
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .12 }) : null;
  [].forEach.call(document.querySelectorAll('.rv'), function (e) { io ? io.observe(e) : e.classList.add('in'); });
  var rb = document.querySelector('[data-ribbon-x]');
  if (rb) rb.addEventListener('click', function () { document.querySelector('.ribbon').hidden = true; });
})();

/* Papa Jay's: Crowd Planner (cheapest pizza mix for N people), menu tracks + search */
(function () {
  var $ = function (s) { return document.querySelector(s); }, SZ = window.__SZ || [], SP = window.__SPECS || [];
  var money = function (n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); };
  var SLICE = Math.PI * 49 / 8;
  var nI = $('#cp-n'), rI = $('#cp-r'), hI = $('#cp-h'), kI = $('#cp-k');
  function sizesFor(k) {
    if (k === 'cheese') return SZ.map(function (s) { return { n: s.n, d: s.d, p: s.price }; });
    var sp = SP[+k]; return [{ n: 'Medium 12"', d: 12, p: sp.M }, { n: 'Large', d: 14, p: sp.L }, { n: 'Extra large', d: 16, p: sp.X }];
  }
  function plan(need, sizes) {
    var best = [0], pick = [-1], i, c;
    for (c = 1; c <= need; c++) {
      var b = Infinity, bp = -1;
      sizes.forEach(function (s, j) { var prev = best[Math.max(0, c - s.a)], v = s.p + prev + 1e-4; if (v < b) { b = v; bp = j; } });
      best[c] = b; pick[c] = bp;
    }
    var counts = sizes.map(function () { return 0; }); c = need;
    while (c > 0) { counts[pick[c]]++; c = Math.max(0, c - sizes[pick[c]].a); }
    return counts;
  }
  function calc() {
    var n = Math.max(1, Math.min(150, Math.floor(+nI.value) || 1)), per = +hI.value, k = kI.value, name = k === 'cheese' ? 'cheese' : SP[+k].name;
    var sizes = sizesFor(k).map(function (s) { s.a = Math.round(Math.PI * s.d * s.d / 4); return s; });
    var need = Math.ceil(n * per * SLICE), counts = plan(need, sizes), tot = 0, area = 0, pies = 0, lines = '', txt = [];
    sizes.forEach(function (s, j) { if (!counts[j]) return; var t = counts[j] * s.p; tot += t; area += counts[j] * s.a; pies += counts[j]; lines += '<li><span><b>' + counts[j] + ' ×</b> ' + s.n + ' ' + name + '</span><i>' + money(t) + '</i></li>'; txt.push(counts[j] + ' x ' + s.n + ' ' + name + ' (' + money(t) + ')'); });
    $('#cp-lines').innerHTML = lines; $('#cp-total').textContent = money(tot); $('#cp-pp').textContent = money(tot / n);
    var feeds = Math.floor(area / (per * SLICE)); $('#cp-feeds').textContent = pies + (pies === 1 ? ' pizza' : ' pizzas') + ' · feeds about ' + feeds;
    var lg = sizes[1], lgn = Math.ceil(need / lg.a), lgt = lgn * lg.p, v = $('#cp-vs');
    if (lgt - tot > 0.005) v.textContent = 'Cheaper than ordering all large: ' + lgn + ' large ' + name + ' would be ' + money(lgt) + '. You keep ' + money(lgt - tot) + '.';
    else v.textContent = 'All large pizzas is already the best deal for this crowd.';
    $('#cp-mail').href = 'mailto:' + window.__EMAIL + '?subject=' + encodeURIComponent('Pizza order for ' + n + ' people') + '&body=' + encodeURIComponent('Hi Jay,\n\nI would like to order for ' + n + ' people (' + per + ' slices each):\n' + txt.join('\n') + '\nTotal before tax: ' + money(tot) + '\n\nPickup or delivery? Date and time:\n');
  }
  function sync(from) { var n = Math.max(1, Math.min(150, Math.floor(+nI.value) || 1)); if (from === 'r') nI.value = rI.value; else rI.value = Math.min(60, n); calc(); }
  nI.addEventListener('input', function () { sync('n'); }); rI.addEventListener('input', function () { sync('r'); });
  $('#cp-m').onclick = function () { nI.value = Math.max(1, (+nI.value || 1) - 1); sync('n'); }; $('#cp-p').onclick = function () { nI.value = Math.min(150, (+nI.value || 0) + 1); sync('n'); };
  hI.onchange = calc; kI.onchange = calc; calc();
  /* menu */
  var tabs = [].slice.call(document.querySelectorAll('#m-tabs button')), panels = [].slice.call(document.querySelectorAll('.m-panel')), q = $('#m-q');
  function show(id) { tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.t === id ? 'true' : 'false'); }); panels.forEach(function (p) { p.hidden = p.dataset.p !== id; }); }
  tabs.forEach(function (t) { t.onclick = function () { q.value = ''; filter(); show(t.dataset.t); var p = document.querySelector('.m-panel[data-p="' + t.dataset.t + '"]'); if (p && window.innerWidth < 900) p.scrollIntoView({ behavior: 'smooth', block: 'start' }); }; });
  [].forEach.call(document.querySelectorAll('[data-go]'), function (b) { b.onclick = function () { q.value = ''; filter(); show(b.dataset.go); $('#menu').scrollIntoView({ behavior: 'smooth', block: 'start' }); }; });
  function filter() {
    var v = q.value.trim().toLowerCase(), n = 0;
    [].forEach.call(document.querySelectorAll('.m-list li'), function (li) { var m = !v || li.dataset.s.indexOf(v) > -1; li.hidden = !m; if (m && v) n++; });
    if (v) panels.forEach(function (p) { p.hidden = !p.querySelector('.m-list li:not([hidden])'); });
    else { var c = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0]; show(c ? c.dataset.t : panels[0].dataset.p); }
    $('#m-empty').hidden = !(v && !n); $('#m-count').textContent = v ? n + ' matches' : '';
  }
  if (q) q.addEventListener('input', filter);
  /* today in hours */
  var nd = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date())];
  [].forEach.call(document.querySelectorAll('.hrs li'), function (li) { if (+li.dataset.dow === nd) li.classList.add('today'); });
})();
