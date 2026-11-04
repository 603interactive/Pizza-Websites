/* Tenney Mountain Pizza: trail order sheet (builder + menu adds, localStorage in try/catch), menu search, ribbon */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var W = window.__WHITE__ || {}, KEY = 'tmp-sheet-v1', lines = [];
  var rb = $('[data-ribbon-x]'); if (rb) rb.addEventListener('click', function () { $('.ribbon').hidden = true; });
  function money(n) { return '$' + n.toFixed(2); }
  try { var s = JSON.parse(localStorage.getItem(KEY) || '[]'); if (Array.isArray(s)) lines = s.filter(function (l) { return l && typeof l.name === 'string'; }).slice(0, 60); } catch (e) {}
  function save() { try { localStorage.setItem(KEY, JSON.stringify(lines)); } catch (e) {} }
  function sizeIdx(sz) { return sz === 'Small' ? 0 : sz === 'Large' ? 1 : -1; }
  function whiteAdd(l) { var a = W[l.sauce], i = sizeIdx(l.size); return (l.white && a && i > -1) ? a[i] : 0; }
  function text(l) { return (l.qty > 1 ? l.qty + ' x ' : '') + (l.size ? l.size + ' ' : '') + l.name + (l.sauce ? (l.white ? ', white sauce' : ', red sauce') : '') + (l.note ? ' (' + l.note + ')' : ''); }
  var toastT;
  function toast(m) { var t = $('#toast'); t.textContent = m; t.classList.add('on'); clearTimeout(toastT); toastT = setTimeout(function () { t.classList.remove('on'); }, 2200); }
  function render() {
    var ol = $('#sh-lines'); ol.innerHTML = '';
    var n = lines.reduce(function (a, l) { return a + l.qty; }, 0);
    lines.forEach(function (l, i) {
      var li = document.createElement('li'), top = document.createElement('div'); top.className = 'l-top';
      var nm = document.createElement('b'); nm.textContent = (l.size ? l.size + ' ' : '') + l.name; top.appendChild(nm);
      var q = document.createElement('span'); q.className = 'qty';
      var mk = function (lab, al, d) { var b = document.createElement('button'); b.type = 'button'; b.textContent = lab; b.setAttribute('aria-label', al + ' ' + l.name); b.onclick = function () { l.qty += d; if (l.qty < 1) lines.splice(i, 1); save(); render(); }; return b; };
      var c = document.createElement('output'); c.textContent = l.qty; q.appendChild(mk('−', 'Fewer', -1)); q.appendChild(c); q.appendChild(mk('+', 'More', 1)); top.appendChild(q); li.appendChild(top);
      if (l.sauce) { var lb = document.createElement('label'); lb.className = 'wh'; var cb = document.createElement('input'); cb.type = 'checkbox'; cb.checked = !!l.white; cb.onchange = function () { l.white = cb.checked; save(); render(); }; lb.appendChild(cb); var a = W[l.sauce], ix = sizeIdx(l.size); lb.appendChild(document.createTextNode(' White sauce' + (a && ix > -1 ? ' (+' + money(a[ix]) + ')' : ''))); li.appendChild(lb); }
      if (l.desc) { var d = document.createElement('p'); d.className = 'l-d'; d.textContent = l.desc; li.appendChild(d); }
      var nl = document.createElement('label'); nl.className = 'nt'; var sp = document.createElement('span'); sp.textContent = 'Note (toppings, no onions…)'; var inp = document.createElement('input'); inp.type = 'text'; inp.value = l.note || ''; inp.maxLength = 120;
      inp.oninput = function () { l.note = inp.value; save(); fin(); }; nl.appendChild(sp); nl.appendChild(inp); li.appendChild(nl); ol.appendChild(li);
    });
    $('#sh-n').textContent = n; $('#dock-n').textContent = n; $('#sh-empty').hidden = lines.length > 0;
    $('#sh-copy').disabled = !lines.length; $('#sh-clear').disabled = !lines.length; fin();
  }
  function fin() {
    var tot = lines.reduce(function (a, l) { return a + whiteAdd(l) * l.qty; }, 0), ad = $('#sh-addons');
    var wc = lines.filter(function (l) { return whiteAdd(l) > 0; }).length;
    ad.hidden = !wc; ad.textContent = wc ? 'White-sauce add-ons on this sheet: ' + money(tot) + ' (on top of base prices, which the shop gives you by phone).' : '';
  }
  function add(o) {
    var f = lines.filter(function (l) { return l.name === o.name && l.size === o.size && l.sauce === o.sauce && (l.note || '') === (o.note || '') && (l.desc || '') === (o.desc || ''); })[0];
    if (f) f.qty++; else { o.qty = 1; lines.push(o); }
    save(); render(); toast('Added: ' + (o.size ? o.size + ' ' : '') + o.name);
  }
  $$('[data-add]').forEach(function (b) { b.onclick = function () { add({ name: b.dataset.name, size: b.dataset.size, sauce: b.dataset.sauce, white: false, note: '', desc: '' }); }; });
  $('#sh-clear').onclick = function () { lines = []; save(); render(); $('#sh-msg').textContent = 'Sheet cleared.'; };
  $('#sh-copy').onclick = function () {
    var t = 'Tenney Mountain Pizza order (603-536-3865):\n' + lines.map(function (l) { return '- ' + text(l); }).join('\n');
    var done = function (ok) { $('#sh-msg').textContent = ok ? 'Copied. Paste it into a text or read it to us when you call.' : 'Could not copy automatically. Select the lines above and copy them.'; };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(function () { done(true); }, function () { done(false); }); else done(false);
  };
  /* builder */
  var B = $('#builder'), sz = function () { return +B.size.value; };
  function bsty() { return +B.kind.value; }
  function bsync() {
    var small = sz() === 0, c3 = $('#chip3 input');
    c3.disabled = !small; if (!small && c3.checked) B.kind.value = '2';
    var lim = bsty(), tp = $$('input[name=top]', B), on = tp.filter(function (x) { return x.checked; });
    tp.forEach(function (x) { x.disabled = lim === 0 || (on.length >= lim && !x.checked); });
    if (lim === 0) tp.forEach(function (x) { x.checked = false; });
    on = tp.filter(function (x) { return x.checked; });
    $('#b-left').textContent = lim ? '(' + on.length + ' of ' + lim + ' chosen)' : '(cheese pizza has none)';
    var w = W.pz[sz()]; $('#b-white').textContent = '+' + money(w);
    var pr = $$('input[name=prem]:checked', B).length;
    $('#b-sum').textContent = [sz() ? 'Large' : 'Small', B.sauce.value + ' sauce', lim ? (lim === 2 ? 'two' : 'three') + ' topping' : 'cheese'].join(' · ') + (on.length ? ': ' + on.map(function (x) { return x.value; }).join(', ') : '') + (pr ? ' + extra: ' + $$('input[name=prem]:checked', B).map(function (x) { return x.value; }).join(', ') : '');
  }
  $$('input', B).forEach(function (i) { i.addEventListener('change', bsync); });
  $('#b-add').onclick = function () {
    var lim = bsty(), on = $$('input[name=top]:checked', B).map(function (x) { return x.value; }), pr = $$('input[name=prem]:checked', B).map(function (x) { return x.value; });
    var nm = lim ? (lim === 2 ? 'Two Topping Pizza' : 'Three Topping Pizza') : 'Cheese Pizza';
    var ds = (on.length ? on.join(', ') : '') + (pr.length ? (on.length ? ' + ' : '') + 'extra ' + pr.join(', ') : '');
    add({ name: nm, size: sz() ? 'Large' : 'Small', sauce: 'pz', white: B.sauce.value === 'white', note: '', desc: ds });
  };
  bsync();
  /* menu search + section filter */
  var q = $('#m-q'), tabs = $$('#m-tabs button'), cur = 'all', cats = $$('.m-cat'), its = $$('.m-it');
  function filt() {
    var v = q.value.trim().toLowerCase(), c = 0;
    its.forEach(function (e) { var m = (!v || e.getAttribute('data-s').indexOf(v) > -1); e.hidden = !m; if (m) c++; });
    cats.forEach(function (s) { var hide = (cur !== 'all' && s.dataset.c !== cur && !v) || !$('.m-it:not([hidden])', s); s.hidden = hide; });
    $('#m-count').textContent = v ? c + (c === 1 ? ' item matches' : ' items match') : ''; $('#m-none').hidden = c > 0;
  }
  q.oninput = filt;
  tabs.forEach(function (t) { t.onclick = function () { cur = t.dataset.t; tabs.forEach(function (x) { var on = x === t; x.classList.toggle('on', on); x.setAttribute('aria-pressed', on ? 'true' : 'false'); }); q.value = ''; filt(); }; });
  render(); filt();
})();
