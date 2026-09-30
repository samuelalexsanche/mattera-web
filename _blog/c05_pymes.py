# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>La pregunta correcta no es "cómo uso IA"</h2>
    <p>Es "qué trabajo repetitivo me está costando horas". La inteligencia artificial no es un objetivo: es una herramienta que rinde cuando se aplica a tareas con respuesta predecible y volumen suficiente. Aplicada a lo demás, cuesta dinero y decepciona.</p>
    <p>Por eso este artículo está ordenado por tamaño de empresa y no por tecnología. Lo que le sirve a un negocio de dos personas no es lo que necesita uno de treinta.</p>

    <h2>Negocio de 1 a 3 personas</h2>
    <p>Aquí el problema es el tiempo del dueño, que hace todo. Tres usos que rinden desde el primer día:</p>
    <p><strong>Responder lo repetitivo.</strong> Precios, horarios, disponibilidad, cómo llegar. Un asistente conectado a WhatsApp con la información del negocio se hace cargo de la mayoría de esos mensajes, incluidos los de la madrugada.</p>
    <p><strong>Redactar lo que cuesta empezar.</strong> Cotizaciones, descripciones de producto, respuestas a reseñas, publicaciones. Aquí la IA acelera un borrador; la revisión sigue siendo tuya, y es indispensable.</p>
    <p><strong>Ordenar lo que llega suelto.</strong> Pasar los datos de un mensaje a una hoja, clasificar consultas por tipo, sacar una lista de pendientes de una conversación larga.</p>

    <h2>Empresa de 4 a 15 personas</h2>
    <p>El problema cambia: ya no es el tiempo de una persona, es la coordinación. Lo que rinde:</p>
    <p><strong>Filtrar y calificar antes de que llegue al humano.</strong> El asistente atiende la primera conversación, resuelve dudas básicas y pasa al vendedor solo lo que tiene intención real, con la conversación resumida.</p>
    <p><strong>Seguimiento que no depende de la memoria.</strong> Registrar cada contacto y disparar el recordatorio en la fecha acordada. En la práctica es la automatización que más ventas recupera.</p>
    <p><strong>Conectar herramientas que no se hablan.</strong> Que lo que entra por WhatsApp aparezca en la hoja o el CRM sin que nadie copie. Es el trabajo menos vistoso y uno de los que más horas devuelve.</p>

    <h2>Empresa de 15 personas en adelante</h2>
    <p>Aquí aparecen dos usos que abajo no tienen sentido:</p>
    <p><strong>Consultar documentación interna.</strong> Catálogos, políticas, listas de precios, manuales. Un sistema que responde con esos documentos evita que tres personas pregunten lo mismo a la misma persona cada día.</p>
    <p><strong>Reportes que se arman solos.</strong> Lo que hoy alguien consolida a mano cada lunes puede salir generado, con la misma fuente y sin errores de copiado.</p>

    <h2>Qué NO conviene automatizar</h2>
{tabla(['Tarea','Por qué no','Qué hacer en su lugar'],
 [['Cerrar una venta grande','Requiere criterio y relación','Que la IA prepare el contexto'],
  ['Atender un reclamo serio','El cliente necesita a una persona','Detectar y escalar de inmediato'],
  ['Decisiones de precio caso por caso','Es criterio comercial','Reglas claras y excepciones humanas'],
  ['Textos legales o fiscales','El error sale caro','Profesional que los valide'],
  ['Diagnóstico técnico complejo','La IA responde con seguridad falsa','Filtrar y pasar con contexto']])}

    <h2>Tres cuidados que evitan problemas caros</h2>
    <p><strong>Datos de clientes.</strong> Antes de conectar una herramienta con información personal, revisa dónde se guarda y quién puede verla. En México aplica la ley de protección de datos, y el aviso de privacidad tiene que reflejar lo que realmente haces con esa información.</p>
    <p><strong>Respuestas inventadas.</strong> Un modelo puede afirmar con total seguridad algo falso. Si el asistente atiende clientes, tiene que trabajar con la documentación del negocio como fuente y decir que no sabe cuando no lo sabe, en vez de improvisar.</p>
    <p><strong>Dependencia de una sola herramienta.</strong> Conviene que los datos vivan en un lugar que sea tuyo y exportable. Si mañana cambia el precio o las condiciones del proveedor, la información se queda contigo.</p>

    <h2>El error más común: empezar por la herramienta de moda</h2>
    <p>Cada pocos meses aparece una herramienta nueva y la tentación es adoptarla primero y buscarle uso después. Eso deja suscripciones activas que nadie abre. El camino contrario cuesta menos: parte de una tarea concreta que se repite, mídela, y solo entonces busca con qué resolverla.</p>
    <p>La otra trampa es el proyecto grande de entrada. Un sistema que intenta automatizar toda la operación de una vez tarda meses en dar señales de vida y suele morir antes. Un alcance chico que funciona en dos semanas genera confianza y paga el siguiente paso.</p>

    <h2>Cuánto cuesta esto en realidad</h2>
    <p>Hay dos rutas y conviene distinguirlas. Usar herramientas de IA directamente — pagar una suscripción y trabajar con ellas — cuesta unos cientos de pesos al mes y sirve para acelerar el trabajo de una persona. Montar un sistema que opere solo, conectado a tu WhatsApp y a tus datos, es un desarrollo: en Mattera arranca desde $10,000 MXN de pago único y desde $1,500 MXN mensuales de operación.</p>
    <p>La forma correcta de decidir no es comparar contra cero, es comparar contra lo que hoy cuesta esa tarea en horas de nómina. Si el trabajo repetitivo consume medio sueldo al mes, la cuenta sale sola; si consume dos horas a la semana, no.</p>

    <h2>Por dónde empezar esta semana</h2>
    <p>Sin comprar nada: cuenta. Durante cinco días, anota cuántos mensajes entran, cuántos se responden con lo mismo, cuántos llegan fuera de horario y cuántos prospectos quedaron sin seguimiento. Con esos cuatro números ya puedes decidir con evidencia.</p>
    <p>Si quieres verlo con más detalle, están <a href="5-senales-necesitas-automatizacion.html">las cinco señales</a> y la guía de <a href="../que-es-automatizacion.html">qué es la automatización con IA</a>. Y si la conclusión es que todavía no te conviene, es una respuesta válida: lo decimos en el diagnóstico en vez de vender un proyecto que no va a rendir.</p>
'''

spec = dict(
    slug='inteligencia-artificial-para-pymes-usos-practicos.html',
    title='Inteligencia artificial para PyMEs: usos prácticos por tamaño de empresa',
    h1='Inteligencia artificial para PyMEs: usos prácticos, por tamaño de empresa',
    titulo_corto='IA para PyMEs: usos prácticos',
    desc='Qué usos de IA rinden en un negocio de 3 personas, en uno de 15 y en uno de 30, qué no conviene automatizar y cuánto cuesta cada ruta en México.',
    bajada='Lo que le sirve a un negocio de dos personas no es lo que necesita uno de treinta. La lista, por tamaño.',
    lede='La pregunta útil no es cómo usar inteligencia artificial, sino qué trabajo repetitivo está costando horas. La IA rinde en tareas con respuesta predecible y volumen suficiente; fuera de eso, cuesta dinero y decepciona. Esta es la lista por tamaño de empresa, con lo que no conviene automatizar.',
    fecha='2026-10-16',
    categoria='IA Aplicada',
    cuerpo=cuerpo,
    cta='¿Quieres la cuenta con tus números en vez de una lista genérica? El diagnóstico dura 30 minutos.',
    ficha='Lo que sirve en un negocio de 3 personas no es lo que necesita uno de 30. Usos que rinden por tamaño, qué no automatizar y cuánto cuesta cada ruta.',
    faq=[('¿Qué puede hacer la IA en una empresa pequeña?','Responder lo repetitivo por WhatsApp, redactar borradores de cotizaciones y publicaciones, y ordenar datos que llegan sueltos. En negocios pequeños el beneficio es el tiempo del dueño.'),
         ('¿Cuánto cuesta implementar IA en una PyME en México?','Hay dos rutas: usar herramientas por suscripción, que cuesta unos cientos de pesos al mes y acelera el trabajo de una persona; o montar un sistema que opere solo, que en Mattera arranca desde $10,000 MXN de desarrollo y $1,500 MXN mensuales de operación.'),
         ('¿Qué no conviene automatizar?','Cerrar ventas grandes, atender reclamos serios, decidir precios caso por caso, redactar textos legales o fiscales y hacer diagnósticos técnicos complejos. En todos esos la IA puede preparar el contexto, no tomar la decisión.'),
         ('¿A partir de qué volumen conviene?','Como referencia, por debajo de cincuenta interacciones al mes con clientes el ahorro no suele justificar la inversión.'),
         ('¿Necesito cambiar mis sistemas actuales?','No necesariamente. La mayoría de los proyectos se conectan a lo que la empresa ya usa: WhatsApp, hojas de cálculo, correo, calendarios.'),
         ('¿Cómo empiezo sin gastar?','Durante cinco días cuenta cuántos mensajes entran, cuántos se repiten, cuántos llegan fuera de horario y cuántos prospectos quedaron sin seguimiento. Con esos cuatro números la decisión deja de ser una corazonada.')],
    relacionado=[('5-senales-necesitas-automatizacion.html','5 señales de que necesitas automatización →'),
                 ('../que-es-automatizacion.html','¿Qué es la automatización con IA? →'),
                 ('como-elegir-un-crm-para-mi-empresa.html','Cómo elegir un CRM →'),
                 ('../servicios/agentes-ia.html','Agentes de IA →')],
    destino=PEND,
)
print(escribir(spec))
