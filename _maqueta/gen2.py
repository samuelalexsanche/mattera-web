# -*- coding: utf-8 -*-
import json,re
P=json.load(open('/tmp/claude-501/parts.json'))
P['qh']=P['qh'].replace('      <a href="industrias/despachos.html">Despachos</a>\n','      <a href="industrias/">Ver todos los giros</a>\n')

# ── PLANES: tabla comparativa ──
filas=[
 ('Páginas','1 página, hasta 6 bloques','Hasta 5 secciones','Secciones ilimitadas, catálogo o blog'),
 ('Asistente de IA 24/7','—','Entrenado con tu negocio, hasta 200 conversaciones al mes','Entrenado a profundidad, hasta 600 conversaciones al mes'),
 ('SEO y GEO','Base técnica','Completos + ficha de Google conectada','Completos + monitoreo en cuatro buscadores con IA'),
 ('Registro de contactos','Formulario y botón de WhatsApp','Cada contacto guardado, con aviso por correo','Panel con estado, notas e historial'),
 ('Agenda','—','Pase a tu WhatsApp con la conversación resumida','El asistente agenda en tu calendario'),
 ('Cambios de contenido','—','1 al mes','4 al mes'),
 ('Reporte','—','Mensual','Quincenal'),
 ('En línea en','5 días','7 días','14 días'),
 ('Mantenimiento','$199/mes','$299/mes','$799/mes'),
]
def celda(v):
    if v=='—': return '<td class="pl-no"><span aria-label="No incluido">—</span></td>'
    return f'<td><span class="pl-si" aria-hidden="true">✓</span>{v}</td>'
tabla=''.join('<tr><th scope="row">%s</th>%s%s%s</tr>'%(f[0],celda(f[1]),celda(f[2]),celda(f[3])) for f in filas)

planes = '''<!-- PLANES -->
<section class="section sec-dark px" data-px="planes" id="sitios-web" aria-labelledby="planes-home-title">
  <p class="section-eyebrow reveal">PRECIOS</p>
  <h2 class="section-title reveal reveal-delay-1" id="planes-home-title">Precio público.<br>Sin cotización.</h2>
  <p class="pl-lede reveal reveal-delay-2">De contado o a <strong>6 meses sin intereses</strong>, al mismo precio. Los tres incluyen <strong>SEO y GEO</strong>.</p>

  <details class="pl-expl reveal">
    <summary>¿Qué son SEO y GEO, en corto?</summary>
    <div class="pl-expl-body">
      <p><strong>SEO</strong> — que tu negocio aparezca cuando alguien busca en Google lo que vendes.</p>
      <p><strong>GEO</strong> — que ChatGPT y otras IA te mencionen por nombre cuando les preguntan quién ofrece tu servicio en tu ciudad. Si tu sitio no está preparado, dan el nombre de tu competencia.</p>
      <p><a href="planes.html">Ver cómo lo corregimos →</a></p>
    </div>
  </details>

  <div class="pl-wrap reveal reveal-delay-1">
    <table class="pl-tabla">
      <caption class="sr-only">Comparación de los tres planes de sitio web</caption>
      <thead>
        <tr>
          <td></td>
          <th scope="col"><span class="pl-tier">T1 · Presencia</span><span class="pl-precio">$5,900</span><span class="pl-msi">$983/mes · 6 MSI</span></th>
          <th scope="col" class="pl-destacado"><span class="pl-badge">Más elegido</span><span class="pl-tier">T2 · Sistema</span><span class="pl-precio">$9,900</span><span class="pl-msi">$1,650/mes · 6 MSI</span></th>
          <th scope="col"><span class="pl-tier">T3 · Operación</span><span class="pl-precio">$19,900</span><span class="pl-msi">$3,317/mes · 6 MSI</span></th>
        </tr>
      </thead>
      <tbody>''' + tabla + '''</tbody>
      <tfoot>
        <tr>
          <td></td>
          <td><a href="https://wa.me/523327874747?text=Hola%2C%20me%20interesa%20el%20plan%20T1%20Presencia%20(%245%2C900)" target="_blank" rel="noopener noreferrer" data-plan="t1" class="btn-outline"><span>Contratar →</span></a></td>
          <td class="pl-destacado"><a href="https://wa.me/523327874747?text=Hola%2C%20me%20interesa%20el%20plan%20T2%20Sistema%20(%249%2C900)" target="_blank" rel="noopener noreferrer" data-plan="t2" class="btn-primary"><span>Contratar →</span></a></td>
          <td><a href="https://wa.me/523327874747?text=Hola%2C%20me%20interesa%20el%20plan%20T3%20Operaci%C3%B3n%20(%2419%2C900)" target="_blank" rel="noopener noreferrer" data-plan="t3" class="btn-outline"><span>Contratar →</span></a></td>
        </tr>
      </tfoot>
    </table>
  </div>
  <p class="pl-nota reveal">Los 6 MSI los otorga tu banco y requieren tarjeta de crédito mexicana. <a href="planes.html">Ver el detalle de cada plan →</a></p>
</section>'''

# ── DUDAS: 5 preguntas ──
faq=P['faq']
items=re.findall(r'<div class="faq-item">.*?</div>\s*</div>', faq, re.S)
elegidas=[]
claves=['¿Cuánto tiempo toma implementarlo?','¿Qué pago una sola vez y qué pago cada mes?','¿Qué pasa si el sistema no funciona como esperaba?','¿El sistema es mío si dejo de trabajar con Mattera?','¿Mi equipo necesita saber de informática?']
for c in claves:
    for it in items:
        if c in it: elegidas.append(it); break
assert len(elegidas)==5, len(elegidas)
dudas='''<!-- DUDAS -->
<section class="section sec-dark" id="faq" aria-labelledby="faq-title">
  <p class="section-eyebrow reveal">DUDAS</p>
  <h2 class="section-title reveal reveal-delay-1" id="faq-title">Preguntas directas.<br>Respuestas honestas.</h2>
  <div class="faq-list reveal reveal-delay-2" style="max-width:760px">
''' + '\n'.join('    '+e for e in elegidas) + '''
  </div>
  <p style="margin-top:1.5rem"><a href="faq.html" class="pl-nota-link">Ver las 50 preguntas completas →</a></p>
</section>'''

# ── CALCULADORA dentro de un desplegable ──
calc=P['calc']
calc_inner=calc[calc.index('>',calc.index('<section'))+1:calc.rindex('</section>')]
calc_inner=re.sub(r'<p class="section-eyebrow[^>]*>.*?</p>','',calc_inner,flags=re.S)
calc_inner=re.sub(r'<h2 class="section-title[^>]*>.*?</h2>','',calc_inner,count=1,flags=re.S)
calculadora='''<!-- CALCULADORA -->
<section class="section sec-paper" id="calculadora" aria-labelledby="calc-title">
  <p class="section-eyebrow reveal">CUÁNTO TE AHORRA</p>
  <h2 class="section-title reveal reveal-delay-1" id="calc-title">Haz el número<br>con tus propios datos.</h2>
  <details class="calc-det reveal reveal-delay-2">
    <summary>Abrir la calculadora</summary>
    <div class="calc-det-body">''' + calc_inner + '''</div>
  </details>
</section>'''

barra='''<!-- BARRA FIJA MÓVIL -->
<div class="barra-movil" role="navigation" aria-label="Accesos rápidos">
  <a href="#sitios-web">Precios</a>
  <a href="#portafolio">Trabajos</a>
  <a href="https://wa.me/523327874747" target="_blank" rel="noopener noreferrer" class="barra-wa">WhatsApp</a>
</div>'''

css=open('/tmp/claude-501/nuevo.css').read()
div='<hr class="divider">\n'
body=(P['nav']+P['hero']+div+P['qh']+div+P['portafolio']+div+planes+div+P['como']+div+calculadora+div+dudas+div+P['cta']+barra+'\n'+P['footer'])
head=P['head']
assert head.count('</head>')==1
head=re.sub(r'<script type="application/ld\+json">.*?</script>\n?','',head,flags=re.S)
head=head.replace('</head>','<style>\n'+css+'</style>\n</head>')
html=head+'<body>'+body
open('preview-inicio.html','w').write(html)
print(len(html))
