const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#main-nav');
function closeMenu(restoreFocus=false){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation');toggle.querySelector('span').textContent='＋';if(restoreFocus)toggle.focus()}
toggle.addEventListener('click',()=>{if(toggle.getAttribute('aria-expanded')==='true')return closeMenu();nav.classList.add('open');toggle.setAttribute('aria-expanded','true');toggle.setAttribute('aria-label','Close navigation');toggle.querySelector('span').textContent='−'});
nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{closeMenu();const target=document.querySelector(link.hash);if(target){target.setAttribute('tabindex','-1');target.focus({preventScroll:true})}}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true')closeMenu(true)});
const media=window.matchMedia('(max-width: 600px)');
media.addEventListener('change',e=>{if(!e.matches)closeMenu();updateVisit()});
const visit=document.querySelector('.mobile-visit');let heroVisible=true;let locationsVisible=false;
function updateVisit(){const show=media.matches&&!heroVisible&&!locationsVisible;visit.classList.toggle('visible',show);visit.setAttribute('aria-hidden',String(!show));visit.tabIndex=show?0:-1}
const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.target.classList.contains('hero'))heroVisible=entry.isIntersecting;else locationsVisible=entry.isIntersecting});updateVisit()},{threshold:0});
observer.observe(document.querySelector('.hero'));observer.observe(document.querySelector('#locations'));
