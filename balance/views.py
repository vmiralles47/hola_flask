# VIEWS es el controlador del modelo vista-controlador, y TEMPLATE serían las vistas.
from flask import render_template, request

from . import app
from .models import ListaMovimientos, Movimiento


@app.route("/")
def home():
    """
    Muestra la lista de movimientos cargados
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    # esta es la madre del cordero. pasamos la lista como variable definica aqui a la que "inicio.html" tendrá acceso
    return render_template("inicio.html", movs=lista.movimientos)


# le tenemos que decir a flask qué metodos tiene permitidos.por defecto los métods POST, PUT o DELETE no los acepta FLASK
@app.route("/nuevo", methods=["GET", "POST"])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    1. Recibo una petición GET: pintar el formulario. las peticiones GET no modifican datos
    2. Recibo una petición POST: 
        - Recojo los datos del formulario
        - Creo un objeto "movimiento" con esos datos
        - Validar que los datos son correctos, que el movimiento es válido (nos la saltamos)
        - Utilizo la lista de movimientos apra agregar el movimiento
        - Si todo es correcto, redireccionar a la lista de movimientos(home)

    """
    if request.method == "GET":
        return render_template("nuevo.html")
    if request.method == "POST":
        # resulta que esto devuelve un diccionario
        mov = Movimiento(request.form)
        lista = ListaMovimientos()
        lista.leer_desde_archivo()
        lista.agregar(mov)
        return str(lista)


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
