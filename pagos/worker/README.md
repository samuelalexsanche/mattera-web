# Webhook de pagos · Mercado Pago → Telegram

Cloudflare Worker que recibe el aviso de Mercado Pago cuando alguien paga un
plan, verifica que sea legítimo, y te manda un mensaje a Telegram con el plan,
el monto, si fue MSI y cuánto te queda después de comisión.

El sitio es estático (GitHub Pages), así que **no puede haber llaves secretas
en el navegador**. Este Worker es el único lugar donde viven.

---

## 1. Crear los links de pago en Mercado Pago

Esto se hace en el panel, no por código.

1. Activa MSI: **Tu negocio → Costos y cuotas → Venta en cuotas sin intereses**
   → "Código QR y pagos online" → deja **6 meses**.
2. Crea **tres** links de pago (**Herramientas para vender → Link de pago**):

   | Plan | Monto | `external_reference` |
   |------|-------|----------------------|
   | T1 Presencia  | $5,900 MXN  | `t1` |
   | T2 Sistema    | $9,900 MXN  | `t2` |
   | T3 Operación  | $19,900 MXN | `t3` |

   Pon el `external_reference` si el panel te lo permite. Si no aparece el
   campo, no pasa nada: el Worker identifica el plan por el monto, porque los
   tres precios son distintos. En ese caso el aviso te llega igual, marcado con
   "identificado por monto" para que sepas que al link le falta la referencia.

   **Ojo con el tipo de link:** tienen que ser links **con monto definido**. Un
   "Link sin monto definido" deja que el cliente escriba la cantidad, así que no
   sirve para vender un plan a precio fijo — pero sí es perfecto para las
   cotizaciones a medida (T4).

3. En cada link, como URL de retorno al aprobar:
   `https://matterasystems.com/gracias.html?plan=t1` (t2 / t3 según el caso).

---

## 2. Configurar el webhook

En **Tu integración → Webhooks**:

- URL: `https://mattera-pagos.mattera.workers.dev`
- Evento: **Pagos (legacy)** — es el webhook clásico `payment`, que es el que
  este Worker lee. NO marcar "Order (Mercado Pago)": usa otro formato.
- Copia la **clave secreta** que genera. La necesitas en el paso 3.

---

## 3. Desplegar

```bash
cd pagos/worker
npx wrangler deploy
```

Luego los secretos, uno por uno. **Wrangler los pide por stdin: no quedan en el
historial de la terminal ni en el repo.**

```bash
npx wrangler secret put MP_ACCESS_TOKEN
npx wrangler secret put MP_WEBHOOK_SECRET
npx wrangler secret put TELEGRAM_BOT_TOKEN
npx wrangler secret put TELEGRAM_CHAT_ID
```

- `MP_ACCESS_TOKEN` → Tus integraciones → Credenciales de **producción**
- `MP_WEBHOOK_SECRET` → la **Clave secreta** de la pantalla de Webhooks.
  NO es el Client Secret: ese es de OAuth y no se usa aquí.
- `TELEGRAM_BOT_TOKEN` → tu bot en @BotFather
- `TELEGRAM_CHAT_ID` → tu chat (escríbele al bot y consulta `/getUpdates`)

### Opcional: evitar avisos duplicados

Mercado Pago puede notificar el mismo pago más de una vez. Con KV se ignora el
repetido:

```bash
npx wrangler kv namespace create PAGOS
```

Pega el `id` que devuelve en `wrangler.toml` (bloque `[[kv_namespaces]]`,
descoméntalo) y vuelve a desplegar.

---

## 4. Comprobar que quedó

```bash
curl https://mattera-pagos.mattera.workers.dev
```

Debe responder `{"ok":true,"servicio":"mattera-pagos"}`.

Después usa el **simulador de notificaciones** de Mercado Pago (está en la misma
pantalla de Webhooks) con un pago real de prueba. Para ver qué pasó:

```bash
npx wrangler tail
```

---

## Cómo se comporta

| Situación | Respuesta | Aviso |
|---|---|---|
| Firma válida y pago aprobado | 200 | sí |
| Firma válida, pago pendiente o rechazado | 200 | no |
| Firma inválida o ausente | 401 | no |
| Notificación que no es de pago | 200 | no |
| Falla Telegram o la API de MP | 500 | MP reintenta cada 15 min |
| Monto distinto al del plan | 200 | sí, **marcado con ⚠️** |

## Decisiones que vale la pena conocer

**El monto se lee de la API, nunca del webhook.** El cuerpo de la notificación
solo trae un id; si confiáramos en él, cualquiera que descubra la URL podría
mandar un "pago aprobado de $19,900". El Worker toma el id, consulta
`/v1/payments/{id}` con el access token, y de ahí saca estatus y monto.

**La firma incluye el id.** El manifest es
`id:<data.id>;request-id:<x-request-id>;ts:<ts>;` con HMAC-SHA256. Está probado
que cambiar el `data.id` invalida la firma, así que no se puede reusar una firma
vieja apuntando a otro pago.

**401 en firma inválida, no 500.** Un 500 haría que MP reintente cada 15 minutos
algo que nunca va a validar.

**Se compara en tiempo constante.** Una comparación normal de strings revela por
dónde coincide y permite adivinar la firma byte por byte.
