#!/usr/bin/env python3
"""Publica el siguiente artículo de la cola.

Los artículos ya escritos y revisados viven en `_blog/pendientes/` (fuera de la
web: no son accesibles ni entran al sitemap). Este script toma el que tenga la
fecha de publicación más antigua, lo mueve a `blog/` y le añade su tarjeta al
índice del blog.

Se ejecuta desde .github/workflows/publicar-articulo.yml dos veces por semana.
El ritmo es deliberado: el plan editorial fija un máximo de dos por semana para
no acercarse al umbral de "contenido a escala" de Google.

Uso:  python3 tools/publicar_pendiente.py [--dry-run]
Sale con código 0 y no hace nada si la cola está vacía.
"""
import json, os, re, sys, glob, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEND = os.path.join(BASE, '_blog', 'pendientes')
BLOG = os.path.join(BASE, 'blog')
INDICE = os.path.join(BLOG, 'index.html')
MESES = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

def siguiente():
    fichas = sorted(glob.glob(os.path.join(PEND, '*.json')))
    candidatos = []
    for f in fichas:
        d = json.load(open(f, encoding='utf-8'))
        html = os.path.join(PEND, d['slug'])
        if os.path.exists(html):
            candidatos.append((d['fecha'], d, f, html))
    return sorted(candidatos)[0] if candidatos else None

def tarjeta(d):
    a, m, _ = d['fecha'].split('-')
    return f'''    <article class="blog-card reveal">
      <div class="blog-card-meta">
        <span class="blog-card-cat">{d['categoria']}</span>
        <time datetime="{d['fecha']}">{MESES[int(m)-1]} {a}</time>
      </div>
      <h2 class="blog-card-title"><a href="{d['slug']}">{d['titulo']}</a></h2>
      <p class="blog-card-excerpt">{d['resumen']}</p>
      <a href="{d['slug']}" class="blog-card-link" aria-label="Leer artículo completo: {d['titulo']}">Leer artículo →</a>
    </article>

'''

def main():
    dry = '--dry-run' in sys.argv
    item = siguiente()
    if not item:
        print('cola vacía: nada que publicar')
        return 0
    fecha, d, ficha, html = item

    if fecha > datetime.date.today().isoformat():
        print(f"el siguiente ({d['slug']}) está fechado {fecha}: aún no toca")
        return 0

    indice = open(INDICE, encoding='utf-8').read()
    if f'href="{d["slug"]}"' in indice:
        print(f"{d['slug']} ya estaba en el índice; solo se mueve el archivo")
    else:
        marca = '    <article class="blog-card reveal">'
        i = indice.index(marca)
        indice = indice[:i] + tarjeta(d) + indice[i:]

    print(f"publicando: {d['slug']} ({d['categoria']}, {fecha})")
    if dry:
        return 0

    os.replace(html, os.path.join(BLOG, d['slug']))
    os.remove(ficha)
    open(INDICE, 'w', encoding='utf-8').write(indice)
    restantes = len(glob.glob(os.path.join(PEND, '*.json')))
    print(f'listo. quedan {restantes} en la cola')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
