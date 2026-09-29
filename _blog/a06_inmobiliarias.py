# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>El problema no es conseguir prospectos, es llamarlos a tiempo</h2>
    <p>Una inmobiliaria con campañas activas recibe contactos todos los días: formularios del portal, mensajes de la publicidad, personas que dejaron su teléfono en una caseta. El cuello de botella casi nunca es la cantidad. Es que la llamada de seguimiento depende de que un asesor se acuerde, tenga hueco y esté de humor para marcar.</p>
    <p>Lo que pasa en la práctica: los contactos de hoy se atienden, los de la semana pasada se enfrían y los de hace un mes ya no existen para nadie. Y el prospecto frío no es prospecto perdido por falta de interés — es alguien que ya compró en otro lado o que sigue esperando que alguien le llame.</p>
    <p>El otro problema es de registro. Si el resultado de cada llamada vive en la cabeza del asesor o en una libreta, el gerente no puede saber cuántos contactos se trabajaron ni por qué no avanzaron.</p>

    <h2>Lo que opera hoy en Vista California Residencial</h2>
    <p>Para <strong>Vista California Residencial</strong>, desarrollo residencial en Guadalajara, el sistema que está en operación hace tres cosas, en este orden:</p>
    <p><strong>Registra al prospecto desde Telegram.</strong> El asesor da de alta al interesado — nombre, teléfono, modelo que le interesa, presupuesto, tipo de crédito, notas — hablando normal con un asistente, sin formularios ni pantallas. Todo queda en una hoja de control que el equipo ya usaba.</p>
    <p><strong>Programa y hace la llamada de seguimiento.</strong> El sistema marca a la hora acordada con voz de IA, sostiene la conversación de seguimiento y detecta cuándo la persona quiere agendar una cita con un asesor humano.</p>
    <p><strong>Anota el resultado.</strong> Al terminar la llamada, el resumen, los siguientes pasos y si hubo cita se escriben solos en la misma hoja. Nadie captura nada después.</p>
    <p>Es un sistema de seguimiento, no de venta. La visita al desarrollo, la negociación y el cierre siguen siendo del asesor.</p>

    <h2>Por qué Telegram y no una plataforma nueva</h2>
    <p>Porque el sistema que nadie abre no sirve. Un CRM con licencia por usuario obliga al asesor a entrar a una pantalla más, y en la práctica termina capturando al final del día — o no capturando. Un asistente en el mismo teléfono donde ya vive el trabajo se usa en el momento, que es cuando el dato es correcto.</p>
{tabla(['Momento','Sin sistema','Con seguimiento automático'],
 [['Llega un interesado','Nota en la libreta o en la cabeza','Queda registrado al instante desde el chat'],
  ['Seguimiento a los 3 días','Depende de que alguien se acuerde','Se programa y se ejecuta solo'],
  ['Resultado de la llamada','Se pierde o se captura tarde','Se escribe solo en la hoja de control'],
  ['Prospecto que no contesta','Se olvida','Vuelve a la cola con reintento'],
  ['Reporte para el gerente','Se arma a mano','Sale de la misma hoja, al día']])}

    <h2>Las tres reglas que hay que decidir antes de automatizar</h2>
    <p>Un sistema de seguimiento no se diseña con tecnología, se diseña con reglas del negocio. Son tres y las tiene que decidir la inmobiliaria, no el proveedor.</p>
    <p><strong>Cuándo se llama.</strong> A las pocas horas del registro, al tercer día, a la semana. No hay una respuesta universal: depende del ciclo del producto. Un departamento de entrega inmediata no se sigue igual que una preventa a dos años.</p>
    <p><strong>Cuántas veces.</strong> Sin un límite, el sistema persigue para siempre a quien ya dijo que no y molesta. Con un límite claro — por ejemplo tres intentos y se marca como frío — la lista se mantiene limpia y el equipo sabe en qué está trabajando de verdad.</p>
    <p><strong>Qué cuenta como avance.</strong> Si el objetivo es la cita, el sistema debe reconocerla y escribirla; si el objetivo es calificar presupuesto, es otro dato el que importa. Cuando esto no se define, el reporte acaba lleno de llamadas hechas y vacío de resultados.</p>

    <h2>Lo que se gana al tener el dato escrito</h2>
    <p>El efecto que más se nota no es la llamada automática: es que al final de la semana existe un registro completo de qué pasó con cada contacto. Con eso el gerente puede ver cuántos prospectos entraron, cuántos se trabajaron, en qué punto se caen y qué campaña trajo a los que sí avanzaron.</p>
    <p>Sin ese registro, las decisiones de inversión publicitaria se toman por sensación. Con él, se toman con evidencia — y esa es normalmente la parte que más dinero mueve, más que las horas ahorradas en marcar.</p>

    <h2>Lo que este tipo de sistema no hace</h2>
    <p>No vende. Una llamada automática no cierra un departamento ni sustituye la visita. Tampoco decide por el asesor: cuando el prospecto muestra intención real, la conversación pasa a una persona con el contexto ya escrito.</p>
    <p>Y no reemplaza al equipo comercial. Lo que quita es el trabajo que nadie quiere hacer — marcar al que no contestó, recordar al de la semana pasada, capturar lo que se dijo — para que el tiempo del asesor se vaya a las conversaciones que sí pueden terminar en venta. El criterio completo está en <a href="../industrias/inmobiliarias.html">sistemas para inmobiliarias</a>.</p>

    <h2>Qué necesita una inmobiliaria para montar algo así</h2>
    <p>Menos de lo que parece. Hace falta una fuente de prospectos que ya exista (portal, publicidad o caseta), un lugar donde vivan los datos — una hoja de cálculo basta para empezar — y una regla clara de seguimiento: a los cuántos días se vuelve a llamar y cuántos intentos se hacen antes de dejarlo ir.</p>
    <p>Lo que no hace falta es cambiar de plataforma ni comprar licencias por asesor. Los sistemas que construimos se conectan a las herramientas que el equipo ya usa; ese criterio está explicado en <a href="../servicios/integraciones.html">integraciones</a> y en <a href="../servicios/crm-para-empresas.html">CRM a medida</a>.</p>
    <p>El desarrollo de un sistema de este tipo arranca desde $10,000 MXN de pago único, con operación mensual desde $1,500 MXN. El alcance exacto sale del diagnóstico de 30 minutos, sin costo.</p>
'''

spec = dict(
    slug='seguimiento-automatico-de-prospectos-inmobiliarios.html',
    title='Seguimiento automático de prospectos inmobiliarios con IA | Mattera',
    h1='Seguimiento de prospectos inmobiliarios: el sistema que llama por ti',
    titulo_corto='Seguimiento automático para inmobiliarias',
    desc='Cómo funciona un sistema que registra prospectos, programa llamadas de seguimiento con voz de IA y anota el resultado solo. El caso de Vista California Residencial en Guadalajara.',
    bajada='El prospecto no se pierde por falta de interés. Se pierde porque nadie volvió a marcarle al tercer día.',
    lede='En una inmobiliaria el cuello de botella no es conseguir prospectos: es el seguimiento, que depende de que un asesor se acuerde. Este es el sistema que opera en Vista California Residencial — registra desde el chat, programa y hace la llamada con voz de IA, y escribe el resultado solo.',
    fecha='2026-09-29',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Cuántos prospectos de hace tres semanas siguen sin seguimiento en tu inmobiliaria?',
    faq=[('¿La llamada automática cierra ventas?','No. Es un sistema de seguimiento: sostiene la conversación, detecta interés y agenda con un asesor. La visita, la negociación y el cierre siguen siendo humanos.'),
         ('¿Hay que cambiar de CRM para usarlo?','No. El sistema se conecta a lo que el equipo ya usa; en este caso los datos viven en una hoja de control. Un CRM con licencia por asesor no es requisito.'),
         ('¿Por qué el asesor lo opera desde Telegram?','Porque el sistema que obliga a abrir una pantalla más termina sin usarse. Registrar desde el chat que ya tiene abierto hace que el dato se capture en el momento, no al final del día.'),
         ('¿Qué pasa si el prospecto no contesta?','Vuelve a la cola con reintento según la regla que defina la inmobiliaria: a los cuántos días se llama y cuántos intentos se hacen antes de darlo por frío.'),
         ('¿Cuánto cuesta un sistema así?','El desarrollo arranca desde $10,000 MXN de pago único y la operación mensual desde $1,500 MXN. El alcance exacto sale del diagnóstico de 30 minutos, sin costo.')],
    relacionado=[('../industrias/inmobiliarias.html','Sistemas para inmobiliarias →'),
                 ('../servicios/crm-para-empresas.html','CRM a medida →'),
                 ('../servicios/agentes-ia.html','Agentes de IA →'),
                 ('5-senales-necesitas-automatizacion.html','5 señales de que necesitas automatización →')],
)
print(escribir(spec))
