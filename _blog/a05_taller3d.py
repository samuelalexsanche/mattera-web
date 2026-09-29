# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>El problema de vender piezas que no existen todavía</h2>
    <p>Un taller de manufactura a medida vende algo incómodo de mostrar: piezas que aún no se fabrican. El cliente llega con una refacción rota, una idea a medias o un archivo, y la primera pregunta siempre es la misma: <em>¿cuánto me cuesta?</em></p>
    <p>Responder eso bien es difícil porque el precio depende de variables que el cliente no conoce: tamaño, material, relleno, tiempo de máquina, postproceso. Y responderlo mal es peor: cotizar a ciegas termina en trabajos que no dejan margen o en clientes que se sienten engañados.</p>
    <p>Por eso la mayoría de los talleres contesta "mándame el archivo y te digo". Funciona, pero filtra mal: consume horas en cotizaciones que nunca se convierten y aleja a quien solo quería un rango para saber si le alcanza.</p>

    <h2>Lo que construimos en Bisel</h2>
    <p><a href="https://bisel3d.com/" target="_blank" rel="noopener">Bisel</a> es el taller de impresión 3D que opera el propio equipo de Mattera en Guadalajara. Es proyecto propio, no de un cliente, y por eso sirve para explicar el criterio sin adornos: lo usamos como banco de pruebas de lo que después ofrecemos.</p>
    <p>El sitio tiene cuatro piezas que cualquier taller a medida necesita:</p>
    <p><strong>Catálogo</strong> de lo que ya se fabrica y se puede comprar tal cual, con envío nacional. Es la venta que no requiere conversación.</p>
    <p><strong>Calculadora de presupuesto</strong>, que da un rango antes de hablar con nadie. Filtra por sí sola: quien busca algo fuera de su presupuesto se entera solo, y quien sigue adelante llega con expectativa realista.</p>
    <p><strong>Cotizador de pieza a medida</strong>, para el trabajo que sí requiere revisión: el cliente describe o sube lo que necesita y la conversación empieza con datos, no desde cero.</p>
    <p><strong>Páginas de servicio y de modelos</strong>, separadas por tipo de trabajo, más un blog. Cada tipo de pieza — refacciones, organizadores, lotes para eventos — tiene su propio espacio en vez de estar todo bajo "servicios".</p>

    <h2>La calculadora hace el trabajo que hacía una persona</h2>
    <p>La diferencia entre pedir un archivo y publicar una calculadora es quién gasta el tiempo.</p>
{tabla(['Situación','Sin calculadora','Con calculadora y catálogo'],
 [['Cliente con presupuesto corto','Se cotiza y no compra','Se entera solo, sin consumir tiempo'],
  ['Cliente que quiere algo del catálogo','Conversación completa','Compra sin hablar con nadie'],
  ['Pieza a medida real','Empieza de cero','Llega con medidas y material definidos'],
  ['Consulta fuera de horario','Espera al día siguiente','Obtiene rango de inmediato'],
  ['Comparar con otro taller','Depende de quién conteste antes','El rango ya está publicado']])}
    <p>El mismo principio aplica a cualquier taller que trabaje bajo pedido: carpintería, herrería, corte láser, rotulación, uniformes. La variable cambia, la lógica no. Publicar un rango de precio no regala el negocio: filtra.</p>
    <p>Hay un beneficio menos obvio. Cuando el rango está publicado, la conversación deja de empezar por el precio y empieza por el problema: qué pieza es, para qué máquina, cuántas se necesitan. Esa es una conversación de taller, y es la que termina en trabajo.</p>

    <h2>El envío cambia el sitio más de lo que parece</h2>
    <p>Un taller que solo atiende su ciudad y uno que manda piezas a todo el país no necesitan el mismo sitio. En el primero basta con teléfono, dirección y ficha de Google. En el segundo hay que resolver desde el principio tres cosas que si se dejan para después complican todo: cómo se cobra el envío, en cuánto tiempo llega y qué pasa si la pieza llega mal.</p>
    <p>Decirlo en público ahorra la mitad de las conversaciones. Quien vende bajo pedido y esconde esos datos termina explicándolos uno por uno en mensajes, y además pierde a quien no quiso preguntar.</p>

    <h2>Cada tipo de pieza merece su propia página</h2>
    <p>Es el mismo criterio que aplicamos en otros giros. Un taller que mete refacciones, organizadores, prototipos y lotes para eventos bajo una sola sección de "servicios" compite por una sola búsqueda. Si cada tipo de trabajo tiene su página, con sus ejemplos, sus materiales y sus tiempos, cada uno puede aparecer cuando alguien busca exactamente eso.</p>
    <p>La ventaja adicional es comercial: esa página se puede mandar por WhatsApp al cliente que preguntó por ese trabajo en particular, en vez de mandarle el sitio entero para que busque.</p>

    <h2>Lo que un taller no debería automatizar</h2>
    <p>La revisión técnica del archivo. Decidir si una pieza aguanta el esfuerzo que va a recibir, si el material propuesto es el correcto o si hay que cambiar el diseño para que se pueda fabricar es criterio de taller, no de formulario. Un sistema que prometa eso automáticamente va a equivocarse en el caso que importa.</p>
    <p>El criterio que usamos para decidir qué sí y qué no está en <a href="../servicios/automatizacion-procesos.html">automatización de procesos</a>: volumen por repetición por costo del error. Cotizar un llavero es repetitivo y barato de equivocar; validar una refacción que va montada en una máquina, no.</p>

    <h2>Cómo se ordena un taller que hoy vende solo por mensaje</h2>
    <p>El orden que recomendamos: primero publicar el catálogo de lo que ya se fabrica, porque es venta inmediata sin conversación. Después la calculadora o el rango público, que filtra. Después el cotizador con datos estructurados. Y al final, si el volumen de mensajes lo justifica, el <a href="../servicios/chatbot-whatsapp.html">asistente de WhatsApp</a> que contesta lo repetitivo y pasa a una persona lo técnico.</p>
    <p>Los <a href="../planes.html">planes de sitio</a> tienen precio público; la calculadora y el cotizador son desarrollo a medida y su alcance se define en el diagnóstico de 30 minutos, que no tiene costo.</p>
'''

spec = dict(
    slug='pagina-web-para-talleres-de-manufactura.html',
    title='Página web para talleres de manufactura a medida | Mattera Systems',
    h1='Página web para un taller que fabrica a medida: catálogo, calculadora y cotizador',
    titulo_corto='Página web para talleres a medida',
    desc='Cómo vende en línea un taller que fabrica bajo pedido: catálogo de lo que ya existe, calculadora que filtra y cotizador con datos. El caso de Bisel, impresión 3D en Guadalajara.',
    bajada='La primera pregunta siempre es cuánto cuesta. Contestarla en público filtra clientes en vez de regalar el negocio.',
    lede='Un taller que fabrica a medida vende piezas que todavía no existen, y eso complica su sitio. Lo que funciona son tres capas: catálogo de lo que ya se fabrica, calculadora que da un rango sin hablar con nadie y cotizador para el trabajo que sí requiere revisión. Así está armado Bisel.',
    fecha='2026-09-29',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Tu taller cotiza cada pieza por mensaje? Se puede publicar un rango y filtrar antes de la conversación.',
    faq=[('¿Publicar precios no me quita ventaja frente a la competencia?','Publicar un rango no es publicar tu costo. Lo que hace es filtrar: quien no tiene presupuesto se entera solo y deja de consumir horas de cotización, y quien sigue llega con expectativa realista.'),
         ('¿Sirve esto para talleres que no son de impresión 3D?','Sí. La lógica es la misma en carpintería, herrería, corte láser, rotulación o uniformes: catálogo de lo que ya se hace, rango público y cotizador para lo que requiere revisión.'),
         ('¿La calculadora sustituye la cotización formal?','No. Da un rango para filtrar; la cotización final la hace el taller después de revisar medidas, material y esfuerzo al que estará sometida la pieza.'),
         ('¿Qué no conviene automatizar en un taller?','La revisión técnica: decidir si una pieza aguanta, si el material es el correcto o si hay que rediseñarla para poder fabricarla. Eso es criterio de taller.'),
         ('¿Bisel es un cliente de Mattera?','No, es proyecto propio del equipo. Lo usamos como banco de pruebas de lo que después ofrecemos a clientes.')],
    relacionado=[('../servicios/automatizacion-procesos.html','Automatización de procesos →'),
                 ('../servicios/paginas-web.html','Sitios web con IA →'),
                 ('pagina-web-para-constructoras-industriales.html','Página web para constructoras →'),
                 ('5-senales-necesitas-automatizacion.html','5 señales de que necesitas automatización →')],
)
print(escribir(spec))
