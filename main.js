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
  const body      = document.getElementById('chatBody');
  const footerEl  = document.getElementById('chatFooterText');
  const inputEl   = document.getElementById('chatInput');
  const sendBtn   = document.getElementById('chatSend');
  if (!body) return;

  const msgs = [
    { type: 'client',    text: '¿Tienen disponibilidad para mañana a las 10?',                           delay: 600  },
    { type: 'assistant', text: 'Sí. Mañana tenemos 10:00 y 12:30. ¿Te agendo a las 10:00 a nombre tuyo?', delay: 1800 },
    { type: 'system',    text: 'cita confirmada · CRM actualizado · 0 intervención humana',               delay: 3000 },
  ];

  /* Guion animado — solo corre cuando NO hay endpoint real */
  function playDemoScript() {
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

  if (window.MATTERA_AGENT_ENDPOINT) {
    /* ── Modo agente real ──────────────────────────────────────── */
    if (footerEl) footerEl.textContent = 'Este asistente es el producto. Pruébalo.';
    if (inputEl)  { inputEl.disabled = false; inputEl.placeholder = 'Escríbele al asistente…'; }
    if (sendBtn)  sendBtn.disabled = false;

    function appendBubble(type, text) {
      const b = document.createElement('div');
      b.className = 'chat-bubble chat-bubble-' + type;
      b.textContent = text;
      body.appendChild(b);
      body.scrollTop = body.scrollHeight;
    }

    const sessionId = sessionStorage.getItem('ms_cid') || (()=>{
      const id = crypto.randomUUID();
      sessionStorage.setItem('ms_cid', id);
      return id;
    })();

    function sendMessage() {
      const text = (inputEl ? inputEl.value.trim() : '');
      if (!text) return;
      appendBubble('client', text);
      if (inputEl) inputEl.value = '';
      if (inputEl) inputEl.disabled = true;
      if (sendBtn) sendBtn.disabled = true;

      fetch(window.MATTERA_AGENT_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sessionId, message: text }),
      })
        .then(r => r.json())
        .then(data => appendBubble('assistant', data.response || data.reply || data.output || ''))
        .catch(() => {
          const b = document.createElement('div');
          b.className = 'chat-bubble chat-bubble-system';
          b.innerHTML = 'Error al conectar. <a href="https://wa.me/523327874747" target="_blank" rel="noopener noreferrer" style="color:var(--bt-orange)">WhatsApp →</a>';
          body.appendChild(b);
          body.scrollTop = body.scrollHeight;
        })
        .finally(() => {
          if (inputEl) inputEl.disabled = false;
          if (sendBtn) sendBtn.disabled = false;
          if (inputEl) inputEl.focus();
        });
    }

    if (sendBtn)  sendBtn.addEventListener('click', sendMessage);
    if (inputEl)  inputEl.addEventListener('keydown', e => { if (e.key === 'Enter') sendMessage(); });

  } else {
    /* ── Modo demo (endpoint no existe) ───────────────────────── */
    playDemoScript();
  }
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

/* ─── CARD DECK (secciones 7, 8, 9) ─────────────────────────── */
/*
 * Mecánica: la zona tiene 300 vh de scroll.
 * t = (px scrollados dentro de la zona) / vh   →   t ∈ [0, N-1]
 * depth de la carta i en el tiempo t: d = i - t
 *   d = 0  →  frente  (front card, escala 1, opacidad 1)
 *   d = 1  →  medio   (scale .92, ty -16 px, opacidad .62)
 *   d = 2  →  atrás   (scale .84, ty -32 px, opacidad .35)
 *   d < 0  →  saliendo (escala y opacidad decrecen, sube y desaparece)
 */
function initCardDeck() {
  const zone  = document.querySelector('.card-deck-zone');
  const inner = document.querySelector('.card-deck-inner');
  if (!zone || !inner || REDUCED) return;
  if (window.innerWidth <= 768) return;   // CSS ya desactiva el efecto en mobile

  const cards = Array.from(inner.querySelectorAll('.card-in-deck'));
  const N     = cards.length;             // 3

  // Lookup table de transforms por depth
  function depthToStyle(d) {
    if (d > N) return { s: 0.84 - (d - N) * 0.04, ty: -32, op: 0 };

    if (d < 0) {
      // Carta saliendo: sale HACIA ARRIBA y encoge
      const t   = Math.min(1, -d);                 // 0→1 mientras d va 0→-1
      const e   = easeOut(t);
      return {
        s:  1 - e * 0.14,                          // 1.0 → 0.86
        ty: -(e * 90),                              // sube hasta -90 px
        op: 1 - e,                                  // desvanece
      };
    }

    // Cartas en la baraja: d ∈ [0, N-1]
    const e  = easeOut(Math.min(d, 1));             // suaviza la interpolación cercana al frente
    const dC = Math.max(0, d);
    return {
      s:  1   - dC * 0.080,                        // 1.00 → 0.84
      ty: -dC * 16,                                 // 0 → -32 px (las traseras "flotan" un poco más arriba)
      op: 1   - dC * 0.325,                         // 1.00 → 0.35
    };
  }

  function update() {
    const vh      = window.innerHeight;
    const zRect   = zone.getBoundingClientRect();
    // t: progreso lineal de la zona bajo el viewport
    // ── Progreso con fase estable + fase de transición ──────────
    //   STABLE  : carta frontal fija  (1.0 × vh de scroll)
    //   TRANSIT : animación al frente (1.5 × vh de scroll)
    //   SLOT    : total por carta     (2.5 × vh)
    //   Zona CSS debe ser: 100vh + (N-1)*SLOT*100vh = 600vh
    const STABLE   = vh * 1.0;
    const TRANSIT  = vh * 1.5;
    const SLOT     = STABLE + TRANSIT;           // 2.5 × vh
    const scrolled = Math.max(0, -zRect.top);    // px dentro de la zona

    const slotIdx  = Math.min(N - 2, Math.floor(scrolled / SLOT));
    const slotProg = (scrolled - slotIdx * SLOT) / SLOT;  // 0‥1 dentro del slot
    const sFrac    = STABLE / SLOT;              // 0.4 — fracción estable

    let t;
    if (scrolled >= SLOT * (N - 1)) {
      t = N - 1;                                 // última carta: queda al frente
    } else if (slotProg <= sFrac) {
      t = slotIdx;                               // fase estable: sin cambio
    } else {
      const p = (slotProg - sFrac) / (1 - sFrac);
      t = slotIdx + easeOut(p);                  // fase de transición
    }
    t = Math.max(0, Math.min(N - 1, t));

    cards.forEach((card, i) => {
      const d    = i - t;                           // depth continuo de esta carta
      const { s, ty, op } = depthToStyle(d);

      // z-index: carta con menor depth (más al frente) → número mayor
      const z    = Math.round(30 - d * 9);

      card.style.transform  = `translateY(${ty.toFixed(2)}px) scale(${s.toFixed(4)})`;
      card.style.opacity    = op.toFixed(3);
      card.style.zIndex     = z;

      // Solo la carta al frente permite scroll interno
      card.style.overflowY  = (d < 0.15) ? 'auto' : 'hidden';
    });
  }

  // También re-aplica si el viewport cambia de tamaño
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
    ticking = false;  // permit next
  }, { passive: true });
  window.addEventListener('resize', update, { passive: true });

  update();    // estado inicial correcto al cargar mid-page
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
  initCardDeck();
  initPricingParallax();
  initPricingCardTilt();
  // Patch after calcUpdate is defined (it's in inline script, already available at DOMContentLoaded)
  patchCalcUpdate();
});
