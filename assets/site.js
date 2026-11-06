/* Existing Google Ads identifiers are preserved. Outbound clicks are NOT sales. */
(() => {
  'use strict';
  const ADS_ID = 'AW-17961565555';
  const CLICK_ACTION = 'AW-17961565555/98brCNTlyZ4cEPP63vRC';
  const KEY = 'mega7-ads-choice-v1';
  const panel = document.getElementById('consent');
  let choice = null;
  let loaded = false;
  try { choice = localStorage.getItem(KEY); } catch { /* Choice remains session-only. */ }
  function enableAds() {
    if (loaded) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ADS_ID);
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + ADS_ID;
    document.head.appendChild(script);
  }
  function setChoice(value) {
    choice = value;
    try { localStorage.setItem(KEY, value); } catch { /* No persistent storage available. */ }
    panel.hidden = true;
    if (value === 'granted') enableAds();
    else if (loaded) window.location.reload();
    document.getElementById('privacy-settings').focus({ preventScroll: true });
  }
  document.getElementById('accept-ads').addEventListener('click', () => setChoice('granted'));
  document.getElementById('decline-ads').addEventListener('click', () => setChoice('denied'));
  document.getElementById('privacy-settings').addEventListener('click', () => {
    panel.hidden = false;
    document.getElementById('decline-ads').focus({ preventScroll: true });
  });
  if (choice === 'granted') enableAds();
  if (choice !== 'granted' && choice !== 'denied') panel.hidden = false;
  document.querySelectorAll('a.affiliate').forEach(link => {
    link.addEventListener('click', () => {
      // Never delay or prevent the native link, including when the tag is blocked.
      if (choice === 'granted' && typeof window.gtag === 'function') {
        window.gtag('event', 'conversion', {
          send_to: CLICK_ACTION,
          event_label: 'outbound_affiliate_click',
          placement: link.dataset.placement
        });
      }
    });
  });
})();
