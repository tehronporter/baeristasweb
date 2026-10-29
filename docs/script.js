const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#main-nav');
function closeMenu(restoreFocus=false){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation');toggle.querySelector('span').textContent='＋';if(restoreFocus)toggle.focus()}
toggle.addEventListener('click',()=>{if(toggle.getAttribute('aria-expanded')==='true')return closeMenu();nav.classList.add('open');toggle.setAttribute('aria-expanded','true');toggle.setAttribute('aria-label','Close navigation');toggle.querySelector('span').textContent='−'});
nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{closeMenu();const target=document.querySelector(link.hash);if(target){target.setAttribute('tabindex','-1');target.focus({preventScroll:true})}}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true')closeMenu(true)});
const media=window.matchMedia('(max-width: 700px)');
media.addEventListener('change',e=>{if(!e.matches)closeMenu();updateVisit()});
const visit=document.querySelector('.mobile-visit');
const visibleRegions=new Map();
function updateVisit(){
  const show=media.matches && visibleRegions.size===4 && ![...visibleRegions.values()].some(Boolean);
  visit.classList.toggle('visible',show);
  visit.setAttribute('aria-hidden',String(!show));
  visit.tabIndex=show?0:-1;
}
if('IntersectionObserver' in window){
  const observer=new IntersectionObserver(entries=>{
    entries.forEach(entry=>visibleRegions.set(entry.target,entry.isIntersecting));
    updateVisit();
  },{threshold:0,rootMargin:'0px 0px 80px 0px'});
  ['.hero','#locations','.closing','.footer'].forEach(selector=>observer.observe(document.querySelector(selector)));
}
