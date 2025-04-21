<p align="center"><img src="https://i.postimg.cc/rz6h2mdp/botfather.png" width="450px" height="250px"></p>
<br>
<h3>🤖 Script para notificar a través de Telegram</h3>
<p>Este script está diseñado para que lo puedas incluir a tu código en python o se utilice de forma adicional con bash u otro lenguaje de scripting.</p>
<p>En mi caso, lo utilizo por ejemplo para notificar las acciones realizadas desde mi file server. Este servidor tiene un script en bash el cual le permite realizar el trabajo deseado y cuando ha finalizado llama a través de una función al script de notificar. Y este posteriormente, envía un mensaje a mi chat de Telegram informándome.</p>
<br>
<h3>⚠️ Requisitos</h3>
<ul>
  <li>Instalar python en el equipo que va a ejecutar dicho script.</li>
  <li>Instalar dependecias de python: requests</li>
</ul>
<br>
<h3>🚀 Procedimiento para darle uso</h3>
<ol>
  <li>Obtener el token y el ID del chat realiza lo siguiente:
    <ol>
      <li>◽ Obtener el token
        <p>Debes ir al botfather y desde allí escribir /mybots, seleccionas tu bot creado y posteriormente consultas la api token.</p>
      </li>
      <li>◽ Obtener el ID del chat
        <p>Debes escribir en la URL de tu navegador la siguiente dirección: https://api.telegram.org/bot{TU_TOKEN}/getUpdates</p>
        <p>Lo que está entre {}, debes especificar tu TOKEN.</p>
        <p>Posteriormente debes localizar la linea donde contiene: "chat":{"id":ID}</p>
        <p>Si no hay información, previamente debes enviarle algún mensaje al chat y actualizar la dirección anterior.</p>
      </li>
    </ol>
    </li>
  <li>Copiar y pegar el token de tu chat bot en la linea: token = "TOKEN"</li>
  <li>Copiar y pegar el ID del chat en la linea: chat_id = "CHATID"</li>
  <li>Por último, probar a ejecutar python3 notificar.py "TEST"</li>
</ol>

