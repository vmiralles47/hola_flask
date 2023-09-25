import csv
# csv es de python

from . import RUTA_FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}"


class ListaMovimientos:
    def __init__(self):
        self.lista_movimientos = []

    def leer_desde_archivo(self):
        self.lista_movimientos = []
        with open(RUTA_FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                self.lista_movimientos.append(fila)

    def __str__(self):
        result = ""
        for mov in self.lista_movimientos:
            result += f"\n{mov}"
        return result
