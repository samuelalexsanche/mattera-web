#!/usr/bin/env python3
"""Pone al día la fecha visible de "actualizado" en las páginas que cambian.

Por qué no escribirla a mano: una fecha fija envejece sola y acaba mintiendo,
igual que el "50 preguntas" que prometía la portada cuando había 41. Esto la
deriva del propio commit.

Cómo funciona: el hook pre-commit lo llama con los archivos que ya están en el
índice. Si el archivo tiene el marcador data-actualizado, le escribe la fecha
de hoy — que es exactamente cuando se está modificando — tanto en el texto
visible como en el dateModified de los datos estructurados.

Las páginas que no cambian conservan su fecha, que es lo correcto: decir que
algo se actualizó hoy cuando no se tocó es la clase de señal falsa que resta
en lugar de sumar.

    python3 tools/fecha_actualizacion.py archivo.html [...]
"""
import datetime, json, re, sys

MESES = ['enero','febrero','marzo','abril','mayo','junio',
         'julio','agosto','septiembre','octubre','noviembre','diciembre']

def legible(iso):
    a, m, d = iso.split('-')
    return f'{int(d)} de {MESES[int(m)-1]} de {a}'

def main(rutas):
    hoy = datetime.date.today().isoformat()
    tocadas = 0
    for p in rutas:
        if not p.endswith('.html'):
            continue
        try:
            h = open(p, encoding='utf-8').read()
        except OSError:
            continue
        if 'data-actualizado' not in h:
            continue
        nuevo = re.sub(r'(<time data-actualizado datetime=")[^"]*("[^>]*>)[^<]*(</time>)',
                       lambda m: m.group(1) + hoy + m.group(2) + legible(hoy) + m.group(3), h)
        # dateModified del nodo WebPage, si lo hay
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', nuevo, re.S)
        if m:
            try:
                datos = json.loads(m.group(1))
                cambio = False
                for n in datos.get('@graph', []):
                    if isinstance(n, dict) and 'dateModified' in n and n.get('@type') in ('WebPage', 'FAQPage', 'CollectionPage', 'DefinedTermSet'):
                        if n['dateModified'] != hoy:
                            n['dateModified'] = hoy
                            cambio = True
                if cambio:
                    nuevo = nuevo[:m.start(1)] + '\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n' + nuevo[m.end(1):]
            except json.JSONDecodeError:
                pass
        if nuevo != h:
            open(p, 'w', encoding='utf-8').write(nuevo)
            print(f'  fecha al día: {p}')
            tocadas += 1
    return tocadas

if __name__ == '__main__':
    main(sys.argv[1:])
