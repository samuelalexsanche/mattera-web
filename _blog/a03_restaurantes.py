# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>El menú en foto es el error más caro de un restaurante</h2>
    <p>La foto del menú pegada en la publicación de Facebook o subida como imagen al sitio tiene tres problemas. No se lee bien en celular, que es donde ocurre casi toda la decisión. No se puede actualizar sin volver a diseñarla. Y para Google es una imagen: no contiene texto, así que nadie que busque "birria en Guadalajara" o el nombre de un platillo va a llegar por ahí.</p>
    <p>El segundo error es tener la carta solo dentro de una aplicación de reparto. Esa plataforma cobra comisión por cada pedido y se queda con el cliente: el restaurante aparece como una opción entre veinte, sin historia, sin marca y sin forma de que alguien lo vuelva a buscar por nombre.</p>

    <h2>Lo que construimos para Birriería Cocula</h2>
    <p><a href="https://birrieriacocula.com/" target="_blank" rel="noopener">Birriería Cocula</a> es un negocio con historia: birria tradicional en Guadalajara desde 1978. El reto no era inventarle una personalidad, era publicarla.</p>
    <p>La carta completa vive en su propia página, como texto: cada platillo con su nombre y su precio, editable sin diseñador. Eso hace dos cosas a la vez — el cliente la lee cómodo en el celular y el buscador puede leer cada platillo.</p>
    <p>El sitio incluye la galería del lugar, la historia del negocio, los datos del local estructurados para que Google los entienda (dirección, horarios, tipo de cocina) y el botón para llegar por mapa. Está hecho como sitio estático: carga rápido incluso con la conexión de la calle, que es donde la gente decide dónde comer.</p>

    <p>Un detalle técnico que en este giro pesa más que en otros: la velocidad. La decisión de dónde comer se toma muchas veces en la calle, con señal mala y con hambre. Un sitio que tarda tres segundos en abrir pierde contra el que abre en uno, aunque el primero se vea mejor. Por eso este tipo de sitios se construyen estáticos, sin plataformas pesadas detrás.</p>

    <h2>Qué busca alguien que quiere comer</h2>
    <p>Las búsquedas de restaurante casi siempre son locales y urgentes: "birria cerca de mí", "birrierías en Guadalajara", "dónde desayunar en Mezquitán". Quien busca así quiere decidir en menos de un minuto. Necesita ver qué hay, cuánto cuesta, dónde está y si está abierto.</p>
{tabla(['Lo que el cliente quiere saber','Menú en imagen','Carta publicada como página'],
 [['Qué platillos hay','Hay que hacer zoom','Se lee y se busca'],
  ['Cuánto cuesta','A veces desactualizado','Se edita el mismo día'],
  ['Si está abierto','Suele faltar','Horario estructurado para Google'],
  ['Cómo llegar','Captura de pantalla','Botón directo al mapa'],
  ['Aparecer al buscar un platillo','Imposible: es imagen','Cada platillo es texto indexable']])}
    <p>La ficha de Google es la otra mitad del trabajo y no la sustituye ningún sitio: ahí ocurre la búsqueda por cercanía. Lo que sí hace el sitio es sostener la ficha — horarios que coinciden, carta que se puede enlazar, fotos propias — y quedarse con el cliente que ya te conoce por nombre.</p>

    <h2>La reseña pesa más que el diseño</h2>
    <p>En este giro conviene decirlo sin adorno: entre dos restaurantes con sitio parecido, gana el que tiene reseñas recientes. No hay diseño que compense una ficha con tres opiniones de hace dos años. Pedir la reseña al cliente satisfecho, en el momento en que está satisfecho, vale más que cualquier rediseño.</p>
    <p>Lo que sí hace el sitio es sostener esa reputación cuando alguien la verifica. El cliente lee una buena reseña, entra al sitio, ve la carta real con precios, fotos del lugar y la historia del negocio, y decide. Si en ese paso encuentra un menú ilegible o una página que tarda, la reseña ya no alcanza.</p>

    <h2>Lo que un restaurante con historia tiene y no usa</h2>
    <p>Los negocios con años tienen algo que ningún local nuevo puede comprar: el origen. Desde cuándo abrieron, de dónde viene la receta, quién la cocinaba antes. En Birriería Cocula eso está escrito en el sitio, no como adorno, sino porque es exactamente lo que distingue a una birriería de otra para quien la busca.</p>
    <p>Ese texto además hace trabajo silencioso: cuando alguien le pregunta a una IA por birrierías tradicionales en Guadalajara, el modelo necesita encontrar escrito en algún lugar qué hace tradicional a ese lugar. Una galería de fotos no lo dice. Un párrafo con la historia y el año de apertura, sí.</p>

    <h2>Dónde entra la automatización en un restaurante</h2>
    <p>Un restaurante recibe siempre las mismas preguntas por WhatsApp o por redes: si hay lugar, si aceptan tarjeta, si tienen servicio a domicilio, a qué hora cierran, si se puede reservar para diez personas. Contestarlas es trabajo predecible, y es justo lo que un <a href="../servicios/chatbot-whatsapp.html">asistente de WhatsApp</a> hace bien.</p>
    <p>Lo que no conviene automatizar en este giro es la reservación complicada ni el reclamo. Un cliente molesto por su pedido necesita una persona, y rápido. El diseño correcto atiende lo repetitivo y pasa lo demás a alguien con el contexto ya resumido. El criterio completo está en <a href="../industrias/restaurantes.html">la página de restaurantes</a>.</p>

    <h2>El orden en que conviene hacerlo</h2>
    <p>Primero, la ficha de Google bien puesta: categoría correcta, horarios reales, fotos propias. Segundo, la carta publicada como página, no como imagen. Tercero, el asistente que contesta lo repetitivo. En ese orden, porque cada paso hace más útil al siguiente.</p>
    <p>Los tres planes de sitio tienen <a href="../planes.html">precio público</a>: para un restaurante de un solo local, el plan de entrada suele alcanzar; si hay varias sucursales o carta que cambia seguido, conviene el siguiente.</p>
'''

spec = dict(
    slug='pagina-web-para-restaurantes.html',
    title='Página web para restaurantes: carta en línea y ficha de Google | Mattera',
    h1='Página web para un restaurante: la carta no va en una foto',
    titulo_corto='Página web para restaurantes',
    desc='Por qué el menú en imagen le cuesta clientes a un restaurante, qué debe tener su sitio y dónde entra la automatización. El caso de Birriería Cocula en Guadalajara.',
    bajada='Quien busca dónde comer decide en menos de un minuto y con el celular en la mano. Esto es lo que necesita encontrar.',
    lede='El sitio de un restaurante sirve cuando resuelve cuatro cosas en un minuto: qué se come, cuánto cuesta, dónde está y si está abierto. Esto es lo que publicamos para Birriería Cocula, y por qué su carta es una página de texto y no una fotografía del menú.',
    fecha='2026-09-29',
    categoria='Casos y giros',
    cuerpo=cuerpo,
    cta='¿Tu carta está en una imagen o dentro de una aplicación de reparto? Eso se puede cambiar esta semana.',
    faq=[('¿Por qué es malo subir el menú como imagen?','Porque no se lee bien en celular, se desactualiza y los buscadores no pueden leer su contenido. Un menú publicado como texto se actualiza el mismo día y permite que alguien llegue buscando un platillo concreto.'),
         ('¿Necesito sitio si ya estoy en las aplicaciones de reparto?','Sí, por una razón: en la aplicación eres una opción entre veinte y pagas comisión por cada pedido. Tu sitio y tu ficha de Google son tuyos y sostienen al cliente que te busca por nombre.'),
         ('¿Qué pasa con la ficha de Google?','Es donde ocurre la búsqueda por cercanía y ningún sitio la sustituye. El sitio la sostiene: horarios que coinciden, carta enlazable y fotos propias.'),
         ('¿Conviene un asistente de WhatsApp en un restaurante?','Sí para lo repetitivo: horario, ubicación, formas de pago, si hay servicio a domicilio, reservas simples. No para un reclamo o una reservación complicada, que necesitan a una persona.'),
         ('¿Cuánto cuesta un sitio así?','Los planes tienen precio público desde $5,900 MXN, con opción a 6 meses sin intereses. Para un local único suele bastar el plan de entrada.')],
    relacionado=[('../industrias/restaurantes.html','Sistemas para restaurantes →'),
                 ('../servicios/chatbot-whatsapp.html','Asistente de WhatsApp →'),
                 ('../servicios/paginas-web.html','Sitios web con IA →'),
                 ('5-senales-necesitas-automatizacion.html','5 señales de que necesitas automatización →')],
)
print(escribir(spec))
