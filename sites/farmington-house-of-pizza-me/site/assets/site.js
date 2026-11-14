(function(){
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return[].slice.call((r||document).querySelectorAll(s))};
var bg=$('.burger'),nav=$('#nav');bg.addEventListener('click',function(){var o=nav.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
$$('#nav a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');bg.setAttribute('aria-expanded',false)})});
var tabs=$$('.tabs button'),panels=$$('.panel'),q=$('#q'),none=$('#none');
function show(i){tabs.forEach(function(b,k){b.setAttribute('aria-selected',k==i)});panels.forEach(function(p,k){p.hidden=k!=i})}
if($('#q')){tabs.forEach(function(b){b.addEventListener('click',function(){q.value='';filter();show(+b.dataset.t)})});
function filter(){var v=q.value.trim().toLowerCase(),n=0;
 if(!v){$$('.items li').forEach(function(l){l.hidden=false});none.hidden=true;var a=tabs.filter(function(b){return b.getAttribute('aria-selected')=='true'})[0];show(a?+a.dataset.t:0);return}
 panels.forEach(function(p){var c=0;$$('li',p).forEach(function(l){var m=l.dataset.s.indexOf(v)>-1;l.hidden=!m;if(m)c++});p.hidden=!c;n+=c});none.hidden=n>0}
q.addEventListener('input',filter)}
var st=$('#status'),H=JSON.parse(st.dataset.hours||'[]');
function f(t){var p=t.split(':'),h=+p[0],m=+p[1],ap=h>=12?'PM':'AM';h=h%12||12;return h+(m?':'+('0'+m).slice(-2):'')+' '+ap}
try{var d=new Date(new Date().toLocaleString('en-US',{timeZone:'America/New_York'})),dow=d.getDay(),mins=d.getHours()*60+d.getMinutes(),msg='',
 row=$('.hrs tr[data-dow="'+dow+'"]');if(row)row.className='today';
 var today=H.filter(function(h){return h.dow.indexOf(dow)>-1})[0];
 if(!H.length){}else if(today){var o=+today.open.split(':')[0]*60+ +today.open.split(':')[1],c=+today.close.split(':')[0]*60+ +today.close.split(':')[1];
  msg=mins>=o&&mins<c?'Open now · until '+f(today.close):mins<o?'Closed · opens today at '+f(today.open):'Closed now'}else msg='Closed today';
 if(msg)st.textContent=msg}catch(e){}
})();
