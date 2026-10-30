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

/* Gilford: Delivery Desk, season hours, menu tabs + search, belt slide */
(function () {
  var $ = function (s) { return document.querySelector(s); }, DD = window.__DD || { fee: 4, tax: .085 };
  var money = function (n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); };
  var sub = $('#dd-sub'), rng = $('#dd-range'), app = $('#dd-app'), town = $('#dd-town');
  function calc() {
    var f = Math.max(0, parseFloat(sub.value) || 0), a = Math.max(0, parseFloat(app.value) || 0), out = town.options[town.selectedIndex].value === 'out';
    var tax = f * DD.tax; $('#dd-f').textContent = money(f); $('#dd-t').textContent = money(tax); $('#dd-d').textContent = out ? 'Call us' : money(DD.fee);
    $('#dd-ours').textContent = money(f + tax + (out ? 0 : DD.fee));
    var v = $('#dd-verdict'), s = $('#dd-save'); v.className = 'verdict';
    if (out) { v.textContent = 'We deliver to Gilford and Laconia only. Pickup and dine-in are always open to you.'; s.textContent = '$0.00'; return; }
    if (!app.value) { v.textContent = 'Type what a delivery app charged you in fees, and we will show the difference.'; s.textContent = '$0.00'; return; }
    var d = a - DD.fee;
    if (d > 0.005) { v.className = 'verdict win'; v.textContent = 'The app added ' + money(a) + ' in fees. We add ' + money(DD.fee) + ' and nothing else. That is ' + money(d) + ' back in your pocket on this order.'; s.textContent = money(d); }
    else { v.textContent = 'Your app fees were about the same as ours (' + money(a) + ' vs ' + money(DD.fee) + '). Ours is flat no matter how big the order.'; s.textContent = '$0.00'; }
  }
  if (sub) {
    sub.addEventListener('input', function () { rng.value = Math.min(120, Math.max(10, +sub.value || 10)); calc(); });
    rng.addEventListener('input', function () { sub.value = rng.value; calc(); });
    app.addEventListener('input', calc); town.addEventListener('change', calc); calc();
  }
  /* seasons */
  var cur = window.__SEASON || 'winter';
  [].forEach.call(document.querySelectorAll('.season'), function (e) { var on = e.dataset.season === cur; e.classList.toggle('on', on); e.querySelector('.now').hidden = !on; });
  var nd = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date())];
  [].forEach.call(document.querySelectorAll('.season.on li'), function (li) { if (li.dataset.dows.split(',').indexOf(String(nd)) > -1) li.classList.add('today'); });
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
  /* parallax: seal drifts, photo belt slides sideways as you scroll */
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var pe = [].slice.call(document.querySelectorAll('[data-depth]')), belt = $('.belt .row'), tick = false;
    var go = function () { tick = false; var y = window.scrollY; pe.forEach(function (e) { e.style.translate = '0 ' + (y * parseFloat(e.dataset.depth)).toFixed(1) + 'px'; }); if (belt) belt.style.translate = (y * -0.35).toFixed(1) + 'px 0'; };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(go); } }, { passive: true });
  }
})();
