# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>El mostrador manda: qué se automatiza y qué no</h2>
    <p>En un restaurante hay una regla que conviene fijar antes de cualquier herramienta: <strong>nada que automatices puede quitarle atención a quien ya está sentado</strong>. Por eso el orden correcto empieza por lo que ocurre fuera del local — el teléfono, el WhatsApp, las redes — y no por la operación del piso.</p>

    <h2>1. Reservaciones</h2>
    <p>Tomar una reserva por teléfono ocupa a alguien dos o tres minutos y obliga a coincidir. Un sistema de reservas muestra los horarios libres, el cliente elige y queda registrado, con confirmación automática y recordatorio el mismo día.</p>
    <p>El recordatorio es lo que más rinde: la mesa que nadie avisó que no iba a usar es dinero perdido que nadie contabiliza.</p>

    <h2>2. Pedidos por WhatsApp</h2>
    <p>Para llevar y a domicilio, el patrón se repite: el cliente pregunta si hay tal platillo, cuánto cuesta, cuánto tarda, si llegan a su colonia. Un asistente conectado al menú responde eso y arma el pedido, y avisa a cocina o al encargado cuando está listo para confirmarse.</p>
    <p>Aquí hay una decisión de negocio, no técnica: ¿quieres que el pedido se cierre solo o que una persona lo confirme? En restaurantes con cocina chica conviene lo segundo, porque el límite real no es tomar el pedido sino poder cumplirlo.</p>

    <h2>3. Las preguntas de siempre</h2>
    <p>Horario, dirección, estacionamiento, si aceptan tarjeta, si hay opciones sin gluten, si se puede llevar mascota, si hay mesa para diez. Son respuestas fijas, llegan todo el día y muchas de madrugada.</p>

    <h2>4. Que el cliente vuelva</h2>
    <p>Es lo que casi nadie hace y lo que más margen deja: quien ya comió contigo y quedó contento es el cliente más barato de recuperar. Un mensaje puntual con la promoción del mes a quien pidió hace seis semanas rinde más que anunciarse a desconocidos — siempre que la persona haya aceptado recibirlo.</p>

    <h2>Lo que no conviene automatizar</h2>
{tabla(['Situación','Quién la atiende','Por qué'],
 [['Reservar, confirmar, recordar','El sistema','Reglas claras y repetitivas'],
  ['Preguntas de menú, horario y pago','El sistema','Respuesta fija'],
  ['Pedido para llevar','El sistema, con confirmación humana','La cocina pone el límite real'],
  ['Una queja por la comida','Una persona, rápido','Se juega la reseña y el cliente'],
  ['Evento grande o privatización','El dueño o el encargado','Es negociación, no trámite'],
  ['El servicio en mesa','El equipo, siempre','Es el producto']])}

    <h2>Lo que sí se puede medir desde la primera semana</h2>
    <p>No hace falta un panel sofisticado. Cuatro números bastan para saber si valió la pena: cuántos mensajes entran al día, cuántos se respondieron sin que nadie los tocara, cuántas reservas se hicieron fuera de horario y cuántas mesas se liberaron a tiempo porque alguien avisó al recibir el recordatorio.</p>
    <p>Esos cuatro se pueden contar a mano la primera semana, antes y después. Si no se mueven, el sistema no te estaba haciendo falta — y es mejor saberlo pronto.</p>

    <h2>El error de automatizar la personalidad</h2>
    <p>Un restaurante con historia tiene una forma de hablar: la de quien está en la caja desde hace veinte años. El asistente puede sonar parecido si se le enseña, pero no debe inventar bromas ni prometer cosas que la cocina no puede cumplir.</p>
    <p>La regla que aplicamos: responde con lo que está escrito en la carta y en las políticas del negocio; si no lo sabe, lo dice y pasa la conversación. Un asistente que improvisa promete una mesa que no hay, y esa reseña la escribe el cliente, no el sistema.</p>

    <h2>Las plataformas de reparto son otra cosa</h2>
    <p>Conviene no confundir: una aplicación de reparto te trae pedidos y te cobra comisión por cada uno, y el cliente queda con ellos. Un pedido que entra por tu WhatsApp es tuyo, sin comisión, y el contacto se queda contigo.</p>
    <p>No se trata de salir de las plataformas: se trata de no depender solo de ellas. El cliente que te descubrió ahí puede volver por tu canal si se lo pones fácil.</p>

    <h2>Antes de automatizar: el menú tiene que estar publicado</h2>
    <p>Un asistente no puede responder precios si el menú vive en una foto que se actualizó hace ocho meses. El orden que funciona: primero la carta publicada como texto en tu sitio — se lee en celular, se edita el mismo día y Google la entiende —, después la ficha de Google al corriente, y hasta entonces el asistente.</p>
    <p>Eso está contado con un caso real en <a href="pagina-web-para-restaurantes.html">la página web de un restaurante</a> y el detalle del giro en <a href="../industrias/restaurantes.html">sistemas para restaurantes</a>.</p>

    <h2>Cuánto cuesta</h2>
    <p>El desarrollo arranca desde $10,000 MXN de pago único y la operación desde $1,500 MXN al mes; si lo que necesitas primero es el sitio con la carta, los planes tienen <a href="../planes.html">precio publicado desde $5,900 MXN</a>. La cuenta se hace contra lo que hoy cuestan las horas al teléfono y las mesas que se quedaron vacías sin aviso.</p>
'''

spec = dict(
    slug='como-automatizar-un-restaurante.html',
    title='Cómo automatizar un restaurante: reservas, pedidos y WhatsApp | Mattera',
    h1='Cómo automatizar un restaurante sin descuidar el mostrador',
    titulo_corto='Automatizar un restaurante',
    desc='Qué automatizar en un restaurante y en qué orden: reservas, pedidos por WhatsApp, preguntas de siempre y clientes que vuelven. Qué debe seguir siendo humano.',
    bajada='Regla primera: nada de lo que automatices puede quitarle atención a quien ya está sentado.',
    lede='En un restaurante conviene automatizar lo que pasa fuera del local: reservaciones con recordatorio, pedidos por WhatsApp, las preguntas de siempre y el mensaje al cliente que no vuelve. Lo que ocurre en el piso —el servicio y las quejas— sigue siendo humano. Este es el orden que funciona.',
    fecha='2026-11-24',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Cuántas llamadas al día se van en reservas y en la misma pregunta de siempre?',
    ficha='Reservas, pedidos por WhatsApp y clientes que vuelven. Qué automatizar primero, qué dejar en manos del equipo y por qué el menú va antes que el asistente.',
    faq=[('¿Conviene automatizar los pedidos a domicilio?','Conviene automatizar la toma del pedido y dejar la confirmación en manos de alguien, sobre todo si la cocina es chica: el límite real no es recibir pedidos, es poder cumplirlos.'),
         ('¿Esto sustituye a las aplicaciones de reparto?','No necesariamente. Lo que hace es que dejes de depender solo de ellas: el pedido que entra por tu WhatsApp no paga comisión y el cliente se queda contigo.'),
         ('¿Qué necesito antes de poner un asistente?','La carta publicada como texto en tu sitio (no una foto) y la ficha de Google al corriente. Sin eso, el asistente no tiene de dónde responder precios.'),
         ('¿El asistente puede tomar reservaciones de grupos grandes?','Puede recibir la solicitud, pero conviene que un encargado confirme: los grupos grandes y los eventos privados son negociación, no trámite.'),
         ('¿Y si un cliente se queja por la comida?','Eso lo atiende una persona, rápido. El sistema debe detectar el reclamo y escalarlo de inmediato, no intentar resolverlo.'),
         ('¿Cuánto cuesta?','El sistema arranca desde $10,000 MXN de desarrollo y $1,500 MXN mensuales. Si primero necesitas el sitio con la carta, los planes están publicados desde $5,900 MXN.')],
    relacionado=[('../industrias/restaurantes.html','Sistemas para restaurantes →'),
                 ('pagina-web-para-restaurantes.html','Caso: página para un restaurante →'),
                 ('como-aparecer-en-google-maps-negocio.html','Cómo aparecer en Google Maps →'),
                 ('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →')],
    destino=PEND,
)
print(escribir(spec))
