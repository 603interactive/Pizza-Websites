/* Uncle Joey's: Chick Stix builder + menu filter */
(function () {
  var S = window.__STIX || {}, $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var tray = $('#tray'); if (!tray) return;
  function money(n) { return '$' + n.toFixed(2); }
  function state() {
    var c = $('input[name=count]:checked'), j = $('input[name=jojo]:checked');
    return { n: +c.value, price: +c.dataset.price, flavor: $('input[name=flavor]:checked').value, jo: +j.value, joPrice: +j.dataset.price, sauces: $$('input[name=sauce]:checked').map(function (x) { return { name: x.value, c: x.dataset.c }; }) };
  }
  function draw(s) {
    var buf = s.flavor === 'Buffalo', fill = buf ? '#E2491B' : '#E3A02F', edge = buf ? '#8E1E05' : '#9A5A0E', hi = buf ? '#FF8A5C' : '#FFD27A';
    var o = '<defs><linearGradient id="gs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#e6dcc6"/></linearGradient></defs>';
    o += '<ellipse cx="230" cy="318" rx="215" ry="16" fill="#000" opacity=".45"/>';
    for (var i = 0; i < s.n; i++) {
      var row = Math.floor(i / 4), col = i % 4, x = 110 + col * 64 + (row % 2) * 30 + ((i * 7) % 9 - 4), y = 222 - row * 27, rot = ((i * 37) % 23) - 11;
      o += '<g class="stix" style="animation-delay:' + (i * 28) + 'ms" transform="translate(' + x + ' ' + y + ') rotate(' + rot + ')"><rect x="-52" y="-15" width="104" height="30" rx="15" fill="' + fill + '" stroke="' + edge + '" stroke-width="3"/><path d="M-36-6 Q0-12 36-6" stroke="' + hi + '" stroke-width="4" fill="none" stroke-linecap="round" opacity=".8"/><circle cx="-18" cy="6" r="2" fill="' + edge + '" opacity=".45"/><circle cx="14" cy="5" r="2.2" fill="' + edge + '" opacity=".45"/><circle cx="30" cy="-1" r="1.8" fill="' + edge + '" opacity=".45"/></g>';
    }
    o += '<path d="M44 238 L416 238 L388 312 L72 312 Z" fill="url(#gs)" stroke="#15110D" stroke-width="3"/>';
    for (var k = 0; k < 9; k++) o += '<path d="M' + (66 + k * 42) + ' 238 L' + (66 + k * 42 + 22) + ' 238 L' + (66 + k * 42 + 17) + ' 312 L' + (66 + k * 42 - 6) + ' 312 Z" fill="#D7261E" opacity=".9"/>';
    o += '<path d="M44 238 L416 238 L388 312 L72 312 Z" fill="none" stroke="#15110D" stroke-width="3"/><rect x="36" y="228" width="388" height="14" rx="7" fill="#15110D"/>';
    if (s.jo) {
      var w = Math.min(s.jo, 24);
      for (var q = 0; q < w; q++) { var rr = Math.floor(q / 6), cc = q % 6, wx = 440 + cc * 18 + (rr % 2) * 9, wy = 292 - rr * 15; o += '<path class="stix" style="animation-delay:' + (q * 22) + 'ms" d="M' + wx + ' ' + wy + ' l16 -4 l4 12 l-18 4 z" fill="#D9A648" stroke="#7a4d10" stroke-width="2" stroke-linejoin="round"/>'; }
      o += '<text x="490" y="318" text-anchor="middle" fill="#F4F1EC" font-family="DM Mono,monospace" font-size="13">' + s.jo + ' Jo Jos</text>';
    }
    s.sauces.forEach(function (z, i) { var cx = 52 + i * 38; o += '<g class="cup" style="animation-delay:' + (i * 40) + 'ms"><path d="M' + (cx - 14) + ' 324 L' + (cx + 14) + ' 324 L' + (cx + 11) + ' 345 L' + (cx - 11) + ' 345 Z" fill="#F4F1EC" stroke="#15110D" stroke-width="2"/><ellipse cx="' + cx + '" cy="324" rx="14" ry="5" fill="' + z.c + '" stroke="#15110D" stroke-width="2"/></g>'; });
    tray.innerHTML = o;
  }
  function ticket(s) {
    var total = s.price + s.joPrice, L = [];
    L.push('<li><span>' + s.n + ' pc ' + s.flavor + ' Chick Stix' + (s.sauces.length ? '<small>Dippers: ' + s.sauces.map(function (z) { return z.name; }).join(', ') + '</small>' : '<small>No dippers picked yet</small>') + '</span><b>' + money(s.price) + '</b></li>');
    if (s.jo) L.push('<li><span>Jo Jo potatoes × ' + s.jo + '</span><b>' + money(s.joPrice) + '</b></li>');
    $('#t-lines').innerHTML = L.join(''); $('#t-total').textContent = money(total);
    return total;
  }
  function update() { var s = state(); draw(s); var t = ticket(s); window.__ticket = { s: s, total: t }; }
  $$('#sb input').forEach(function (i) { i.addEventListener('change', update); }); update();
  $('#t-copy').addEventListener('click', function () {
    var t = window.__ticket, s = t.s, txt = "Uncle Joey's ticket\n" + s.n + ' pc ' + s.flavor + ' Chick Stix' + (s.sauces.length ? '\nDippers: ' + s.sauces.map(function (z) { return z.name; }).join(', ') : '') + (s.jo ? '\n' + s.jo + ' Jo Jo potatoes' : '') + '\nTotal ' + money(t.total) + ' (printed-menu price, before tax)\nCall (603) 424-5693', b = this;
    function done() { b.textContent = 'Copied!'; setTimeout(function () { b.textContent = 'Copy ticket'; }, 1800); }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(done, done);
    else { var a = document.createElement('textarea'); a.value = txt; document.body.appendChild(a); a.select(); try { document.execCommand('copy'); } catch (e) {} a.remove(); done(); }
  });
  /* menu filter */
  var cat = 'all', q = '', tabs = $$('.tabs button'), tks = $$('.tk');
  function filter() {
    var any = false;
    tks.forEach(function (t) {
      var show = cat === 'all' || t.dataset.cat === cat, hits = 0;
      $$('li', t).forEach(function (li) { var m = !q || li.dataset.t.indexOf(q) > -1; li.hidden = !m; if (m) hits++; });
      t.hidden = !(show && hits); if (!t.hidden) any = true;
    });
    $('#none').hidden = any;
  }
  tabs.forEach(function (b) { b.addEventListener('click', function () { tabs.forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on'); cat = b.dataset.cat; filter(); }); });
  $('#q').addEventListener('input', function () { q = this.value.trim().toLowerCase(); filter(); });
})();
