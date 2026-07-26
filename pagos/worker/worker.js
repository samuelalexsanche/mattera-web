/**
 * ═══════════════════════════════════════════════════════════════
 * MATTERA SYSTEMS · Webhook de pagos (Mercado Pago)
 * Cloudflare Worker
 *
 * Qué hace, en orden:
 *   1. Valida la firma HMAC-SHA256 del header x-signature.
 *   2. Consulta el pago REAL en la API de Mercado Pago.
 *   3. Si quedó aprobado, avisa por Telegram con plan, monto y MSI.
 *   4. Responde 200 (si algo falla responde 500 para que MP reintente).
 *
 * ── Por qué se consulta la API en el paso 2 ──────────────────────
 * El cuerpo del webhook solo trae un id. NUNCA se debe confiar en él
 * para montos ni estatus: quien conozca la URL podría inventar un
 * "pago aprobado". El monto y el estatus se leen siempre de la API.
 *
 * ── Secretos (se configuran con `wrangler secret put`, nunca en git) ──
 *   MP_ACCESS_TOKEN     Access token de producción de Mercado Pago
 *   MP_WEBHOOK_SECRET   "Clave secreta" del webhook en Tus integraciones
 *   TELEGRAM_BOT_TOKEN  Token del bot que recibe el aviso
 *   TELEGRAM_CHAT_ID    Chat al que se manda el aviso
 *
 * ── Opcional ────────────────────────────────────────────────────
 *   KV binding `PAGOS`  Para no avisar dos veces del mismo pago.
 *                       Sin él el Worker funciona, pero MP puede
 *                       notificar varias veces el mismo pago.
 * ═══════════════════════════════════════════════════════════════
 */

// Base de la API. Se puede sobrescribir con MP_API_BASE para poder
// probar el flujo completo contra un servidor simulado en local.
const MP_API_DEFAULT = 'https://api.mercadopago.com';

// Los planes viven aquí para poder validar que el monto cobrado
// corresponde al plan, y detectar un link mal configurado.
const PLANES = {
  t1: { nombre: 'T1 · Presencia', monto: 5900 },
  t2: { nombre: 'T2 · Sistema', monto: 9900 },
  t3: { nombre: 'T3 · Operación', monto: 19900 },
};

export default {
  async fetch(request, env) {
    if (request.method === 'GET') {
      // sonda de vida, para comprobar que el Worker está desplegado
      return json({ ok: true, servicio: 'mattera-pagos' });
    }
    if (request.method !== 'POST') {
      return json({ error: 'method not allowed' }, 405);
    }

    try {
      return await manejar(request, env);
    } catch (err) {
      console.error('fallo no controlado:', err && err.stack || err);
      // 500 -> Mercado Pago reintenta cada 15 min
      return json({ error: 'internal' }, 500);
    }
  },
};

async function manejar(request, env) {
  const url = new URL(request.url);
  const raw = await request.text();

  // ── 1. Validar firma ──────────────────────────────────────────
  // El manifest de MP es:  id:<data.id>;request-id:<x-request-id>;ts:<ts>;
  // El data.id se toma del QUERY STRING, no del cuerpo.
  const firma = request.headers.get('x-signature') || '';
  const requestId = request.headers.get('x-request-id') || '';
  const dataId = url.searchParams.get('data.id') || url.searchParams.get('id') || '';

  if (!env.MP_WEBHOOK_SECRET) {
    console.error('falta MP_WEBHOOK_SECRET');
    return json({ error: 'not configured' }, 500);
  }

  const valida = await firmaValida(firma, requestId, dataId, env.MP_WEBHOOK_SECRET);
  if (!valida) {
    console.warn('firma inválida', { requestId, dataId });
    // 401 y NO 500: no queremos que reintente algo que nunca va a validar
    return json({ error: 'invalid signature' }, 401);
  }

  // ── 2. Solo nos interesan notificaciones de pago ───────────────
  let cuerpo = {};
  try { cuerpo = JSON.parse(raw || '{}'); } catch { /* body vacío es posible */ }
  const tipo = cuerpo.type || url.searchParams.get('type') || '';
  if (tipo !== 'payment') {
    return json({ ok: true, ignorado: tipo || 'sin tipo' });
  }

  const pagoId = String((cuerpo.data && cuerpo.data.id) || dataId || '');
  if (!pagoId) return json({ ok: true, ignorado: 'sin id' });

  // ── 3. Evitar avisos duplicados (si hay KV) ─────────────────────
  if (env.PAGOS) {
    const yaVisto = await env.PAGOS.get('avisado:' + pagoId);
    if (yaVisto) return json({ ok: true, duplicado: pagoId });
  }

  // ── 4. Consultar el pago real en la API ────────────────────────
  const pago = await consultarPago(pagoId, env.MP_ACCESS_TOKEN, env.MP_API_BASE);
  if (!pago) return json({ error: 'no se pudo leer el pago' }, 500);

  if (pago.status !== 'approved') {
    // pendiente, rechazado, en revisión: se acusa recibo y no se avisa
    return json({ ok: true, estatus: pago.status });
  }

  // ── 5. Avisar ──────────────────────────────────────────────────
  await avisar(pago, env);

  if (env.PAGOS) {
    // 60 días es de sobra: los reintentos de MP duran horas, no meses
    await env.PAGOS.put('avisado:' + pagoId, '1', { expirationTtl: 60 * 60 * 24 * 60 });
  }

  return json({ ok: true, pago: pagoId });
}

/** Valida el HMAC del header x-signature (formato `ts=...,v1=...`). */
async function firmaValida(headerFirma, requestId, dataId, secreto) {
  const partes = {};
  for (const trozo of headerFirma.split(',')) {
    const i = trozo.indexOf('=');
    if (i > 0) partes[trozo.slice(0, i).trim()] = trozo.slice(i + 1).trim();
  }
  const ts = partes.ts;
  const v1 = partes.v1;
  if (!ts || !v1) return false;

  // MP documenta el id en minúsculas; si viene con mayúsculas la firma falla.
  const id = String(dataId).toLowerCase();
  const manifest = `id:${id};request-id:${requestId};ts:${ts};`;

  const key = await crypto.subtle.importKey(
    'raw',
    new TextEncoder().encode(secreto),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign'],
  );
  const mac = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(manifest));
  const esperado = [...new Uint8Array(mac)]
    .map((b) => b.toString(16).padStart(2, '0'))
    .join('');

  return comparaSegura(esperado, v1.toLowerCase());
}

/** Comparación en tiempo constante: no revela el prefijo correcto. */
function comparaSegura(a, b) {
  if (a.length !== b.length) return false;
  let dif = 0;
  for (let i = 0; i < a.length; i++) dif |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return dif === 0;
}

async function consultarPago(id, token, base) {
  if (!token) { console.error('falta MP_ACCESS_TOKEN'); return null; }
  const res = await fetch(`${base || MP_API_DEFAULT}/v1/payments/${encodeURIComponent(id)}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) {
    console.error('MP respondió', res.status, await res.text().catch(() => ''));
    return null;
  }
  return res.json();
}

/**
 * Averigua qué plan se compró.
 *
 * Primero por `external_reference` (t1/t2/t3), que es lo confiable. Si el
 * panel de Mercado Pago no permitió capturarla al crear el link, se cae al
 * monto: los tres precios son distintos, así que identifican el plan sin
 * ambigüedad. Devuelve también cómo se identificó, para poder avisar cuando
 * fue por monto y convenga arreglar el link.
 */
function identificarPlan(pago) {
  const ref = String(pago.external_reference || '').toLowerCase();
  if (PLANES[ref]) return { plan: PLANES[ref], via: 'referencia', ref };

  const monto = Number(pago.transaction_amount || 0);
  for (const clave of Object.keys(PLANES)) {
    if (Math.abs(monto - PLANES[clave].monto) < 1) {
      return { plan: PLANES[clave], via: 'monto', ref };
    }
  }
  return { plan: null, via: 'ninguna', ref };
}

async function avisar(pago, env) {
  const { plan, via, ref } = identificarPlan(pago);
  const monto = Number(pago.transaction_amount || 0);
  const cuotas = Number(pago.installments || 1);
  const neto = pago.transaction_details && pago.transaction_details.net_received_amount;

  const avisos = [];
  // Se identificó por monto: el pago es válido, pero al link le falta la
  // referencia y conviene ponerla para no depender del precio.
  if (plan && via === 'monto') {
    avisos.push(`ℹ️ Identificado por monto${ref ? ` (la referencia decía "${ref}")` : ' (el link no trae external_reference)'}. Ponle la referencia al link.`);
  }
  // Referencia válida pero monto distinto: link mal configurado.
  if (plan && via === 'referencia' && Math.abs(monto - plan.monto) > 1) {
    avisos.push(`⚠️ El monto no coincide con ${plan.nombre} ($${plan.monto.toLocaleString('es-MX')}). Revisa el link de pago.`);
  }
  // Ni referencia ni monto conocido: probablemente el link sin monto definido
  // (cotización a medida). Es legítimo, solo hay que saber que no es un plan.
  if (!plan) {
    avisos.push('ℹ️ No corresponde a T1/T2/T3 — seguramente es una cotización a medida.');
  }
  const alerta = avisos.length ? '\n' + avisos.join('\n') : '';

  const lineas = [
    '💰 *Pago aprobado*',
    '',
    `*Plan:* ${plan ? plan.nombre : 'a medida / sin identificar'}`,
    `*Monto:* $${monto.toLocaleString('es-MX')} ${pago.currency_id || 'MXN'}`,
    `*Pago:* ${cuotas > 1 ? `${cuotas} MSI` : 'una sola exhibición'}`,
    neto != null ? `*Te llega:* $${Number(neto).toLocaleString('es-MX')} (ya sin comisión)` : null,
    '',
    `*Cliente:* ${(pago.payer && pago.payer.email) || 'sin correo'}`,
    (pago.payer && (pago.payer.first_name || pago.payer.last_name))
      ? `*Nombre:* ${[pago.payer.first_name, pago.payer.last_name].filter(Boolean).join(' ')}` : null,
    `*Método:* ${pago.payment_method_id || '?'}`,
    `*ID:* \`${pago.id}\``,
    alerta,
  ].filter(Boolean);

  await notificarTelegram(lineas.join('\n'), env);
}

async function notificarTelegram(texto, env) {
  if (!env.TELEGRAM_BOT_TOKEN || !env.TELEGRAM_CHAT_ID) {
    console.warn('Telegram sin configurar; el aviso solo queda en el log');
    console.log(texto);
    return;
  }
  const res = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: env.TELEGRAM_CHAT_ID,
      text: texto,
      parse_mode: 'Markdown',
      disable_web_page_preview: true,
    }),
  });
  if (!res.ok) {
    // se lanza para que el Worker devuelva 500 y MP reintente el aviso
    throw new Error('Telegram falló: ' + res.status + ' ' + await res.text().catch(() => ''));
  }
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}
