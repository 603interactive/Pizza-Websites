/* Charlestown: Soft-Serve Sundae Maker, menu tabs/search, catering form, parallax */
(function () {
  var $ = function (s) { return document.querySelector(s); }, IC = window.__IC || {};
  var COL = { 'Vanilla': ['#F7EBC6'], 'Chocolate': ['#5B3524'], 'Twist': ['#F7EBC6', '#5B3524'], 'Banana': ['#F6E27B'], 'Black Cherry': ['#7C2745'], 'Blackberry': ['#5E3263'], 'Butter Pecan': ['#E9CB8E'], 'Cheesecake': ['#F5E7D2'], 'Cotton Candy': ['#F6A9D6', '#9CD5F4'], 'Peanut Butter': ['#C9914F'], 'Pineapple': ['#F9D957'], 'Strawberry': ['#F59BAA'], 'Creme De Menthe': ['#A8E4C4'], 'Espresso': ['#6D4B37'], 'German Chocolate': ['#7C4E2B'], 'Blueberry': ['#7D8CDB'], 'Coffee': ['#A97F5E'], 'Mocha': ['#8C5C46'] };
  var SAUCE = { 'Hot Fudge': '#4A2616', 'Strawberry': '#D92F4B', 'Peanut Butter': '#C58B44' }, SODA = { 'Root Beer': '#6B3A1E', 'Cola': '#3A2216', 'Creamsicle': '#FFA24D' };
  var MIX = { 'M&M': ['#D92F4B', '#2E6FD8', '#F2C21B', '#2E9B4F', '#E8742A'], 'Cookies & Cream': ['#3A2A24', '#4A3830', '#2A1E1A'], 'Reese’s Pieces': ['#E8742A', '#F2C21B', '#7B4A24'], 'Peanut Butter Cup': ['#5B3524', '#C9914F'] };
  var FMT = [
    { id: 'cone', name: 'Cone', list: 'scoops', max: 2, leg: 'Pick up to 2 flavors', noun: 'cone' },
    { id: 'waffle', name: 'Waffle Cone', list: 'scoops', max: 2, leg: 'Pick up to 2 flavors', noun: 'waffle cone' },
    { id: 'dish', name: 'Dish', list: 'scoops', max: 3, leg: 'Pick up to 3 flavors', noun: 'dish' },
    { id: 'sundae', name: 'Sundae', list: 'scoops', max: 2, leg: 'Pick up to 2 flavors', ex: 'sundaes', exLeg: 'Pick a topping', noun: 'sundae' },
    { id: 'flurry', name: 'Flurry', list: 'flurries', max: 1, leg: 'Pick your mix-in', noun: 'flurry' },
    { id: 'float', name: 'Float', list: 'floats', max: 1, leg: 'Pick a soda', noun: 'float' },
    { id: 'shake', name: 'Milkshake', list: 'shakes', max: 1, leg: 'Pick a flavor', noun: 'milkshake' }];
  var st = { f: FMT[0], sel: ['Vanilla'], ex: 'Hot Fudge' }, uid = 0;
  var cols = function (n) { return COL[n] || ['#EEE']; };
  function scoop(cx, cy, r, name) {
    var c = cols(name), id = 'sc' + (++uid), g = '<clipPath id="' + id + '"><circle cx="' + cx + '" cy="' + cy + '" r="' + r + '"/></clipPath><g clip-path="url(#' + id + ')"><rect x="' + (cx - r) + '" y="' + (cy - r) + '" width="' + 2 * r + '" height="' + 2 * r + '" fill="' + c[0] + '"/>';
    if (c.length > 1) g += '<path d="M' + (cx - r) + ' ' + (cy - r * .4) + 'Q' + cx + ' ' + (cy + r * .5) + ' ' + (cx + r) + ' ' + (cy - r * .4) + '" fill="none" stroke="' + c[1] + '" stroke-width="' + r * .55 + '"/><path d="M' + (cx - r) + ' ' + (cy + r * .45) + 'Q' + cx + ' ' + (cy + r * 1.2) + ' ' + (cx + r) + ' ' + (cy + r * .45) + '" fill="none" stroke="' + c[1] + '" stroke-width="' + r * .5 + '"/>';
    g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="url(#shade)"/><ellipse cx="' + (cx - r * .3) + '" cy="' + (cy - r * .45) + '" rx="' + r * .32 + '" ry="' + r * .18 + '" fill="#fff" opacity=".35" transform="rotate(-25 ' + (cx - r * .3) + ' ' + (cy - r * .45) + ')"/></g><circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="#000" stroke-opacity=".22" stroke-width="1.5"/>';
    var skirt = cols(name)[0];
    return g + '<path d="M' + (cx - r * .98) + ' ' + (cy + r * .3) + 'q' + r * .12 + ' ' + r * .5 + ' ' + r * .36 + ' ' + r * .5 + 'q' + r * .3 + ' ' + r * .12 + ' ' + r * .62 + ' 0q' + r * .3 + ' ' + r * .12 + ' ' + r * .62 + ' 0q' + r * .24 + ' 0 ' + r * .38 + ' -' + r * .5 + '" fill="' + skirt + '" stroke="#000" stroke-opacity=".22" stroke-width="1.5" stroke-linejoin="round"/>';
  }
  function cone(waffle, flv) {
    var a = '<path d="M92 196h116L150 340z" fill="' + (waffle ? '#D79B4E' : '#E9B76A') + '" stroke="#8A5A1E" stroke-width="3" stroke-linejoin="round"/><path d="M112 196l48 132M136 196l20 140M164 196l-20 140M188 196l-48 132M100 222h100M110 252h80M122 284h56M134 312h32" stroke="#8A5A1E" stroke-width="2" opacity=".55" fill="none"/>';
    if (waffle) a += '<path d="M84 196h132" stroke="#8A5A1E" stroke-width="10" stroke-linecap="round"/>';
    if (flv.length > 1) return a + scoop(150, 172, 54, flv[0]) + scoop(150, 108, 46, flv[1]);
    return a + scoop(150, 140, 62, flv[0]);
  }
  function dish(flv) {
    var a = '<path d="M50 236h200c0 54-40 96-100 96S50 290 50 236z" fill="#fff" stroke="#22304D" stroke-width="4"/><path d="M62 262h176" stroke="#C41E2A" stroke-width="10" opacity=".85"/><ellipse cx="150" cy="236" rx="100" ry="14" fill="#F3EAD4" stroke="#22304D" stroke-width="4"/>';
    var pos = flv.length === 1 ? [[150, 188, 56]] : flv.length === 2 ? [[110, 198, 48], [190, 198, 48]] : [[106, 204, 44], [194, 204, 44], [150, 150, 48]];
    return '<path d="M120 350h60" stroke="#22304D" stroke-width="0"/>' + a + flv.map(function (n, i) { return scoop(pos[i][0], pos[i][1], pos[i][2], n); }).join('');
  }
  function sundae(flv, sauce) {
    var s = SAUCE[sauce] || '#4A2616', a = '<path d="M80 200h140c0 46-26 78-70 82-44-4-70-36-70-82z" fill="#E9F4FA" stroke="#22304D" stroke-width="4" opacity=".95"/><path d="M146 282h8v44h-8z" fill="#E9F4FA" stroke="#000" stroke-opacity=".22" stroke-width="1.5"/><ellipse cx="150" cy="336" rx="52" ry="10" fill="#E9F4FA" stroke="#22304D" stroke-width="4"/>';
    var sc = flv.length > 1 ? scoop(118, 186, 44, flv[0]) + scoop(184, 186, 44, flv[1]) : scoop(150, 176, 56, flv[0]);
    var sauceP = '<path d="M88 150c20-26 44-34 62-34s42 8 62 34c-6 18-12 6-18 22-6-14-10 14-18 24-8-20-14 8-26 14-8-16-16-6-22-22-8 10-12-6-20-16-10 6-14-6-20-22z" fill="' + s + '" opacity=".95"/>';
    var cream = '<g fill="#fff" stroke="#241C1A" stroke-opacity=".3" stroke-width="2"><circle cx="150" cy="112" r="14"/><circle cx="132" cy="120" r="12"/><circle cx="168" cy="120" r="12"/></g><circle cx="150" cy="96" r="9" fill="#C41E2A"/>';
    return a + sc + sauceP + cream;
  }
  function shake(flv) {
    var c = cols(flv[0])[0];
    return '<path d="M130 40l30 -26" stroke="#C41E2A" stroke-width="9" stroke-linecap="round"/><path d="M142 30l22 -18" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 8"/><path d="M70 110h160l-24 220c-2 10-10 16-20 16h-72c-10 0-18-6-20-16z" fill="' + c + '" stroke="#22304D" stroke-width="4"/><path d="M80 170h140" stroke="#fff" stroke-opacity=".35" stroke-width="8"/><path d="M84 130c0-26 30-38 66-38s66 12 66 38c0 12-16 16-30 12-12 14-28 6-36 12-8-6-24 2-36-12-14 4-30 0-30-12z" fill="#fff" stroke="#241C1A" stroke-opacity=".3" stroke-width="2"/><circle cx="150" cy="82" r="10" fill="#C41E2A"/>';
  }
  function flurry(mix) {
    var m = MIX[mix[0]] || MIX['M&M'], dots = '', i, x, y;
    for (i = 0; i < 26; i++) { x = 96 + ((i * 53) % 108); y = 120 + ((i * 37) % 84); dots += '<rect x="' + x + '" y="' + y + '" width="11" height="9" rx="3" fill="' + m[i % m.length] + '" transform="rotate(' + (i * 40 % 90) + ' ' + x + ' ' + y + ')"/>'; }
    return '<path d="M84 220h132l-16 112c-1 8-8 14-16 14h-68c-8 0-15-6-16-14z" fill="#fff" stroke="#22304D" stroke-width="4"/><path d="M90 262h120" stroke="#C41E2A" stroke-width="14"/><path d="M78 224c0-60 32-110 72-110s72 50 72 110z" fill="#F7EBC6" stroke="#241C1A" stroke-opacity=".35" stroke-width="2"/>' + dots + '<path d="M196 70l-30 70" stroke="#22304D" stroke-width="8" stroke-linecap="round"/><ellipse cx="200" cy="60" rx="14" ry="20" fill="#22304D" transform="rotate(20 200 60)"/>';
  }
  function float_(soda) {
    var c = SODA[soda[0]] || '#6B3A1E';
    return '<path d="M168 60l26-44" stroke="#C41E2A" stroke-width="9" stroke-linecap="round"/><path d="M76 96h148l-20 232c-1 12-10 20-22 20h-64c-12 0-21-8-22-20z" fill="' + c + '" stroke="#22304D" stroke-width="4"/><path d="M92 150h116" stroke="#fff" stroke-opacity=".28" stroke-width="8"/><path d="M82 100c0-10 14-14 30-12 8-10 28-12 38-4 12-8 30-6 36 4 20-2 32 4 32 12z" fill="#fff" opacity=".9"/>' + scoop(150, 80, 40, 'Vanilla');
  }
  function art() {
    var f = st.f.id, flv = st.sel.length ? st.sel : ['Vanilla'], body;
    if (f === 'cone') body = cone(false, flv); else if (f === 'waffle') body = cone(true, flv); else if (f === 'dish') body = dish(flv);
    else if (f === 'sundae') body = sundae(flv, st.ex); else if (f === 'shake') body = shake(flv); else if (f === 'flurry') body = flurry(flv); else body = float_(flv);
    $('#sm-art').innerHTML = '<svg viewBox="0 0 300 360" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><radialGradient id="shade" cx=".35" cy=".3" r=".85"><stop offset="0" stop-color="#fff" stop-opacity=".3"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></radialGradient></defs><ellipse cx="150" cy="352" rx="78" ry="8" fill="#22304D" opacity=".14"/>' + body + '</svg>';
  }
  function words() {
    var f = st.f, n = st.sel.slice(), j = function (a) { return a.length > 1 ? a.slice(0, -1).join(', ') + ' & ' + a[a.length - 1] : a[0]; };
    if (f.id === 'flurry') return n[0] + ' flurry'; if (f.id === 'float') return n[0] + ' float'; if (f.id === 'shake') return n[0] + ' milkshake';
    if (f.id === 'sundae') return j(n) + ' sundae with ' + st.ex.toLowerCase();
    return j(n) + ' ' + f.noun;
  }
  function chip(parent, label, pressed, color, fn) {
    var b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-pressed', pressed ? 'true' : 'false');
    if (color) { var s = document.createElement('span'); s.className = 'sw'; s.style.background = color; b.appendChild(s); }
    b.appendChild(document.createTextNode(label)); b.onclick = fn; parent.appendChild(b);
  }
  function render(skipFmt) {
    var f = st.f;
    if (!skipFmt) { var fm = $('#sm-fmt'); fm.innerHTML = ''; FMT.forEach(function (x) { chip(fm, x.name, x.id === f.id, null, function () { st.f = x; st.sel = x.list === 'scoops' ? (x.id === 'cone' || x.id === 'waffle' || x.id === 'dish' || x.id === 'sundae' ? ['Vanilla'] : [IC[x.list][0]]) : [IC[x.list][0]]; if (x.ex) st.ex = IC[x.ex][0]; render(); }); }); }
    $('#sm-fl-leg').textContent = '2 · ' + f.leg;
    var fv = $('#sm-flv'); fv.innerHTML = '';
    IC[f.list].forEach(function (n) {
      var on = st.sel.indexOf(n) > -1, col = (COL[n] || SODA[n] ? (COL[n] ? COL[n][0] : SODA[n]) : (MIX[n] ? MIX[n][0] : null));
      chip(fv, n, on, col, function () {
        var i = st.sel.indexOf(n);
        if (f.max === 1) st.sel = [n]; else if (i > -1) { if (st.sel.length > 1) st.sel.splice(i, 1); } else { if (st.sel.length >= f.max) st.sel.shift(); st.sel.push(n); }
        render(true);
      });
    });
    var ex = $('#sm-ex'); ex.hidden = !f.ex;
    if (f.ex) { $('#sm-ex-leg').textContent = '3 · ' + f.exLeg; var ev = $('#sm-exv'); ev.innerHTML = ''; IC[f.ex].forEach(function (n) { chip(ev, n, st.ex === n, SAUCE[n], function () { st.ex = n; render(true); }); }); }
    art(); $('#sm-name').textContent = 'Your ' + words() + '.';
  }
  if ($('#sm-art')) {
    render();
    $('#sm-rand').onclick = function () {
      st.f = FMT[Math.floor(Math.random() * FMT.length)]; var L = IC[st.f.list], k = st.f.max === 1 ? 1 : 1 + Math.floor(Math.random() * st.f.max), a = [];
      while (a.length < k) { var p = L[Math.floor(Math.random() * L.length)]; if (a.indexOf(p) < 0) a.push(p); }
      st.sel = a; if (st.f.ex) st.ex = IC[st.f.ex][Math.floor(Math.random() * IC[st.f.ex].length)]; render();
    };
    $('#sm-copy').onclick = function () {
      var t = 'Hi! I’d like a ' + words() + ' please.', b = $('#sm-copy');
      var done = function () { b.textContent = 'Copied!'; setTimeout(function () { b.textContent = 'Copy my order'; }, 1800); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, function () { b.textContent = t; }); else b.textContent = t;
    };
  }
  /* ---- menu tabs + search ---- */
  var tabs = [].slice.call(document.querySelectorAll('#m-tabs button')), panels = [].slice.call(document.querySelectorAll('.m-panel')), q = $('#m-q');
  function showTab(t) { tabs.forEach(function (b) { b.setAttribute('aria-selected', b.getAttribute('data-t') === t ? 'true' : 'false'); }); panels.forEach(function (p) { p.hidden = p.getAttribute('data-p') !== t; }); }
  tabs.forEach(function (b) { b.addEventListener('click', function () { q.value = ''; filter(); showTab(b.getAttribute('data-t')); }); });
  function filter() {
    var v = q.value.trim().toLowerCase(), shown = 0, cards = document.querySelectorAll('.m-panel .card');
    [].forEach.call(cards, function (c) { var ok = !v || c.getAttribute('data-t').indexOf(v) > -1; c.hidden = !ok; if (ok) shown++; });
    if (v) { panels.forEach(function (p) { p.hidden = !p.querySelector('.card:not([hidden])'); }); }
    else { var cur = tabs.filter(function (b) { return b.getAttribute('aria-selected') === 'true'; })[0]; showTab(cur ? cur.getAttribute('data-t') : tabs[0].getAttribute('data-t')); }
    $('#m-count').textContent = v ? shown + ' match' + (shown === 1 ? '' : 'es') : ''; $('#m-empty').hidden = !v || shown > 0;
  }
  if (q) q.addEventListener('input', filter);
  /* ---- catering form ---- */
  var cf = $('#cf');
  if (cf) cf.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = function () { $('#cf-ok').hidden = false; cf.reset(); };
    if (location.protocol === 'file:') return ok();
    var body = new URLSearchParams(new FormData(cf)).toString();
    fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: body }).then(ok, ok);
  });
  /* ---- parallax ---- */
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var els = [].slice.call(document.querySelectorAll('[data-par]')), tick = false;
    var run = function () { tick = false; var vh = window.innerHeight;
      els.forEach(function (s) { var r = s.getBoundingClientRect(); if (r.bottom < -100 || r.top > vh + 100) return; var c = r.top + r.height / 2 - vh / 2;
        [].forEach.call(s.querySelectorAll('[data-depth]'), function (e) { e.style.transform = 'translate3d(0,' + (c * +e.getAttribute('data-depth')).toFixed(1) + 'px,0)'; }); }); };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
  }
})();
