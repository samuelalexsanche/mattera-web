# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>El problema no es conseguir prospectos</h2>
    <p>Casi ninguna inmobiliaria se queja de que falten interesados. Se queja de otra cosa: de que llegan muchos, casi todos preguntan lo mismo, y para cuando alguien los atiende ya se enfriaron o ya compraron en otro lado.</p>
    <p>El tiempo de respuesta es la variable que más pesa en bienes raíces, porque el interesado rara vez pregunta en un solo lugar. Manda el mismo mensaje a cuatro anuncios y se queda con quien le conteste primero y mejor. No es deslealtad: es que está comparando.</p>
    <p>Y hay un segundo problema que cuesta más caro todavía: el asesor gasta sus mejores horas con gente que nunca iba a comprar. Visitas a propiedades fuera de presupuesto, recorridos con quien apenas está viendo, llamadas a quien ya firmó en otro desarrollo.</p>

    <h2>Qué se automatiza, en orden</h2>
    <p>El orden importa, porque automatizar lo último antes que lo primero no sirve de nada.</p>
    <ul class="lista-check">
      <li><strong>Primero: la respuesta inmediata.</strong> Que nadie espere. A cualquier hora, incluido el domingo, cuando se hacen la mitad de las búsquedas de vivienda.</li>
      <li><strong>Segundo: calificar.</strong> Zona, presupuesto, tipo de propiedad, si necesita crédito y si ya tiene preaprobación. Cinco datos que cambian por completo a quién le toca atenderlo.</li>
      <li><strong>Tercero: agendar.</strong> La visita se aparta en el calendario del asesor correcto dentro de la misma conversación, sin pasar por una llamada.</li>
      <li><strong>Cuarto: el seguimiento.</strong> Al que no respondió, al que visitó y no volvió a escribir, al que dijo "lo platico con mi esposa". Aquí es donde se pierden más operaciones.</li>
    </ul>
    <p>El cuarto punto es el que casi nadie hace bien, y no por flojera: es que requiere acordarse de decenas de personas en fechas distintas, durante meses. Es trabajo de sistema, no de memoria.</p>

    <h2>Calificar no es interrogar</h2>
    <p>Aquí está el error más común al automatizar una inmobiliaria: convertir la conversación en un formulario. El interesado escribe por una casa y recibe siete preguntas seguidas antes de que nadie le haya dicho nada útil. Se va.</p>
    <p>Lo que funciona es al revés: primero darle lo que pidió — el precio, si sigue disponible, dónde está, cuántas recámaras — y sacar los datos de calificación dentro de la plática, en el orden en que salgan de forma natural. El dato se obtiene igual, pero la persona no siente que la están filtrando.</p>

    <h2>Qué debe seguir siendo humano</h2>
    <p>Decirlo claro evita decepciones y malas implementaciones.</p>
{tabla(['Tarea','¿Se automatiza?','Por qué'],
 [['Contestar precio y disponibilidad','Sí','Dato fijo, pregunta constante'],
  ['Agendar y recordar la visita','Sí','Regla clara, nadie la disfruta'],
  ['Seguimiento a los que no contestaron','Sí','Es memoria y calendario'],
  ['Enseñar la propiedad','No','Ahí se vende, y se vende en persona'],
  ['Negociar el precio','No','Depende de contexto y de relación'],
  ['Acompañar el trámite del crédito','No','Cada caso es distinto y hay dinero de por medio']])}
    <p>El asistente no cierra operaciones. Lo que hace es que el asesor llegue a la cita sabiendo quién es la persona, qué busca y cuánto puede pagar — en vez de descubrirlo durante el recorrido.</p>

    <h2>Lo que hay que tener antes de automatizar</h2>
    <p>Tres cosas, y si faltan conviene resolverlas primero:</p>
    <p><strong>El inventario en algún lado consultable.</strong> Aunque sea una hoja de cálculo bien llevada. Si los precios y las disponibilidades viven en la cabeza de tres personas y se contradicen entre sí, el sistema va a repetir esas contradicciones más rápido.</p>
    <p><strong>Reglas de asignación.</strong> A quién le toca cada prospecto: por zona, por tipo de propiedad, por turno. Si hoy se asigna "al que esté libre", eso no se puede automatizar hasta que sea una regla.</p>
    <p><strong>Un lugar donde quede el historial.</strong> Si cada asesor guarda sus conversaciones en su propio teléfono, cuando esa persona se va se va la cartera con ella. Es el riesgo que más caro sale y el que menos se nombra.</p>

    <h2>El seguimiento largo, que es donde está el dinero</h2>
    <p>Comprar una casa no se decide en una semana. Entre el primer mensaje y la firma pasan meses, y en esos meses el interesado desaparece, vuelve, compara, consulta con su familia y cambia de opinión dos veces.</p>
    <p>Ahí se pierde la mayoría de las operaciones, y no por mal servicio: por aritmética. Un asesor con cuarenta prospectos activos no puede acordarse de quién pidió que le marcaran en tres semanas. El que sí se acuerda es quien tiene la lista escrita, y casi nadie la tiene.</p>
    <p>Un sistema de seguimiento no hace nada ingenioso: nada más no se le olvida. Sabe que a esta persona le tocaba un mensaje hoy, sabe qué se habló la última vez y sabe que ya se le insistió tres veces y conviene parar. Eso último importa tanto como lo primero — insistir de más también pierde clientes.</p>
    <p>Dos reglas que conviene fijar desde el principio: cada cuándo se contacta a alguien que no responde, y cuándo se da por cerrado. Sin esas dos reglas escritas, el seguimiento automático se convierte en acoso automático.</p>

    <h2>Hasta dónde llega, con un caso real</h2>
    <p>En una inmobiliaria de Guadalajara opera un sistema que programa y hace llamadas de seguimiento a prospectos con voz de inteligencia artificial, y anota solo el resultado de cada una. El asesor no marca ni captura: recibe el resumen y decide a quién vale la pena dedicarle la tarde.</p>
    <p>El recorrido completo, paso a paso, está en <a href="seguimiento-automatico-de-prospectos-inmobiliarios.html">el caso del seguimiento automático de prospectos</a>. Lo que vale la pena notar es qué parte se automatizó: la que se hace igual todas las veces. La visita y la negociación siguen siendo del asesor.</p>
'''

spec = dict(
    slug='como-automatizar-una-inmobiliaria.html',
    title='Cómo automatizar una inmobiliaria: qué sí y qué no',
    h1='Cómo automatizar una inmobiliaria',
    titulo_corto='Automatizar una inmobiliaria',
    desc='Qué automatizar primero en bienes raíces, cómo calificar sin interrogar, y qué tiene que seguir haciendo el asesor.',
    bajada='El problema no es que falten prospectos. Es que llegan todos juntos, preguntan lo mismo y nadie alcanza a contestarles a tiempo.',
    lede='Automatizar una inmobiliaria significa que la respuesta al interesado sea inmediata a cualquier hora, que se califique dentro de la plática en vez de con un formulario, que la visita se agende sola y que el seguimiento no dependa de que alguien se acuerde. Lo que no se automatiza es enseñar la propiedad ni negociar.',
    fecha='2026-12-04',
    categoria='Operaciones',
    cuerpo=cuerpo,
    cta='¿Cuántos prospectos se te enfrían por no contestar a tiempo? En 30 minutos te decimos qué parte se puede ir sola.',
    ficha='Qué automatizar primero en bienes raíces, cómo calificar sin interrogar al interesado, y qué tiene que seguir haciendo el asesor.',
    faq=[('¿Qué se puede automatizar en una inmobiliaria?','La respuesta inmediata a cualquier hora, la calificación del prospecto dentro de la conversación, el agendado de visitas en el calendario del asesor y el seguimiento a quienes no respondieron. Enseñar la propiedad y negociar el precio siguen siendo del asesor.'),
         ('¿Por qué importa tanto el tiempo de respuesta en bienes raíces?','Porque el interesado rara vez pregunta en un solo lugar: manda el mismo mensaje a varios anuncios y avanza con quien le conteste primero y mejor. Si tu respuesta llega al día siguiente, la conversación ya ocurrió en otro lado.'),
         ('¿El asistente puede calificar prospectos sin molestar?','Sí, si está bien diseñado. El error común es soltar siete preguntas seguidas antes de dar información. Lo que funciona es responder primero lo que la persona pidió y obtener los datos dentro de la plática, conforme salen.'),
         ('¿Qué necesito tener antes de automatizar una inmobiliaria?','El inventario en un lugar consultable aunque sea una hoja de cálculo, reglas claras de a quién le toca cada prospecto, y un lugar común donde quede el historial de las conversaciones.'),
         ('¿Qué pasa si un asesor se va de la empresa?','Ese es justo el riesgo de tener las conversaciones en el teléfono de cada quien: la cartera se va con la persona. Con el historial en un sistema común, el siguiente asesor retoma sabiendo qué se habló.'),
         ('¿El sistema puede hacer llamadas de seguimiento?','Sí. Hay sistemas que programan y ejecutan llamadas de seguimiento con voz de IA y registran solo el resultado, para que el asesor reciba el resumen en vez de marcar uno por uno.')],
    relacionado=[('seguimiento-automatico-de-prospectos-inmobiliarios.html','Caso: seguimiento de prospectos →'),
                 ('../industrias/inmobiliarias.html','Automatización para inmobiliarias →'),
                 ('../servicios/agentes-ia.html','Agentes de IA →'),
                 ('../servicios/crm-para-empresas.html','CRM a medida →'),
                 ('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →')],
    destino=PEND,
)
print(escribir(spec))
