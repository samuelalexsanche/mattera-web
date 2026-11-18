#!/usr/bin/env python3
"""
Genera sitemap.xml desde los archivos reales del repo.

Corre solo en cada push (.github/workflows/indexnow.yml). Al añadir una página
nueva no hay que tocar nada ni volver a Search Console: entra sola al sitemap
y se avisa a Bing por IndexNow.

Reglas:
- Se excluye cualquier página con robots noindex (ej. gracias.html).
- lastmod = fecha del último commit que tocó el archivo, no "hoy". Si fuera
  "hoy", el sitemap cambiaría en cada ejecución y Google dejaría de creerle.
- La prioridad va por rol comercial, no por profundidad de carpeta.
"""
import glob, os, re, subprocess, datetime, sys

BASE = 'https://matterasystems.com'

PRIORIDAD = {
    'index.html':                            ('1.0', 'weekly'),
    'agencia-ia-guadalajara.html':           ('0.9', 'monthly'),
    'planes.html':                           ('0.9', 'weekly'),
    'servicios/chatbot-whatsapp.html':       ('0.9', 'monthly'),
    'servicios/paginas-web.html':            ('0.9', 'monthly'),
    'servicios/crm-para-empresas.html':      ('0.8', 'monthly'),
    'servicios/agentes-ia.html':             ('0.8', 'monthly'),
    'servicios/automatizacion-procesos.html':('0.8', 'monthly'),
    'servicios/integraciones.html':          ('0.8', 'monthly'),
    'faq.html':                              ('0.8', 'monthly'),
    'que-es-automatizacion.html':            ('0.8', 'monthly'),
    'industrias/index.html':                 ('0.7', 'monthly'),
    'blog/index.html':                       ('0.7', 'weekly'),
    'nosotros.html':                         ('0.6', 'monthly'),
    'privacidad.html':                       ('0.3', 'yearly'),
}

def meta(p):
    if p in PRIORIDAD:
        return PRIORIDAD[p]
    if p == 'en/index.html':        return ('0.9', 'weekly')
    if p.startswith('en/'):         return ('0.6', 'monthly')
    if p.startswith('servicios/'):  return ('0.8', 'monthly')
    if p.startswith('industrias/'): return ('0.7', 'monthly')
    if p.startswith('blog/'):       return ('0.6', 'monthly')
    return ('0.5', 'monthly')

def _pendientes():
    """Archivos con cambios sin commitear (en el índice o en el árbol).

    Hacen falta porque el hook pre-commit corre ANTES de que exista el commit:
    `git log` todavía devolvería la fecha vieja para un archivo que se está
    modificando ahora. Sin esto, el sitemap del hook nunca coincide con el que
    CI calcula después del commit, CI lo vuelve a commitear, y ese segundo
    commit dispara un segundo despliegue de Pages que cancela el primero.
    """
    try:
        salida = subprocess.run(['git', 'status', '--porcelain'],
                                capture_output=True, text=True, timeout=20).stdout
    except Exception:
        return set()
    rutas = set()
    for linea in salida.splitlines():
        if len(linea) > 3:
            ruta = linea[3:].strip().strip('"')
            # los renombrados vienen como "viejo -> nuevo"
            rutas.add(ruta.split(' -> ')[-1])
    return rutas

_SIN_COMMITEAR = _pendientes()

def lastmod(p):
    if p in _SIN_COMMITEAR:
        return datetime.date.today().isoformat()
    try:
        d = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', p],
                           capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        d = ''
    return d or datetime.date.today().isoformat()

def url_de(p):
    if p == 'index.html':
        return BASE + '/'
    if p.endswith('/index.html'):
        return f'{BASE}/{p[:-10]}'
    return f'{BASE}/{p}'

# Páginas que existen en los dos idiomas: español -> inglés
PAREJAS = {
    'index.html':  'en/index.html',
    'planes.html': 'en/pricing.html',
}

def pareja(p):
    """Devuelve (url_es, url_en) si la página tiene versión en el otro idioma."""
    if p in PAREJAS:
        return url_de(p), url_de(PAREJAS[p])
    inverso = {v: k for k, v in PAREJAS.items()}
    if p in inverso:
        return url_de(inverso[p]), url_de(p)
    return None

def indexable(p):
    html = open(p, encoding='utf-8').read()
    return not re.search(r'name=["\']robots["\'][^>]*noindex', html)

def main():
    patrones = ['*.html', 'servicios/*.html', 'industrias/*.html', 'blog/*.html',
                'en/*.html', 'en/services/*.html', 'en/industries/*.html']
    paginas = sorted({p for pat in patrones for p in glob.glob(pat)})
    incluidas = [p for p in paginas if indexable(p)]
    excluidas = [p for p in paginas if p not in incluidas]

    incluidas.sort(key=lambda p: (-float(meta(p)[0]), p))

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
           ' xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in incluidas:
        pr, cf = meta(p)
        out += ['  <url>',
                f'    <loc>{url_de(p)}</loc>',
                f'    <lastmod>{lastmod(p)}</lastmod>',
                f'    <changefreq>{cf}</changefreq>',
                f'    <priority>{pr}</priority>']
        par = pareja(p)
        if par:
            es_u, en_u = par
            out += [f'    <xhtml:link rel="alternate" hreflang="es-MX" href="{es_u}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="en" href="{en_u}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="x-default" href="{es_u}"/>']
        out += ['  </url>']
    out.append('</urlset>')
    nuevo = '\n'.join(out) + '\n'

    anterior = ''
    if os.path.exists('sitemap.xml'):
        anterior = open('sitemap.xml', encoding='utf-8').read()

    if nuevo == anterior:
        print(f'sitemap.xml sin cambios ({len(incluidas)} URLs)')
        return 0

    open('sitemap.xml', 'w', encoding='utf-8').write(nuevo)
    print(f'sitemap.xml actualizado: {len(incluidas)} URLs')
    for p in excluidas:
        print(f'  excluida por noindex: {p}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
