# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>1. La misma pregunta llega cuarenta veces al día</h2>
    <p>Horarios, precios, dirección, disponibilidad, si aceptan tarjeta. Si alguien de tu equipo contesta todos los días las mismas cinco preguntas, ese tiempo no está produciendo nada: está reponiendo información que ya existe y que podría entregarse sola.</p>
    <p>La prueba es simple. Abre la conversación de WhatsApp de tu negocio y cuenta cuántos de los últimos treinta mensajes entrantes se responden con una frase que ya escribiste antes. Si pasan de la mitad, tienes trabajo repetitivo medible, no una sospecha.</p>
    <p>Esta señal es la más común y también la más barata de resolver: la información ya está escrita en algún lado; el sistema solo tiene que entregarla en el momento en que la piden.</p>

    <h2>2. Los mensajes de la noche se contestan al día siguiente</h2>
    <p>Un cliente que escribe a las 10 de la noche y recibe respuesta a las 9 de la mañana ya tuvo once horas para escribirle a otro. No es un problema de esfuerzo de tu equipo: es un problema de horario. Nadie puede cubrir las 24 horas de un negocio con turnos humanos sin multiplicar la nómina.</p>
    <p>Revisa a qué hora entran los mensajes. Si una parte relevante cae fuera de tu horario, en fin de semana o en día festivo, estás perdiendo conversaciones que ya pagaste por generar: esos mensajes llegaron por tu publicidad, tu ficha de Google o tu página.</p>

    <h2>3. El seguimiento depende de que alguien se acuerde</h2>
    <p>Esta es la señal más cara y la más difícil de ver, porque no aparece en ningún reporte. El interesado pidió informes, se le mandó la cotización y ahí murió. No porque no quisiera comprar, sino porque nadie volvió a escribirle al tercer día.</p>
    <p>El seguimiento manual falla por diseño: compite contra la urgencia del día. Cuando el equipo está atendiendo a los clientes de hoy, los prospectos de la semana pasada siempre pierden. Un sistema que registra cada contacto y dispara el recordatorio en el momento acordado no es más inteligente que tu equipo — simplemente no se distrae.</p>

    <h2>4. La misma información se captura dos o tres veces</h2>
    <p>Llega un mensaje por WhatsApp, alguien copia los datos a una hoja de cálculo, después los vuelve a escribir en el sistema de facturación o en la agenda. Cada copia manual es tiempo y una oportunidad de error de dedo: un teléfono mal escrito es un cliente perdido sin que nadie se entere.</p>
    <p>Esta señal casi siempre aparece cuando el negocio creció por partes: primero el WhatsApp, luego el Excel, luego la agenda, luego el sistema de facturación. Cada herramienta funciona bien sola y ninguna se habla con la otra. La conexión entre ellas es de las automatizaciones más rápidas de implementar, porque no cambia cómo trabaja el equipo: solo elimina el paso de copiar.</p>

    <h2>5. No sabes cuántos clientes te escribieron el mes pasado</h2>
    <p>Si para responder esa pregunta hay que contar conversaciones a mano, no hay dato: hay recuerdo. Y sin dato no se puede decidir dónde invertir, qué campaña sirvió ni cuántas personas hacen falta.</p>
    <p>Esta señal suele ser la que más pesa a mediano plazo. El negocio que sabe cuántas consultas recibe, de dónde vienen y cuántas terminaron en venta puede crecer sobre evidencia. El que no lo sabe crece a tientas.</p>

    <h2>Cuál de las cinco resolver primero</h2>
    <p>No todas cuestan lo mismo ni devuelven lo mismo. En el diagnóstico las ordenamos con un criterio simple: volumen por repetición por costo del error.</p>
{tabla(['Señal','Qué la resuelve','Dificultad'],
 [['Preguntas repetidas','Asistente que responde con la información del negocio','Baja'],
  ['Mensajes fuera de horario','El mismo asistente, disponible 24/7','Baja'],
  ['Seguimiento olvidado','Registro de contactos con recordatorios automáticos','Media'],
  ['Captura duplicada','Integración entre las herramientas que ya usas','Media'],
  ['Falta de números','Registro y reporte de conversaciones y resultados','Media']])}
    <p>La recomendación práctica: empieza por donde el trabajo es repetitivo y la respuesta es predecible. Automatizar primero lo que exige criterio humano es la forma más rápida de gastar dinero en un sistema que nadie va a querer usar.</p>

    <h2>Cuándo automatizar NO es la respuesta</h2>
    <p>Hay negocios que todavía no necesitan esto, y vale más decirlo que vender un proyecto que no va a rendir. Si tienes menos de cincuenta interacciones con clientes al mes, el ahorro no justifica la inversión. Si tu proceso está mal definido, automatizarlo solo hace que el desorden ocurra más rápido. Y si cada cliente exige criterio profundo desde el primer segundo, lo que conviene es apoyar a la persona, no reemplazar la conversación.</p>
    <p>En Mattera eso se dice en el diagnóstico. Preferimos no arrancar un proyecto a arrancarlo sabiendo que no va a rendir. Puedes ver el criterio completo en <a href="../que-es-automatizacion.html">qué es la automatización con IA</a> y en el <a href="automatizacion-vs-contratar-personal.html">comparativo entre automatizar y contratar</a>.</p>

    <h2>La señal falsa: "todos lo están haciendo"</h2>
    <p>Que un competidor haya puesto un asistente en su sitio no es un diagnóstico. Es publicidad suya. La decisión de automatizar se toma con las horas de tu propia operación, no con lo que se ve desde fuera en la página de alguien más.</p>
    <p>Lo mismo aplica al revés: hay negocios chicos, de dos personas, donde el volumen de mensajes ya justifica un asistente, y empresas de treinta empleados donde lo que conviene primero es ordenar el proceso. El tamaño no decide; decide el trabajo repetitivo por unidad de tiempo.</p>
    <p>Por eso el primer paso nunca es elegir herramienta. Es contar: cuántos mensajes entran, cuántos se repiten, a qué hora llegan y cuántos se quedaron sin seguimiento el mes pasado. Con esos cuatro números la decisión deja de ser una corazonada.</p>

    <h2>Cómo saber si tu caso aplica</h2>
    <p>El diagnóstico que hacemos dura 30 minutos y no tiene costo. Mapeamos tus flujos, contamos dónde se va el tiempo y te decimos qué parte es automatizable hoy, cuál conviene dejar como está y qué costaría. Si al final la conclusión es que no conviene, también la decimos.</p>
'''

spec = dict(
    slug='5-senales-necesitas-automatizacion.html',
    title='5 señales de que tu negocio necesita automatización | Mattera Systems',
    h1='5 señales de que tu negocio necesita automatización',
    titulo_corto='5 señales de que necesitas automatización',
    desc='Cómo saber si tu operación ya pide automatizarse: las cinco señales concretas, cuál resolver primero y cuándo automatizar no es la respuesta.',
    bajada='No es una cuestión de tamaño ni de sector. Son cinco síntomas medibles — y uno de ellos cuesta más caro que los otros cuatro juntos.',
    lede='Un negocio necesita automatización cuando su equipo dedica horas a tareas repetitivas con respuesta predecible: contestar las mismas preguntas, capturar los mismos datos dos veces y dar seguimiento de memoria. Estas son las cinco señales que lo delatan, en orden de qué tan caro sale ignorarlas.',
    fecha='2026-09-29',
    categoria='Operaciones',
    cuerpo=cuerpo,
    cta='¿Quieres saber cuáles de estas cinco señales tiene tu negocio y cuánto tiempo recuperarías?',
    faq=[
        ('¿A partir de cuántos clientes conviene automatizar?','Como referencia práctica, por debajo de cincuenta interacciones al mes con clientes el ahorro no suele justificar la inversión. Por encima de ese volumen, el trabajo repetitivo ya consume horas que se pueden medir.'),
        ('¿Automatizar significa despedir gente?','No. Lo que se automatiza es la parte repetitiva y predecible del trabajo: contestar lo mismo, capturar datos, recordar seguimientos. Cerrar ventas, resolver casos complicados y atender a un cliente molesto siguen siendo humanos.'),
        ('¿Cuánto tarda en implementarse?','El promedio de Mattera es de 11 días hábiles desde el diagnóstico hasta el lanzamiento. La mayor parte de ese tiempo no la ocupa la tecnología, sino definir con claridad cómo opera el negocio.'),
        ('¿Cuánto cuesta?','El desarrollo arranca desde $10,000 MXN de pago único y la operación mensual desde $1,500 MXN. El precio exacto sale del diagnóstico, que dura 30 minutos y no tiene costo.'),
        ('¿Y si mi proceso está desordenado?','Entonces primero se ordena. Automatizar un proceso mal diseñado solo hace que el desorden ocurra más rápido; eso lo decimos en el diagnóstico en lugar de arrancar el proyecto.'),
    ],
    relacionado=[('automatizacion-vs-contratar-personal.html','Automatizar o contratar: cuándo cada uno →'),
                 ('como-funciona-un-chatbot-de-ia-en-la-practica.html','Cómo funciona un chatbot de IA →'),
                 ('../que-es-automatizacion.html','¿Qué es la automatización con IA? →'),
                 ('../servicios/automatizacion-procesos.html','Automatización de procesos →')],
)
print(escribir(spec))
