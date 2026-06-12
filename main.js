/* ═══════════════════════════════════════════════════════════════
   MATTERA SYSTEMS · main.js
   Animations: chat demo, counter, timeline, slider, scroll reveal
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ─── EASE-OUT CUBIC ─────────────────────────────────────────── */
function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

/* ─── COUNTER ANIMATION ──────────────────────────────────────── */
function animateCount(el, target, duration) {
  if (REDUCED) { el.textContent = target.toLocaleString('es-MX'); return; }
  const start = performance.now();
  (function tick(now) {
    const t = Math.min((now - start) / duration, 1);
    el.textContent = Math.round(easeOut(t) * target).toLocaleString('es-MX');
    if (t < 1) requestAnimationFrame(tick);
  })(start);
}

function initCounter() {
  const el = document.getElementById('heroCounter');
  if (!el) return;
  const target = parseInt(el.dataset.target || '312', 10);
  if (REDUCED) { el.textContent = target.toLocaleString('es-MX'); return; }
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      animateCount(el, target, 1200);
      obs.unobserve(e.target);
    });
  }, { threshold: 0.4 });
  obs.observe(el.closest('.hero-counter') || el);
}

/* ─── CHAT DEMO ──────────────────────────────────────────────── */
function initChatDemo() {
  const body = document.getElementById('chatBody');
  if (!body) return;

  const msgs = [
    { type: 'client',    text: '¿Tienen disponibilidad para mañana a las 10?',                           delay: 600  },
    { type: 'assistant', text: 'Sí. Mañana tenemos 10:00 y 12:30. ¿Te agendo a las 10:00 a nombre tuyo?', delay: 1800 },
    { type: 'system',    text: 'cita confirmada · CRM actualizado · 0 intervención humana',               delay: 3000 },
  ];

  if (REDUCED) {
    msgs.forEach(({ type, text }) => {
      const b = document.createElement('div');
      b.className = 'chat-bubble chat-bubble-' + type;
      b.textContent = text;
      body.appendChild(b);
    });
    return;
  }

  msgs.forEach(({ type, text, delay }) => {
    setTimeout(() => {
      const b = document.createElement('div');
      b.className = 'chat-bubble chat-bubble-' + type;
      b.textContent = text;
      b.style.cssText = 'opacity:0;transform:translateY(8px)';
      body.appendChild(b);
      requestAnimationFrame(() => requestAnimationFrame(() => {
        b.style.transition = 'opacity 250ms ease, transform 250ms ease';
        b.style.opacity = '1';
        b.style.transform = 'translateY(0)';
      }));
      body.scrollTop = body.scrollHeight;
    }, delay);
  });
}

/* ─── TIMELINE DRAW ──────────────────────────────────────────── */
function initTimeline() {
  const timelines = document.querySelectorAll('.timeline');
  if (!timelines.length) return;

  if (REDUCED) {
    timelines.forEach(tl => {
      tl.classList.add('tl-visible');
      tl.querySelectorAll('.timeline-node').forEach(n => n.classList.add('tl-node-visible'));
    });
    return;
  }

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const tl = e.target;
      tl.classList.add('tl-visible');
      tl.querySelectorAll('.timeline-node').forEach((node, i) => {
        setTimeout(() => node.classList.add('tl-node-visible'), 150 + i * 150);
      });
      obs.unobserve(tl);
    });
  }, { threshold: 0.25 });

  timelines.forEach(tl => obs.observe(tl));
}

/* ─── SLIDER PROGRESS ────────────────────────────────────────── */
function updateSliderPct(input) {
  const pct = ((input.value - input.min) / (input.max - input.min)) * 100;
  input.style.setProperty('--slider-pct', pct + '%');
}

function initSliders() {
  document.querySelectorAll('input[type="range"]').forEach(s => {
    updateSliderPct(s);
    s.addEventListener('input', () => updateSliderPct(s));
  });
}

/* ─── CALC VALUE FLASH ───────────────────────────────────────── */
function patchCalcUpdate() {
  const orig = window.calcUpdate;
  if (!orig || REDUCED) return;
  window.calcUpdate = function() {
    orig.call(this);
    ['resCostoActual','resDesarrollo','resOperativo',
     'resAhorroMensual','resAhorroAnual','resPayback','resHoras'].forEach(id => {
      const el = document.getElementById(id);
      if (!el) return;
      el.style.transition = 'opacity 120ms ease';
      el.style.opacity = '.3';
      setTimeout(() => { el.style.opacity = '1'; }, 120);
    });
    document.querySelectorAll('input[type="range"]').forEach(s => updateSliderPct(s));
  };
}

/* ─── SCROLL REVEAL (stagger on card groups) ─────────────────── */
function initRevealStagger() {
  if (REDUCED) return;
  // Add stagger delay to siblings inside grid containers
  document.querySelectorAll('.servicios-grid, .why-grid').forEach(grid => {
    grid.querySelectorAll('.reveal').forEach((el, i) => {
      el.style.transitionDelay = (el.style.transitionDelay ? 0 : i * 80) + 'ms';
    });
  });
}

/* ─── PRICING SECTION PARALLAX ──────────────────────────────── */
function initPricingParallax() {
  const section = document.getElementById('agenda');
  const layers  = section ? section.querySelectorAll('[data-pricing-depth]') : [];
  if (!layers.length || REDUCED) return;

  let ticking = false;

  function update() {
    const rect = section.getBoundingClientRect();
    // Only animate while section is in / near viewport
    if (rect.bottom < -200 || rect.top > window.innerHeight + 200) { ticking = false; return; }
    const progress = -rect.top / (section.offsetHeight || 1);

    layers.forEach(layer => {
      const depth = parseFloat(layer.dataset.pricingDepth || '0');
      const y = progress * depth * 120;
      layer.style.transform = `translateY(${y.toFixed(2)}px)`;
    });
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });

  // Initial position
  update();
}

/* ─── PRICING CARDS: subtle mouse tilt ──────────────────────── */
function initPricingCardTilt() {
  if (REDUCED) return;
  document.querySelectorAll('.pricing-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = ((e.clientX - r.left) / r.width  - 0.5) * 8;
      const y = ((e.clientY - r.top)  / r.height - 0.5) * 5;
      card.style.transform = `translateY(-6px) rotateX(${(-y).toFixed(2)}deg) rotateY(${x.toFixed(2)}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transition = 'transform 400ms ease';
      card.style.transform = '';
      setTimeout(() => { card.style.transition = ''; }, 400);
    });
    card.addEventListener('mouseenter', () => {
      card.style.transition = 'transform 120ms ease';
    });
  });
}

/* ─── INIT ───────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initCounter();
  initChatDemo();
  initTimeline();
  initSliders();
  initRevealStagger();
  initPricingParallax();
  initPricingCardTilt();
  // Patch after calcUpdate is defined (it's in inline script, already available at DOMContentLoaded)
  patchCalcUpdate();
});
