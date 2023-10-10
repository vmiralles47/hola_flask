import csv
from datetime import date
# csv es de python

from . import RUTA_FICHERO

CLAVES_IGNORADAS = ["errores"]


class Movimiento:
    def __init__(self, dic_datos):

        self.errores = []
        fecha = dic_datos.get("fecha", "")
        self.concepto = dic_datos.get("concepto", "Gastos varios")
        self.tipo = dic_datos.get("tipo")
        self.cantidad = dic_datos.get("cantidad")
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append(f"****la fecha {fecha} no es una fecha válida")

      # property es un decorador qeu viene de serie con python
      # convierte el método en atributo por lo que al llamarla no hay que poner paréntesis

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f"{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}"

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(fila)
                self.movimientos.append(movimiento)

    def agregar(self, movimiento):
        """
        Agrega el movimiento a la lista y actualiza el CSV
        """
        if not isinstance(movimiento, Movimiento):
            raise ValueError("No puedes agregar, no es un movimiento")
        self.movimientos.append(movimiento)
        self.guardar_archivo()

    def guardar_archivo(self):
        """
        actualiza el archivo csv con los movimientos que 
        hay en la lista de movimientos
        1.Vaciar el archivo
        2. Escribir la cabecera del fichero con los nombres de los campos
        3 conocer la ruta del fichero donde lo tenemos qeu guardar
        4 recoger cada dato y guardarlo en una linea separada por comas
        - 
        """
        with open(RUTA_FICHERO, "w") as csvfile:  # con el open modo "w", al escribirlo ya lo vaciamos
            # convierte self.movimientos en un diccinario del que extramos las claves a una lista
            cabeceras = list(self.movimientos[0].__dict__.keys())
            # lo que pasa  es que tb añade "errores" que como no queremos que figure en nuestra movimientos.csv, añademos
            # a una CLAVES_IGNORADAS cuyo contenido extraeremos de cabeceras. asi es más mantenible.
            for clave in CLAVES_IGNORADAS:
                cabeceras.remove(clave)
            writer = csv.DictWriter(csvfile, fieldnames=cabeceras)
            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                for clave in CLAVES_IGNORADAS:
                    mov_dict.pop(clave)
                writer.writerow(mov_dict)

    def __str__(self):
        result = ""
        for mov in self.movimientos:
            result += f"\n{mov}"
        return result

    def __repr__(self):
        return self.__str__()
