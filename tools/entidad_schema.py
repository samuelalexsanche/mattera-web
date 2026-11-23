#!/usr/bin/env python3
"""Ata cada página a la misma entidad Mattera en los datos estructurados.

El problema que resuelve: la portada define el negocio con
@id https://matterasystems.com/#organization, pero el resto de las páginas
repetía un Organization suelto, sin @id, o no mencionaba a la empresa. Para un
motor que lee datos estructurados, un Organization sin @id en cada página es
una empresa distinta cada vez: nada ata las 56 respuestas del FAQ, el glosario
ni los artículos a la misma entidad que tiene la dirección, el teléfono y las
redes.

Qué hace:
  · sustituye los Organization sueltos de publisher/provider/author por una
    referencia {"@id": ...#organization};
  · añade a cada página un nodo Organization mínimo con ese mismo @id, para
    que la referencia resuelva aunque el motor lea la página sola;
  · deja intacta la portada y la página local, que ya definen la entidad
    completa con LocalBusiness.

    python3 tools/entidad_schema.py [--revisar]
"""
import glob, json, re, sys

ID = 'https://matterasystems.com/#organization'
PATRONES = ['*.html', 'servicios/*.html', 'industrias/*.html', 'blog/*.html',
            'en/*.html', 'en/services/*.html', 'en/industries/*.html']
# Estas ya definen la entidad completa; tocarlas sería duplicarla.
COMPLETAS = {'index.html', 'agencia-ia-guadalajara.html'}

MINIMO = {"@type": "Organization", "@id": ID, "name": "Mattera Systems",
          "url": "https://matterasystems.com/",
          "description": ("Agencia de inteligencia artificial en Guadalajara que automatiza "
                          "operaciones de empresa: agentes de IA, automatización de procesos, "
                          "integración entre sistemas, CRM a medida, asistentes de WhatsApp y sitios web.")}

def ref(valor):
    """Organization suelto -> referencia por @id. Lo demás se deja igual."""
    if isinstance(valor, dict) and valor.get('@type') == 'Organization' and '@id' not in valor:
        if valor.get('name', '').startswith('Mattera'):
            return {'@id': ID}
    return valor

def main():
    revisar = '--revisar' in sys.argv
    tocadas = 0
    for p in sorted({x for pat in PATRONES for x in glob.glob(pat)}):
        if p in COMPLETAS:
            continue
        h = open(p, encoding='utf-8').read()
        if re.search(r'name=["\']robots["\'][^>]*noindex', h):
            continue
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
        if not m:
            continue
        try:
            datos = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        grafo = datos.get('@graph')
        if grafo is None:
            grafo = [datos]
            datos = {'@context': 'https://schema.org', '@graph': grafo}

        antes = json.dumps(datos, ensure_ascii=False, sort_keys=True)
        for n in grafo:
            if not isinstance(n, dict):
                continue
            for campo in ('publisher', 'provider', 'author'):
                if campo in n:
                    n[campo] = ref(n[campo])
        if not any(isinstance(n, dict) and n.get('@id') == ID for n in grafo):
            grafo.insert(0, MINIMO)
        if json.dumps(datos, ensure_ascii=False, sort_keys=True) == antes:
            continue
        tocadas += 1
        print('  ', p)
        if revisar:
            continue
        nuevo = json.dumps(datos, ensure_ascii=False, indent=2)
        open(p, 'w', encoding='utf-8').write(h[:m.start(1)] + '\n' + nuevo + '\n' + h[m.end(1):])
    print(f'\npáginas {"por atar" if revisar else "atadas"} a la entidad: {tocadas}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
