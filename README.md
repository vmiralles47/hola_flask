# hola_flask
toma de contacto con flask


## A tener en cuenta
Flask necesita un servidor web para que la app funcione
El servidor web es el que se encarga de recibir las peticiones y enviarlas a nuestro programa en Flask. Flask le da el resultado al servidor web y el servidor web se lo envía al navegador.

Para facilitar el desarrollo de nuestra aplicación, Flask nos proporciona un servidor **SOLAMENTE PARA DESARROLLO**, es decir, solo está preparado para facilitarnos las pruebas en nuesrta máquina local. se activa con flask run

## VAriables de entorno
- linux/Mac
export FLASK_APP=hello
export FLASK_DEBUG=True

- Windows
set FLASK_APP=hello
set FLASK_DEBUG=True