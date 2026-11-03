/* Enfield: The Week at EHOP (daily-deal calculator), menu tabs + search, party calc, parallax */
(function () {
  var $ = function (s) { return document.querySelector(s); }, DAYS = window.__DAYS || [], LG = window.__LG || [];
  var money = function (n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); };
  var nd = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date())];
  var rail = $('#wk-rail'), btns = [].slice.call(rail.querySelectorAll('button')), st = { qty: 1, a: 0, b: 0 };
  function dayOf(dow) { return DAYS.filter(function (d) { return d.dow === dow; })[0]; }
  function row(l, v, cls) { return '<div class="' + (cls || '') + '"><span>' + l + '</span><b>' + v + '</b></div>'; }
  function stepper(label, id, min, max, val, unit) {
    return '<label for="' + id + '">' + label + '</label><div class="step"><button type="button" data-st="-" aria-label="Fewer">−</button><input id="' + id + '" type="number" inputmode="numeric" min="' + min + '" max="' + max + '" value="' + val + '"><button type="button" data-st="+" aria-label="More">+</button></div>' + (unit ? '<small>' + unit + '</small>' : '');
  }
  function sel(label, id, idx) {
    return '<label for="' + id + '">' + label + '</label><select id="' + id + '">' + LG.map(function (p, i) { return '<option value="' + i + '"' + (i === idx ? ' selected' : '') + '>' + p.name + ' · ' + money(p.price) + '</option>'; }).join('') + '</select>';
  }
  function render(dow) {
    var d = dayOf(dow), ctl = $('#wk-ctl'), out = $('#wk-out');
    btns.forEach(function (b) { var on = +b.dataset.dow === dow; b.setAttribute('aria-selected', on ? 'true' : 'false'); b.classList.toggle('today', +b.dataset.dow === nd); });
    $('#wk-day').textContent = d.day + (dow === nd ? ' · today' : ''); $('#wk-title').textContent = d.title; $('#wk-line').textContent = d.line;
    $('#wk-sheet').dataset.kind = d.kind;
    if (d.kind === 'closed') { ctl.innerHTML = '<p class="closed">Enfield House of Pizza is closed on Mondays.</p><button type="button" class="btn" id="wk-go">See Tuesday’s deal</button>'; out.innerHTML = ''; $('#wk-go').onclick = function () { render(2); }; return; }
    if (d.kind === 'pair') ctl.innerHTML = stepper('How many pairs of large cheese pizzas?', 'wk-q', 1, 6, st.qty, 'Two large cheese pizzas per pair');
    if (d.kind === 'wings') ctl.innerHTML = stepper('How many wings?', 'wk-q', 1, 100, st.qty > 6 ? st.qty : 20, 'Any quantity, any flavor on the menu');
    if (d.kind === 'single') ctl.innerHTML = stepper('How many small cheese pizzas?', 'wk-q', 1, 8, st.qty, '');
    if (d.kind === 'beer') ctl.innerHTML = stepper('How many bottles?', 'wk-q', 1, 3, Math.min(st.qty, 3), 'EHOP policy: 3 drink limit');
    if (d.kind === 'free2l') ctl.innerHTML = sel('First large pizza', 'wk-a', 0) + sel('Second large pizza', 'wk-b', 1);
    if (d.kind === 'sunday') ctl.innerHTML = sel('Your large regular-priced pizza', 'wk-a', 3);
    [].forEach.call(ctl.querySelectorAll('[data-st]'), function (b) { b.onclick = function () { var i = $('#wk-q'); i.value = Math.min(+i.max, Math.max(+i.min, (+i.value || 1) + (b.dataset.st === '+' ? 1 : -1))); calc(); }; });
    [].forEach.call(ctl.querySelectorAll('input,select'), function (i) { i.oninput = calc; i.onchange = calc; });
    calc();
  }
  function calc() {
    var cur = btns.filter(function (b) { return b.getAttribute('aria-selected') === 'true'; })[0], d = dayOf(+cur.dataset.dow), out = $('#wk-out'), qi = $('#wk-q'), q = qi ? Math.max(+qi.min, Math.min(+qi.max, Math.floor(+qi.value) || +qi.min)) : 1;
    if (qi) st.qty = q;
    var html = '', deal, reg;
    if (d.kind === 'pair') { deal = d.price * q; reg = 2 * d.reg * q; html = row('Two for Tuesday price', money(deal)) + row('Regular menu price (' + (2 * q) + ' × ' + money(d.reg) + ')', money(reg), 'reg') + row('You save', money(reg - deal), 'save'); }
    else if (d.kind === 'wings') { deal = d.price * q; reg = d.reg * q; html = row('Wing It Wednesday (' + q + ' × $0.90)', money(deal)) + row('Regular price (8 wings for $11.99)', money(reg), 'reg') + row('You save', money(reg - deal), 'save'); }
    else if (d.kind === 'single') { deal = d.price * q; reg = d.reg * q; html = row('Throw Back Thursday price', money(deal)) + row('Regular small cheese (' + money(d.reg) + ' each)', money(reg), 'reg') + row('You save', money(reg - deal), 'save'); }
    else if (d.kind === 'beer') { html = row('Bottle price', 'Regular less $1.00 each') + row('You save', money(q * d.price), 'save'); }
    else if (d.kind === 'free2l') { var a = LG[+$('#wk-a').value], b = LG[+$('#wk-b').value]; html = row(a.name, money(a.price)) + row(b.name, money(b.price)) + row('Two large pizzas', money(a.price + b.price), 'tot') + row('Free 2 liter', 'On the house', 'save'); }
    else if (d.kind === 'sunday') { var p = LG[+$('#wk-a').value]; html = row(p.name + ' (large)', money(p.price)) + row('Large cheese pizza', '$10.00') + row('Your total', money(p.price + 10), 'tot') + row('You save on the cheese', money(d.reg - 10), 'save'); }
    out.innerHTML = html + '<a class="btn btn-gold" href="' + (window.__ORDER || '#') + '" rel="noopener">Order it online</a>';
  }
  btns.forEach(function (b) { b.onclick = function () { st.qty = 1; render(+b.dataset.dow); }; });
  [].forEach.call(document.querySelectorAll('.rail'), function () {});
  var ord = document.querySelector('.top .btn'); window.__ORDER = ord ? ord.getAttribute('href') : '#';
  rail.addEventListener('keydown', function (e) { var i = btns.indexOf(document.activeElement); if (i < 0) return; if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); var n = btns[(i + (e.key === 'ArrowRight' ? 1 : btns.length - 1)) % btns.length]; n.focus(); n.click(); } });
  render(nd === 1 ? 2 : nd);
  /* party */
  var pn = $('#pp-n'), pt = $('#pp-t');
  function pc() { var n = Math.max(1, Math.min(60, Math.floor(+pn.value) || 1)); pt.textContent = money(n * 10); }
  if (pn) { pn.addEventListener('input', pc); $('#pp-m').onclick = function () { pn.value = Math.max(1, (+pn.value || 1) - 1); pc(); }; $('#pp-p').onclick = function () { pn.value = Math.min(60, (+pn.value || 0) + 1); pc(); }; pc(); }
  /* today in hours list */
  [].forEach.call(document.querySelectorAll('.hrs li'), function (li) { if (+li.dataset.dow === nd) li.classList.add('today'); });
  /* menu */
  var tabs = [].slice.call(document.querySelectorAll('#m-tabs button')), panels = [].slice.call(document.querySelectorAll('.m-panel')), q = $('#m-q');
  function show(id) { tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.t === id ? 'true' : 'false'); }); panels.forEach(function (p) { p.hidden = p.dataset.p !== id; }); }
  tabs.forEach(function (t) { t.onclick = function () { q.value = ''; filter(); show(t.dataset.t); var p = document.querySelector('.m-panel[data-p="' + t.dataset.t + '"]'); if (p && window.innerWidth < 900) p.scrollIntoView({ behavior: 'smooth', block: 'start' }); }; });
  function filter() {
    var v = q.value.trim().toLowerCase(), n = 0;
    [].forEach.call(document.querySelectorAll('.m-list li'), function (li) { var m = !v || li.dataset.s.indexOf(v) > -1; li.hidden = !m; if (m && v) n++; });
    if (v) panels.forEach(function (p) { p.hidden = !p.querySelector('.m-list li:not([hidden])'); });
    else { var c = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0]; show(c ? c.dataset.t : panels[0].dataset.p); }
    $('#m-empty').hidden = !(v && !n); $('#m-count').textContent = v ? n + ' matches' : '';
  }
  if (q) q.addEventListener('input', filter);
  /* collage drifts */
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var pe = [].slice.call(document.querySelectorAll('[data-depth]')), tick = false;
    var go = function () { tick = false; var y = window.scrollY; pe.forEach(function (e) { e.style.translate = '0 ' + (y * parseFloat(e.dataset.depth)).toFixed(1) + 'px'; }); };
    if (pe.length) window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(go); } }, { passive: true });
  }
})();
