/**
 * ═══════════════════════════════════════════════════════════════
 * MATTERA SYSTEMS · Links de pago
 *
 * PEGA AQUÍ los tres links de pago de Mercado Pago y listo: los botones
 * "Contratar" empezarán a cobrar en línea automáticamente.
 *
 * Mientras estén vacíos, los botones siguen yendo a WhatsApp como hoy.
 * Así el sitio nunca queda con un botón roto: o cobra, o conversa.
 *
 * Dónde salen: Mercado Pago → Herramientas para vender → Link de pago.
 * Cada link debe llevar `external_reference` = t1 / t2 / t3, porque es lo
 * único que le dice al webhook qué plan se compró.
 * (Ver pagos/worker/README.md)
 * ═══════════════════════════════════════════════════════════════
 */
window.MATTERA_PAGOS = {
  t1: 'https://mpago.la/1bwWWsK', // $5,900  · verificado en el checkout
  t2: 'https://mpago.la/2NWNhHr', // $9,900  · verificado en el checkout
  t3: 'https://mpago.la/31qnam6', // $19,900 · verificado en el checkout
};

(function () {
  'use strict';
  var links = window.MATTERA_PAGOS || {};

  document.addEventListener('DOMContentLoaded', function () {
    var botones = document.querySelectorAll('[data-plan]');
    for (var i = 0; i < botones.length; i++) {
      var b = botones[i];
      var url = links[b.getAttribute('data-plan')];
      if (!url) continue; // sin configurar: se queda el enlace a WhatsApp

      b.href = url;
      // el pago abre en la misma pestaña: perder el contexto a media compra
      // hace que la gente abandone
      b.removeAttribute('target');
      b.removeAttribute('rel');

      var texto = b.querySelector('span') || b;
      if (/contratar/i.test(texto.textContent)) texto.textContent = 'Contratar y pagar →';
    }
  });
})();
