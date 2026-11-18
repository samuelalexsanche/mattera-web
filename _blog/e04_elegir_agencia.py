# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Primero: ¿de verdad necesitas una agencia?</h2>
    <p>Hay tres caminos y el más caro no siempre es el que parece.</p>
{tabla(['Camino','Cuándo conviene','Dónde duele'],
 [['Hacerlo en casa','Ya tienes alguien técnico con tiempo libre de verdad','El tiempo libre rara vez existe; el proyecto se queda a medias'],
  ['Freelancer','Una automatización acotada, con alcance claro','Si se va, nadie más entiende lo que construyó'],
  ['Agencia','Varios sistemas conectados, operación continua','Cuesta más y hay que elegir bien a quién'],
  ['Plataforma lista','El problema es común y el software ya lo resuelve','Pagas por usuario y te adaptas a su forma de trabajar']])}
    <p>La pregunta que ordena la decisión no es cuál es mejor, sino quién va a mantenerlo dentro de un año. Un sistema sin nadie que lo cuide se degrada: cambian los precios, cambia una herramienta, Meta cambia una regla, y lo que funcionaba deja de funcionar en silencio.</p>

    <h2>Las seis preguntas que separan a una agencia seria</h2>
    <p>Hazlas en la primera llamada. Las respuestas distinguen más que cualquier portafolio.</p>

    <h3>1. ¿De quién son los datos y cómo me los llevo?</h3>
    <p>La respuesta correcta es inmediata y concreta: son tuyos y se exportan completos, en un formato que otro sistema pueda leer. Si hay titubeo, si la exportación "se puede solicitar", o si el sistema vive solo dentro de una herramienta propia de la agencia, estás comprando una jaula. Pregúntalo antes de firmar, no después.</p>

    <h3>2. ¿Con qué lo vas a construir?</h3>
    <p>Que te nombren las herramientas. Si la respuesta es "tecnología propia" sin más detalle, el riesgo es que nadie más pueda mantenerlo. Herramientas conocidas — las de automatización, los modelos de los proveedores grandes, bases de datos estándar — significan que si un día cambias de proveedor, el siguiente entiende lo que hay.</p>

    <h3>3. ¿Qué pasa cuando el sistema se equivoca?</h3>
    <p>Todos se equivocan. Lo que distingue a quien sabe es que ya tenga respuesta: a quién escala, qué queda registrado, cómo se detecta. Si te prometen que responderá bien el 100% de los casos, o no han puesto nada en producción o te están diciendo lo que quieres oír.</p>

    <h3>4. ¿Qué incluye la mensualidad y qué no?</h3>
    <p>Pide la línea divisoria por escrito. Normalmente los ajustes al sistema existente entran y los procesos nuevos se cotizan aparte. El problema no es dónde esté la raya: es que no esté dicha antes de la primera factura con un concepto que no esperabas.</p>

    <h3>5. ¿Puedo ver algo funcionando?</h3>
    <p>No un video editado: algo que puedas usar tú. Un sitio publicado, un asistente con el que puedas escribir, un número al que mandar un mensaje. Una agencia que automatiza y no tiene nada suyo operando es una señal por sí misma.</p>

    <h3>6. ¿Qué me vas a decir que no se puede?</h3>
    <p>Es la pregunta más reveladora y casi nadie la hace. Quien ha implementado de verdad tiene una lista de cosas que no funcionan o que no conviene automatizar. Quien dice que todo se puede todavía no se ha topado con un sistema cerrado, una regla de Meta o un proceso que cambia cada semana.</p>

    <h2>Las señales de alarma</h2>
    <ul class="lista-no">
      <li><strong>Garantizan resultados en números.</strong> "Aumenta tus ventas 40%" depende de tu producto, tu precio y tu equipo, no del sistema. Quien lo promete no controla ninguna de las tres.</li>
      <li><strong>Prometen aparecer primero en ChatGPT.</strong> No existe ese control. Se puede aumentar la probabilidad de que te citen; garantizar el primer lugar, no.</li>
      <li><strong>No hay diagnóstico antes del precio.</strong> Cotizar sin conocer la operación es adivinar, y lo que se adivina se ajusta después, siempre hacia arriba.</li>
      <li><strong>Casos sin nombre.</strong> "Una distribuidora del Bajío ahorró 300 horas" no se puede verificar. Un caso real tiene nombre, o al menos algo publicado que puedas abrir.</li>
      <li><strong>Contrato largo obligatorio.</strong> Si el sistema funciona, no hace falta amarrar al cliente. La permanencia forzosa protege al proveedor, no a ti.</li>
    </ul>

    <h2>Cómo comparar dos propuestas sin marearte</h2>
    <p>Las propuestas rara vez son comparables tal cual llegan. Llévalas a la misma tabla antes de decidir:</p>
{tabla(['Qué comparar','Qué estás buscando'],
 [['Pago único y mensualidad, por separado','Que no escondan costo recurrente dentro del desarrollo'],
  ['Qué entra en la mensualidad','Ajustes sí, procesos nuevos no: que esté dicho'],
  ['Costos de terceros','Meta, servidores, licencias: suelen ir aparte y nadie los menciona'],
  ['Fecha comprometida','Una fecha, no "unas semanas"'],
  ['Qué pasa si se pasan de fecha','Si no hay consecuencia, la fecha es un deseo'],
  ['Permanencia mínima','Entre menos amarre, más confianza tiene el proveedor en su trabajo'],
  ['Propiedad y exportación','Tuyo, exportable, en formato estándar']])}
    <p>Si una propuesta no te deja llenar esta tabla, ya aprendiste algo de cómo va a ser trabajar con ellos.</p>

    <h2>Una nota sobre el precio</h2>
    <p>La propuesta más barata suele ser la que menos preguntó. Cotizar sin diagnóstico es más rápido y sale más bajo, porque no incluye lo que todavía no se sabe — y lo que no se sabe aparece después, en forma de ajustes que no estaban contemplados.</p>
    <p>Eso no significa que lo caro sea mejor. Significa que el número solo se puede comparar cuando las dos propuestas describen el mismo alcance. Si una dice "asistente de WhatsApp" y la otra detalla qué responde, con qué datos, conectado a qué y quién lo mantiene, no estás comparando precios: estás comparando dos cosas distintas.</p>
'''

spec = dict(
    slug='como-elegir-agencia-de-automatizacion.html',
    title='Cómo elegir con quién automatizar tu empresa',
    h1='Cómo elegir con quién automatizar tu empresa',
    titulo_corto='Elegir agencia de automatización',
    desc='Agencia, freelancer o en casa; las seis preguntas que separan a quien sabe, las señales de alarma y cómo comparar dos propuestas.',
    bajada='La propuesta más barata suele ser la que menos preguntó. Y la más cara no siempre es la que más sabe.',
    lede='Para elegir con quién automatizar, lo que decide no es el portafolio sino seis preguntas: de quién son los datos, con qué se construye, qué pasa cuando falla, qué incluye la mensualidad, si puedes ver algo funcionando y qué te van a decir que no se puede. Esto es cómo hacerlas y qué respuestas deberían preocuparte.',
    fecha='2026-12-08',
    categoria='Operaciones',
    cuerpo=cuerpo,
    cta='Si estás comparando propuestas y quieres una tercera para contrastar, el diagnóstico es de 30 minutos y sin costo.',
    ficha='Agencia, freelancer o en casa; las seis preguntas que separan a quien sabe de quien improvisa, y cómo comparar dos propuestas que no se parecen.',
    faq=[('¿Conviene una agencia, un freelancer o hacerlo internamente?','Depende de quién va a mantenerlo dentro de un año. Un freelancer funciona para una automatización acotada; en casa funciona si de verdad hay alguien técnico con tiempo; una agencia tiene sentido cuando son varios sistemas conectados y hace falta que alguien los opere de forma continua.'),
         ('¿Qué debo preguntar antes de contratar una agencia de automatización?','De quién son los datos y cómo se exportan, con qué herramientas se va a construir, qué pasa cuando el sistema se equivoca, qué entra en la mensualidad y qué no, si puedes ver algo funcionando, y qué te van a decir que no se puede hacer.'),
         ('¿Cuáles son las señales de alarma al contratar automatización?','Que garanticen resultados en números, que prometan aparecer primero en ChatGPT, que coticen sin diagnóstico previo, que presenten casos sin nombre ni nada verificable, y que exijan permanencia mínima obligatoria.'),
         ('¿De quién son los datos del sistema que me construyan?','Tuyos, y la respuesta debería ser inmediata. Exigible: exportación completa, en un formato que otro sistema pueda leer, cuando tú lo pidas. Si el sistema solo vive dentro de una herramienta propia del proveedor, estás comprando una dependencia.'),
         ('¿Por qué una propuesta es mucho más barata que otra?','Casi siempre porque preguntó menos. Cotizar sin diagnóstico sale más bajo porque no incluye lo que todavía no se sabe, y eso aparece después como ajustes no contemplados. Dos precios solo se pueden comparar si describen el mismo alcance.'),
         ('¿Puede alguien garantizar que una IA recomiende mi negocio?','No. No existe un control sobre lo que responde un modelo, ni publicidad dentro de esas respuestas. Lo que sí se puede es aumentar la probabilidad de ser citado: que la página se encuentre, que los datos se puedan verificar y que haya menciones de terceros.')],
    relacionado=[('../nosotros.html','Quiénes somos →'),
                 ('../planes.html','Precios públicos →'),
                 ('../servicios/automatizacion-procesos.html','Automatización de procesos →'),
                 ('automatizacion-vs-contratar-personal.html','¿Automatizar o contratar? →'),
                 ('cuanto-cuesta-un-crm-en-mexico.html','Cuánto cuesta un CRM →'),
                 ('../glosario.html','Glosario de términos →')],
    destino=PEND,
)
print(escribir(spec))
