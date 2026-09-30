# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Qué es exactamente lo que vas a crear</h2>
    <p>No es "una página en Maps". Es un <strong>perfil de empresa en Google</strong>, la ficha que aparece a la derecha cuando alguien busca tu nombre y el pin que sale en el mapa cuando alguien busca tu servicio cerca. Es gratis y la administras tú.</p>
    <p>Importa distinguirla de tu sitio web: son cosas distintas y se complementan. La ficha gana las búsquedas por cercanía ("cerca de mí", "en Zapopan"); el sitio sostiene a quien ya te está evaluando y gana las búsquedas por tema.</p>

    <h2>Paso 1: crear o reclamar la ficha</h2>
    <p>Entra a <a href="https://business.google.com/" target="_blank" rel="noopener">business.google.com</a> con la cuenta de Google que vayas a usar siempre para el negocio — no una personal que después nadie recuerde. Busca el nombre de tu negocio antes de crearlo: muchas fichas ya existen porque Google las generó sola o porque un cliente la creó. Si aparece, se reclama en vez de duplicar.</p>
    <p>Tener dos fichas del mismo negocio es uno de los errores más caros: dividen las reseñas y confunden a Google sobre cuál es la buena.</p>

    <h2>Paso 2: elegir bien la categoría principal</h2>
    <p>Este es el campo que más pesa y el que más se elige a la ligera. La categoría principal define para qué búsquedas puede aparecer tu ficha. Una tienda de abarrotes catalogada como "tienda" compite en un universo distinto al de "supermercado" o "tienda de conveniencia".</p>
    <p>El criterio práctico: elige la que describe <em>lo que eres</em>, no lo que también haces. Para lo demás están las categorías secundarias, que puedes agregar después sin tocar la principal.</p>

    <h2>Paso 3: dirección y área de servicio</h2>
    <p>Aquí hay una decisión que casi nadie toma bien. Si atiendes en un local al que la gente llega, pones dirección. Si vas tú al cliente o trabajas de forma remota, <strong>no pongas dirección</strong>: configura un área de servicio.</p>
    <p>Publicar la dirección de tu casa porque "hay que llenar el campo" tiene dos consecuencias: la expones públicamente y te arriesgas a que Google suspenda la ficha si detecta que ahí no atiendes al público.</p>

    <h2>Paso 4: verificación</h2>
    <p>Google pide comprobar que el negocio es tuyo. Según el caso, la verificación llega por video, por postal al domicilio, por teléfono o por correo. La de video es hoy la más común: te pide grabar el exterior, el interior y algo que demuestre que operas ahí, como equipo o documentación.</p>
    <p>Recomendación práctica: ten a la mano una factura de servicios o el comprobante del local antes de empezar, y graba con calma. Si la rechazan, se puede reintentar, pero cada intento tarda días.</p>

    <h2>Paso 5: completar lo que sí mueve la aguja</h2>
{tabla(['Campo','Por qué importa','Error frecuente'],
 [['Categoría principal','Define en qué búsquedas apareces','Elegir la más general'],
  ['Horario','Aparece en "abierto ahora"','No coincide con el del sitio'],
  ['Teléfono','Llamadas directas desde el mapa','Un número distinto al del sitio'],
  ['Sitio web','Manda tráfico y da contexto','Dejarlo vacío'],
  ['Fotos','Influye en el clic','Solo el logotipo, sin lugar ni trabajo'],
  ['Productos y servicios','Palabras con las que te encuentran','Quedarse vacío']]) }
    <p>Los datos tienen que coincidir con los de tu sitio, letra por letra: mismo nombre, mismo teléfono, mismo horario. Esa consistencia es lo que vuelve verificable tu negocio, tanto para Google como para las IA que hoy responden preguntas — el mismo criterio que explicamos en <a href="que-es-geo-optimizacion-para-ia.html">qué es GEO</a>.</p>

    <h2>Paso 6: las reseñas, que son el verdadero ranking</h2>
    <p>Entre dos negocios parecidos y a la misma distancia, gana el que tiene reseñas recientes y respondidas. No hay atajo legítimo: se piden, una por una, al cliente satisfecho y en el momento en que está satisfecho.</p>
    <p>Dos reglas: nunca compres reseñas — Google las detecta y la sanción cae sobre tu ficha, no sobre quien te las vendió — y responde todas, incluidas las malas, en tono corto y sin discutir. Quien lee reseñas negativas está leyendo tu respuesta, no el reclamo.</p>

    <h2>Cómo se decide quién sale primero en el mapa</h2>
    <p>Google lo explica con tres factores: relevancia, distancia y prominencia. Relevancia es qué tanto coincide tu ficha con lo que la persona buscó — ahí pesan la categoría, los servicios y la descripción. Distancia es qué tan cerca estás de quien busca, y no se puede cambiar. Prominencia es qué tan conocido es tu negocio: reseñas, menciones en otros sitios, tráfico a tu página.</p>
    <p>De los tres, dos están en tus manos. Sobre la distancia no se puede hacer nada, y por eso ninguna agencia seria promete el primer lugar: el resultado cambia según dónde esté parado quien busca. Quien te garantice "el número uno en Maps" te está vendiendo algo que no controla.</p>

    <h2>Errores que cuestan semanas</h2>
    <p>Poner la ciudad o las palabras clave dentro del nombre del negocio ("Dentista Zapopan Clínica X") va contra las reglas y es causa de suspensión. Cambiar la dirección y el nombre al mismo tiempo reinicia la confianza de la ficha. Y crear una segunda ficha porque "la primera no aparece" empeora justo lo que intentabas arreglar.</p>

    <h2>Qué hacer después de publicarla</h2>
    <p>La ficha no es un trámite que se hace una vez. Lo que la mantiene viva: fotos nuevas de vez en cuando, horarios actualizados en días festivos, respuestas a las preguntas que la gente deja y publicaciones ocasionales. Un perfil que no se toca en un año compite peor que uno que se mantiene.</p>
    <p>Y del lado de tu sitio: que exista, que cargue rápido y que diga lo mismo que la ficha. Si no tienes sitio, la ficha funciona igual, pero pierdes al cliente que quiere verificarte antes de escribir. Los <a href="../planes.html">planes</a> están publicados con precio.</p>
'''

spec = dict(
    slug='como-aparecer-en-google-maps-negocio.html',
    title='Cómo aparecer en Google Maps con tu negocio: guía paso a paso',
    h1='Cómo aparecer en Google Maps con tu negocio',
    titulo_corto='Cómo aparecer en Google Maps',
    desc='Guía real para crear, verificar y posicionar tu ficha de negocio en Google Maps: categoría, dirección, verificación por video, reseñas y los errores que provocan suspensiones.',
    bajada='Es gratis y toma una tarde. Los errores que cuestan semanas se cometen en dos campos: la categoría y la dirección.',
    lede='Para aparecer en Google Maps necesitas un perfil de empresa en Google: se crea gratis en business.google.com, se verifica (hoy casi siempre por video) y se completa con categoría, horario y fotos. Estos son los pasos en orden, y los errores que hacen que una ficha nueva no aparezca o termine suspendida.',
    fecha='2026-10-02',
    categoria='Visibilidad local',
    cuerpo=cuerpo,
    cta='¿Tu ficha de Google y tu sitio dicen lo mismo? Esa incoherencia es de las que más cuestan.',
    ficha='Crear la ficha es gratis y toma una tarde. Lo que cuesta semanas son dos campos mal llenados: la categoría principal y la dirección. Guía paso a paso.',
    faq=[('¿Cuánto cuesta aparecer en Google Maps?','Nada. El perfil de empresa en Google es gratuito; lo único que exige es verificar que el negocio es tuyo.'),
         ('¿Puedo aparecer sin dirección física?','Sí. Si atiendes a domicilio o de forma remota, se configura un área de servicio en vez de una dirección. Publicar tu domicilio particular cuando no atiendes ahí puede provocar la suspensión de la ficha.'),
         ('¿Cuánto tarda en aparecer mi ficha?','Después de verificarla suele ser cuestión de días. La verificación por video puede tardar más si la rechazan y hay que repetirla.'),
         ('¿Por qué mi ficha no sale cuando busco mi servicio?','Las causas más comunes son una categoría principal mal elegida, falta de reseñas frente a la competencia cercana y datos incompletos. La distancia del usuario también pesa y eso no se controla.'),
         ('¿Sirve poner la ciudad en el nombre del negocio?','No, y está prohibido. Meter palabras clave o la ciudad en el nombre es causa de suspensión; el nombre debe ser el real del negocio.'),
         ('¿Necesito sitio web si ya tengo la ficha?','La ficha gana las búsquedas por cercanía, pero quien quiere verificarte antes de escribir busca tu sitio. Se complementan: la ficha atrae, el sitio convence.')],
    relacionado=[('que-es-geo-optimizacion-para-ia.html','¿Qué es GEO? →'),
                 ('../servicios/paginas-web.html','Sitios web con SEO y GEO →'),
                 ('pagina-web-para-restaurantes.html','Página web para restaurantes →'),
                 ('../planes.html','Planes y precios →')],
    destino=PEND,
)
print(escribir(spec))
