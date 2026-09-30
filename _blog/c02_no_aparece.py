# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Primero: comprueba si estás o no estás</h2>
    <p>Antes de diagnosticar, mide. Abre Google y escribe <code>site:tudominio.com</code> (sin espacio después de los dos puntos). Lo que salga es, aproximadamente, lo que Google tiene indexado de tu sitio.</p>
    <p>Tres resultados posibles: no aparece nada — no estás indexado; aparecen algunas páginas — estás parcialmente indexado; aparecen todas pero nadie llega — el problema no es de indexación, es de posición o de demanda.</p>
    <p>La herramienta que da la respuesta exacta es <a href="https://search.google.com/search-console" target="_blank" rel="noopener">Search Console</a>, gratis, del propio Google. Ahí, en "Indexación de páginas", te dice cuántas están dentro y el motivo de cada exclusión.</p>

    <h2>Causa 1: el sitio bloquea a Google sin querer</h2>
    <p>Pasa más de lo que parece, sobre todo en sitios recién lanzados: quedó activa la instrucción de no indexar que se usa mientras se construye. Se ve en la etiqueta <code>noindex</code> del código o en un <code>robots.txt</code> que prohíbe el paso.</p>
    <p>Cómo comprobarlo: abre <code>tudominio.com/robots.txt</code> y revisa que no diga <code>Disallow: /</code>. En Search Console, la inspección de URL te dirá literalmente si la página está excluida por una etiqueta.</p>

    <h2>Causa 2: Google la descubrió y decidió no indexarla</h2>
    <p>Es el motivo más frecuente y el más incómodo, porque no es un error técnico: es un juicio de valor. Search Console lo llama <strong>"Descubierta: actualmente sin indexar"</strong>. Significa que conoce la dirección y no ha considerado que valga la pena leerla.</p>
    <p>Las causas habituales: la página no tiene enlaces internos que la sostengan, su contenido es muy corto o se parece demasiado al de otra, o el sitio es nuevo y todavía no tiene autoridad.</p>
    <p>La solución no es pedir indexación otra vez: es darle razones. Enlázala desde páginas que sí estén indexadas, haz que su contenido sea único y suficiente, y quítale las variantes duplicadas.</p>

    <h2>Causa 3: el contenido no existe hasta que el navegador lo arma</h2>
    <p>Si tu sitio está hecho con un constructor moderno que carga el contenido con JavaScript, es posible que el robot vea una página casi vacía. Comprobación rápida: clic derecho, "ver código fuente de la página", y busca un párrafo que sepas que está publicado. Si no está ahí, tu contenido depende de JavaScript y eso complica tanto a Google como a las IA que responden preguntas.</p>

    <h2>Causa 4: existe, pero nadie busca eso</h2>
    <p>Un caso real y frecuente: el sitio está indexado, la empresa aparece si buscas su nombre, y aun así no llega nadie. El problema es que las páginas contestan preguntas que nadie hace — "bienvenidos a nuestra empresa", "calidad y compromiso" — en vez de las que sí se buscan.</p>
    <p>El arreglo no es técnico, es de contenido: una página por cada cosa que vendes, escrita con las palabras que usa el cliente, no con las de tu folleto.</p>

    <h2>Causa 5: estás, pero en la página cuatro</h2>
    <p>Aquí ya es una competencia por posición. Influyen la antigüedad del dominio, los enlaces de otros sitios, la profundidad del contenido y qué tan bien responde a la intención de quien busca. Se mueve, pero con trabajo sostenido, no con un ajuste de una tarde.</p>

    <h2>Lo que casi nadie revisa: las versiones duplicadas de tu sitio</h2>
    <p>Un mismo sitio puede existir en cuatro direcciones distintas a la vez: con www y sin www, con http y con https. Si las cuatro responden, Google ve cuatro sitios parecidos y tiene que adivinar cuál es el bueno. La fuerza se reparte y ninguna versión llega lejos.</p>
    <p>El arreglo es elegir una y redirigir las otras con una redirección permanente, además de declarar la dirección buena con la etiqueta canónica en cada página. Es media hora de trabajo y evita un problema que no se ve desde fuera.</p>
    <p>El mismo cuidado aplica a páginas que existen dos veces por accidente, como <code>/servicios</code> y <code>/servicios/index.html</code>. Cada duplicado obliga a Google a escoger, y cada elección que hace por ti es una que pierdes tú.</p>

    <h2>Tabla de diagnóstico</h2>
{tabla(['Síntoma','Causa probable','Qué hacer'],
 [['No sale nada con site:','Bloqueo por noindex o robots.txt','Revisar etiqueta y robots.txt'],
  ['Salen unas páginas, otras no','Descubierta sin indexar','Enlaces internos y contenido propio'],
  ['Sale el inicio y nada más','Sitio sin estructura interna','Una página por servicio, enlazadas'],
  ['Sale todo, no llega nadie','Contenido sin demanda','Escribir sobre lo que sí se busca'],
  ['Sales pero en posiciones bajas','Falta de autoridad y profundidad','Contenido más completo y enlaces']]) }

    <h2>Cuánto tarda en arreglarse</h2>
    <p>Depende de la causa. Un bloqueo técnico se corrige el mismo día y Google suele responder en días. Una página sin enlaces que empieza a recibirlos puede tardar semanas. Ganar posiciones en una búsqueda competida es cuestión de meses, y quien prometa otra cosa está vendiendo humo.</p>
    <p>Conviene decirlo claro: no existe forma de pagarle a Google para que indexe tu sitio. Los anuncios compran espacio publicitario, no indexación.</p>

    <h2>El orden en que conviene atacarlo</h2>
    <p>Primero lo técnico, que es barato: quitar bloqueos, comprobar que el contenido está en el código fuente, publicar un sitemap y conectarlo a Search Console. Después la estructura: una página por servicio y enlaces internos entre ellas. Al final, el contenido que responde preguntas reales.</p>
    <p>Ese es exactamente el orden que seguimos en los proyectos que hacemos: lo explicamos en <a href="../servicios/paginas-web.html">sitios web con SEO y GEO</a>. Y si además quieres que las IA puedan citarte, el criterio está en <a href="que-es-geo-optimizacion-para-ia.html">qué es GEO</a>.</p>
'''

spec = dict(
    slug='por-que-mi-pagina-web-no-aparece-en-google.html',
    title='Por qué mi página web no aparece en Google: diagnóstico en 5 causas',
    h1='Por qué tu página web no aparece en Google',
    titulo_corto='Por qué no aparece mi página',
    desc='Cómo comprobar si tu sitio está indexado y las cinco causas reales por las que no aparece en Google, ordenadas por frecuencia, con la forma de verificar cada una.',
    bajada='Antes de contratar a nadie: hay una búsqueda de diez segundos que te dice si el problema es técnico o de contenido.',
    lede='Si tu página no aparece en Google, escribe en el buscador <code>site:tudominio.com</code>: lo que salga es lo que Google tiene indexado. A partir de ahí hay cinco causas posibles, y solo dos son técnicas. Estas son, en orden de frecuencia, con la forma de comprobar cada una.',
    fecha='2026-10-06',
    categoria='Visibilidad',
    cuerpo=cuerpo,
    cta='¿Quieres saber en qué punto se está atorando tu sitio? Lo revisamos contigo, sin costo.',
    ficha='Una búsqueda de diez segundos te dice si el problema es técnico o de contenido. Las cinco causas reales, ordenadas por frecuencia, y cómo comprobar cada una.',
    faq=[('¿Cómo sé si mi sitio está indexado en Google?','Busca site:tudominio.com en Google: lo que aparezca es aproximadamente lo indexado. El dato exacto está en Search Console, en el informe de indexación de páginas.'),
         ('¿Qué significa "Descubierta: actualmente sin indexar"?','Que Google conoce la dirección pero no la ha considerado suficientemente valiosa para leerla e indexarla. Suele deberse a falta de enlaces internos, contenido corto o duplicado, o poca autoridad del sitio.'),
         ('¿Puedo pagarle a Google para que indexe mi sitio?','No. Los anuncios compran espacio publicitario, no indexación. La indexación depende de que el sitio sea accesible y su contenido valga la pena.'),
         ('¿Cuánto tarda Google en indexar una página nueva?','De días a semanas. Se acelera pidiendo la indexación en Search Console y enlazando la página desde otras que ya estén indexadas.'),
         ('¿Mi sitio hecho con un constructor puede tener problemas?','Puede, si el contenido se arma con JavaScript en el navegador. Compruébalo viendo el código fuente de la página: si tu texto no está ahí, los rastreadores podrían no verlo.'),
         ('¿Y si aparezco pero no llega nadie?','Entonces el problema no es de indexación sino de demanda o de posición: tus páginas contestan preguntas que nadie hace, o están en resultados a los que no llega el usuario.')],
    relacionado=[('que-es-geo-optimizacion-para-ia.html','¿Qué es GEO? →'),
                 ('como-aparecer-en-google-maps-negocio.html','Cómo aparecer en Google Maps →'),
                 ('../servicios/paginas-web.html','Sitios web con SEO y GEO →'),
                 ('../faq.html','50 preguntas frecuentes →')],
    destino=PEND,
)
print(escribir(spec))
