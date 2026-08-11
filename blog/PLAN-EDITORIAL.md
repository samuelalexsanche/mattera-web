# Plan editorial del blog

Cola de temas para la rutina automática de contenido. Cada tema sale de
**búsquedas reales** del autocompletado de Google México, no de intuición.

**Cómo se usa:** la rutina toma el primer tema con estado `pendiente`, escribe
el artículo, lo marca como `publicado` con la fecha, y hace commit. Si la cola
se vacía, la rutina debe investigar temas nuevos y proponerlos aquí antes de
escribir.

---

## Cola

### 1. Cómo aparecer en Google Maps con tu negocio
- **Estado:** pendiente
- **Slug:** `como-aparecer-en-google-maps-negocio.html`
- **Cubre:** `como aparecer en google maps` · `maps gratis` · `maps mi negocio` · `como aparecer en google gratis`
- **Ángulo:** paso a paso real de crear y verificar una ficha, incluyendo los
  errores que cuestan tiempo (elegir mal la categoría principal, publicar una
  dirección cuando no atiendes al público, horario que no coincide con el sitio).
- **Enlaza a:** `/agencia-ia-guadalajara.html`, `/servicios/paginas-web.html`

### 2. Por qué tu página web no aparece en Google
- **Estado:** pendiente
- **Slug:** `por-que-mi-pagina-web-no-aparece-en-google.html`
- **Cubre:** `por que no aparece mi pagina web en los buscadores` · `mi pagina web no aparece` · `como aparecer en google`
- **Ángulo:** diagnóstico ordenado por frecuencia — sitemap incompleto, índice
  desactualizado, falta de autoridad, contenido que nadie busca. Formato de
  checklist con cómo verificar cada causa.
- **Enlaza a:** `/servicios/paginas-web.html`, `/blog/que-es-geo-optimizacion-para-ia.html`

### 3. Cómo mejorar el SEO de tu página web
- **Estado:** pendiente
- **Slug:** `como-mejorar-el-seo-de-mi-pagina-web.html`
- **Cubre:** `como mejorar el seo de mi pagina web` · `mejorar el rendimiento` · `mejorar el diseño`
- **Ángulo:** qué mover primero según impacto real, y qué es pérdida de tiempo.

### 4. Cómo elegir un CRM para tu empresa
- **Estado:** pendiente
- **Slug:** `como-elegir-un-crm-para-mi-empresa.html`
- **Cubre:** `como elegir un crm` · `crm para empresas pequeñas` · `crm para empresas medianas`
- **Ángulo:** criterios de decisión, y por qué la mayoría de los CRM se abandonan.
- **Enlaza a:** `/servicios/crm-para-empresas.html`

### 5. Inteligencia artificial para PyMEs: usos prácticos
- **Estado:** pendiente
- **Slug:** `inteligencia-artificial-para-pymes-usos-practicos.html`
- **Cubre:** `inteligencia artificial para pymes uso práctico` · `y prompts` · `como automatizar procesos con chatgpt`
- **Ángulo:** casos concretos por tamaño de empresa, con el criterio de cuándo
  NO conviene.
- **Enlaza a:** `/servicios/automatizacion-procesos.html`

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
