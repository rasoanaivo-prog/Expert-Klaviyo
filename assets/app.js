(() => {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#mobile-nav');
  const closeMenu = () => { menu.hidden = true; toggle.setAttribute('aria-expanded', 'false'); };
  toggle.addEventListener('click', () => {
    const opening = toggle.getAttribute('aria-expanded') !== 'true';
    menu.hidden = !opening;
    toggle.setAttribute('aria-expanded', String(opening));
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && !menu.hidden) { closeMenu(); toggle.focus(); }
  });
  matchMedia('(min-width: 901px)').addEventListener('change', e => { if (e.matches) closeMenu(); });
  document.querySelectorAll('[data-language]').forEach(a => a.addEventListener('click', () => {
    const target = new URL(a.href);
    target.hash = location.hash;
    a.href = target.href;
  }));
  const dialog = document.querySelector('#proof-dialog');
  const dialogImage = dialog.querySelector('img');
  const transcript = dialog.querySelector('.transcript');
  const dialogLabel = dialog.querySelector('#dialog-label');
  const defaultLabel = dialogLabel.textContent;
  let opener;
  document.querySelectorAll('[data-proof]').forEach(button => button.addEventListener('click', () => {
    opener = button;
    dialogLabel.textContent = button.dataset.modalLabel || defaultLabel;
    dialog.classList.toggle('media-wide', button.dataset.view === 'wide');
    dialog.classList.toggle('media-design', button.dataset.view === 'design');
    dialogImage.src = button.dataset.proof;
    dialogImage.alt = button.querySelector('img').alt;
    transcript.replaceChildren(document.querySelector(button.dataset.transcript).content.cloneNode(true));
    dialog.showModal();
    dialog.scrollTop = 0;
    document.body.classList.add('dialog-open');
  }));
  dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', e => {
    if (e.target !== dialog) return;
    const r = dialog.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => { document.body.classList.remove('dialog-open'); opener?.focus(); });
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
    }), { threshold: .08 });
    document.querySelectorAll('.reveal').forEach(el => { el.classList.add('ready'); observer.observe(el); });
  }
})();
