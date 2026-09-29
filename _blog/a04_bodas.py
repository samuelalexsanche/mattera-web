# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>Quien contrata una boda de destino compra confianza a distancia</h2>
    <p>Una pareja que se casa en México viviendo en otro país toma una decisión de mucho dinero sin conocer a nadie en persona. No puede visitar el lugar, no puede tomarse un café con la organizadora y no conoce a los proveedores. Lo único que tiene para decidir es lo que ve en internet.</p>
    <p>Eso cambia lo que el sitio tiene que hacer. No basta con verse bonito: tiene que probar que esas bodas ocurrieron, que fueron distintas entre sí y que alguien las coordinó de principio a fin. Un carrusel de veinte fotos sueltas no prueba nada — podrían ser de cualquiera.</p>
    <p>Hay una segunda barrera: el idioma. Si la pareja habla inglés y el sitio solo está en español, la lectura se vuelve un esfuerzo justo en el momento en que estaba evaluando si confiar.</p>

    <h2>Lo que construimos para Luxury and Blush Events</h2>
    <p><a href="https://luxuryandblush.com/" target="_blank" rel="noopener">Luxury and Blush Events</a> organiza bodas de destino en México y su público principal son parejas extranjeras. El sitio ya existía, pero estaba mal hecho: no dejaba ver el trabajo.</p>
    <p>El rediseño se apoyó en dos decisiones. La primera: <strong>cada boda tiene su propia galería</strong>, con su lugar, su año y sus fotos, en vez de un revoltijo de imágenes. Así la pareja no ve "fotos de bodas": ve bodas completas, una por una, y puede reconocer la que se parece a la que imagina.</p>
    <p>La segunda: el sitio es <strong>bilingüe</strong>. El mismo contenido existe en inglés y en español y se cambia con un botón, sin mandar al visitante a otra versión incompleta. Hay además una página aparte de reseñas y reconocimientos, que es lo que una pareja busca cuando ya se está convenciendo.</p>

    <h2>Por qué una galería por boda y no una sola</h2>
{tabla(['Lo que la pareja evalúa','Galería revuelta','Una galería por boda'],
 [['¿Ha hecho bodas como la mía?','Hay que adivinar','Se ve la boda completa, con su lugar'],
  ['¿Trabaja en mi destino?','No se distingue','Cada galería trae su ubicación'],
  ['¿Es su trabajo o fotos de banco?','Duda razonable','Serie completa del mismo evento'],
  ['¿Puedo enseñárselo a mi pareja?','Enlace genérico','Enlace a esa boda en particular'],
  ['¿Aparece al buscar el destino?','Una sola página compite','Cada galería puede posicionar']])}
    <p>El efecto en buscadores es el mismo principio que aplicamos en otros giros: una página por unidad real de trabajo. Quien busca "wedding planner en Riviera Nayarit" o "boda en hacienda en Jalisco" necesita encontrar una página que trate exactamente eso. Si todo el trabajo vive en una sola página, hay una sola oportunidad.</p>

    <h2>Las reseñas y los premios van en su propia página</h2>
    <p>En este giro la prueba social pesa tanto como el portafolio, y conviene darle espacio propio en vez de esparcir testimonios sueltos entre las fotos. Una página de reseñas y reconocimientos cumple dos funciones: la pareja que ya está convencida encuentra ahí el último empujón, y quien busca el nombre de la organizadora junto con la palabra "opiniones" llega a una página que responde exactamente eso.</p>
    <p>La regla que aplicamos siempre: solo se publica lo que se puede verificar. Testimonios reales, con nombre del evento o del lugar cuando la pareja lo autoriza. Inventar reseñas es la forma más rápida de perder la confianza que todo el sitio intentaba construir, y además arriesga una penalización de Google.</p>

    <h2>Lo que las IA necesitan para recomendarte</h2>
    <p>Cada vez más parejas empiezan preguntándole a una IA: "quién organiza bodas de destino en la Riviera Nayarit", "wedding planners para bodas en México con servicio en inglés". Para que un modelo pueda dar tu nombre necesita encontrar escrito, en texto plano y verificable, qué haces, dónde operas y en qué idiomas atiendes.</p>
    <p>Eso no se resuelve con fotos, por buenas que sean. Se resuelve con texto: descripciones de cada boda con su ubicación, una página que diga con todas sus letras en qué destinos trabajas, y datos de contacto consistentes en el sitio, la ficha de Google y las redes. Es el mismo criterio que explicamos en <a href="que-es-geo-optimizacion-para-ia.html">qué es GEO</a>.</p>

    <h2>El seguimiento es el punto débil del giro</h2>
    <p>En bodas, entre la primera consulta y la firma pueden pasar meses. La pareja escribe, pide disponibilidad de fecha, pregunta por presupuesto aproximado y luego desaparece dos o tres semanas mientras decide. Ese es exactamente el escenario donde el seguimiento manual falla: cuando la organizadora está en plena temporada, los prospectos de hace tres semanas se pierden.</p>
    <p>Aquí es donde un <a href="../servicios/crm-para-empresas.html">registro de contactos con recordatorios</a> vale más que cualquier otra automatización: no se trata de contestar más rápido, sino de que ninguna pareja quede sin respuesta de seguimiento. Y con diferencia de horario, la respuesta inmediata fuera de horario también pesa: una consulta que entra a las 3 de la mañana hora de México es media mañana en Europa.</p>
    <p>Lo que no conviene automatizar en este giro es la conversación de venta. Una boda se vende con criterio, sensibilidad y trato personal. El sistema atiende lo previo — disponibilidad, rangos, cómo trabaja la organizadora, qué incluye — y entrega la conversación resumida.</p>

    <h2>Qué se lleva de aquí una organizadora de eventos</h2>
    <p>Tres cosas concretas: publica cada evento como página propia, con lugar y año; ten el sitio en el idioma de quien te contrata; y registra cada consulta con su fecha de seguimiento. Lo demás — diseño, fotos, redes — ayuda, pero no sustituye a esas tres.</p>
    <p>Si quieres ver cómo se traduce a precio y plazo, los <a href="../planes.html">planes están publicados</a>. Para un sitio con galerías por evento, el plan intermedio o el mayor son los que tienen sentido, porque el número de páginas crece con cada boda que agregas.</p>
'''

spec = dict(
    slug='pagina-web-para-wedding-planners.html',
    title='Página web para wedding planners y bodas de destino | Mattera Systems',
    h1='Página web para wedding planners: cómo se vende una boda a distancia',
    titulo_corto='Página web para wedding planners',
    desc='Qué necesita el sitio de una organizadora de bodas de destino para que una pareja extranjera confíe: galería por boda, sitio bilingüe y seguimiento que no se olvida.',
    bajada='Una pareja que se casa en México desde otro país decide con lo que ve en internet. Un carrusel de fotos sueltas no prueba nada.',
    lede='El sitio de una wedding planner de bodas de destino funciona cuando prueba tres cosas: que esas bodas ocurrieron, que fueron distintas entre sí y que alguien las coordinó completas. Esto es lo que rediseñamos para Luxury and Blush Events, con una galería por boda y el sitio en dos idiomas.',
    fecha='2026-09-29',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Organizas eventos y tu trabajo está en un carrusel de fotos? Se puede publicar evento por evento.',
    faq=[('¿Por qué una galería por boda en vez de una sola?','Porque la pareja no evalúa fotos, evalúa bodas completas. Además cada galería con su lugar y su año es una página que puede posicionarse por ese destino; una sola galería compite por una sola búsqueda.'),
         ('¿Vale la pena tener el sitio en inglés?','En bodas de destino, sí: buena parte de las parejas son extranjeras. El contenido debe existir completo en ambos idiomas, no una versión reducida en inglés.'),
         ('¿Se puede automatizar la venta de una boda?','No, y no conviene intentarlo. Lo que se automatiza es lo previo: disponibilidad de fechas, rangos, qué incluye el servicio y el seguimiento a quien no ha respondido. La conversación de venta sigue siendo personal.'),
         ('¿Qué automatización rinde más en este giro?','El registro de contactos con recordatorios de seguimiento. Entre la primera consulta y la firma pasan meses y es ahí donde se pierden parejas interesadas.'),
         ('¿Qué plan conviene para un sitio con muchas galerías?','El intermedio o el mayor, porque el número de páginas crece con cada evento publicado. Los precios están publicados en la página de planes.')],
    relacionado=[('../servicios/paginas-web.html','Sitios web con IA →'),
                 ('../servicios/crm-para-empresas.html','CRM a medida →'),
                 ('pagina-web-para-restaurantes.html','Página web para restaurantes →'),
                 ('../planes.html','Planes y precios →')],
)
print(escribir(spec))
