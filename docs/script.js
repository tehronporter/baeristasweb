const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
function closeMenu(restoreFocus = false) {
  nav.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-label', 'Open navigation');
  toggle.querySelector('span').textContent = '＋';
  if (restoreFocus) toggle.focus();
}
toggle.addEventListener('click', () => {
  if (toggle.getAttribute('aria-expanded') === 'true') return closeMenu();
  nav.classList.add('open');
  toggle.setAttribute('aria-expanded', 'true');
  toggle.setAttribute('aria-label', 'Close navigation');
  toggle.querySelector('span').textContent = '−';
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  closeMenu();
  const target = document.querySelector(link.hash);
  if (target) { target.setAttribute('tabindex', '-1'); target.focus({ preventScroll: true }); }
}));
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') closeMenu(true);
});
window.matchMedia('(min-width: 601px)').addEventListener('change', e => { if (e.matches) closeMenu(); });
