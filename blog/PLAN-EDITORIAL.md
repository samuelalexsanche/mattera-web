# Plan editorial del blog

Cola de temas para la rutina automática de contenido. Cada tema sale de
**búsquedas reales** del autocompletado de Google México, no de intuición.

**Cómo se usa (desde 2026-09-30):** los cinco temas de esta cola ya están
escritos y revisados; viven en `_blog/pendientes/` (fuera de la web, no entran
al sitemap). El flujo `.github/workflows/publicar-articulo.yml` corre martes y
viernes, publica el siguiente cuando llega su fecha, le añade su tarjeta al
índice, regenera el sitemap y avisa a IndexNow.

Cuando la cola se vacíe hay que investigar temas nuevos con búsquedas reales,
escribirlos con `_blog/gen_articulo.py` apuntando a `_blog/pendientes/` y
fecharlos con al menos tres días de separación.

---

## Cola

### 1. Cómo integrar WhatsApp con tu CRM o tu sistema
- **Estado:** escrito, en cola para 2026-11-17
- **Slug:** `como-integrar-whatsapp-con-tu-crm-o-sistema.html`
- **Resumen:** Hay tres cosas que se llaman WhatsApp y solo una se conecta. Qué pide Meta, las tres formas de hacerlo con sus costos, y la trampa de la ventana de 24 horas.

### 2. Cómo automatizar una clínica dental o un consultorio
- **Estado:** escrito, en cola para 2026-11-20
- **Slug:** `como-automatizar-una-clinica-dental-o-consultorio.html`
- **Resumen:** Primero las preguntas repetidas, después la agenda, al final el seguimiento. Qué no debe tocar nunca un asistente y cómo se cuidan los datos del paciente.

### 3. Cómo automatizar un restaurante sin descuidar el mostrador
- **Estado:** escrito, en cola para 2026-11-24
- **Slug:** `como-automatizar-un-restaurante.html`
- **Resumen:** Reservas, pedidos por WhatsApp y clientes que vuelven. Qué automatizar primero, qué dejar en manos del equipo y por qué el menú va antes que el asistente.

---

## Reglas de escritura (no negociables)

1. **Nunca inventar datos sobre Mattera.** Precios, plazos, garantías y casos
   salen exclusivamente de `/llms.txt`. Si un dato no está ahí, no se escribe.
2. **Sin reseñas ni calificaciones.** Mattera no tiene reseñas verificables;
   inventarlas destruye la confianza y arriesga penalización.
3. **Citar fuentes reales** con enlace cuando se den cifras de mercado o se
   describa cómo funciona una herramienta de terceros.
4. **Voz de marca:** directa, sin superlativos, sin "revoluciona" ni "potencia".
   Se dice lo que el producto no hace. Se prefiere el dato al adjetivo.
5. **Formato citable** (para que las IA puedan extraer respuestas):
   - Definición que responda la búsqueda en las primeras 40–60 palabras
   - Pasos numerados y al menos una tabla comparativa
   - Sección de preguntas frecuentes con `FAQPage` en JSON-LD
   - Enlaces internos al servicio relacionado
6. **Extensión:** 900–1,500 palabras. Por debajo de 900 no aporta; por encima
   de 1,500 se diluye.
7. **Si la investigación no da material sólido, no se publica.** Es preferible
   saltarse una semana a publicar relleno.

## Frecuencia

Dos artículos por semana como máximo. Publicar más rápido no acelera el
posicionamiento y sí acerca el umbral de "scaled content abuse" de Google.
