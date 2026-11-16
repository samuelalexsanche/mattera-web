# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Dónde se va el tiempo en una clínica</h2>
    <p>Si llevas la cuenta una semana, el patrón es casi siempre el mismo: la recepción contesta las mismas cinco preguntas (precio de la consulta, si aceptan tarjeta, horario, dirección, si hay lugar hoy), coordina citas por teléfono mientras hay pacientes esperando, y a nadie le queda tiempo para llamar a quien no volvió.</p>
    <p>Ninguna de esas tres es un problema de actitud. Son trabajo repetitivo con respuesta predecible, que es exactamente lo que conviene automatizar — y conviene en ese orden, porque el primero es el más barato de resolver.</p>

    <h2>1. Las preguntas repetidas</h2>
    <p>Un asistente conectado a tu WhatsApp responde precios, horarios, ubicación, formas de pago y qué incluye cada estudio o tratamiento. Está entrenado con la información de tu clínica, no con conocimiento general de internet, y cuando la pregunta sale de ahí la pasa a una persona.</p>
    <p>El efecto que más se nota no es el ahorro: es que los mensajes de la noche y del domingo dejan de quedarse sin respuesta. En salud privada, el paciente que no recibe respuesta escribe a la siguiente clínica.</p>

    <h2>2. La agenda</h2>
    <p>Agendar por teléfono obliga a dos personas a coincidir. El sistema muestra los horarios libres, el paciente elige, y la cita queda escrita en el calendario que ya usan. Después manda el recordatorio un día antes.</p>
    <p>El recordatorio es la parte que más rinde: la inasistencia es el costo invisible de toda clínica. Cada hueco que nadie avisó es un espacio que se pudo haber ocupado.</p>

    <h2>3. El paciente que no volvió</h2>
    <p>Limpieza cada seis meses, revisión anual, control de tratamiento. Todo el mundo sabe que hay que recordarlo y casi nadie lo hace, porque compite contra la urgencia del día. Un sistema que avisa en la fecha acordada no es más listo que tu equipo: simplemente no se distrae.</p>

    <h2>Lo que NO conviene automatizar en una clínica</h2>
{tabla(['Situación','Quién debe atenderla','Por qué'],
 [['Dudas de precio y horario','El asistente','Respuesta fija y verificable'],
  ['Agendar o mover una cita','El asistente','Proceso con reglas claras'],
  ['Recordatorios y seguimiento','El asistente','Trabajo repetitivo en fecha fija'],
  ['Un síntoma o una molestia','Personal clínico','Es criterio médico, no información'],
  ['Urgencias','Personal, de inmediato','El tiempo cuenta'],
  ['Resultados de estudios','Personal clínico','Requiere interpretación y trato']])}
    <p>Esto no es una limitación técnica: es diseño correcto. Un asistente que opina sobre un síntoma es un riesgo para el paciente y para la clínica. El nuestro tiene prohibido hacerlo y está obligado a pasar esos casos a una persona.</p>

    <h2>Lo que cambia para la recepcionista</h2>
    <p>La pregunta que siempre sale en la primera llamada: ¿y entonces para qué quiero recepción? Para lo que de verdad importa, que es atender bien a quien está parado enfrente. Hoy esa persona hace dos trabajos a la vez y los dos salen a medias: contesta el teléfono mientras un paciente espera a que lo registren.</p>
    <p>Después del cambio, la recepción sigue siendo quien recibe, quien cobra, quien resuelve el caso raro y quien calma al paciente molesto. Lo que deja de hacer es teclear la misma respuesta cuarenta veces y perseguir confirmaciones por teléfono.</p>
    <p>Conviene decirlo adentro antes de instalarlo. El sistema que el equipo percibe como amenaza se sabotea solo: alguien deja de registrar, alguien contesta por fuera, y a los dos meses nadie sabe qué pasó con cada paciente.</p>

    <h2>Cómo se ve la primera semana</h2>
    <p>No empieza perfecto, y conviene saberlo. Los primeros días aparecen preguntas que nadie anticipó, formas de escribir que el asistente no entiende y casos que conviene pasar antes a una persona. Eso se ajusta sobre la marcha, con las conversaciones reales a la vista.</p>
    <p>Lo que sí funciona desde el día uno: los mensajes fuera de horario tienen respuesta, las preguntas de precio y horario dejan de interrumpir, y cada contacto queda registrado. El refinamiento fino toma entre dos y cuatro semanas.</p>

    <h2>Los datos del paciente</h2>
    <p>En México aplica la Ley Federal de Protección de Datos Personales en Posesión de los Particulares, y los datos de salud son datos sensibles: exigen consentimiento expreso y cuidado adicional. Tres decisiones que conviene tomar antes de automatizar nada:</p>
    <p>Qué información va a tocar el sistema — lo mínimo para agendar suele bastar: nombre, teléfono y motivo general de la cita, sin historial clínico. Dónde se guardan esas conversaciones y quién puede verlas. Y que tu aviso de privacidad diga lo que realmente haces con esa información.</p>
    <p>Si tu clínica necesita que los datos se queden en servidores dentro de México, se puede montar así.</p>

    <h2>Cuánto cuesta y en cuánto se paga</h2>
    <p>El desarrollo de un sistema de este tipo arranca desde $10,000 MXN de pago único y la operación mensual desde $1,500 MXN. La cuenta honesta no se hace contra cero, sino contra lo que hoy cuestan esas horas de recepción y las citas que se pierden.</p>
    <p>Un criterio práctico: si tu clínica recibe menos de cincuenta mensajes de pacientes al mes, todavía no sale. Si recibe varios al día y hay huecos por inasistencia, sí.</p>
    <p>El detalle para este giro está en <a href="../industrias/clinicas.html">sistemas para clínicas</a>, y lo que conviene automatizar primero en cualquier negocio, en <a href="5-senales-necesitas-automatizacion.html">las cinco señales</a>.</p>
'''

spec = dict(
    slug='como-automatizar-una-clinica-dental-o-consultorio.html',
    title='Cómo automatizar una clínica dental o consultorio | Mattera Systems',
    h1='Cómo automatizar una clínica dental o un consultorio',
    titulo_corto='Automatizar una clínica',
    desc='Qué automatizar en una clínica y en qué orden: preguntas repetidas, agenda y recordatorios. Qué NO debe tocar un asistente y cómo se manejan los datos del paciente en México.',
    bajada='Tres cosas se llevan las horas de recepción. Las tres se resuelven, y en este orden.',
    lede='En una clínica conviene automatizar en este orden: primero las preguntas repetidas de WhatsApp, después la agenda con sus recordatorios, y al final el seguimiento al paciente que no volvió. Lo que no se automatiza nunca es el criterio clínico. Así se hace, y así se cuidan los datos del paciente.',
    fecha='2026-11-20',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Cuántos mensajes de pacientes contesta tu recepción al día? Con ese número sale la cuenta.',
    ficha='Primero las preguntas repetidas, después la agenda, al final el seguimiento. Qué no debe tocar nunca un asistente y cómo se cuidan los datos del paciente.',
    faq=[('¿Un asistente de IA puede dar diagnósticos?','No, y no debe. En una clínica el asistente atiende información fija —precios, horarios, agenda, recordatorios— y está obligado a pasar a personal clínico cualquier pregunta sobre un síntoma, un resultado o una urgencia.'),
         ('¿Qué pasa con los datos de los pacientes?','Son datos sensibles bajo la ley mexicana de protección de datos. Conviene que el sistema toque lo mínimo (nombre, teléfono y motivo general), decidir dónde se guardan las conversaciones y que el aviso de privacidad lo refleje. Los datos pueden quedarse en servidores dentro de México.'),
         ('¿Reduce las inasistencias?','El recordatorio automático un día antes es la medida que más ayuda, porque permite que el paciente avise a tiempo y el hueco se pueda ocupar. No publicamos cifras de resultados de clientes.'),
         ('¿Sirve para un consultorio de un solo médico?','Si recibe varios mensajes de pacientes al día, sí: el beneficio es el tiempo de quien hoy contesta. Por debajo de unos cincuenta mensajes al mes, todavía no justifica la inversión.'),
         ('¿Se conecta con la agenda que ya usamos?','Sí, siempre que sea una agenda que se deje conectar, como Google Calendar. Si usan un sistema cerrado, se evalúa otra salida en la llamada.'),
         ('¿Cuánto cuesta?','Desde $10,000 MXN de desarrollo, pago único, y desde $1,500 MXN mensuales de operación. El alcance exacto sale de una llamada de 30 minutos sin costo.')],
    relacionado=[('../industrias/clinicas.html','Sistemas para clínicas →'),
                 ('5-senales-necesitas-automatizacion.html','5 señales de que necesitas automatización →'),
                 ('como-integrar-whatsapp-con-tu-crm-o-sistema.html','Cómo integrar WhatsApp con tu CRM →'),
                 ('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →')],
    destino=PEND,
)
print(escribir(spec))
