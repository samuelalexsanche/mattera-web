/* =====================================================================
   MATTERA SYSTEMS — Worker de contactos
   Worker: mattera-leads  →  https://mattera-leads.mattera.workers.dev

   Guarda los contactos que la gente deja en la página, en una base D1 de
   la propia cuenta: sin servicios de terceros, sin cookies y sin rastreo.

   La llave para consultar los contactos vive como SECRETO del Worker:
       npx wrangler secret put PANEL_KEY

   Rutas:
     POST /lead              — guarda un contacto (desde la página)
     GET  /export?key=...    — descarga todos los contactos en CSV
     GET  /contar?key=...    — cuántos van (para revisar sin descargar)
   ===================================================================== */

const ALLOWED_ORIGINS = [
  'https://matterasystems.com',
  'https://www.matterasystems.com',
  'https://demo.matterasystems.com',
  'https://samuelalexsanche.github.io',
  'http://localhost:4321',
  'http://127.0.0.1:4321',
];

const MAX_BODY_BYTES = 8 * 1024;
const LIMITES = { nombre: 80, telefono: 25, giro: 120, dolor: 400 };

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const cors = corsHeaders(origin);
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });

    // Consulta de contactos: la autoriza la llave, no el origen, porque se
    // abre directamente en el navegador o con curl.
    if (request.method === 'GET' && (url.pathname === '/export' || url.pathname === '/contar')) {
      if (!env.PANEL_KEY) return json({ error: 'Falta configurar PANEL_KEY.' }, 500, cors);
      if (url.searchParams.get('key') !== env.PANEL_KEY) {
        return json({ error: 'No autorizado.' }, 401, cors);
      }
      return url.pathname === '/contar' ? contar(env, cors) : exportar(env, cors);
    }

    if (request.method !== 'POST' || url.pathname !== '/lead') {
      return json({ error: 'No encontrado.' }, 404, cors);
    }

    // Igual que en el Worker del chat: sin Origin válido no se escribe nada,
    // para que la base no se llene desde fuera de la página.
    if (!isAllowed(origin)) return json({ error: 'Origen no autorizado.' }, 403, cors);

    if (Number(request.headers.get('Content-Length') || 0) > MAX_BODY_BYTES) {
      return json({ error: 'Petición demasiado grande.' }, 413, cors);
    }

    let d;
    try { d = await request.json(); } catch { return json({ error: 'JSON inválido.' }, 400, cors); }

    const nombre = limpia(d.nombre, LIMITES.nombre);
    const telefono = limpiaTel(d.telefono);
    const giro = limpia(d.giro, LIMITES.giro);
    const dolor = limpia(d.dolor, LIMITES.dolor);

    if (!nombre) return json({ error: 'Falta el nombre.' }, 400, cors);
    if (!telefono || telefono.replace(/\D/g, '').length < 10) {
      return json({ error: 'El teléfono necesita al menos 10 dígitos.' }, 400, cors);
    }

    const horas = entero(d.horas_anio, 0, 1000000);
    const personas = entero(d.personas, 0, 500);
    const origen = d.origen === 'expo' ? 'expo' : 'sitio';

    try {
      // Si la persona ya se registró, se actualiza su ficha en vez de duplicarla.
      await env.DB.prepare(
        `INSERT INTO leads (creado, nombre, telefono, giro, dolor, horas_anio, personas, origen)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
         ON CONFLICT(telefono) DO UPDATE SET
           nombre     = excluded.nombre,
           giro       = COALESCE(NULLIF(excluded.giro, ''), leads.giro),
           dolor      = COALESCE(NULLIF(excluded.dolor, ''), leads.dolor),
           horas_anio = COALESCE(excluded.horas_anio, leads.horas_anio),
           personas   = COALESCE(excluded.personas, leads.personas)`
      ).bind(new Date().toISOString(), nombre, telefono, giro, dolor, horas, personas, origen).run();
    } catch (e) {
      console.error('No se pudo guardar el contacto', String(e));
      return json({ error: 'No se pudo guardar. Inténtalo otra vez.' }, 500, cors);
    }

    return json({ ok: true }, 200, cors);
  },
};

async function contar(env, cors) {
  const r = await env.DB.prepare('SELECT COUNT(*) AS n FROM leads').first();
  const hoy = await env.DB.prepare(
    "SELECT COUNT(*) AS n FROM leads WHERE creado >= datetime('now','-1 day')"
  ).first();
  return json({ total: r?.n ?? 0, ultimas_24h: hoy?.n ?? 0 }, 200, cors);
}

async function exportar(env, cors) {
  const { results } = await env.DB.prepare(
    `SELECT creado, nombre, telefono, giro, dolor, horas_anio, personas, origen, nota
       FROM leads ORDER BY creado DESC`
  ).all();

  const cab = ['Fecha', 'Nombre', 'Teléfono', 'A qué se dedica', 'Qué le quita tiempo',
               'Horas al año', 'Personas', 'Origen', 'Nota'];
  const filas = (results || []).map((r) => [
    r.creado, r.nombre, r.telefono, r.giro, r.dolor, r.horas_anio, r.personas, r.origen, r.nota,
  ]);
  // BOM para que Excel abra los acentos bien.
  const csv = '﻿' + [cab, ...filas].map((f) => f.map(celda).join(',')).join('\r\n');

  return new Response(csv, {
    status: 200,
    headers: {
      ...cors,
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': `attachment; filename="contactos-mattera-${hoyISO()}.csv"`,
      'Cache-Control': 'no-store',
    },
  });
}

// Una celda que empieza por = + - @ la interpretan Excel y Sheets como fórmula:
// se antepone un apóstrofo para que se lea como texto.
function celda(v) {
  if (v === null || v === undefined) return '';
  let s = String(v);
  if (/^[=+\-@\t\r]/.test(s)) s = "'" + s;
  return '"' + s.replace(/"/g, '""') + '"';
}

function hoyISO() { return new Date().toISOString().slice(0, 10); }

function limpia(v, max) {
  if (typeof v !== 'string') return '';
  return v.replace(/[\u0000-\u001f\u007f]/g, ' ').trim().slice(0, max);
}

function limpiaTel(v) {
  if (typeof v !== 'string') return '';
  return v.replace(/[^\d+()\-\s]/g, '').trim().slice(0, LIMITES.telefono);
}

function entero(v, min, max) {
  const n = Number(v);
  if (!Number.isFinite(n)) return null;
  return Math.min(max, Math.max(min, Math.round(n)));
}

function isAllowed(origin) { return ALLOWED_ORIGINS.includes(origin); }

function corsHeaders(origin) {
  return {
    'Access-Control-Allow-Origin': isAllowed(origin) ? origin : ALLOWED_ORIGINS[0],
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    Vary: 'Origin',
  };
}

function json(obj, status, cors) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...cors, 'Content-Type': 'application/json; charset=utf-8' },
  });
}
