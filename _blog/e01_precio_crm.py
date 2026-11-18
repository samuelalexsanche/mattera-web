# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_articulo import escribir, tabla
PEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pendientes')

cuerpo = f'''    <h2>Hay dos formas de cobrar, y cambian todo</h2>
    <p>Antes de comparar precios conviene entender que no estás comparando lo mismo. Un CRM se cobra de dos maneras y cada una se comporta distinto con el tiempo.</p>
    <p><strong>Por usuario, cada mes.</strong> Es el modelo de las herramientas de catálogo. Pagas una cuota mensual por cada persona que entra al sistema. Es barato el primer mes y crece con tu equipo, para siempre.</p>
    <p><strong>Desarrollo una vez, operación fija.</strong> Es el modelo de un CRM a medida. Pagas la construcción al inicio y después una mensualidad que no depende de cuánta gente lo use.</p>
    <p>La pregunta correcta no es cuál cuesta menos hoy, sino cuál cuesta menos en el segundo año con el equipo que vas a tener.</p>

    <h2>Qué cobran las herramientas de catálogo</h2>
    <p>Estos son precios de lista de planes de entrada, por usuario y por mes, tomados de los directorios de software en noviembre de 2026. Casi todos se publican en dólares: a los precios en dólares hay que sumarles el tipo de cambio y el IVA.</p>
{tabla(['Herramienta','Plan de entrada','Nota'],
 [['Bigin de Zoho','Desde 7 USD por usuario/mes','Pensado para equipos chicos'],
  ['Zoho CRM','Desde 14 USD por usuario/mes','El más completo de los económicos'],
  ['HubSpot','Desde 20 USD por usuario/mes','Tiene versión gratuita con límites'],
  ['SugarCRM','Desde 59 USD por usuario/mes','Orientado a empresa mediana'],
  ['Plataformas de WhatsApp en México','Desde unos 490 a 1,800 MXN al mes','Suelen limitar usuarios o conversaciones']])}
    <p>Los precios en dólares salen de las fichas de <a href="https://www.getapp.com.mx/software/9908/zoho-crm" target="_blank" rel="noopener">GetApp México</a>; los rangos en pesos de las plataformas enfocadas a WhatsApp vienen de comparativas publicadas por proveedores del mismo mercado, así que conviene verificarlos en la página oficial de cada uno antes de decidir. Los planes de entrada casi siempre excluyen lo que más se usa: automatizaciones, reportes a la medida y número de contactos.</p>

    <h2>La cuenta que casi nadie hace</h2>
    <p>Tomemos un equipo de seis personas con una herramienta de 20 dólares por usuario al mes. Son 120 dólares mensuales, unos 2,400 pesos al tipo de cambio de hoy, más IVA. En dos años son cerca de 60,000 pesos, y al final de esos dos años no tienes nada: dejas de pagar y pierdes el acceso.</p>
    <p>Si el equipo crece a diez personas, la misma herramienta pasa a unos 4,000 pesos mensuales sin que haya cambiado nada más. Ese es el punto que sorprende: el costo sube por contratar gente, no por usar más el sistema.</p>
    <p>Un CRM a medida invierte la curva. Con nuestros precios publicados — desarrollo <strong>desde $10,000 MXN</strong> y operación <strong>desde $1,500 MXN al mes</strong> — el primer año es más caro que una suscripción barata, y a partir de ahí la diferencia se abre a favor del desarrollo, sobre todo si el equipo crece.</p>

    <h2>Los costos que no aparecen en la tabla de precios</h2>
    <p>Hasta la propia Salesforce lo dice en su sitio: <a href="https://www.salesforce.com/mx/small-business/is-salesforce-too-expensive/" target="_blank" rel="noopener">el costo real de un CRM barato no es la cuota mensual</a>, sino lo que pasa alrededor. Cuatro cosas que conviene presupuestar desde el principio:</p>
    <ul class="lista-check">
      <li><strong>La migración.</strong> Pasar lo que tienes hoy, aunque sea una hoja de cálculo, cuesta horas de alguien.</li>
      <li><strong>La capacitación.</strong> No las dos horas de la demostración: las semanas en que el equipo trabaja más lento mientras aprende.</li>
      <li><strong>Las conexiones.</strong> Que el CRM hable con tu WhatsApp, tu facturación o tu sitio casi nunca viene incluido.</li>
      <li><strong>Quedársele chico.</strong> Cambiar de CRM a los tres años cuesta más que el primero, porque ya tienes datos e historial dentro.</li>
    </ul>

    <h2>El costo que de verdad importa: el CRM vacío</h2>
    <p>Hay un gasto que supera a todos los anteriores y no se mide en pesos: el CRM que nadie llena. Pasa en la mayoría de las implementaciones, y el motivo siempre es el mismo. Si el vendedor tiene que cerrar WhatsApp, abrir otra herramienta y escribir lo que acaba de pasar, no lo va a hacer.</p>
    <p>A los dos meses el sistema está a medias, los reportes mienten y nadie confía en ellos. Ahí da igual si pagaste 7 dólares o 59: el dinero ya se perdió completo.</p>
    <p>Por eso vale más preguntar cómo se llena un CRM que cuánto cuesta. Si se llena con captura manual, el precio es lo de menos. Si se llena solo, desde las conversaciones que de todos modos ya ocurren, entonces la inversión tiene de dónde salir.</p>

    <h2>¿Y si sigo con la hoja de cálculo?</h2>
    <p>Es la opción que de verdad compite con todas las anteriores, aunque ningún comparativo la ponga en la tabla. Una buena parte de las empresas mexicanas lleva sus clientes en Excel o en Google Sheets, y hay que decirlo: para un negocio chico, con un vendedor y pocos clientes al mes, funciona.</p>
    <p>Deja de funcionar en un punto concreto y reconocible. Son tres señales:</p>
    <ul class="lista-no">
      <li>Dos personas editan el mismo archivo y una pisa lo de la otra.</li>
      <li>Nadie sabe quién tenía que llamarle a quién esta semana.</li>
      <li>El dato está en la hoja, pero la conversación real está en el WhatsApp de alguien, y las dos cosas no se parecen.</li>
    </ul>
    <p>La tercera es la que decide. Mientras la verdad de lo que pasó con un cliente viva en el teléfono de una persona, cualquier hoja — y cualquier CRM — va a estar desactualizada. El problema no se arregla comprando software: se arregla haciendo que lo que pasa en WhatsApp quede registrado solo.</p>

    <h2>Cómo decidir, en tres preguntas</h2>
    <p><strong>¿Tu proceso de venta se parece al de cualquiera?</strong> Si sí, una herramienta de catálogo cumple y es más rápida de arrancar.</p>
    <p><strong>¿Cuánta gente va a entrar al sistema en dos años?</strong> Si son tres personas, la licencia por usuario no duele. Si son doce, haz la multiplicación antes de firmar.</p>
    <p><strong>¿Quién va a capturar los datos?</strong> Si la respuesta es "el equipo, cuando pueda", ninguna de las dos opciones va a funcionar, y lo que necesitas primero es que el registro sea automático.</p>
'''

spec = dict(
    slug='cuanto-cuesta-un-crm-en-mexico.html',
    title='Cuánto cuesta un CRM en México: precios reales',
    h1='Cuánto cuesta un CRM en México',
    titulo_corto='Cuánto cuesta un CRM',
    desc='Qué cobran los CRM de catálogo por usuario, qué cuesta uno a medida, y el punto en que uno sale más barato que el otro.',
    bajada='Los precios de lista no mienten, pero tampoco cuentan toda la historia. Lo caro está en otro lado.',
    lede='Un CRM en México cuesta desde unos 7 dólares por usuario al mes en las herramientas de catálogo, o desde $10,000 MXN de desarrollo más $1,500 MXN mensuales si se construye a medida. Cuál sale más barato depende de cuánta gente lo va a usar y de si alguien va a capturar los datos a mano.',
    fecha='2026-11-27',
    categoria='Operaciones',
    cuerpo=cuerpo,
    cta='¿Quieres saber cuál de los dos modelos te sale mejor con tu equipo y tu proceso? Te lo decimos con tus números.',
    ficha='Qué cobran los CRM de catálogo por usuario, qué cuesta uno a medida y dónde está el punto en que uno sale más barato que el otro.',
    faq=[('¿Cuánto cuesta un CRM en México?','Las herramientas de catálogo arrancan alrededor de 7 a 20 dólares por usuario al mes en sus planes de entrada, más tipo de cambio e IVA. Un CRM a medida se cobra distinto: desarrollo desde $10,000 MXN una sola vez y operación desde $1,500 MXN mensuales, sin costo por usuario.'),
         ('¿Conviene más pagar licencia o mandar a hacer uno?','Depende del tamaño del equipo y de qué tan propio sea tu proceso. Con pocos usuarios y un proceso estándar, la licencia es más barata y más rápida. Con un equipo que crece o un proceso con vueltas propias, el desarrollo sale mejor a partir del segundo año.'),
         ('¿Hay CRM gratuitos que sirvan?','Sí, varios tienen versión gratuita con límites de contactos, usuarios o automatizaciones. Funcionan para empezar y para probar si tu equipo de verdad va a usar un CRM. El problema aparece cuando el límite llega justo en el momento en que ya dependes del sistema.'),
         ('¿Qué costos se olvidan al presupuestar un CRM?','La migración de lo que ya tienes, la capacitación del equipo, las conexiones con las herramientas que usas y, el más caro de todos, cambiar de CRM años después con los datos adentro.'),
         ('¿Por qué fracasan tantos CRM?','Porque piden captura manual. Si registrar la conversación es un paso extra después del trabajo, el equipo deja de hacerlo y a los dos meses el sistema está vacío. Un CRM que se llena solo desde WhatsApp no tiene ese problema.'),
         ('¿Puedo quedarme con mi CRM actual y solo conectarlo?','Sí, y suele ser el camino más barato. Si tu CRM permite conexiones, se le puede enlazar WhatsApp para que se llene solo sin cambiar de herramienta ni volver a capacitar al equipo.')],
    relacionado=[('../servicios/crm-para-empresas.html','CRM a medida →'),
                 ('como-elegir-un-crm-para-mi-empresa.html','Cómo elegir un CRM →'),
                 ('../servicios/integraciones.html','Conectar WhatsApp con tu CRM →'),
                 ('como-integrar-whatsapp-con-tu-crm-o-sistema.html','Guía: integrar WhatsApp →'),
                 ('../planes.html','Planes y precios →')],
    destino=PEND,
)
print(escribir(spec))
