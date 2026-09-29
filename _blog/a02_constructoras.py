# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>El problema de vender obra industrial por internet</h2>
    <p>Una constructora industrial no vende por impulso. Del otro lado hay un gerente de planta, un comprador corporativo o un director de proyecto que necesita verificar tres cosas antes de levantar el teléfono: que hayas hecho obra parecida a la suya, que operes en su estado y que tengas las certificaciones que su empresa exige.</p>
    <p>La mayoría de los sitios de constructoras responden mal esas tres preguntas. Presentan la empresa en una sola página, meten las obras en una galería sin nombre ni ubicación y dejan las certificaciones en un PDF. El visitante no encuentra lo que vino a verificar y se va con quien sí lo muestre.</p>
    <p>En buscadores el efecto es peor: un sitio de una página compite por una sola búsqueda. Quien busca "nave industrial en Querétaro" o "montaje de estructura de acero para automotriz" nunca llega, porque no hay una página que trate ese tema.</p>

    <h2>Lo que construimos para CAABSA STEEL</h2>
    <p><a href="https://caabsasteel.mx/" target="_blank" rel="noopener">CAABSA STEEL</a> es una constructora industrial con obra en varios estados del país. Su sitio anterior no dejaba ver ese trabajo. El que opera hoy tiene 148 páginas, y esa cifra no es presumir tamaño: es la estructura del negocio traducida a direcciones web.</p>
    <p>Cada obra tiene página propia, con su cliente, su ubicación, sus metros construidos y sus fotos. Cada sector — automotriz, alimenticio, logístico, corporativo, aeronáutico, industrial — tiene la suya, y lista todas las obras de ese ramo. Cada región y cada estado también. Así, la persona que busca por su industria llega a la página de su industria, y la que busca por su estado llega a la de su estado.</p>
    <p>Todo el sitio existe además en inglés, en rutas propias, porque una parte de sus clientes son corporativos extranjeros que evalúan proveedores en México.</p>
    <p>El sitio incluye un asistente de IA que responde dudas sobre sectores, cobertura y proceso constructivo, y formularios que llegan al correo de la empresa con la conversación ya resumida. El asistente tiene prohibido inventar precios o plazos: cuando la pregunta es de números, deriva a un ingeniero.</p>

    <h2>Por qué una obra por página no es exageración</h2>
    <p>Es la diferencia entre competir por una búsqueda y competir por cientos. Un sitio de una página responde a "constructora industrial". Un sitio con página por obra, sector, región y estado responde también a "quién construyó la planta de X", "naves industriales en el Bajío" o "estructura de acero para planta alimenticia".</p>
{tabla(['Qué busca el cliente','Sitio de una página','Sitio estructurado por obra y sector'],
 [['"Constructora industrial"','Aparece, con mucha competencia','Aparece, con más respaldo'],
  ['"Nave industrial en Querétaro"','No hay página que lo trate','Página de estado con sus obras'],
  ['"Estructura de acero automotriz"','No aparece','Página de sector con obras del ramo'],
  ['Verificar experiencia','Galería sin contexto','Ficha de obra con cliente y metros'],
  ['Comprador extranjero','Solo español','Versión en inglés equivalente']])}
    <p>Lo mismo aplica cuando quien pregunta es una IA. Cuando alguien le pide a ChatGPT una constructora con experiencia en cierto sector y cierta región, el modelo necesita encontrar esa relación escrita en algún lado. Una galería de fotos no la contiene; una ficha de obra con cliente, sector y estado, sí.</p>

    <h2>Qué pasa con la consulta cuando llega</h2>
    <p>En obra industrial el volumen de consultas es bajo y el valor de cada una es alto. Eso cambia el diseño: no se trata de filtrar cientos de mensajes, sino de que ninguno se caiga y de que el ingeniero reciba la consulta con contexto suficiente para responder sin tres correos de ida y vuelta.</p>
    <p>Por eso el formulario no pide solo nombre y teléfono: pregunta sector, ubicación y tipo de proyecto, y esos datos llegan al correo de la empresa dentro del mismo mensaje, con botones para responder o llamar. El asistente cumple la función previa: atiende al visitante que todavía está explorando, le muestra obras parecidas a la suya y le explica el proceso, de modo que cuando llena el formulario ya sabe con quién está hablando.</p>
    <p>La otra mitad del trabajo es de horario. Un comprador que revisa proveedores lo hace cuando puede, muchas veces fuera de oficina. Que a las diez de la noche alguien pueda preguntar si trabajan en cierto estado y obtener respuesta inmediata evita que esa evaluación se detenga hasta el día siguiente — que es, en la práctica, cuando se pierde frente a otro proveedor que sí contestó.</p>

    <h2>Lo que este caso tiene de replicable</h2>
    <p>El material ya existía. Las fotos de obra estaban en las carpetas de la empresa, los datos de cada proyecto en su currículum corporativo. Lo que no existía era la estructura que convierte ese archivo en páginas que alguien pueda encontrar.</p>
    <p>Eso se repite en casi toda empresa industrial con años de trayectoria: el respaldo está, pero disperso en documentos internos. El trabajo no es inventar contenido, es ordenarlo.</p>
    <p>Un punto que sí exige disciplina: no inventar. En el proceso aparecieron ciudades y cifras que nadie podía respaldar y se corrigieron antes de publicar. En obra industrial, un dato falso se detecta rápido y cuesta la credibilidad completa.</p>

    <h2>Qué ofrece Mattera a una constructora</h2>
    <p>El mismo esquema: <a href="../servicios/paginas-web.html">sitio estructurado por obra, sector y región</a>, con SEO y GEO; <a href="../servicios/chatbot-whatsapp.html">asistente de IA</a> que filtra consultas y resume antes de pasarlas a un humano; y formularios conectados al correo de la empresa, sin plataformas intermedias.</p>
    <p>Si tu empresa tiene obra terminada y no la tiene publicada con nombre, sector y ubicación, ese es el trabajo pendiente. Los precios de los planes de sitio están <a href="../planes.html">publicados</a>; para un sitio del tamaño del de una constructora, el alcance se define en el diagnóstico.</p>
'''

spec = dict(
    slug='pagina-web-para-constructoras-industriales.html',
    title='Página web para constructoras industriales: el caso CAABSA STEEL | Mattera',
    h1='Página web para una constructora industrial: qué tiene que mostrar',
    titulo_corto='Página web para constructoras industriales',
    desc='Qué necesita el sitio de una constructora industrial para que un comprador la considere: obra por página, sector, región y versión en inglés. El caso CAABSA STEEL.',
    bajada='Quien evalúa a una constructora verifica tres cosas antes de llamar. Un sitio de una página no responde ninguna.',
    lede='El sitio de una constructora industrial funciona cuando deja verificar tres cosas en minutos: qué obra ha hecho, en qué sectores y en qué estados opera. Esto es lo que construimos para CAABSA STEEL y por qué su sitio tiene una página por obra en vez de una galería.',
    fecha='2026-09-29',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Tu empresa tiene obra terminada que no aparece en tu sitio? Eso se puede ordenar y publicar.',
    faq=[('¿Cuántas páginas necesita el sitio de una constructora?','Tantas como obras, sectores y regiones tenga documentadas. El criterio no es la cantidad, es que cada búsqueda relevante tenga una página que la responda; en el caso de CAABSA STEEL son 148 páginas en español e inglés.'),
         ('¿Sirve de algo publicar obras antiguas?','Sí. La obra terminada es la prueba de experiencia que busca un comprador industrial. Mientras la ficha tenga cliente, sector, ubicación y fotos reales, sigue sirviendo años después.'),
         ('¿El sitio puede estar en inglés también?','Sí, y en obra industrial suele valer la pena: muchos compradores son corporativos extranjeros. Se publica en rutas propias por idioma para que cada versión pueda posicionarse por separado.'),
         ('¿El asistente de IA da precios de obra?','No. En este tipo de proyecto el asistente tiene prohibido dar precios o plazos: responde sobre sectores, cobertura y proceso, y deriva al equipo cuando la pregunta es de números.'),
         ('¿Qué pasa si no tengo fotos profesionales?','Se trabaja con las fotos de obra que la empresa ya tiene. En este caso el material salió de las carpetas internas del cliente; lo que faltaba no eran fotos, era estructura.')],
    relacionado=[('../servicios/paginas-web.html','Sitios web con IA →'),
                 ('que-es-geo-optimizacion-para-ia.html','¿Qué es GEO? →'),
                 ('../industrias/distribuidoras.html','Sistemas para distribuidoras →'),
                 ('../planes.html','Planes y precios →')],
)
print(escribir(spec))
