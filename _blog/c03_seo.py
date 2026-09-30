# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Antes de mover nada: mide</h2>
    <p>Sin datos, mejorar el SEO es adivinar. Conecta tu sitio a <a href="https://search.google.com/search-console" target="_blank" rel="noopener">Search Console</a> — es gratis y tarda diez minutos — y mira tres cosas: cuántas páginas están indexadas, qué búsquedas ya te muestran y en qué posición.</p>
    <p>Ese último dato es el que ordena el trabajo. Una búsqueda que ya te da impresiones en la posición 8 está a un empujón de la primera página; una en la posición 80 necesita otro tipo de esfuerzo.</p>

    <h2>1. Arregla lo que impide indexar (horas)</h2>
    <p>No tiene sentido optimizar páginas que Google no puede leer. Revisa que no quede una etiqueta <code>noindex</code> del desarrollo, que <code>robots.txt</code> no bloquee el sitio, que exista un sitemap y que el contenido esté en el código fuente y no dependa de JavaScript.</p>
    <p>Es el trabajo más barato y el de mayor rendimiento cuando hay un problema. Si no lo hay, se resuelve en una tarde y pasas al siguiente.</p>

    <h2>2. Una página por cada cosa que vendes (días)</h2>
    <p>El error estructural más común: meter los seis servicios en la misma página. Ese sitio compite por una búsqueda. Si cada servicio tiene su página, con su título, su explicación y sus preguntas, cada uno puede posicionarse por separado.</p>
    <p>Lo mismo aplica por ciudad y por giro cuando tiene sentido real — no páginas vacías repetidas cambiando el nombre de la ciudad, que Google detecta y penaliza, sino páginas con contenido propio para cada caso.</p>

    <h2>3. Títulos que respondan a lo que se busca (horas)</h2>
    <p>El título de la pestaña y la descripción son lo que ve la gente en los resultados. Dos reglas: que el título empiece por lo que la persona escribió y que la descripción diga qué va a encontrar, no lo maravillosa que es tu empresa.</p>
    <p>Aquí se gana rápido en páginas que ya tienen impresiones y pocos clics: no hace falta subir de posición, basta con que el resultado se vea más útil que el de al lado.</p>

    <h2>4. Enlaces internos (horas, y se subestiman)</h2>
    <p>Una página sin enlaces desde tu propio sitio es una página que Google considera poco importante. Enlazar desde las páginas que ya funcionan hacia las que quieres levantar es de lo más efectivo que puedes hacer sin escribir nada nuevo.</p>
    <p>La regla práctica: cada página debería recibir al menos tres enlaces desde otras páginas del mismo sitio, con texto de enlace que describa el destino — "asistente de WhatsApp", no "clic aquí".</p>

    <h2>5. Contenido que responda preguntas reales (semanas)</h2>
    <p>Aquí está el trabajo que de verdad mueve el tráfico a mediano plazo, y también el más lento. La clave no es escribir mucho, es escribir sobre lo que la gente busca. El autocompletado de Google y la sección "otras preguntas" son gratis y dicen exactamente qué se pregunta.</p>
    <p>Formato que funciona: la respuesta en las primeras cincuenta palabras, pasos numerados, una tabla y una sección de preguntas frecuentes. Ese formato también es el que las IA pueden extraer y citar.</p>

    <h2>6. Velocidad y celular (horas)</h2>
    <p>No es el factor que más pesa, pero es el que más rápido se arregla y el que más afecta a las ventas. Comprime las imágenes, quita lo que no se usa y comprueba el sitio en un celular con conexión mala, no en tu computadora con fibra.</p>

    <h2>Cómo elegir por dónde empezar con tus propios datos</h2>
    <p>Search Console permite ordenar las búsquedas por impresiones y ver la posición media de cada una. Con esa tabla, el trabajo se prioriza solo:</p>
    <p><strong>Impresiones con posición entre 5 y 15.</strong> Es la fruta madura. Ya apareces, falta empujar. Aquí rinde mejorar el título, ampliar la página y enlazarla desde otras.</p>
    <p><strong>Impresiones con posición mayor a 30.</strong> Google te ve, pero no te considera buena respuesta. Aquí hace falta contenido mucho mejor, no ajustes cosméticos.</p>
    <p><strong>Impresiones altas con clics en cero.</strong> Revisa si son búsquedas de tu marca, donde los clics se van a tu inicio, o si tu título y descripción no invitan frente a los resultados vecinos.</p>
    <p>Trabajar con esa tabla en vez de con una lista genérica de "buenas prácticas" es la diferencia entre mover lo que ya tiene demanda y gastar meses en páginas que nadie busca.</p>

    <h2>Qué es pérdida de tiempo</h2>
{tabla(['Práctica común','Por qué no sirve'],
 [['Repetir la palabra clave muchas veces','Google dejó de contar repeticiones hace más de una década'],
  ['Comprar paquetes de enlaces','Riesgo de penalización que cuesta más que el beneficio'],
  ['Meter la ciudad en cada título sin contenido local','Páginas vacías que no se indexan'],
  ['Cambiar el diseño esperando subir','El diseño no es un factor de posición'],
  ['Publicar textos genéricos a diario','Sin demanda detrás, no traen a nadie'],
  ['Perseguir búsquedas gigantes','Compiten con sitios de años; mejor las específicas']])}

    <h2>Un orden realista para tres meses</h2>
    <p><strong>Mes 1:</strong> medir, arreglar lo técnico, ordenar la estructura por servicio y reescribir títulos y descripciones.</p>
    <p><strong>Mes 2:</strong> enlaces internos, ficha de Google al día y las dos o tres páginas que ya tienen impresiones, mejoradas.</p>
    <p><strong>Mes 3:</strong> contenido nuevo sobre las preguntas que salieron de los datos, no de la intuición.</p>
    <p>Los resultados en SEO se miden en meses, no en semanas, y quien prometa lo contrario está vendiendo otra cosa. Si quieres ver cómo lo aplicamos, está en <a href="../servicios/paginas-web.html">sitios web con SEO y GEO</a>; y para que además las IA puedan citarte, en <a href="que-es-geo-optimizacion-para-ia.html">qué es GEO</a>.</p>
'''

spec = dict(
    slug='como-mejorar-el-seo-de-mi-pagina-web.html',
    title='Cómo mejorar el SEO de tu página web: qué mover primero',
    h1='Cómo mejorar el SEO de tu página web, en orden de impacto',
    titulo_corto='Cómo mejorar el SEO',
    desc='Qué hacer primero para mejorar el SEO de un sitio, ordenado por impacto y tiempo: indexación, estructura por servicio, títulos, enlaces internos y contenido. Y qué es pérdida de tiempo.',
    bajada='La diferencia entre un sitio que mejora y uno que no suele estar en el orden, no en el esfuerzo.',
    lede='Mejorar el SEO de una página web sigue un orden: primero que Google pueda indexarla, después que cada servicio tenga su propia página, luego títulos y enlaces internos, y al final contenido que responda preguntas reales. Esto es lo que rinde en cada paso, cuánto tarda y qué es pérdida de tiempo.',
    fecha='2026-10-09',
    categoria='Visibilidad',
    cuerpo=cuerpo,
    cta='¿Quieres saber en qué punto de esta lista está tu sitio hoy? Lo revisamos sin costo.',
    ficha='Primero que Google pueda leerla, después la estructura, luego los títulos y al final el contenido. Qué rinde en cada paso, cuánto tarda y qué no sirve.',
    faq=[('¿Cuánto tarda en verse el resultado del SEO?','Los arreglos técnicos se reflejan en días; los cambios de estructura y contenido, en semanas o meses. En búsquedas competidas, meses. Quien prometa resultados en días está vendiendo otra cosa.'),
         ('¿Qué mejora primero: el diseño o el contenido?','El contenido y la estructura. El diseño no es un factor de posición, aunque sí influye en que quien llega se quede.'),
         ('¿Sirve repetir la palabra clave muchas veces?','No. Google dejó de premiar la repetición hace más de una década y el exceso puede perjudicar. Lo que cuenta es responder bien a la intención de quien busca.'),
         ('¿Conviene comprar enlaces?','No. Los paquetes de enlaces arriesgan una penalización que cuesta más que el beneficio. Los enlaces que sirven se ganan con contenido que alguien quiera citar.'),
         ('¿Qué herramienta gratuita necesito?','Search Console, de Google. Muestra qué páginas están indexadas, por qué búsquedas apareces y en qué posición. Es la base para decidir qué mover.'),
         ('¿Mejorar el SEO sirve también para que me citen las IA?','En buena medida sí: comparten el trabajo técnico y de estructura. Lo que añade el GEO es el acceso de los rastreadores que citan y la información verificable.')],
    relacionado=[('por-que-mi-pagina-web-no-aparece-en-google.html','Por qué no aparece tu página →'),
                 ('que-es-geo-optimizacion-para-ia.html','¿Qué es GEO? →'),
                 ('como-aparecer-en-google-maps-negocio.html','Cómo aparecer en Google Maps →'),
                 ('../servicios/paginas-web.html','Sitios web con SEO y GEO →')],
    destino=PEND,
)
print(escribir(spec))
