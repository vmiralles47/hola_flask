from flask import Flask

# instanciamos Flask, tenemos que pasar un nombre de app
app = Flask(__name__)


@app.route("/")
def hola():
    return "Hola, soy Flask. ¿Como te llamas?"


@app.route("/adios")
def adios():
    return "Te dejo, que tengo hambre."
