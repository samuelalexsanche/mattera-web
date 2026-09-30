# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Por qué se abandonan los CRM</h2>
    <p>La razón casi nunca es que el sistema sea malo. Es que captura el dato <em>después</em> del trabajo. El vendedor termina la llamada, sigue con la siguiente y deja la captura para el final del día; al final del día está cansado y anota la mitad. A la semana, el CRM tiene datos incompletos; al mes, nadie confía en sus reportes; al trimestre, se abre solo cuando el jefe pregunta.</p>
    <p>De ahí sale el criterio más importante para elegir: <strong>gana el que menos trabajo extra pide</strong>. Un CRM que exige quince campos por contacto está diseñado para el reporte, no para quien vende.</p>

    <h2>Las cinco preguntas que ordenan la decisión</h2>
    <p><strong>1. ¿Dónde ocurre hoy la conversación?</strong> Si tus clientes escriben por WhatsApp, un CRM que no vive ahí obliga a copiar y pegar. Esa fricción es la que mata la adopción.</p>
    <p><strong>2. ¿Quién va a capturar y cuándo?</strong> Si la respuesta honesta es "al final del día, si se acuerda", necesitas un sistema que capture solo o desde el mismo chat.</p>
    <p><strong>3. ¿Qué decisión vas a tomar con esos datos?</strong> Si no sabes qué vas a mirar cada semana, no necesitas un CRM todavía: necesitas definir el proceso comercial.</p>
    <p><strong>4. ¿Cuántas personas lo van a usar?</strong> El precio por usuario al mes cambia el cálculo por completo cuando el equipo crece.</p>
    <p><strong>5. ¿Qué pasa si te quieres ir?</strong> Pregunta antes de firmar cómo se exportan tus datos. Si la respuesta es vaga, ya sabes el costo de salir.</p>

    <h2>Las tres opciones reales</h2>
{tabla(['','CRM de catálogo','Hoja de cálculo ordenada','CRM a medida'],
 [['Costo inicial','Bajo o nulo','Nulo','Desarrollo de una vez'],
  ['Costo mensual','Por usuario, crece con el equipo','Nulo','Operación, no por usuario'],
  ['Adopción','Depende de la disciplina','Alta al inicio, frágil después','Alta si captura desde donde ya trabajan'],
  ['Se adapta a tu proceso','Tú te adaptas a él','Total, pero sin controles','Total'],
  ['Integración con WhatsApp','Variable, a veces de pago','Manual','Nativa si así se diseña'],
  ['Cuándo conviene','Proceso estándar y equipo disciplinado','Menos de 30 contactos al mes','Proceso propio o volumen alto']])}
    <p>No hay una respuesta universal. Un despacho con proceso estándar y cinco vendedores probablemente esté bien con un CRM de catálogo. Una empresa cuyo proceso no se parece al del catálogo termina pagando licencias por un sistema que usa al treinta por ciento.</p>

    <h2>Señales de que te están vendiendo de más</h2>
    <p>Módulos que no vas a usar, precio por usuario cuando la mitad del equipo solo consulta, implementación cobrada aparte y un contrato anual antes de haber probado nada. Ninguna es motivo automático para descartar, pero todas merecen pregunta.</p>
    <p>La contraparte también existe: quien dice que todo se resuelve con una hoja de cálculo. Funciona al principio y deja de funcionar cuando dos personas editan a la vez, nadie sabe cuál es la versión buena y no hay historial de qué se le dijo a quién.</p>

    <h2>El error de empezar por la herramienta</h2>
    <p>La secuencia que falla es siempre la misma: alguien contrata un CRM, lo configura un fin de semana y después intenta que el equipo cambie su forma de trabajar para alimentarlo. Eso se sostiene tres semanas.</p>
    <p>La secuencia que funciona empieza por escribir el proceso real, no el ideal: cómo entra un cliente hoy, quién lo atiende primero, en qué momento se decide si es buen prospecto, cuándo se le vuelve a escribir y cuándo se da por perdido. Con eso en una hoja, elegir herramienta es fácil, porque ya sabes qué tiene que resolver.</p>
    <p>Hay una prueba honesta para saber si el proceso está escrito: pregúntale a dos vendedores cuándo se considera perdido un prospecto. Si dan respuestas distintas, no hay proceso, hay costumbres — y ningún sistema arregla eso.</p>

    <h2>La migración: lo que nadie cuenta</h2>
    <p>Si ya tienes clientes registrados en algún lado, esos datos hay que moverlos, y ahí aparecen los problemas: teléfonos con formatos distintos, contactos duplicados, registros sin dueño. Limpiar eso es trabajo aburrido que casi siempre se subestima y que conviene hacer antes de estrenar, no después.</p>
    <p>Un consejo práctico: migra primero solo lo que está activo. Arrastrar tres años de contactos muertos al sistema nuevo garantiza que la primera impresión del equipo sea una lista llena de basura.</p>

    <h2>Qué debe hacer un CRM, en concreto</h2>
    <p>Tres cosas, y en este orden: que cada contacto quede registrado sin trabajo extra; que el seguimiento se dispare solo en la fecha acordada; y que al final de la semana exista un número confiable de cuántos entraron, cuántos avanzaron y por qué se cayeron los demás.</p>
    <p>Todo lo demás — tableros, automatizaciones, integraciones — es útil cuando esas tres funcionan. Antes, es decoración sobre un dato incompleto.</p>

    <h2>Cómo lo hacemos nosotros</h2>
    <p>Los CRM que construimos parten de dónde ya trabaja el equipo. En una inmobiliaria, el asesor registra al prospecto hablando con un asistente desde el mismo teléfono donde atiende; el sistema programa el seguimiento y escribe solo el resultado. Está contado en <a href="seguimiento-automatico-de-prospectos-inmobiliarios.html">este caso</a>.</p>
    <p>El criterio de fondo: sin licencia por usuario, conectado a lo que ya usas y con tus datos siempre exportables. Está explicado en <a href="../servicios/crm-para-empresas.html">CRM a medida</a>; el desarrollo arranca desde $10,000 MXN de pago único y la operación desde $1,500 MXN al mes.</p>
    <p>Y si después de leer esto tu conclusión es que todavía no necesitas un CRM, también es una respuesta válida. Eso lo decimos en el diagnóstico.</p>
'''

spec = dict(
    slug='como-elegir-un-crm-para-mi-empresa.html',
    title='Cómo elegir un CRM para tu empresa (y por qué la mayoría se abandona)',
    h1='Cómo elegir un CRM para tu empresa',
    titulo_corto='Cómo elegir un CRM',
    desc='Las cinco preguntas que ordenan la decisión, la comparación entre CRM de catálogo, hoja de cálculo y desarrollo a medida, y por qué la mayoría de los CRM terminan abandonados.',
    bajada='La mayoría de los CRM no fracasan por malos: fracasan porque piden capturar el dato después del trabajo.',
    lede='Elegir un CRM se decide con cinco preguntas: dónde ocurre hoy la conversación con tus clientes, quién va a capturar y cuándo, qué decisión vas a tomar con esos datos, cuántas personas lo usarán y qué pasa si te quieres ir. Lo demás son funciones que suenan bien en la demostración.',
    fecha='2026-10-13',
    categoria='Operaciones',
    cuerpo=cuerpo,
    cta='¿Tu equipo captura al final del día o no captura? Ese dato decide qué tipo de CRM necesitas.',
    ficha='No fracasan por malos: fracasan porque piden capturar después del trabajo. Las cinco preguntas que ordenan la decisión y las tres opciones reales.',
    faq=[('¿Por qué se abandonan tantos CRM?','Porque exigen capturar el dato después del trabajo. Si el vendedor tiene que entrar a otra pantalla al final del día, captura la mitad; con datos incompletos nadie confía en los reportes y el sistema deja de usarse.'),
         ('¿Conviene un CRM de catálogo o uno a medida?','Si tu proceso comercial es estándar y el equipo es disciplinado, uno de catálogo suele bastar. Si tu proceso es propio, el volumen es alto o pagarías licencias por gente que solo consulta, conviene evaluar uno a medida.'),
         ('¿Una hoja de cálculo puede servir como CRM?','Al inicio sí, con pocos contactos al mes. Deja de servir cuando varias personas editan a la vez, no hay historial de conversaciones ni recordatorios automáticos.'),
         ('¿Qué debe hacer como mínimo un CRM?','Registrar cada contacto sin trabajo extra, disparar el seguimiento solo en la fecha acordada y dar un número confiable de cuántos entraron, cuántos avanzaron y por qué se cayeron los demás.'),
         ('¿Qué pregunto antes de contratar uno?','Cómo se exportan tus datos si decides irte, si el precio es por usuario, si la implementación se cobra aparte y si hay contrato mínimo de permanencia.'),
         ('¿Cuánto cuesta un CRM a medida?','En Mattera el desarrollo arranca desde $10,000 MXN de pago único y la operación mensual desde $1,500 MXN, sin licencia por usuario. El alcance exacto sale del diagnóstico.')],
    relacionado=[('seguimiento-automatico-de-prospectos-inmobiliarios.html','Caso: seguimiento inmobiliario →'),
                 ('../servicios/crm-para-empresas.html','CRM a medida →'),
                 ('5-senales-necesitas-automatizacion.html','5 señales de que necesitas automatización →'),
                 ('../servicios/integraciones.html','Integraciones →')],
    destino=PEND,
)
print(escribir(spec))
