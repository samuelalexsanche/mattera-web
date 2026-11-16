# -*- coding: utf-8 -*-
"""Genera la versión en inglés de una página a partir de la española.

Qué hace, además de traducir con el diccionario:
  · lang="en", canonical a la URL /en/, y hreflang en los dos sentidos
  · rutas relativas corregidas (la página vive un nivel más abajo)
  · el botón de idioma pasa a ser un enlace real entre versiones, no JS:
    así Google indexa las dos versiones por separado
  · quita el sistema viejo de traducción por JavaScript
"""
import re, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def traducir(html, dic):
    # de la frase más larga a la más corta, para no partir frases dentro de otras
    for es in sorted(dic, key=len, reverse=True):
        en = dic[es]
        if es and es != en:
            html = html.replace(es, en)
    return html

def generar(origen, destino, dic, title, desc, es_url, en_url, profundidad=1):
    s = open(os.path.join(BASE, origen), encoding='utf-8').read()

    # el sistema viejo de i18n por JS sale de las dos versiones
    s = re.sub(r'// ── i18n SYSTEM.*?(?=</script>)', '', s, flags=re.S)
    s = re.sub(r'\sdata-i18n="[^"]*"', '', s)

    s = traducir(s, dic)

    s = s.replace('<html lang="es-MX">', '<html lang="en">')
    s = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', s, count=1, flags=re.S)
    s = re.sub(r'<link rel="canonical" href=".*?">',
               f'<link rel="canonical" href="{en_url}">\n'
               f'<link rel="alternate" hreflang="es-MX" href="{es_url}">\n'
               f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{es_url}">', s, count=1)
    s = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{en_url}">', s, count=1)
    s = re.sub(r'<meta property="og:locale" content=".*?">', '<meta property="og:locale" content="en_US">', s, count=1)

    # rutas relativas: la página en inglés cuelga de /en/
    subir = '../' * profundidad
    def arreglar(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(('http', '//', '#', 'mailto:', 'tel:', '/')):
            return m.group(0)
        return f'{attr}="{subir}{url}"'
    s = re.sub(r'(href|src)="([^"]+)"', arreglar, s)

    # el botón de idioma: enlace real a la versión en español
    # el botón de idioma: enlace real a la versión en español (venga como botón o como enlace)
    nuevo = f'<a id="lang-toggle" class="lang-toggle" href="{es_url}" hreflang="es-MX" aria-label="Ver en español">ES</a>'
    s = re.sub(r'<button id="lang-toggle"[^>]*>.*?</button>', nuevo, s, flags=re.S)
    s = re.sub(r'<a id="lang-toggle"[^>]*>.*?</a>', nuevo, s, flags=re.S)

    os.makedirs(os.path.dirname(os.path.join(BASE, destino)) or '.', exist_ok=True)
    open(os.path.join(BASE, destino), 'w', encoding='utf-8').write(s)
    return destino

def marcar_es(ruta_es, es_url, en_url):
    """Añade hreflang y el enlace al inglés en la página española."""
    p = os.path.join(BASE, ruta_es)
    s = open(p, encoding='utf-8').read()
    if 'hreflang="en"' not in s:
        s = re.sub(r'(<link rel="canonical" href="[^"]*">)',
                   r'\1\n' + f'<link rel="alternate" hreflang="es-MX" href="{es_url}">\n'
                             f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
                             f'<link rel="alternate" hreflang="x-default" href="{es_url}">', s, count=1)
    nuevo = f'<a id="lang-toggle" class="lang-toggle" href="{en_url}" hreflang="en" aria-label="View in English">EN</a>'
    s = re.sub(r'<button id="lang-toggle"[^>]*>.*?</button>', nuevo, s, flags=re.S)
    s = re.sub(r'<a id="lang-toggle"[^>]*>.*?</a>', nuevo, s, flags=re.S)
    s = re.sub(r'// ── i18n SYSTEM.*?(?=</script>)', '', s, flags=re.S)
    s = re.sub(r'\sdata-i18n="[^"]*"', '', s)
    open(p, 'w', encoding='utf-8').write(s)
    return ruta_es
