(() => {
  document.querySelectorAll('[data-calendly]').forEach(link => {
    link.addEventListener('click', event => {
      // Keep the real link usable if the widget is blocked or not loaded yet.
      if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey ||
          event.shiftKey || event.altKey || !window.Calendly?.initPopupWidget) return;
      event.preventDefault();
      if (document.querySelector('.calendly-overlay')) return;

      const offer = link.closest('dialog');
      const returnTo = offer
        ? document.querySelector(`[data-open-offer="${offer.id}"]`)
        : link;
      const openBooking = () => {
        try {
          window.Calendly.initPopupWidget({ url: link.href });
        } catch {
          window.location.assign(link.href);
          return;
        }
        const overlay = document.querySelector('.calendly-overlay');
        if (!overlay) {
          window.location.assign(link.href);
          return;
        }
        const observer = new MutationObserver(() => {
          if (overlay.isConnected) return;
          observer.disconnect();
          returnTo?.focus({ preventScroll: true });
        });
        observer.observe(document.body, { childList: true });
      };

      // Native offer dialogs sit above regular overlays: close them first.
      if (offer?.open) {
        offer.addEventListener('close', openBooking, { once: true });
        offer.close();
      } else {
        openBooking();
      }
    });
  });
})();
