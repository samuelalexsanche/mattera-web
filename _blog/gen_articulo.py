# -*- coding: utf-8 -*-
"""Genera artículos del blog con la plantilla real del sitio.

Uso: from gen_articulo import escribir; escribir(spec)
El cuerpo se escribe a mano en cada spec (nada de texto generado en serie):
aquí solo vive el armazón — cabecera, esquema, navegación, pie.

Reglas que hace cumplir la plantilla (ver blog/PLAN-EDITORIAL.md):
  · FAQ obligatorio con FAQPage en JSON-LD
  · enlaces internos al servicio relacionado
  · nada de cifras de clientes: eso se valida al escribir el cuerpo
"""
import json, os, re, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(BASE, 'blog', 'como-funciona-un-chatbot-de-ia-en-la-practica.html')
MESES = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

def _mes(fecha):
    a, m, _ = fecha.split('-')
    return f"{MESES[int(m)-1].capitalize()} {a}"

def tabla(encabezados, filas):
    th = ''.join(f'<th>{h}</th>' for h in encabezados)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in f) + '</tr>' for f in filas)
    return f'<div class="tabla-wrap"><table class="tabla-comp"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def faq_html(pares):
    items = ''
    for p, r in pares:
        items += (f'    <div class="faq-item">\n'
                  f'      <button class="faq-btn" aria-expanded="false" onclick="toggleFaq(this)">{p}<span class="faq-icon" aria-hidden="true">+</span></button>\n'
                  f'      <div class="faq-answer" role="region"><p>{r}</p></div>\n'
                  f'    </div>\n')
    return items

def _limpio(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()

def escribir(s):
    plantilla = open(PLANTILLA, encoding='utf-8').read()
    url = f"https://matterasystems.com/blog/{s['slug']}"
    faqs = s.get('faq', [])

    schema = {
        "@context": "https://schema.org",
        "@graph": [{
            "@type": "Article",
            "headline": s['h1'],
            "description": s['desc'],
            "author": {"@type": "Organization", "name": "Mattera Systems"},
            "image": "https://matterasystems.com/og/og-blog.png",
            "publisher": {"@type": "Organization", "name": "Mattera Systems", "url": "https://matterasystems.com/"},
            "datePublished": s['fecha'],
            "dateModified": s.get('modificado', s['fecha']),
            "url": url,
            "inLanguage": "es-MX",
            "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://matterasystems.com/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://matterasystems.com/blog/"},
                {"@type": "ListItem", "position": 3, "name": s['titulo_corto'], "item": url}]}
        }]
    }
    if faqs:
        schema["@graph"].append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": _limpio(p),
             "acceptedAnswer": {"@type": "Answer", "text": _limpio(r)}} for p, r in faqs]})

    cabeza = plantilla[:plantilla.index('</head>')]
    cuerpo_pie = plantilla[plantilla.index('<footer>'):]

    # ── <head> ──
    cabeza = re.sub(r'<title>.*?</title>', f"<title>{s['title']}</title>", cabeza, flags=re.S)
    cabeza = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{s["desc"]}">', cabeza, flags=re.S)
    cabeza = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{url}">', cabeza)
    cabeza = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{s["h1"]}">', cabeza, flags=re.S)
    cabeza = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{s["desc"]}">', cabeza, flags=re.S)
    cabeza = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{url}">', cabeza)
    cabeza = re.sub(r'<meta property="article:published_time" content=".*?">',
                    f'<meta property="article:published_time" content="{s["fecha"]}">\n<meta property="article:modified_time" content="{s.get("modificado", s["fecha"])}">', cabeza)
    cabeza = re.sub(r'<script type="application/ld\+json">.*?</script>',
                    '<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=2) + '\n</script>', cabeza, flags=re.S)

    # ── cabecera del artículo ──
    nav_y_header = plantilla[plantilla.index('<body>'):plantilla.index('<!-- ARTICLE HEADER -->')]

    cta = s.get('cta', '¿Quieres saber qué parte de tu operación es automatizable y cuánto tiempo recuperaría tu equipo?')
    faq_bloque = ''
    if faqs:
        faq_bloque = f'''
<hr class="divider">

<section class="section sec-dark" aria-labelledby="faq-art">
  <div class="article-body">
    <h2 class="article-faq-h2" id="faq-art">Preguntas frecuentes</h2>
    <div class="faq-list" style="max-width:760px;margin-top:1.5rem">
{faq_html(faqs)}    </div>
  </div>
</section>
'''
    rel = ''.join(f'<a href="{h}" class="pp-rel">{t}</a>' for h, t in s.get('relacionado', []))
    rel_bloque = f'''
<hr class="divider">

<section class="section sec-alt" aria-labelledby="rel-art">
  <div class="pp-wrap">
    <h2 class="pp-h2" id="rel-art">Para seguir leyendo</h2>
    <div class="pp-rels">{rel}</div>
  </div>
</section>
''' if rel else ''

    doc = f'''{cabeza}</head>
{nav_y_header}<!-- ARTICLE HEADER -->
<div class="article-header-wrap sec-dark px" data-px="editorial">
  <div class="article-header">
    <nav class="breadcrumb" aria-label="Ruta de navegación">
      <a href="../">Inicio</a>
      <span aria-hidden="true">›</span>
      <a href="index.html">Blog</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">{s['titulo_corto']}</span>
    </nav>
    <div class="article-meta">
      <span class="blog-card-cat">{s['categoria']}</span>
      <time datetime="{s['fecha']}">{_mes(s['fecha'])}</time>
      <span>·</span>
      <span>Mattera Systems</span>
    </div>
    <h1 class="article-h1 reveal">{s['h1']}</h1>
    <p class="article-deck reveal reveal-delay-1">{s['bajada']}</p>
  </div>
</div>

<hr class="divider">

<!-- ARTICLE BODY -->
<section class="section sec-paper">
  <div class="article-body">

    <p class="article-lede">{s['lede']}</p>

{s['cuerpo']}
  </div>

  <!-- MID-ARTICLE CTA -->
  <div class="article-mid-cta reveal">
    <p>{cta}</p>
    <a href="https://wa.me/523327874747" target="_blank" rel="noopener noreferrer" class="btn-primary"><span>Agendar diagnóstico →</span></a>
  </div>
</section>
{faq_bloque}{rel_bloque}
</main>

{cuerpo_pie}'''
    if faqs and 'function toggleFaq' not in doc:
        doc = doc.replace('<script>\nfunction toggleMobileNav()', '''<script>
function toggleFaq(btn){
  const answer=btn.nextElementSibling;
  const abierto=btn.getAttribute('aria-expanded')==='true';
  document.querySelectorAll('.faq-btn').forEach(b=>{b.setAttribute('aria-expanded','false');b.nextElementSibling.classList.remove('open');});
  if(!abierto){btn.setAttribute('aria-expanded','true');answer.classList.add('open');}
}
function toggleMobileNav()''')
    carpeta = s.get('destino') or os.path.join(BASE, 'blog')
    os.makedirs(carpeta, exist_ok=True)
    destino = os.path.join(carpeta, s['slug'])
    open(destino, 'w', encoding='utf-8').write(doc)
    if s.get('ficha'):
        json.dump({'slug': s['slug'], 'categoria': s['categoria'], 'fecha': s['fecha'],
                   'titulo': s['h1'], 'resumen': s['ficha']},
                  open(os.path.splitext(destino)[0] + '.json', 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=2)
    palabras = len(_limpio(s['lede'] + ' ' + s['cuerpo']).split())
    return destino, palabras
