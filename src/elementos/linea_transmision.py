# Archivo que define la clase LineaTransmision, heredada de ElementoRed
from src.elementos.elemento_red import ElementoRed

class LineaTransmision(ElementoRed):
    """Clase que representa una línea de transmisión en el sistema."""
    def __init__(self, id_elemento: int, nombre_elemento: str, id_barra_origen: int, id_barra_destino: int, capacidad_maxima: float, reactancia: float):
        super().__init__(id_elemento, nombre_elemento)
        self.id_barra_origen = id_barra_origen
        self.id_barra_destino = id_barra_destino
        self.capacidad_maxima = None
        self.set_capacidad_maxima(capacidad_maxima)
        self.reactancia = None
        self.set_reactancia(reactancia)

    # Métodos getter
    def get_id_barra_origen(self):
        return self.id_barra_origen

    def get_id_barra_destino(self):
        return self.id_barra_destino

    def get_capacidad_maxima(self):
        return self.capacidad_maxima

    def get_reactancia(self):
        return self.reactancia

    # Métodos setter
    def set_capacidad_maxima(self, capacidad_maxima: float):
        if capacidad_maxima is None or capacidad_maxima < 0:
            raise ValueError("La capacidad máxima no puede ser nula o negativa.")
        self.capacidad_maxima = capacidad_maxima

    def set_reactancia(self, reactancia: float):
        if reactancia is None or reactancia < 0:
            raise ValueError("La reactancia no puede ser nula o negativa.")
        self.reactancia = reactancia