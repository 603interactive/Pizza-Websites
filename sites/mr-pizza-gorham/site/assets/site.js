/* Mr. Pizza: pie builder (menu prices), menu tabs + search, mobile nav */
(function () {
  var $ = function (s) { return document.querySelector(s); }, $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };
  var rb = $('[data-ribbon-x]'); if (rb) rb.onclick = function () { $('.ribbon').hidden = true; };
  var bg = $('.burger'), nav = $('#nav');
  bg.onclick = function () { var o = nav.classList.toggle('open'); bg.setAttribute('aria-expanded', o); };
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); bg.setAttribute('aria-expanded', 'false'); bg.focus(); } });

  // pie builder: cheese pie 10"/16" = $10/$16, each topping +$1/+$2, extra cheese +$4/+$4
  var BASE = [10, 16], TOP = [1, 2], XC = 4, SZ = ['10"', '16"'];
  function pie() {
    var s = +($('input[name=size]:checked') || { value: 0 }).value, picks = $$('#bp input[name=top]:checked').map(function (i) { return i.value; }), xc = $('#bp-xc').checked;
    var total = BASE[s] + picks.length * TOP[s] + (xc ? XC : 0);
    $('#bp-total').textContent = '$' + total;
    var t = SZ[s] + ' cheese pie' + (picks.length ? ' + ' + picks.join(', ') : '') + (xc ? ' + extra cheese' : '');
    $('#bp-sum').textContent = t + '.';
  }
  $$('#bp input').forEach(function (i) { i.addEventListener('change', pie); });
  $('#bp-reset').onclick = function () { $$('#bp input[type=checkbox]').forEach(function (i) { i.checked = false; }); $$('#bp input[name=size]')[0].checked = true; pie(); };
  pie();

  // menu tabs + search
  var tabs = $$('#m-tabs button'), panels = $$('.m-panel'), q = $('#m-q');
  function show(i) { tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === i ? 'true' : 'false'); t.tabIndex = k === i ? 0 : -1; }); panels.forEach(function (p, k) { p.hidden = k !== i; }); $('#m-count').textContent = ''; $('#m-none').hidden = true; $$('[data-g]').forEach(function (g) { g.hidden = false; }); }
  tabs.forEach(function (t, i) {
    t.onclick = function () { q.value = ''; $$('.m-it').forEach(function (e) { e.hidden = false; }); show(i); };
    t.onkeydown = function (e) { var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1; if (n >= 0 && n < tabs.length) { e.preventDefault(); tabs[n].focus(); tabs[n].click(); } };
  });
  show(0);
  q.oninput = function () {
    var v = q.value.trim().toLowerCase();
    if (!v) { var cur = tabs.map(function (t) { return t.getAttribute('aria-selected') === 'true'; }).indexOf(true); $$('.m-it').forEach(function (e) { e.hidden = false; }); show(cur < 0 ? 0 : cur); return; }
    var c = 0; $$('.m-it').forEach(function (e) { var m = e.getAttribute('data-s').indexOf(v) > -1; e.hidden = !m; if (m) c++; });
    $$('[data-g]').forEach(function (g) { g.hidden = true; });
    panels.forEach(function (p) { p.hidden = !p.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = c + (c === 1 ? ' item' : ' items') + ' match'; $('#m-none').hidden = c > 0;
  };
})();
