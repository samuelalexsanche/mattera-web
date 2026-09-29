# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>Vender un producto digital genera preguntas, no ventas inmediatas</h2>
    <p>Quien vende software, plantillas o cursos por internet enfrenta un patrón conocido: el producto se puede comprar a cualquier hora, pero la duda que frena la compra llega también a cualquier hora. ¿Sirve para mi versión de Excel? ¿Incluye actualizaciones? ¿Me dan factura? ¿Cómo lo recibo? ¿Funciona en Mac?</p>
    <p>Son preguntas con respuesta fija. El problema no es que sean difíciles: es que llegan en volumen, se repiten y la mitad entra fuera de horario. Cuando la respuesta tarda un día, el interesado ya cerró la pestaña.</p>
    <p>El segundo patrón: el cliente que ya compró vuelve a escribir. Cómo instalar, cómo recuperar el archivo, qué pasa si cambió de computadora. Ese soporte es necesario, pero es también el trabajo más repetitivo del negocio.</p>

    <h2>El sistema que opera en Herramientas Excel</h2>
    <p><a href="https://herramientasexcel.com/" target="_blank" rel="noopener">Herramientas Excel</a> vende software de precios unitarios para presupuestos de obra. Su cliente es alguien técnico — ingenieros, arquitectos, contratistas — que compara antes de comprar y pregunta con detalle.</p>
    <p>El asistente que opera ahí atiende por WhatsApp y hace tres cosas:</p>
    <p><strong>Contesta con la información real del producto</strong>: qué incluye, cómo se entrega, qué requisitos tiene, cómo se factura. Está entrenado con la documentación del negocio, no con conocimiento general de internet.</p>
    <p><strong>Da seguimiento</strong> a quien preguntó y no volvió, en el plazo que el dueño define. Es la diferencia entre una conversación que se enfría y una venta que se recupera.</p>
    <p><strong>Deja todo registrado en un panel</strong> donde el dueño ve las conversaciones, en qué punto quedaron y qué pasó; además recibe avisos de lo que necesita su atención, sin tener que revisar el teléfono todo el día.</p>
    <p>Hay una decisión de diseño que vale la pena explicar: los avisos al dueño no van por WhatsApp, van por un canal aparte. WhatsApp solo permite escribirle libremente a alguien dentro de una ventana de 24 horas; un aviso importante no puede depender de eso.</p>

    <h2>Cómo se evita que el asistente invente</h2>
    <p>En un producto técnico, una respuesta inventada cuesta una devolución. Por eso el asistente trabaja con la documentación del negocio como única fuente: si algo no está escrito ahí, no lo afirma, lo dice y pasa la conversación a una persona.</p>
{tabla(['Tipo de pregunta','Quién la atiende','Por qué'],
 [['Qué incluye, precio, entrega','El asistente','Respuesta fija y verificable'],
  ['Compatibilidad y requisitos','El asistente','Está en la documentación'],
  ['Facturación estándar','El asistente','Proceso repetible'],
  ['Caso raro o reclamo','Una persona','Requiere criterio'],
  ['Descuento o excepción','El dueño','Es decisión comercial']])}
    <p>Esa frontera no es una limitación del modelo: es el diseño correcto. Un asistente que responde todo termina respondiendo mal justo en el caso que importa.</p>

    <h2>El soporte posventa es la mitad del ahorro</h2>
    <p>La conversación de venta se lleva la atención, pero en un producto digital el volumen real está después de la compra: cómo se instala, dónde quedó el archivo, qué hacer al cambiar de computadora, cómo se actualiza. Son preguntas resueltas, repetidas y casi siempre urgentes para quien las hace.</p>
    <p>Atenderlas de inmediato tiene un efecto que se nota en las reseñas: el cliente que recibe respuesta en segundos a la medianoche no percibe un robot, percibe un proveedor serio. Y el que espera al día siguiente con el producto detenido escribe otra cosa muy distinta en la reseña.</p>
    <p>Aquí también hay frontera. Si el archivo no abre por un problema real del producto, eso no lo resuelve un asistente: lo escala con el contexto completo — versión, sistema operativo, qué intentó el cliente — para que la persona que responde no tenga que empezar la conversación desde cero.</p>

    <h2>Cuándo NO conviene poner un asistente</h2>
    <p>Si el negocio digital recibe pocas consultas al mes, el ahorro no justifica la inversión y conviene esperar. Si el producto cambia cada semana y la documentación no alcanza a actualizarse, el asistente va a responder con información vieja, que es peor que no responder. Y si el diferenciador del negocio es precisamente el trato uno a uno del fundador, automatizar la primera conversación puede quitar justo lo que hace valer el producto.</p>
    <p>Esa evaluación es parte del diagnóstico. Preferimos decir que no conviene a montar un sistema que va a dar problemas en el caso importante.</p>

    <h2>Qué se lleva cualquier negocio digital de aquí</h2>
    <p>Este esquema sirve igual para quien vende cursos, plantillas, suscripciones o software de nicho. Tres piezas: documentación escrita que el asistente pueda usar, un canal donde el cliente ya está — casi siempre WhatsApp — y un lugar donde quede el registro de cada conversación.</p>
    <p>La pieza que más se subestima es la primera. Antes de automatizar hay que escribir con claridad qué vendes, qué incluye, qué no incluye y cómo se entrega. Ese trabajo no lo hace la tecnología, y sin él no hay asistente que funcione. Es el mismo punto que explicamos en <a href="5-senales-necesitas-automatizacion.html">las cinco señales</a>: automatizar un proceso mal definido solo hace que el desorden ocurra más rápido.</p>
    <p>Si quieres ver cómo se arma la pieza conversacional, está en <a href="../servicios/chatbot-whatsapp.html">asistente de WhatsApp</a>; el registro y el panel, en <a href="../servicios/crm-para-empresas.html">CRM a medida</a>.</p>
'''

spec = dict(
    slug='asistente-whatsapp-para-negocios-digitales.html',
    title='Asistente de WhatsApp para vender software y productos digitales | Mattera',
    h1='Asistente de WhatsApp para un negocio digital: atender, dar seguimiento y registrar',
    titulo_corto='Asistente para negocios digitales',
    desc='Cómo atiende un asistente de IA las dudas previas a la compra de un producto digital, da seguimiento y deja registro en un panel. El caso de Herramientas Excel.',
    bajada='El producto se compra a cualquier hora, y la duda que frena la compra también llega a cualquier hora.',
    lede='Quien vende software, plantillas o cursos recibe siempre las mismas preguntas antes de la compra, y la mitad llega fuera de horario. Este es el sistema que opera en Herramientas Excel: un asistente de WhatsApp que responde con la documentación real del producto, da seguimiento y deja todo registrado.',
    fecha='2026-09-29',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Cuántas preguntas repetidas contestas al día antes de que alguien compre?',
    faq=[('¿El asistente puede inventar información del producto?','No debe, y por eso se entrena con la documentación del negocio como única fuente. Si algo no está escrito ahí, lo dice y pasa la conversación a una persona. En un producto técnico, una respuesta inventada cuesta una devolución.'),
         ('¿Por qué los avisos al dueño no van por WhatsApp?','Porque WhatsApp solo permite escribir libremente dentro de una ventana de 24 horas desde el último mensaje del usuario. Un aviso importante no puede depender de esa ventana, así que va por un canal aparte.'),
         ('¿Sirve para cursos o suscripciones?','Sí. El esquema es el mismo para cualquier producto digital: documentación escrita, atención en el canal donde ya está el cliente y registro de cada conversación.'),
         ('¿Qué hay que tener listo antes de automatizar?','La documentación: qué vendes, qué incluye, qué no incluye y cómo se entrega. Ese trabajo no lo hace la tecnología y sin él ningún asistente funciona bien.'),
         ('¿El dueño ve las conversaciones?','Sí, en un panel donde queda el registro de cada conversación y su estado, además de avisos de lo que necesita su atención.')],
    relacionado=[('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →'),
                 ('../servicios/crm-para-empresas.html','CRM a medida →'),
                 ('como-funciona-un-chatbot-de-ia-en-la-practica.html','Cómo funciona un chatbot de IA →'),
                 ('../servicios/agentes-ia.html','Agentes de IA →')],
)
print(escribir(spec))
