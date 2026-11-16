# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Primero: cuál de los tres WhatsApp tienes</h2>
    <p>Esta es la confusión que hace perder más tiempo. Hay tres cosas distintas con el mismo nombre.</p>
{tabla(['Qué es','Para qué sirve','¿Se puede conectar?'],
 [['WhatsApp normal','Uso personal','No'],
  ['WhatsApp Business (la app)','Negocio chico, un teléfono, respuestas rápidas','No de forma oficial'],
  ['Conexión oficial de WhatsApp Business','Conectar con otros sistemas y atender en automático','Sí, es la única vía legítima']])}
    <p>La app de WhatsApp Business funciona bien hasta cierto punto: etiquetas, catálogo, mensajes de bienvenida. Lo que no hace es hablar con tu CRM, con tu agenda o con tu sistema de facturación. Para eso se necesita la conexión oficial, que Meta otorga a empresas verificadas.</p>
    <p>Hay servicios que prometen conectar la app normal por caminos no oficiales. Evítalos: Meta bloquea esos números, y perder el número de WhatsApp de tu negocio es perder tu lista de clientes.</p>

    <h2>Qué pide Meta para darte la conexión oficial</h2>
    <p>Tres cosas: que tu empresa esté verificada (acta constitutiva y RFC), un número de teléfono que no esté usándose hoy en la app de WhatsApp Business, y un perfil de empresa con nombre y categoría. El trámite toma de días a un par de semanas según qué tan rápido responda Meta.</p>
    <p>Dos advertencias que casi nadie dice a tiempo. Si usas tu número actual, tendrás que darlo de baja de la app antes de migrarlo: durante ese rato no recibes mensajes. Y los mensajes que tú inicias fuera de una ventana de 24 horas tienen que ir en plantillas aprobadas por Meta, con un costo por mensaje.</p>

    <h2>Qué se puede conectar, en la práctica</h2>
    <p><strong>Con tu CRM.</strong> Cada conversación queda registrada en la ficha del cliente, sin que nadie copie y pegue. Es la conexión más pedida y la que más horas devuelve.</p>
    <p><strong>Con tu agenda.</strong> El cliente pide cita por WhatsApp y el sistema la escribe en el calendario, con recordatorio incluido.</p>
    <p><strong>Con tu catálogo o inventario.</strong> El asistente responde precios y existencias leyendo de donde ya los tienes, sea una hoja de cálculo o tu ERP.</p>
    <p><strong>Con tu correo.</strong> Cuando llega un contacto que importa, alguien se entera sin tener que mirar el teléfono.</p>
    <p>Lo que decide qué es posible no es WhatsApp: es si tu otra herramienta se deja conectar. Casi todas las conocidas sí; algunos sistemas viejos a la medida, no, y ahí se evalúa otra salida.</p>

    <h2>Las tres formas de hacerlo, con sus costos reales</h2>
{tabla(['Camino','Cuándo conviene','Qué cuesta'],
 [['Plataforma de chat lista (varias en el mercado)','Equipo de ventas que solo necesita bandeja compartida','Pago por usuario al mes, crece con el equipo'],
  ['Conectar con una herramienta de automatización','Flujos sencillos entre dos o tres sistemas','Suscripción de la herramienta + armado'],
  ['Sistema a medida sobre la conexión oficial','Reglas propias, varios sistemas, asistente con IA','Desarrollo una vez + operación mensual']])}
    <p>No hay una respuesta única. Si lo que necesitas es que tres vendedores compartan un número, una plataforma de chat lista es lo más barato y rápido. Si necesitas que el sistema responda solo, lea tu catálogo y escriba en tu CRM, eso ya es un desarrollo.</p>

    <h2>Lo que nadie te dice antes de empezar</h2>
    <p><strong>La ventana de 24 horas.</strong> Puedes responder libremente dentro de las 24 horas posteriores al último mensaje del cliente. Pasado ese tiempo, solo puedes escribirle con una plantilla aprobada, y cada una se cobra. Cualquier diseño de seguimiento tiene que considerarlo.</p>
    <p><strong>Las plantillas se aprueban, no se improvisan.</strong> Meta revisa el texto. Las que parecen publicidad masiva se rechazan.</p>
    <p><strong>Un número, un sistema.</strong> El mismo número no puede estar en la app de WhatsApp Business y en la conexión oficial al mismo tiempo.</p>
    <p><strong>El historial no se migra.</strong> Al pasar a la conexión oficial, las conversaciones viejas de la app se quedan en la app.</p>

    <h2>Un error caro: automatizar antes de ordenar</h2>
    <p>Conectar WhatsApp con un CRM que nadie usa no arregla nada: solo hace que los datos lleguen más rápido a un lugar que nadie abre. Antes de conectar conviene tener claro quién atiende, en qué momento se considera cliente y cuándo se da por perdido.</p>
    <p>La prueba rápida: pídele a dos personas de tu equipo que te digan qué hacen cuando entra un mensaje nuevo. Si responden distinto, lo que falta no es tecnología, es acuerdo.</p>

    <h2>Qué pasa con los datos de tus clientes</h2>
    <p>Al conectar WhatsApp con otros sistemas, las conversaciones empiezan a guardarse en algún lado. Conviene decidirlo tú: en tu CRM, en tu hoja, en tu servidor. Y conviene que tu aviso de privacidad diga lo que realmente haces con esa información, porque en México aplica la ley de protección de datos personales.</p>
    <p>Dos cosas que recomendamos siempre: que el acceso del sistema se limite a lo que necesita para trabajar, y que puedas exportar todo si mañana cambias de proveedor. Si quien te lo monta no sabe responder dónde quedan los datos, esa es la respuesta.</p>

    <h2>Por dónde empezar sin gastar</h2>
    <p>Antes de contratar nada, cuenta durante una semana: cuántos mensajes entran, cuántos se responden con lo mismo, cuántos llegan fuera de horario y cuántos terminan en venta. Si la mayoría son preguntas repetidas, un asistente conectado rinde desde el primer mes. Si son pocas y cada una necesita criterio, lo que te sirve es una bandeja compartida, no un sistema.</p>
    <p>En Mattera hacemos la conexión completa con la vía oficial: <a href="../servicios/chatbot-whatsapp.html">asistente de WhatsApp</a> y <a href="../servicios/integraciones.html">conexiones con tus herramientas</a>. El desarrollo arranca desde $10,000 MXN de pago único y la operación desde $1,500 MXN al mes. El alcance sale de una llamada de 30 minutos, sin costo.</p>
'''

spec = dict(
    slug='como-integrar-whatsapp-con-tu-crm-o-sistema.html',
    title='Cómo integrar WhatsApp con tu CRM o tu sistema | Mattera Systems',
    h1='Cómo integrar WhatsApp con tu CRM o tu sistema',
    titulo_corto='Integrar WhatsApp con tu CRM',
    desc='Qué WhatsApp se puede conectar y cuál no, qué pide Meta, las tres formas de hacerlo con sus costos y las trampas: la ventana de 24 horas, las plantillas y el historial.',
    bajada='Hay tres cosas distintas que se llaman WhatsApp y solo una se conecta. Empezar por la equivocada cuesta semanas.',
    lede='Para integrar WhatsApp con tu CRM necesitas la conexión oficial de WhatsApp Business: ni el WhatsApp normal ni la app de Business se conectan de forma legítima. Esto es lo que pide Meta, las tres maneras de hacerlo con sus costos y las trampas que nadie menciona antes de empezar.',
    fecha='2026-11-17',
    categoria='Integraciones',
    cuerpo=cuerpo,
    cta='¿Quieres que tu WhatsApp escriba solo en tu CRM? Te decimos si se puede con tus herramientas.',
    ficha='Hay tres cosas que se llaman WhatsApp y solo una se conecta. Qué pide Meta, las tres formas de hacerlo con sus costos, y la trampa de la ventana de 24 horas.',
    faq=[('¿Puedo conectar mi WhatsApp Business normal a un CRM?','No de forma oficial. La app de WhatsApp Business no se conecta con otros sistemas; para eso existe la conexión oficial de WhatsApp Business, que Meta otorga a empresas verificadas. Los servicios que prometen conectar la app por vías no oficiales exponen tu número a que lo bloqueen.'),
         ('¿Qué necesito para que Meta me dé la conexión oficial?','Que tu empresa esté verificada con acta constitutiva y RFC, un número que no esté en uso en la app de WhatsApp Business y un perfil de empresa con nombre y categoría. El trámite toma de días a un par de semanas.'),
         ('¿Qué es la ventana de 24 horas?','Puedes responder libremente durante las 24 horas siguientes al último mensaje del cliente. Después solo puedes escribirle con plantillas aprobadas por Meta, y cada envío tiene un costo.'),
         ('¿Se pierde el historial de conversaciones al migrar?','Sí. Las conversaciones que viven en la app de WhatsApp Business se quedan ahí; la conexión oficial empieza con historial nuevo.'),
         ('¿Puedo usar el mismo número que uso hoy?','Sí, pero hay que darlo de baja de la app antes de migrarlo, y durante ese rato no se reciben mensajes. Muchos negocios prefieren estrenar número y avisar el cambio.'),
         ('¿Cuánto cuesta conectarlo?','Depende del camino: una plataforma de chat lista cobra por usuario al mes; un sistema a medida sobre la conexión oficial arranca desde $10,000 MXN de desarrollo y $1,500 MXN mensuales de operación.')],
    relacionado=[('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →'),
                 ('../servicios/integraciones.html','Integraciones →'),
                 ('como-elegir-un-crm-para-mi-empresa.html','Cómo elegir un CRM →'),
                 ('asistente-whatsapp-para-negocios-digitales.html','Caso: asistente para un negocio digital →')],
    destino=PEND,
)
print(escribir(spec))
