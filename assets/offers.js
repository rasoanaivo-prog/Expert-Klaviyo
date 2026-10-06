(() => {
  let opener = null;
  document.querySelectorAll('[data-open-offer]').forEach(button => {
    button.addEventListener('click', () => {
      const dialog = document.getElementById(button.dataset.openOffer);
      if (!dialog || dialog.open) return;
      opener = button;
      dialog.showModal();
      dialog.scrollTop = 0;
      document.body.classList.add('offer-dialog-open');
    });
  });
  document.querySelectorAll('.offer-dialog').forEach(dialog => {
    dialog.querySelector('[data-close-offer]').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right ||
          event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    });
    dialog.addEventListener('close', () => {
      document.body.classList.remove('offer-dialog-open');
      opener?.focus({ preventScroll: true });
    });
  });
})();
