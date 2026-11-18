#!/usr/bin/env python3
"""Pone un autor con nombre en los artículos, en lugar de la empresa.

Un artículo firmado por una organización no dice nada sobre quién sabe del
tema. Google y los motores generativos tratan la autoría con nombre, cargo y
especialidad como señal de calidad: es parte de poder responder "¿quién dice
esto y por qué le creo?".

La portada ya define a la persona con @id .../#founder, incluido jobTitle y
knowsAbout. Este script hace que los artículos la referencien por ese mismo
@id, y deja publisher apuntando a la empresa. Así quedan separadas las dos
preguntas: quién lo escribió y quién lo publica.

    python3 tools/autor_schema.py [--revisar]
"""
import glob, json, re, sys

AUTOR = 'https://matterasystems.com/#founder'
ORG = 'https://matterasystems.com/#organization'

PERSONA = {"@type": "Person", "@id": AUTOR,
           "name": "Samuel Alexander Gonzalez Legaspi",
           "jobTitle": "Fundador de Mattera Systems",
           "worksFor": {"@id": ORG},
           "knowsAbout": ["Automatización de procesos de negocio",
                          "Agentes de inteligencia artificial",
                          "Integración de sistemas",
                          "Chatbots de WhatsApp Business",
                          "CRM a medida"]}

def main():
    revisar = '--revisar' in sys.argv
    tocadas = 0
    for p in sorted(glob.glob('blog/*.html')):
        h = open(p, encoding='utf-8').read()
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
        if not m:
            continue
        try:
            datos = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        grafo = datos.get('@graph', [])
        articulo = next((n for n in grafo if isinstance(n, dict) and n.get('@type') == 'Article'), None)
        if not articulo:
            continue
        if articulo.get('author') == {'@id': AUTOR}:
            continue
        articulo['author'] = {'@id': AUTOR}
        articulo.setdefault('publisher', {'@id': ORG})
        if not any(isinstance(n, dict) and n.get('@id') == AUTOR for n in grafo):
            grafo.insert(1, PERSONA)
        tocadas += 1
        print('  ', p)
        if revisar:
            continue
        nuevo = json.dumps(datos, ensure_ascii=False, indent=2)
        open(p, 'w', encoding='utf-8').write(h[:m.start(1)] + '\n' + nuevo + '\n' + h[m.end(1):])
    print(f'\nartículos {"por firmar" if revisar else "firmados"}: {tocadas}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
