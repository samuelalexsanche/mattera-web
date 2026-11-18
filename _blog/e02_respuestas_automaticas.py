# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Cómo se activan, paso a paso</h2>
    <p>Las respuestas automáticas vienen incluidas en la app gratuita de WhatsApp Business. No hace falta contratar nada. Son dos, y se configuran en el mismo lugar:</p>
    <ul class="lista-check">
      <li><strong>Mensaje de bienvenida.</strong> Se manda solo cuando alguien te escribe por primera vez, o después de 14 días sin hablarse.</li>
      <li><strong>Mensaje de ausencia.</strong> Se manda fuera del horario que tú marques.</li>
    </ul>
    <p>La ruta es: abre la app de WhatsApp Business, entra a <strong>Herramientas para la empresa</strong> y elige <strong>Mensaje de ausencia</strong> o <strong>Mensaje de bienvenida</strong>. Escribes el texto, decides a quién se le manda y listo. Toma cinco minutos.</p>
    <p>Hay una tercera cosa que se confunde con éstas: las <strong>respuestas rápidas</strong>. Esas no son automáticas. Son atajos de texto que alguien de tu equipo tiene que elegir y enviar a mano. Ahorran tecleo, no tiempo de respuesta.</p>

    <h2>Hasta dónde llegan, dicho sin adornos</h2>
    <p>Esto es lo que conviene saber antes de darlas por resueltas: un mensaje de ausencia no contesta nada. Avisa que no estás.</p>
    <p>El cliente escribe "¿tienen disponibilidad para el sábado?" a las diez de la noche y recibe "Gracias por escribirnos, te responderemos en horario de oficina". Esa respuesta no resuelve su duda ni lo acerca a comprar. Solo evita el silencio, que ya es algo, pero es poco.</p>
    <p>El límite es de diseño, no de configuración: la app manda el mismo texto a todos, sin leer lo que preguntaron. No hay forma de que responda distinto según el mensaje, porque la app no entiende el mensaje.</p>

    <h2>Qué hace cada cosa, en una tabla</h2>
{tabla(['','Respuestas de la app','Asistente con IA'],
 [['Qué cuesta','Gratis','Desarrollo + mensualidad'],
  ['Qué contesta','Un texto fijo, igual para todos','La duda concreta de cada quien'],
  ['¿Lee lo que preguntan?','No','Sí'],
  ['¿Agenda, cotiza, registra?','No','Sí, si se conecta a tus sistemas'],
  ['¿Pasa a una persona?','No','Sí, con el contexto de lo hablado'],
  ['Cuándo basta','Avisar horarios y ubicación','Cuando la pregunta repetida ya cuesta ventas']])}
    <p>No hay trampa en la comparación: si lo único que necesitas es avisar tu horario, la app gratuita lo hace bien y no tiene caso pagar por otra cosa.</p>

    <h2>Las tres señales de que ya no alcanzan</h2>
    <p>Hay un punto en que las respuestas automáticas dejan de ayudar y empiezan a estorbar, porque el cliente siente que le contestó una máquina sin resolverle nada. Se reconoce por tres síntomas:</p>
    <ul class="lista-no">
      <li><strong>Contestas lo mismo todo el día.</strong> Precio, horario, si hay lugar, si aceptan tarjeta. Si la misma pregunta llega decenas de veces, el mensaje de bienvenida no la está absorbiendo.</li>
      <li><strong>Los mensajes de la noche se contestan al día siguiente.</strong> Y para entonces la persona ya preguntó en otro lado.</li>
      <li><strong>Alguien de tu equipo vive en el teléfono.</strong> Cuando contestar WhatsApp ya es el trabajo de una persona, el costo dejó de ser cero.</li>
    </ul>

    <h2>Lo que sigue: el número tiene que salir de la app</h2>
    <p>Aquí está el dato que cambia la decisión y que casi nadie menciona a tiempo. Para que un asistente conteste de verdad, el número tiene que operar sobre la conexión oficial de WhatsApp Business — no sobre la app gratuita.</p>
    <p>Y un número no puede estar en los dos lados al mismo tiempo. O vive en la app, con sus respuestas fijas, o vive en la conexión oficial, con un sistema atendiendo. Migrar el número de siempre se puede, pero hay un rato en que no recibe mensajes, y el historial viejo se queda en la app.</p>
    <p>Por eso muchos negocios estrenan número para el asistente y dejan el de siempre para los clientes de toda la vida. Es una decisión que conviene tomar al principio, no a medio camino. El detalle completo está en la <a href="como-integrar-whatsapp-con-tu-crm-o-sistema.html">guía para integrar WhatsApp</a>.</p>

    <h2>El error que quema el número</h2>
    <p>Hay una tentación que aparece justo cuando descubres la automatización, y conviene nombrarla: mandar mensajes a una lista de gente que no te escribió primero.</p>
    <p>La app de WhatsApp Business tiene listas de difusión, y es fácil pensar que sirven para promociones. El problema es que solo llegan a quien te tenga guardado en sus contactos, y que los reportes de spam se acumulan contra tu número. WhatsApp no avisa antes: el número deja de funcionar y con él se va tu lista de clientes, las conversaciones y el enlace que repartiste en tus redes.</p>
    <p>La diferencia que importa es quién empezó la conversación. Responder a quien te escribió es seguro y no cuesta. Escribirle tú a alguien que no te ha escrito es lo que hay que hacer con cuidado, con su permiso, y —en la conexión oficial— con plantillas que Meta revisa una por una.</p>
    <p>Dicho corto: automatizar la respuesta es buena idea; automatizar el envío masivo es la forma más rápida de perder el número.</p>

    <h2>Qué escribir mientras tanto</h2>
    <p>Si por ahora te quedas con las respuestas de la app, que al menos trabajen. Tres reglas que las vuelven útiles:</p>
    <p><strong>Contesta la pregunta más común en el propio mensaje.</strong> En vez de "te responderemos pronto", pon el horario, la dirección y el rango de precios. Mucha gente solo quería eso.</p>
    <p><strong>Di cuándo vas a responder, con una hora.</strong> "Mañana antes de las 10" sirve; "a la brevedad" no dice nada y suena a formulario.</p>
    <p><strong>Deja una salida para lo urgente.</strong> Un teléfono, una dirección, un enlace para agendar. Si la persona tiene prisa, dale por dónde.</p>
'''

spec = dict(
    slug='respuestas-automaticas-whatsapp-negocio.html',
    title='Respuestas automáticas de WhatsApp: hasta dónde llegan',
    h1='Respuestas automáticas de WhatsApp: hasta dónde llegan',
    titulo_corto='Respuestas automáticas de WhatsApp',
    desc='Cómo activarlas en la app gratuita, qué resuelven de verdad y en qué momento dejan de alcanzar para un negocio que vende por WhatsApp.',
    bajada='Son gratis y se activan en cinco minutos. También avisan que no estás en vez de contestar lo que te preguntaron.',
    lede='Las respuestas automáticas de WhatsApp Business se activan gratis desde la app, en Herramientas para la empresa, y sirven para mandar un mensaje de bienvenida o avisar que estás fuera de horario. Lo que no hacen es leer lo que el cliente preguntó ni responderle: para eso hace falta otra cosa, y esto es cómo saber cuándo ya te toca.',
    fecha='2026-12-01',
    categoria='Operaciones',
    cuerpo=cuerpo,
    cta='¿Tu equipo ya vive contestando lo mismo por WhatsApp? Te decimos qué parte se puede ir sola y qué conviene dejar con una persona.',
    ficha='Cómo activarlas gratis en la app, qué resuelven de verdad y las tres señales de que tu negocio ya necesita algo que sí lea lo que preguntan.',
    faq=[('¿Cómo pongo respuestas automáticas en WhatsApp Business?','En la app de WhatsApp Business, entra a Herramientas para la empresa y elige Mensaje de bienvenida o Mensaje de ausencia. Escribes el texto, eliges a quién se le envía y queda activo. Es gratis y toma unos minutos.'),
         ('¿Cuál es la diferencia entre respuesta automática y respuesta rápida?','La automática se envía sola, sin que nadie intervenga. La respuesta rápida es un atajo de texto que una persona de tu equipo tiene que elegir y mandar: ahorra tecleo, no tiempo de respuesta.'),
         ('¿Las respuestas automáticas pueden contestar preguntas de precio o disponibilidad?','No. La app manda un texto fijo, igual para todos, sin leer lo que preguntaron. Para responder la duda concreta de cada persona hace falta un asistente sobre la conexión oficial de WhatsApp Business.'),
         ('¿Puedo tener un asistente en el mismo número donde uso la app de WhatsApp Business?','No al mismo tiempo. Un número opera en la app o en la conexión oficial, no en las dos. Se puede migrar el número de siempre, pero durante el cambio no recibe mensajes y el historial anterior se queda en la app.'),
         ('¿Cuándo deja de alcanzar la respuesta automática gratuita?','Cuando contestas la misma pregunta decenas de veces al día, cuando los mensajes de la noche se quedan sin respuesta hasta el día siguiente, o cuando atender WhatsApp ya se volvió el trabajo de una persona.'),
         ('¿Qué conviene escribir en el mensaje de ausencia?','La respuesta a lo que más te preguntan — horario, dirección, rango de precios —, una hora concreta en la que vas a responder, y una salida para lo urgente, como un teléfono o un enlace para agendar.')],
    relacionado=[('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →'),
                 ('como-integrar-whatsapp-con-tu-crm-o-sistema.html','Guía: integrar WhatsApp →'),
                 ('como-funciona-un-chatbot-de-ia-en-la-practica.html','Cómo funciona un chatbot de IA →'),
                 ('../servicios/agentes-ia.html','Agentes de IA →'),
                 ('../faq.html','Preguntas frecuentes →')],
    destino=PEND,
)
print(escribir(spec))
