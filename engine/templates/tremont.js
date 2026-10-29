/* Tremont: Points Ladder, menu search, lunch badge, parallax */
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var ITEMS = window.__ITEMS || [], RW = window.__REWARDS || [];
  var money = function (n) { return '$' + n.toFixed(2); };
  /* ---- Points Ladder ---- */
  var tabsEl = $('#lp-tabs'), listEl = $('#lp-list'), cartEl = $('#lp-cart');
  if (tabsEl && listEl) {
    var cats = []; ITEMS.forEach(function (i) { if (cats.indexOf(i.cat) < 0) cats.push(i.cat); });
    var cur = cats[0], cart = {};
    function renderTabs() {
      tabsEl.innerHTML = '';
      cats.forEach(function (c) {
        var b = document.createElement('button'); b.type = 'button'; b.setAttribute('role', 'tab'); b.textContent = c; b.setAttribute('aria-selected', c === cur ? 'true' : 'false');
        b.onclick = function () { cur = c; renderTabs(); renderList(); }; tabsEl.appendChild(b);
      });
    }
    function renderList() {
      listEl.innerHTML = '';
      ITEMS.forEach(function (it, idx) {
        if (it.cat !== cur) return;
        var li = document.createElement('li'), t = document.createElement('div');
        t.innerHTML = '<b></b>' + (it.desc ? '<small></small>' : ''); t.querySelector('b').textContent = it.name; if (it.desc) t.querySelector('small').textContent = it.desc;
        var sz = document.createElement('div'); sz.className = 'sz';
        it.opts.forEach(function (o, oi) {
          var b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', 'Add ' + it.name + (o.l ? ' ' + o.l : '') + ' ' + money(o.p));
          b.innerHTML = (o.l ? '<i>' + o.l + '</i>' : '') + money(o.p);
          b.onclick = function () { var k = idx + ':' + oi; cart[k] = (cart[k] || 0) + 1; renderCart(); }; sz.appendChild(b);
        });
        li.appendChild(t); li.appendChild(sz); listEl.appendChild(li);
      });
    }
    function renderCart() {
      var keys = Object.keys(cart).filter(function (k) { return cart[k] > 0; }), tot = 0;
      cartEl.innerHTML = '';
      if (!keys.length) cartEl.innerHTML = '<li class="empty">Nothing yet. Pick a pizza, a grinder, anything.</li>';
      keys.forEach(function (k) {
        var p = k.split(':'), it = ITEMS[+p[0]], o = it.opts[+p[1]], q = cart[k]; tot += o.p * q;
        var li = document.createElement('li');
        li.innerHTML = '<span></span><span class="q"><button type="button" aria-label="Remove one">−</button><span>' + q + '</span><button type="button" aria-label="Add one">+</button></span>';
        li.firstChild.textContent = it.name + (o.l ? ' (' + o.l + ')' : '') + ' · ' + money(o.p * q);
        var bs = li.querySelectorAll('button'); bs[0].onclick = function () { cart[k]--; renderCart(); }; bs[1].onclick = function () { cart[k]++; renderCart(); };
        cartEl.appendChild(li);
      });
      var pts = Math.floor(tot + 1e-9);
      $('#lp-total').textContent = money(tot); $('#lp-pts').textContent = pts.toLocaleString();
      var nxt = null; RW.forEach(function (r) { if (!nxt && r[0] > pts) nxt = r; });
      $('#lp-next').textContent = !keys.length ? 'Start with any item to climb.' : nxt ? (nxt[0] > 5000 ? 'Only ' + (nxt[0] - pts).toLocaleString() + ' points to the Porsche. Kidding. Mostly.' : (nxt[0] - pts) + ' more point' + (nxt[0] - pts === 1 ? '' : 's') + ' to ' + nxt[1].toLowerCase() + ' (' + nxt[0] + ').') : 'You have climbed the whole ladder.';
      [].forEach.call($('#lp-rungs').children, function (li, i) { li.classList.toggle('on', RW[i][0] <= pts && pts > 0); });
    }
    var rg = $('#lp-rungs'); RW.forEach(function (r) { var li = document.createElement('li'); if (r[0] > 5000) li.className = 'joke'; li.innerHTML = '<b></b><span></span>'; li.firstChild.textContent = r[0].toLocaleString(); li.lastChild.textContent = r[1]; rg.appendChild(li); });
    $('#lp-clear').onclick = function () { cart = {}; renderCart(); };
    renderTabs(); renderList(); renderCart();
  }
  /* ---- menu search ---- */
  var q = $('#m-q');
  if (q) q.addEventListener('input', function () {
    var v = q.value.trim().toLowerCase(), shown = 0;
    [].forEach.call(document.querySelectorAll('.m-it'), function (e) { var ok = !v || e.getAttribute('data-t').indexOf(v) > -1; e.hidden = !ok; if (ok) shown++; });
    [].forEach.call(document.querySelectorAll('[data-cat]'), function (c) { c.hidden = !c.querySelector('.m-it:not([hidden])'); });
    $('#m-count').textContent = v ? shown + ' match' + (shown === 1 ? '' : 'es') : ''; $('#m-empty').hidden = shown > 0;
  });
  /* ---- lunch badge (Mon-Fri 11:00-14:30 New York) ---- */
  var lb = document.querySelector('[data-lunch]');
  if (lb) {
    var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
    p.forEach(function (x) { o[x.type] = x.value; });
    var m = (+o.hour % 24) * 60 + +o.minute, wk = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].indexOf(o.weekday) > -1;
    if (wk && m >= 660 && m < 870) lb.textContent = 'Lunch special on right now · until 2:30';
  }
  /* ---- parallax ---- */
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var els = [].slice.call(document.querySelectorAll('[data-par]')), tick = false;
    var run = function () {
      tick = false; var vh = window.innerHeight;
      els.forEach(function (s) {
        var r = s.getBoundingClientRect(); if (r.bottom < -100 || r.top > vh + 100) return;
        var c = (r.top + r.height / 2 - vh / 2);
        [].forEach.call(s.querySelectorAll('[data-depth]'), function (e) { e.style.transform = 'translate3d(0,' + (c * +e.getAttribute('data-depth')).toFixed(1) + 'px,0)'; });
      });
    };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
  }
})();
