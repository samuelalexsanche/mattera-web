import re
src=open('index.html').read()

def block(marker, end='</section>'):
    a=src.index(marker); b=src.index(end,a)+len(end); return src[a:b]

head_end=src.index('<body>')
head=src[:head_end]
head=head.replace('<title>','<meta name="robots" content="noindex,nofollow">\n<title>MAQUETA · ',1)

nav=src[src.index('<body>')+len('<body>'):src.index('<!-- HERO -->')]
portafolio=block('<!-- PORTAFOLIO -->')
como=block('<!-- CÓMO FUNCIONA -->')
calc=block('<!-- CALCULADORA -->')
cta=block('<!-- CTA FINAL -->')
industrias=block('<!-- INDUSTRIAS STRIP -->')
faq=block('<!-- FAQ -->')
hero=block('<!-- HERO -->')
footer=src[src.index('<footer>'):]

# ── HERO: quita micro-línea vieja, agrega tira de capturas ──
tira='''  <div class="hero-proof reveal reveal-delay-4">
        <p class="hero-proof-label">Sitios publicados por Mattera</p>
        <div class="hero-proof-strip">
          <a href="https://caabsasteel.mx/" target="_blank" rel="noopener"><img src="art/portafolio/caabsa.webp" width="960" height="540" alt="Sitio de CAABSA STEEL" loading="lazy"><span>caabsasteel.mx</span></a>
          <a href="https://birrieriacocula.com/" target="_blank" rel="noopener"><img src="art/portafolio/birrieria.webp" width="960" height="540" alt="Sitio de Birriería Cocula" loading="lazy"><span>birrieriacocula.com</span></a>
          <a href="https://luxuryandblush.com/" target="_blank" rel="noopener"><img src="art/portafolio/luxury.webp" width="960" height="540" alt="Sitio de Luxury and Blush" loading="lazy"><span>luxuryandblush.com</span></a>
          <a href="https://bisel3d.com/" target="_blank" rel="noopener"><img src="art/portafolio/bisel.webp" width="960" height="540" alt="Sitio de Bisel" loading="lazy"><span>bisel3d.com</span></a>
        </div>
        <a href="#portafolio" class="hero-proof-more">Ver el portafolio completo →</a>
      </div>
'''
m=re.search(r'[ \t]*<p class="hero-microline[^>]*>.*?</p>\n', hero, flags=re.S)
assert m, 'microline no encontrada'
hero=hero[:m.start()]+hero[m.end():]
i=hero.rindex('</section>')
hero=hero[:i]+tira+hero[i:]
hero=hero.replace('<a href="#calculadora" class="btn-ghost-outline" data-i18n="hero.cta2">Calcular mi ahorro</a>',
                  '<a href="#portafolio" class="btn-ghost-outline">Ver trabajos →</a>')

# ── QUÉ HACEMOS (6 tarjetas con mini interfaz) ──
def art(svg): return f'<div class="qh-art" aria-hidden="true">{svg}</div>'
A='var(--accent)'
svg_chat='''<svg viewBox="0 0 200 110" fill="none"><rect x="1" y="1" width="198" height="108" rx="6" fill="rgba(255,255,255,.03)" stroke="currentColor" stroke-opacity=".18"/><rect x="14" y="18" width="96" height="20" rx="10" fill="currentColor" fill-opacity=".14"/><rect x="24" y="26" width="60" height="4" rx="2" fill="currentColor" fill-opacity=".45"/><rect x="74" y="48" width="112" height="24" rx="10" fill="var(--accent)" fill-opacity=".9"/><rect x="86" y="54" width="78" height="4" rx="2" fill="#151910" fill-opacity=".55"/><rect x="86" y="62" width="52" height="4" rx="2" fill="#151910" fill-opacity=".35"/><rect x="14" y="80" width="70" height="16" rx="8" fill="currentColor" fill-opacity=".14"/><circle cx="24" cy="88" r="2.5" fill="currentColor" fill-opacity=".5"/><circle cx="32" cy="88" r="2.5" fill="currentColor" fill-opacity=".5"/><circle cx="40" cy="88" r="2.5" fill="currentColor" fill-opacity=".5"/></svg>'''
svg_agente='''<svg viewBox="0 0 200 110" fill="none"><rect x="1" y="1" width="198" height="108" rx="6" fill="rgba(255,255,255,.03)" stroke="currentColor" stroke-opacity=".18"/><circle cx="100" cy="55" r="20" stroke="var(--accent)" stroke-width="2"/><path d="M100 41v-14M100 83v-14M80 55H60M140 55h-20" stroke="currentColor" stroke-opacity=".45" stroke-width="2"/><rect x="40" y="46" width="20" height="18" rx="3" fill="currentColor" fill-opacity=".18"/><rect x="140" y="46" width="20" height="18" rx="3" fill="currentColor" fill-opacity=".18"/><rect x="90" y="16" width="20" height="12" rx="3" fill="currentColor" fill-opacity=".18"/><rect x="90" y="82" width="20" height="12" rx="3" fill="currentColor" fill-opacity=".18"/><circle cx="100" cy="55" r="6" fill="var(--accent)"/></svg>'''
svg_crm='''<svg viewBox="0 0 200 110" fill="none"><rect x="1" y="1" width="198" height="108" rx="6" fill="rgba(255,255,255,.03)" stroke="currentColor" stroke-opacity=".18"/><rect x="14" y="16" width="52" height="78" rx="4" fill="currentColor" fill-opacity=".07"/><rect x="74" y="16" width="52" height="78" rx="4" fill="currentColor" fill-opacity=".07"/><rect x="134" y="16" width="52" height="78" rx="4" fill="currentColor" fill-opacity=".07"/><rect x="20" y="24" width="40" height="16" rx="3" fill="currentColor" fill-opacity=".22"/><rect x="20" y="46" width="40" height="16" rx="3" fill="currentColor" fill-opacity=".22"/><rect x="80" y="24" width="40" height="16" rx="3" fill="var(--accent)" fill-opacity=".85"/><rect x="80" y="46" width="40" height="16" rx="3" fill="currentColor" fill-opacity=".22"/><rect x="140" y="24" width="40" height="16" rx="3" fill="currentColor" fill-opacity=".22"/></svg>'''
svg_conex='''<svg viewBox="0 0 200 110" fill="none"><rect x="1" y="1" width="198" height="108" rx="6" fill="rgba(255,255,255,.03)" stroke="currentColor" stroke-opacity=".18"/><rect x="18" y="38" width="36" height="34" rx="5" fill="currentColor" fill-opacity=".18"/><rect x="82" y="38" width="36" height="34" rx="5" fill="var(--accent)" fill-opacity=".85"/><rect x="146" y="38" width="36" height="34" rx="5" fill="currentColor" fill-opacity=".18"/><path d="M54 55h28M118 55h28" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/><path d="M74 51l8 4-8 4M138 51l8 4-8 4" fill="var(--accent)"/></svg>'''
svg_rep='''<svg viewBox="0 0 200 110" fill="none"><rect x="1" y="1" width="198" height="108" rx="6" fill="rgba(255,255,255,.03)" stroke="currentColor" stroke-opacity=".18"/><rect x="24" y="62" width="20" height="30" rx="2" fill="currentColor" fill-opacity=".25"/><rect x="54" y="48" width="20" height="44" rx="2" fill="currentColor" fill-opacity=".25"/><rect x="84" y="54" width="20" height="38" rx="2" fill="currentColor" fill-opacity=".25"/><rect x="114" y="32" width="20" height="60" rx="2" fill="var(--accent)" fill-opacity=".9"/><rect x="144" y="42" width="20" height="50" rx="2" fill="currentColor" fill-opacity=".25"/><path d="M24 26h60" stroke="currentColor" stroke-opacity=".3" stroke-width="3"/></svg>'''
svg_web='''<svg viewBox="0 0 200 110" fill="none"><rect x="1" y="1" width="198" height="108" rx="6" fill="rgba(255,255,255,.03)" stroke="currentColor" stroke-opacity=".18"/><path d="M1 22h198" stroke="currentColor" stroke-opacity=".18"/><circle cx="14" cy="11.5" r="3" fill="currentColor" fill-opacity=".3"/><circle cx="26" cy="11.5" r="3" fill="currentColor" fill-opacity=".3"/><circle cx="38" cy="11.5" r="3" fill="currentColor" fill-opacity=".3"/><rect x="16" y="34" width="84" height="8" rx="3" fill="currentColor" fill-opacity=".35"/><rect x="16" y="48" width="60" height="6" rx="3" fill="currentColor" fill-opacity=".2"/><rect x="16" y="68" width="52" height="18" rx="4" fill="var(--accent)" fill-opacity=".9"/><rect x="116" y="34" width="68" height="52" rx="4" fill="currentColor" fill-opacity=".12"/></svg>'''
cards=[
 (svg_web,'Sitio web que vende','Carga rápido, sale en Google y convierte visitas en conversaciones.','servicios/paginas-web.html','Ver sitios web'),
 (svg_chat,'Atención en WhatsApp 24/7','Responde dudas, toma pedidos y agenda citas mientras tú duermes.','servicios/chatbot-whatsapp.html','Ver asistente de WhatsApp'),
 (svg_agente,'Asistente que conoce tu negocio','Entrenado con tus productos, precios y tu forma de atender.','servicios/agentes-ia.html','Ver agentes de IA'),
 (svg_crm,'Todo tu seguimiento en un lugar','Clientes, conversaciones y pedidos ordenados, sin depender de la memoria.','servicios/crm-para-empresas.html','Ver CRM a medida'),
 (svg_conex,'Tus herramientas, conectadas','WhatsApp con el CRM, formularios con el correo: sin capturar dos veces.','servicios/integraciones.html','Ver integraciones'),
 (svg_rep,'Procesos que corren solos','Cotizar, dar seguimiento y reportar deja de consumir horas del equipo.','servicios/automatizacion-procesos.html','Ver automatización'),
]
qh='<!-- QUÉ HACEMOS -->\n<section class="section sec-dark px" data-px="sistemas" id="servicios" aria-labelledby="servicios-title">\n  <p class="section-eyebrow reveal">QUÉ HACEMOS</p>\n  <h2 class="section-title reveal reveal-delay-1" id="servicios-title">Seis piezas. Un solo sistema<br>operando tu negocio.</h2>\n  <div class="qh-grid">\n'
for i,(svg,t,d,href,link) in enumerate(cards):
    qh+=f'''    <a class="qh-card reveal reveal-delay-{i%3+1}" href="{href}">
      {art(svg)}
      <h3 class="qh-title">{t}</h3>
      <p class="qh-desc">{d}</p>
      <span class="qh-link">{link} →</span>
    </a>\n'''
qh+='  </div>\n'
# chips de industrias dentro de la misma sección
chips=re.search(r'<div class="industrias-strip.*?</div>', industrias, re.S)
qh+='''  <div class="qh-industrias reveal">
    <p class="qh-ind-label">Lo aplicamos por giro:</p>
    <div class="qh-chips">
      <a href="industrias/clinicas.html">Clínicas</a>
      <a href="industrias/inmobiliarias.html">Inmobiliarias</a>
      <a href="industrias/restaurantes.html">Restaurantes</a>
      <a href="industrias/distribuidoras.html">Distribuidoras</a>
      <a href="industrias/despachos.html">Despachos</a>
    </div>
  </div>
</section>'''

open('/tmp/claude-501/parts.py','w').write('')
import json
json.dump({'head':head,'nav':nav,'hero':hero,'qh':qh,'portafolio':portafolio,'como':como,'calc':calc,'faq':faq,'cta':cta,'footer':footer},open('/tmp/claude-501/parts.json','w'))
print('ok', {k:len(v) for k,v in json.load(open('/tmp/claude-501/parts.json')).items()})
