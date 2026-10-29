/* Charlestown: menu tabs/search, catering form */
(function () {
  var $ = function (s) { return document.querySelector(s); };
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
