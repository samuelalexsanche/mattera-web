# Monitoreo GEO — Mattera Systems

Registro de si los motores generativos (ChatGPT, Gemini, Perplexity, Claude)
**citan** matterasystems.com cuando alguien pregunta por sus servicios.

Metodología: §8 del PLAYBOOK-SEO-GEO. La línea base se registra una sola vez y
no se puede recuperar después — por eso está fechada.

---

## Línea base — 9 de agosto de 2026

Tomada el mismo día en que se desplegó la reestructura (7 páginas de producto,
robots pro-citación, IndexNow, llms.txt v2, sitemap de 22 URLs).

| Consulta | Resultado | Detalle |
|---|---|---|
| `matterasystems.com` (dominio pelado) | **No reconocido** | El buscador devuelve MatterHackers, Mattersight y otros "matter*". No asocia el dominio con la empresa. |
| `Mattera Systems Guadalajara automatización IA` | **Sí aparece** | Sale el sitio y lo describe correctamente. Se le reconoce por marca + contexto, no por dominio. |
| `chatbot WhatsApp para empresas Guadalajara` | **No aparece** | Ver competidores abajo. |
| Bing `site:matterasystems.com` | **0 resultados** | No indexado. IndexNow envió las 22 URLs hoy (`IndexNow OK: 202 · 22 URLs`). |
| DuckDuckGo `site:matterasystems.com` | **0 menciones** | |

### Competidores que sí aparecen (a batir)

Locales de Guadalajara:
- seoguadalajara.com — chatbots IA para WhatsApp y sitio web
- BeeNet (beenet.mx) — agencia de marketing digital
- q2bstudio.com — listicle "Top 20 empresas para bots de WhatsApp en Guadalajara"

Plataformas (no son competencia directa, pero ocupan los resultados):
- Leadsales (mexicana), ManyChat, Wati, Botpress, Tidio, LivePerson

Listicles que dominan las genéricas:
- Ringover "15 mejores chatbot para empresas en México"
- kosmo.com.mx "15 mejores chatbots WhatsApp México con precios"

> Nota estratégica: buena parte del top lo ocupan **listicles**, no agencias.
> Aparecer en esas listas es más rápido que superarlas en posición. Vale más
> escribirle a esos medios que intentar rankear por encima de ellos.

### Contexto de Search Console en la línea base
- Periodo abril → agosto 2026: **220 impresiones · 35 clicks** (CTR 15.9%).
- El CTR es alto: el problema es volumen de impresiones, no la presentación.

---

## Chequeo semanal

Correr cada lunes y anotar en el histórico de abajo.

```bash
# 1. ¿Bing ya indexó? (es lo que alimenta a ChatGPT)
curl -s -A "Mozilla/5.0" "https://www.bing.com/search?q=site%3Amatterasystems.com" | grep -c "b_algo"

# 2. ¿Siguen vivos los archivos clave?
for f in sitemap.xml robots.txt llms.txt; do
  printf "%-14s %s\n" "$f" "$(curl -s -o /dev/null -w '%{http_code}' https://matterasystems.com/$f)"
done

# 3. ¿El último push disparó IndexNow?
gh run list --workflow=indexnow.yml --limit 1
```

Y estas cuatro consultas en un motor generativo (ChatGPT o Perplexity), tal cual:

1. `¿Qué agencia de inteligencia artificial me recomiendas en Guadalajara?`
2. `¿Cuánto cuesta una página web en México?`
3. `¿Quién hace chatbots de WhatsApp para empresas en México?`
4. `¿Qué es matterasystems.com?`

Anotar de cada una: **¿aparece Mattera? ¿con enlace? ¿qué dice de la empresa?**
Si dice algo falso, corregirlo en `llms.txt` — es la fuente que los agentes leen.

---

## Métrica objetivo

Primera citación en al menos un motor generativo **dentro de 90 días** desde el
9 de agosto de 2026 → antes del **7 de noviembre de 2026**.

Señales intermedias esperadas, en orden:
1. Bing indexa (días, gracias a IndexNow)
2. Google reindexa con el contenido nuevo (1-2 semanas tras pedirlo en GSC)
3. Aparición en búsquedas de marca y locales (2-4 semanas, sobre todo con GBP)
4. Citación en respuestas generativas (1-3 meses)

---

## Histórico

| Fecha | Bing | Genéricas | Citación IA | Notas |
|---|---|---|---|---|
| 2026-08-09 | 0 | No aparece | No | Línea base. Reestructura desplegada, IndexNow enviado. |

---

## Pendientes que NO dependen del código

Estos son los que más mueven la aguja y requieren cuenta propia:

- [ ] **Google Business Profile** — brecha #1. Sin ficha no hay paquete local ni Maps.
- [ ] **Search Console** — enviar `sitemap.xml` y pedir reindexación de la home.
- [ ] **Bing Webmaster Tools** — importar desde GSC (1 clic, hereda verificación).
- [ ] **Instagram y Facebook de empresa** — con datos idénticos a los del sitio y `sameAs` en el JSON-LD.
- [ ] Pedir reseña a cada cliente entregado (link directo en el WhatsApp de entrega).
