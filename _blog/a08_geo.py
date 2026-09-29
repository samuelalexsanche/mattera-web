# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla

cuerpo = f'''    <h2>Qué significa GEO</h2>
    <p>GEO son las siglas de <em>Generative Engine Optimization</em>, en español <strong>optimización para motores generativos</strong>. "Motor generativo" es cualquier sistema que, en vez de devolver una lista de enlaces, redacta una respuesta: ChatGPT, Perplexity, Claude, Copilot o los resúmenes con IA que Google ya muestra arriba de los resultados.</p>
    <p>El término no es de una agencia: viene de un trabajo académico publicado en noviembre de 2023 por investigadores de Princeton, el Instituto de Tecnología de Georgia, Allen Institute for AI y IIT Delhi, titulado precisamente <a href="https://arxiv.org/abs/2311.09735" target="_blank" rel="noopener">GEO: Generative Engine Optimization</a>. Ese trabajo planteó el problema que hoy tiene cualquier negocio: cuando la respuesta la redacta una máquina, ¿de qué depende que te mencione a ti?</p>

    <h2>GEO y SEO: la diferencia en una frase</h2>
    <p><strong>El SEO busca que aparezcas en una lista. El GEO busca que te nombren en una respuesta.</strong></p>
    <p>El mismo ejemplo, la misma persona. Alguien necesita un dentista en Zapopan. Si escribe "dentista en Zapopan" en Google, ve una lista y elige. El SEO es el trabajo que te pone en esa lista y no en la página cuatro.</p>
    <p>Si esa misma persona le pregunta a ChatGPT "¿qué dentista me recomiendas en Zapopan?", no recibe diez opciones: recibe dos o tres nombres. El GEO es el trabajo que hace posible que uno de esos nombres sea el tuyo.</p>
{tabla(['','SEO','GEO'],
 [['Qué optimiza','Posición en una lista de resultados','Probabilidad de ser mencionado en una respuesta'],
  ['Cómo busca el usuario','Palabras sueltas','Preguntas completas'],
  ['Qué recibe','Diez resultados por página','Dos o tres nombres'],
  ['Quién decide','El algoritmo de ranking','El modelo, con lo que pudo leer y verificar'],
  ['Cómo se mide','Posición, clics, impresiones','Menciones en respuestas, citas al dominio'],
  ['Trabajo técnico','Velocidad, estructura, enlaces','Lo mismo, más acceso de rastreadores y datos verificables']])}
    <p>No se sustituyen. Buena parte del trabajo técnico sirve para los dos: un sitio rápido, ordenado y bien descrito. La diferencia está en qué tan explícita y verificable es la información.</p>

    <h2>Por qué importa ahora y no en tres años</h2>
    <p>Porque hay menos lugares. Una página de resultados ofrece diez opciones y publicidad; una respuesta generada cierra el tema con dos o tres nombres. El que no está, no existe en esa conversación — y el usuario ni siquiera sabe que faltaba alguien.</p>
    <p>Es la misma historia del SEO alrededor de 2010: los negocios que hicieron el trabajo temprano ocuparon posiciones que después costó años disputar. La diferencia es que esta vez el espacio disponible es más chico.</p>

    <h2>Cómo decide una IA a quién mencionar</h2>
    <p>No hay fórmula pública, y quien diga que la conoce está vendiendo algo. Lo que sí existe son condiciones verificables que determinan si tu sitio <em>puede</em> siquiera entrar en la conversación. <strong>Si un sistema de IA no puede leer tu sitio, no puede mencionarlo.</strong> Eso no es opinión: es cómo funcionan estos sistemas.</p>

    <h3>1. Que los rastreadores tengan permiso de entrar</h3>
    <p>Todo sitio tiene un archivo <code>robots.txt</code> que dice qué programas automáticos pueden leerlo. Muchos bloquean ahí a GPTBot, ClaudeBot, PerplexityBot u OAI-SearchBot sin que el dueño lo sepa, muchas veces porque la plantilla venía así. Son tres líneas de texto y deciden si tu negocio puede ser leído.</p>
    <p>Conviene distinguir: unos rastreadores alimentan respuestas <em>con enlace a la fuente</em> y otros solo recogen texto para entrenar modelos. Permitir a los primeros y bloquear a los segundos es una decisión razonable, y es la que aplicamos en este sitio.</p>

    <h3>2. Que el contenido no dependa de JavaScript</h3>
    <p>Muchos sitios modernos se arman en el navegador: el servidor manda una página casi vacía y el navegador la llena. Para una persona es invisible; para varios rastreadores de IA no, porque no ejecutan JavaScript. Ven una página en blanco donde tú ves tu negocio completo. Este es el punto que más sitios reprueban sin sospecharlo.</p>
    <p>Comprobarlo es fácil: abre tu página, haz clic derecho, "ver código fuente de la página" y busca un párrafo que sepas que está publicado. Si no aparece en ese código, tu contenido depende de JavaScript.</p>

    <h3>3. Que la información esté estructurada</h3>
    <p>Una máquina puede leer "Av. Vallarta 1200, Guadalajara" sin entender que es tu dirección. Los datos estructurados — el formato JSON-LD de schema.org — lo dicen explícitamente: esto es un negocio, esto su dirección, esto su horario, estos sus servicios, esta su pregunta frecuente con su respuesta. Es la diferencia entre texto que se interpreta y datos que se afirman.</p>

    <h3>4. Que lo que afirmas se pueda verificar en otro lado</h3>
    <p>Un modelo confía más en lo que aparece repetido y consistente en varias fuentes. Si tu nombre, teléfono, dirección y descripción coinciden en tu sitio, tu ficha de Google y tus redes, el dato se vuelve verificable. Si cada lugar dice algo distinto, ninguno es confiable.</p>

    <h2>Qué hacer esta semana, en orden</h2>
    <p>Primero, revisa tu <code>robots.txt</code> y confirma que los rastreadores que citan tienen permiso. Segundo, comprueba que tu contenido está en el código fuente. Tercero, pon datos estructurados de negocio local y de preguntas frecuentes. Cuarto, haz coincidir tus datos en sitio, ficha de Google y redes.</p>
    <p>Y luego el trabajo que no es técnico: escribir respuestas claras a las preguntas reales que hace tu cliente. Un modelo cita lo que puede extraer — una definición en dos líneas, una tabla, un dato con fuente. No cita un folleto lleno de adjetivos.</p>

    <h2>Cómo saber si funciona</h2>
    <p>La medición del GEO todavía es artesanal, y conviene decirlo en lugar de prometer un panel mágico. Lo que sí se puede hacer: preguntar a ChatGPT, Perplexity y Google por tu servicio en tu ciudad, con las mismas preguntas, cada semana, y anotar si te mencionan. En Search Console, además, ya existe una sección de IA generativa donde se ven impresiones de ese tipo de respuestas.</p>
    <p>La prueba más barata es la primera: pregúntale ahora mismo a ChatGPT quién ofrece tu servicio en tu ciudad. Si no apareces, le está dando a tus clientes el nombre de tu competencia.</p>

    <h2>Lo que GEO no es</h2>
    <p>No es pagar por aparecer: no existe publicidad dentro de esas respuestas. No es meter tu marca cien veces en el texto; los modelos no premian repetición. No es un servicio que garantice menciones, porque nadie controla lo que responde un modelo. Y no sustituye al SEO: si Google no te encuentra, las IA tampoco.</p>
    <p>Lo que sí es: preparar tu sitio para que pueda ser leído, entendido y verificado. Eso está en tus manos, se comprueba y se hace una sola vez bien.</p>
'''

spec = dict(
    slug='que-es-geo-optimizacion-para-ia.html',
    title='Qué es GEO (optimización para motores generativos) y en qué se diferencia del SEO',
    h1='Qué es GEO: la optimización para que las IA te mencionen',
    titulo_corto='¿Qué es GEO?',
    desc='GEO es la optimización para motores generativos: el trabajo para que ChatGPT, Perplexity o Google te nombren en su respuesta. Qué significa, en qué se diferencia del SEO y qué revisar en tu sitio.',
    bajada='El SEO te pone en una lista de diez. El GEO decide si eres uno de los dos o tres nombres que da una IA.',
    lede='GEO (<em>Generative Engine Optimization</em>, optimización para motores generativos) es el trabajo de preparar un sitio para que los sistemas de inteligencia artificial puedan leerlo, entenderlo y mencionarlo cuando alguien les pregunta. Dicho corto: el SEO busca que aparezcas en una lista; el GEO, que te nombren en una respuesta.',
    fecha='2026-07-24',
    modificado='2026-09-29',
    categoria='IA Aplicada',
    cuerpo=cuerpo,
    cta='¿Quieres saber si hoy tu sitio puede ser leído y citado por una IA? Lo revisamos contigo, sin costo.',
    faq=[('¿Qué significa GEO?','GEO son las siglas de Generative Engine Optimization: optimización para motores generativos, es decir, para sistemas que redactan una respuesta en vez de devolver una lista de enlaces, como ChatGPT, Perplexity o los resúmenes con IA de Google.'),
         ('¿GEO reemplaza al SEO?','No. Se complementan y comparten buena parte del trabajo técnico. Si Google no puede encontrar ni entender tu sitio, los motores generativos tampoco.'),
         ('¿De dónde viene el término GEO?','De un trabajo académico publicado en noviembre de 2023 por investigadores de Princeton, Georgia Tech, Allen Institute for AI e IIT Delhi, titulado "GEO: Generative Engine Optimization".'),
         ('¿Se puede pagar para aparecer en las respuestas de ChatGPT?','No existe publicidad dentro de esas respuestas. Lo que sí se puede hacer es preparar el sitio para que pueda ser leído, entendido y verificado por esos sistemas.'),
         ('¿Cómo mido si una IA me menciona?','Hoy se hace a mano: preguntar cada semana lo mismo a ChatGPT, Perplexity y Google sobre tu servicio en tu ciudad, y anotar si apareces. Search Console además tiene una sección de IA generativa con impresiones de ese tipo de respuestas.'),
         ('¿Qué es lo primero que debo revisar en mi sitio?','El archivo robots.txt, para confirmar que no estás bloqueando a los rastreadores que citan fuentes, y si tu contenido aparece en el código fuente de la página o depende de JavaScript para mostrarse.')],
    relacionado=[('../servicios/paginas-web.html','Sitios web con SEO y GEO →'),
                 ('pagina-web-para-constructoras-industriales.html','Caso: constructora industrial →'),
                 ('../planes.html','Planes y precios →'),
                 ('../faq.html','50 preguntas frecuentes →')],
)
print(escribir(spec))
