# VIEWS es el controlador del modelo vista-controlador, y TEMPLATE serían las vistas.
from flask import render_template

from . import app
from .models import ListaMovimientos


@app.route("/")
def home():
    """
    Muestra la lista de movimientos cargados
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    # esta es la madre del cordero. pasamos la lista como variable definica aqui a la que "inicio.html" tendrá acceso
    return render_template("inicio.html", movs=lista.movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    return render_template("nuevo.html")


@app.route("/modificar")
def update():
    """
    permite editar los datos de un movimento creado previamente
    """
    return "Actualizar movimiento"


@app.route("/borrar")
def delete():
    """
    borra un movimiento existente
    """
    return "Borrar movimiento"
