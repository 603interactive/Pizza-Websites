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

/* Golden Acres: Size Lab, drawn pies, menu search */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var PIES = window.__PIES || [], AREA14 = Math.PI * 49, AREA20 = Math.PI * 100;
  function hash(s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  function rng(seed) { var s = seed || 1; return function () { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; }; }
  function pt(r, rad) { var a = r() * 6.2832, d = Math.sqrt(r()) * rad; return [100 + Math.cos(a) * d, 100 + Math.sin(a) * d, a]; }
  var T = [
    ['pepperoni', 13, function (x, y, r) { return '<circle cx="' + x + '" cy="' + y + '" r="8.5" fill="#B5291B" stroke="#7B1710" stroke-width="1.5"/><circle cx="' + (x - 2) + '" cy="' + (y - 2) + '" r="1.4" fill="#7B1710"/><circle cx="' + (x + 3) + '" cy="' + (y + 2) + '" r="1.2" fill="#7B1710"/>'; }],
    ['salami', 8, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="7" fill="#962C26" stroke="#5E1612" stroke-width="1.2"/><circle cx="' + (x + 2) + '" cy="' + (y - 1) + '" r="1.5" fill="#F0D9C8"/><circle cx="' + (x - 2) + '" cy="' + (y + 2) + '" r="1.2" fill="#F0D9C8"/>'; }],
    ['sausage', 16, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="4" fill="#8C5733" stroke="#5C3519" stroke-width="1"/>'; }],
    ['ham', 9, function (x, y, r, a) { return '<rect x="' + (x - 6) + '" y="' + (y - 4.5) + '" width="12" height="9" rx="2" fill="#EE9AA0" stroke="#C86A72" stroke-width="1" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['bacon', 10, function (x, y, r, a) { return '<rect x="' + (x - 8) + '" y="' + (y - 2) + '" width="16" height="4" rx="2" fill="#B5472E" stroke="#7C2A19" stroke-width=".8" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['meatball', 6, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="9" fill="#6A3B24" stroke="#3E2012" stroke-width="1.5"/><circle cx="' + (x - 3) + '" cy="' + (y - 3) + '" r="2.4" fill="#936040"/>'; }],
    ['hamburger', 18, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="2.8" fill="#70492F"/>'; }],
    ['onion', 10, function (x, y, r, a) { return '<ellipse cx="' + x + '" cy="' + y + '" rx="8" ry="3.6" fill="none" stroke="#EBDDF3" stroke-width="2" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['green pepper', 10, function (x, y, r, a) { return '<path d="M' + (x - 7) + ' ' + y + ' q7 -9 14 0" fill="none" stroke="#5E9B34" stroke-width="3" stroke-linecap="round" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['pepper', 8, function (x, y, r, a) { return '<path d="M' + (x - 7) + ' ' + y + ' q7 -9 14 0" fill="none" stroke="#5E9B34" stroke-width="3" stroke-linecap="round" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['mushroom', 10, function (x, y) { return '<path d="M' + (x - 7) + ' ' + (y + 2) + ' q7 -11 14 0 z" fill="#D8C3A5" stroke="#9C8566" stroke-width="1"/><rect x="' + (x - 2) + '" y="' + (y + 2) + '" width="4" height="4" fill="#E8DAC2"/>'; }],
    ['olive', 12, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="4.6" fill="none" stroke="#1E1E1E" stroke-width="2.6"/>'; }],
    ['tomato', 9, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="8.5" fill="#D6402B" stroke="#9E2615" stroke-width="1.2"/><circle cx="' + x + '" cy="' + y + '" r="4.5" fill="#E8684F"/>'; }],
    ['broccoli', 11, function (x, y) { return '<g fill="#3F7F2E"><circle cx="' + (x - 3) + '" cy="' + y + '" r="3.6"/><circle cx="' + (x + 3) + '" cy="' + (y - 1) + '" r="3.6"/><circle cx="' + x + '" cy="' + (y + 3) + '" r="3.4"/></g>'; }],
    ['chicken', 12, function (x, y, r, a) { return '<rect x="' + (x - 6) + '" y="' + (y - 3.5) + '" width="12" height="7" rx="3.5" fill="#EBCB96" stroke="#B78E50" stroke-width="1" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['feta', 16, function (x, y, r, a) { return '<rect x="' + (x - 3) + '" y="' + (y - 3) + '" width="6" height="6" rx="1" fill="#FFFFFF" stroke="#E5E1D4" stroke-width=".8" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['pineapple', 10, function (x, y, r, a) { return '<path d="M' + (x - 6) + ' ' + (y + 4) + ' L' + x + ' ' + (y - 6) + ' L' + (x + 6) + ' ' + (y + 4) + ' z" fill="#F4D548" stroke="#C79C12" stroke-width="1" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['spinach', 14, function (x, y, r, a) { return '<ellipse cx="' + x + '" cy="' + y + '" rx="7" ry="3.5" fill="#2F6A2D" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['basil', 8, function (x, y, r, a) { return '<ellipse cx="' + x + '" cy="' + y + '" rx="6" ry="3.2" fill="#2E8B3C" stroke="#1D5E27" stroke-width=".8" transform="rotate(' + (a * 57) + ' ' + x + ' ' + y + ')"/>'; }],
    ['ricotta', 7, function (x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="6" fill="#FFFDF5" stroke="#E9E3CF" stroke-width="1"/>'; }]
  ];
  function pieSVG(p) {
    var txt = (p.name + ' ' + (p.desc || '')).toLowerCase(), r = rng(hash(p.name)), white = /olive oil|alfredo|\bwhite\b|no sauce/.test(txt) && !/pizza sauce/.test(txt);
    var o = '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="100" cy="100" r="100" fill="#D6994A"/><circle cx="100" cy="100" r="92" fill="#E3AE62"/>';
    o += '<circle cx="100" cy="100" r="86" fill="' + (white ? '#F4E4B8' : '#C93A21') + '"/><circle cx="100" cy="100" r="82" fill="#F3C74F"/>';
    for (var i = 0; i < 26; i++) { var q = pt(r, 76); o += '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="' + (6 + r() * 11) + '" fill="' + (r() > .5 ? '#F9DD85' : '#E6B23C') + '" opacity=".55"/>'; }
    for (i = 0; i < 9; i++) { q = pt(r, 78); o += '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="' + (2 + r() * 3) + '" fill="#C98B2E" opacity=".7"/>'; }
    var seen = {};
    T.forEach(function (t) {
      var k = t[0]; if (txt.indexOf(k) < 0) return;
      if (k === 'pepper' && /green pepper|roasted/.test(txt) && seen['green pepper']) return;
      if ((k === 'pepper' || k === 'green pepper') && /pepperoni/.test(txt) && !/green pepper|peppers/.test(txt)) return;
      seen[k] = 1; for (var n = 0; n < t[1]; n++) { var q2 = pt(r, 74); o += t[2](q2[0].toFixed(1), q2[1].toFixed(1), r, q2[2]); }
    });
    if (/hot honey|honey/.test(txt)) for (i = 0; i < 6; i++) { q = pt(r, 60); o += '<path d="M' + (q[0] - 20) + ' ' + q[1] + ' q10 -12 20 0 t20 0" fill="none" stroke="#E8A317" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>'; }
    if (/ranch/.test(txt)) for (i = 0; i < 5; i++) { q = pt(r, 55); o += '<path d="M' + (q[0] - 22) + ' ' + q[1] + ' q11 10 22 0 t22 0" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".92"/>'; }
    if (/buffalo/.test(txt)) for (i = 0; i < 5; i++) { q = pt(r, 55); o += '<path d="M' + (q[0] - 22) + ' ' + q[1] + ' q11 -10 22 0 t22 0" fill="none" stroke="#E2561C" stroke-width="2.6" stroke-linecap="round" opacity=".9"/>'; }
    if (/bbq/.test(txt)) for (i = 0; i < 5; i++) { q = pt(r, 55); o += '<path d="M' + (q[0] - 22) + ' ' + q[1] + ' q11 10 22 0 t22 0" fill="none" stroke="#5B2A12" stroke-width="2.6" stroke-linecap="round" opacity=".9"/>'; }
    if (/oregano/.test(txt)) for (i = 0; i < 40; i++) { q = pt(r, 78); o += '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="1" fill="#4B7A2A"/>'; }
    return o + '<circle cx="100" cy="100" r="99" fill="none" stroke="rgba(120,70,20,.35)" stroke-width="2"/></svg>';
  }
  /* lab */
  var picker = $('#picker'); if (!picker || !PIES.length) return;
  var cur = 0, rankEl = $('#rank'), scale = $('#scale');
  function money(n) { return '$' + n.toFixed(2); }
  function cents(p, a) { return p / a * 100; }
  PIES.forEach(function (p, i) { p.c20 = cents(p.p20, AREA20); p.c14 = cents(p.p14, AREA14); });
  picker.innerHTML = PIES.map(function (p, i) { return '<label><input type="radio" name="pie" value="' + i + '"' + (i === 0 ? ' checked' : '') + '><span>' + p.name + '<small>from ' + money(p.p14) + '</small></span></label>'; }).join('');
  var order = PIES.map(function (p, i) { return i; }).sort(function (a, b) { return PIES[a].c20 - PIES[b].c20; }), maxC = Math.max.apply(null, PIES.map(function (p) { return p.c20; }));
  rankEl.innerHTML = order.map(function (i) { var p = PIES[i]; return '<li data-i="' + i + '"><button type="button"><span>' + p.name + '</span><span class="bar"><i style="width:' + Math.round(p.c20 / maxC * 100) + '%"></i></span><span>' + p.c20.toFixed(1) + '¢</span></button></li>'; }).join('');
  function tween(el, to, dec) { var from = +el.dataset.v || 0, t0 = performance.now(), reduce = matchMedia('(prefers-reduced-motion:reduce)').matches; el.dataset.v = to; if (reduce) { el.textContent = to.toFixed(dec); return; } (function f(t) { var k = Math.min(1, (t - t0) / 600), e = 1 - Math.pow(1 - k, 3); el.textContent = (from + (to - from) * e).toFixed(dec); if (k < 1) requestAnimationFrame(f); })(t0); }
  function render(i) {
    cur = i; var p = PIES[i];
    ['d14', 'd20'].forEach(function (id) {
      var d = $('#' + id); d.classList.add('swap');
      setTimeout(function () { if (p.photo) { d.style.backgroundImage = 'url(' + p.photo + ')'; d.innerHTML = ''; } else { d.style.backgroundImage = 'none'; d.innerHTML = pieSVG(p); } d.classList.remove('swap'); }, 120);
    });
    $('#p14').textContent = money(p.p14); $('#p20').textContent = money(p.p20);
    $('#cap').textContent = p.photo ? (p.cap || 'Real photo from the shop. Circles are drawn to true size.') : 'Illustrated from the menu description. Circles are drawn to true size.';
    tween($('#a14'), AREA14, 0); tween($('#a20'), AREA20, 0); tween($('#c14'), p.c14, 1); tween($('#c20'), p.c20, 1);
    var ar = AREA20 / AREA14, pr = p.p20 / p.p14;
    $('#verdict').innerHTML = pr < ar ? 'The 20" is <b>' + ar.toFixed(1) + ' times</b> the pizza for <b>' + pr.toFixed(1) + ' times</b> the price.' : 'The 20" is <b>' + ar.toFixed(1) + ' times</b> the pizza for <b>' + pr.toFixed(1) + ' times</b> the price. Same value per bite.';
    $$('li', rankEl).forEach(function (li) { li.classList.toggle('on', +li.dataset.i === i); });
  }
  picker.addEventListener('change', function (e) { if (e.target.name === 'pie') render(+e.target.value); });
  rankEl.addEventListener('click', function (e) { var li = e.target.closest('li'); if (!li) return; var i = +li.dataset.i; var inp = $('input[value="' + i + '"]', picker); inp.checked = true; render(i); inp.scrollIntoView({ block: 'nearest', inline: 'nearest' }); $('#scale').scrollIntoView({ block: 'center', behavior: 'smooth' }); });
  $('#rectog').addEventListener('change', function () { $('#rec').hidden = !this.checked; });
  function fit() { var w = $('#stage').clientWidth; scale.style.setProperty('--u', Math.max(6, Math.min(w / 37, 24)) + 'px'); }
  if ('ResizeObserver' in window) new ResizeObserver(fit).observe($('#stage')); window.addEventListener('resize', fit); fit(); render(0);
  /* menu search */
  var q = $('#q'), asl = $$('.aisle');
  q.addEventListener('input', function () {
    var v = q.value.trim().toLowerCase(), any = false;
    asl.forEach(function (a) { var hits = 0; $$('li', a).forEach(function (li) { var m = !v || li.dataset.t.indexOf(v) > -1; li.hidden = !m; if (m) hits++; }); a.hidden = !hits; if (hits) any = true; });
    $('#none').hidden = any;
  });
})();
