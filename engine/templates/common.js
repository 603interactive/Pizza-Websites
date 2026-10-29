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
