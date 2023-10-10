import os
from flask import Flask

# se hace desde elpunto de entrada desde donde arranca la aplicacion.
RUTA_FICHERO = os.path.join("balance", "data", "movimientos.csv")

app = Flask(__name__)
print("El nombre de la app Flask es", __name__)
