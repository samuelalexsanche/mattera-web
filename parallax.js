/* ═══════════════════════════════════════════════════════════════
   MATTERA SYSTEMS · parallax.js
   Fondos de arte con parallax de scroll para secciones.

   Uso:  <section class="section sec-dark px" data-px="sistemas">
   El script inyecta la capa de imagen; el HTML solo declara el motivo.

   Motivos disponibles (art/*.webp):
     hero · sistemas · industrias · editorial · planes · cierre

   Notas de diseño:
   - La capa va DEBAJO del contenido y por encima del fondo de la sección.
     La opacidad se define en CSS (--px-op) para no romper el contraste AA.
   - Solo se animan las secciones visibles (IntersectionObserver).
   - Se desactiva con prefers-reduced-motion y en pantallas muy angostas,
     donde el parallax cuesta batería y no aporta.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hosts = [];

  function build() {
    var nodes = document.querySelectorAll('.px[data-px]');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (el.querySelector(':scope > .px-bg')) continue;

      var art = el.getAttribute('data-px');
      var layer = document.createElement('div');
      layer.className = 'px-bg';
      layer.setAttribute('aria-hidden', 'true');
      layer.style.backgroundImage = 'url("/art/' + art + '.webp")';
      // se inserta primero para quedar detrás del contenido
      el.insertBefore(layer, el.firstChild);

      hosts.push({ el: el, layer: layer, depth: parseFloat(el.getAttribute('data-px-depth')) || 0.18, on: false });
    }
  }

  function observe() {
    if (!('IntersectionObserver' in window)) {
      for (var i = 0; i < hosts.length; i++) hosts[i].on = true;
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        var e = entries[i];
        for (var j = 0; j < hosts.length; j++) {
          if (hosts[j].el === e.target) { hosts[j].on = e.isIntersecting; break; }
        }
      }
    }, { rootMargin: '120px 0px' });
    for (var k = 0; k < hosts.length; k++) io.observe(hosts[k].el);
  }

  // Se evalúa en cada frame, no solo al cargar: así el parallax se activa o
  // se apaga al redimensionar o girar el dispositivo, sin recargar.
  function animable() {
    return !REDUCED && window.innerWidth >= 600;
  }

  var queued = false;
  function onScroll() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(update);
  }

  function update() {
    queued = false;
    if (!animable()) {
      // se limpian los transforms para que las capas queden centradas
      for (var n = 0; n < hosts.length; n++) hosts[n].layer.style.transform = '';
      return;
    }
    var vh = window.innerHeight;
    for (var i = 0; i < hosts.length; i++) {
      var h = hosts[i];
      if (!h.on) continue;
      var r = h.el.getBoundingClientRect();
      // progreso: +0.5 cuando la sección entra por abajo, -0.5 cuando sale por arriba
      var prog = ((vh - r.top) / (vh + r.height)) - 0.5;
      // la capa tiene 12% de holgura arriba y abajo; el tope se queda dentro
      var ty = -prog * h.depth * r.height;
      h.layer.style.transform = 'translate3d(0,' + ty.toFixed(1) + 'px,0)';
    }
  }

  function init() {
    build();
    if (!hosts.length) return;
    observe();
    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    window.addEventListener('orientationchange', onScroll, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
