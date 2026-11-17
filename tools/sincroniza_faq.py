#!/usr/bin/env python3
"""
Hace que el FAQPage de cada página diga exactamente lo que la página enseña.

Google solo muestra el resultado enriquecido de preguntas frecuentes si cada
pregunta y cada respuesta del marcado están visibles en la página. Cuando el
texto visible se edita y el JSON-LD no, el bloque entero deja de valer — y de
paso los motores generativos citan texto que el visitante nunca ve.

Este script lee el acordeón visible (.faq-btn + .faq-answer) y reescribe el
mainEntity del FAQPage con esas mismas preguntas y respuestas, palabra por
palabra. Las páginas sin acordeón visible no se tocan: se avisan para
resolverlas a mano.

    python3 tools/sincroniza_faq.py            # aplica
    python3 tools/sincroniza_faq.py --revisar  # solo informa, no escribe
"""
import glob, html as H, json, re, sys

PATRONES = ['*.html', 'servicios/*.html', 'industrias/*.html', 'blog/*.html',
            'en/*.html', 'en/services/*.html', 'en/industries/*.html']

def visibles(h):
    pares = []
    for m in re.finditer(r'class="faq-btn"[^>]*>(.*?)</button>\s*<div class="faq-answer"[^>]*>(.*?)</div>', h, re.S):
        q = ' '.join(H.unescape(re.sub(r'<[^>]+>', ' ', m.group(1))).split()).rstrip(' +').strip()
        a = ' '.join(H.unescape(re.sub(r'<[^>]+>', ' ', m.group(2))).split())
        if q and a:
            pares.append({"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}})
    return pares

def main():
    revisar = '--revisar' in sys.argv
    tocadas = avisos = 0
    for p in sorted({x for pat in PATRONES for x in glob.glob(pat)}):
        h = open(p, encoding='utf-8').read()
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
        if not m:
            continue
        try:
            datos = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        nodos = datos.get('@graph', [datos]) if isinstance(datos, dict) else datos
        faq = next((n for n in nodos if isinstance(n, dict) and n.get('@type') == 'FAQPage'), None)
        if not faq:
            continue

        pares = visibles(h)
        if not pares:
            print(f'  AVISO  {p}: tiene FAQPage con {len(faq.get("mainEntity", []))} preguntas '
                  f'pero la página no enseña ningún acordeón. Resolver a mano.')
            avisos += 1
            continue
        if faq.get('mainEntity') == pares:
            continue
        antes = len(faq.get('mainEntity', []))
        print(f'  {p}: {antes} -> {len(pares)} preguntas')
        tocadas += 1
        if revisar:
            continue
        faq['mainEntity'] = pares
        nuevo = json.dumps(datos, ensure_ascii=False, indent=2)
        open(p, 'w', encoding='utf-8').write(h[:m.start(1)] + '\n' + nuevo + '\n' + h[m.end(1):])
    print(f'\npáginas {"por corregir" if revisar else "corregidas"}: {tocadas} | avisos: {avisos}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
