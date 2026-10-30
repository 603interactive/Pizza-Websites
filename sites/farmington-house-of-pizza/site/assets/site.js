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

/* Farmington: Pie Studio (build vs buy), menu tabs + search, hero parallax */
(function () {
  var $ = function (s) { return document.querySelector(s); }, S = window.__STUDIO;
  var money = function (n) { return '$' + n.toFixed(2); };
  if (S && $('#st-size')) {
    var size = 0, sel = {}, SZ = ['Medium', 'Large'];
    var vp = S.veg.price, mp = S.meat.price;
    var kind = {}; S.veg.items.forEach(function (n) { kind[n] = 'veg'; }); S.meat.items.forEach(function (n) { kind[n] = 'meat'; });
    var tp = function (n, sz) { return (kind[n] === 'veg' ? vp : mp)[sz]; };
    var buildPrice = function (set, sz) { var t = S.cheese[sz]; Object.keys(set).forEach(function (n) { t += tp(n, sz); }); return t; };
    var segEl = $('#st-size');
    SZ.forEach(function (l, i) {
      var b = document.createElement('button'); b.type = 'button'; b.setAttribute('role', 'radio'); b.innerHTML = l + '<small>' + money(S.cheese[i]) + ' cheese</small>';
      b.onclick = function () { size = i; render(); }; segEl.appendChild(b);
    });
    function chips(host, items) {
      items.forEach(function (n) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'tp'; b.setAttribute('aria-pressed', 'false'); b.dataset.n = n; b.textContent = n;
        b.onclick = function () { if (sel[n]) delete sel[n]; else sel[n] = 1; render(); }; host.appendChild(b);
      });
    }
    chips($('#st-veg'), S.veg.items); chips($('#st-meat'), S.meat.items);
    $('#st-clear').onclick = function () { sel = {}; render(); };
    function specStats(sp) {
      var need = sp.tops.filter(function (n) { return !sel[n]; }), extras = Object.keys(sel).filter(function (n) { return sp.tops.indexOf(n) < 0; });
      var overlap = Object.keys(sel).length - extras.length, buy = sp.price[size], build = buildPrice(sel, size);
      extras.forEach(function (n) { buy += tp(n, size); }); need.forEach(function (n) { build += tp(n, size); });
      return { need: need, extras: extras, overlap: overlap, buy: buy, build: build, save: build - buy };
    }
    function render() {
      [].forEach.call(segEl.children, function (b, i) { b.setAttribute('aria-checked', i === size ? 'true' : 'false'); });
      $('#st-vp').textContent = money(vp[size]) + ' each'; $('#st-mp').textContent = money(mp[size]) + ' each';
      [].forEach.call(document.querySelectorAll('.tp'), function (b) { b.setAttribute('aria-pressed', sel[b.dataset.n] ? 'true' : 'false'); });
      var lines = $('#st-lines'); lines.innerHTML = '';
      var add = function (a, b) { var li = document.createElement('li'); li.innerHTML = '<span></span><b></b>'; li.firstChild.textContent = a; li.lastChild.textContent = b; lines.appendChild(li); };
      add(SZ[size] + ' cheese pizza', money(S.cheese[size]));
      Object.keys(sel).forEach(function (n) { add('+ ' + n, money(tp(n, size))); });
      $('#st-total').textContent = money(buildPrice(sel, size));
      var tip = $('#st-tip'), best = null;
      if (Object.keys(sel).length) S.specials.forEach(function (sp) { var st = specStats(sp); st.sp = sp; if (st.overlap > 0 && st.save > 0.005 && (!best || st.need.length < best.need.length || (st.need.length === best.need.length && st.save > best.save))) best = st; });
      if (best) {
        tip.hidden = false; tip.className = 't-tip win';
        tip.textContent = best.need.length ? 'Add ' + best.need.join(', ') + ' and it becomes our ' + best.sp.name + ': ' + money(best.buy) + ' as a specialty instead of ' + money(best.build) + ' built. You save ' + money(best.save) + '.'
          : 'That is our ' + best.sp.name + '. Order it as a specialty for ' + money(best.buy) + ' instead of ' + money(best.build) + ' built. You save ' + money(best.save) + '.';
      } else if (Object.keys(sel).length) { tip.hidden = false; tip.className = 't-tip'; tip.textContent = 'Building it yourself is the best price for this combination.'; }
      else tip.hidden = true;
      S.specials.forEach(function (sp, i) {
        var card = document.getElementById('sp' + i); if (!card) return;
        var st = specStats(sp), full = {}; sp.tops.forEach(function (n) { full[n] = 1; });
        card.querySelector('.sp-b').textContent = money(buildPrice(full, size)); card.querySelector('.sp-p').textContent = money(sp.price[size]);
        card.querySelector('.sp-s').textContent = 'Save ' + money(buildPrice(full, size) - sp.price[size]);
      });
    }
    var row = $('#st-specs');
    S.specials.forEach(function (sp, i) {
      var c = document.createElement('div'); c.className = 'sp'; c.id = 'sp' + i;
      c.innerHTML = '<h4></h4><p></p><div class="sp-n"><span>Specialty <b class="sp-p"></b></span><span>Built <s class="sp-b"></s></span></div><p class="sp-s"></p><button type="button" class="btn btn-line btn-sm">Load into the Studio</button>';
      c.querySelector('h4').textContent = sp.name; c.querySelector('p').textContent = sp.tops.join(', ');
      c.querySelector('button').onclick = function () { sel = {}; sp.tops.forEach(function (n) { sel[n] = 1; }); render(); $('#st-size').scrollIntoView({ block: 'center', behavior: 'smooth' }); };
      row.appendChild(c);
    });
    render();
  }
  /* menu */
  var tabs = [].slice.call(document.querySelectorAll('#m-tabs button')), panels = [].slice.call(document.querySelectorAll('.m-panel')), q = $('#m-q');
  function show(id) { tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.t === id ? 'true' : 'false'); }); panels.forEach(function (p) { p.hidden = p.dataset.p !== id; }); }
  tabs.forEach(function (t) { t.onclick = function () { q.value = ''; filter(); show(t.dataset.t); }; });
  function filter() {
    var v = q.value.trim().toLowerCase(), n = 0;
    [].forEach.call(document.querySelectorAll('.m-list li'), function (li) { var m = !v || li.dataset.s.indexOf(v) > -1; li.hidden = !m; if (m && v) n++; });
    if (v) panels.forEach(function (p) { var any = p.querySelector('.m-list li:not([hidden])'); p.hidden = !any; });
    else { var cur = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0]; show(cur ? cur.dataset.t : panels[0].dataset.p); }
    $('#m-empty').hidden = !(v && !n); $('#m-count').textContent = v ? n + ' matches' : '';
  }
  if (q) q.addEventListener('input', filter);
  /* parallax */
  var pe = [].slice.call(document.querySelectorAll('[data-depth]'));
  if (pe.length && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var tick = false;
    var go = function () { tick = false; var y = window.scrollY; pe.forEach(function (e) { e.style.translate = '0 ' + (y * parseFloat(e.dataset.depth)).toFixed(1) + 'px'; }); };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(go); } }, { passive: true });
  }
  /* today */
  var d = new Date(new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date()) && Date.now());
  var nd = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short' }).format(new Date())];
  var li = document.querySelector('.hrs li[data-dow="' + nd + '"]'); if (li) li.classList.add('today');
})();
