# Archivo para definir la clase Carga, heredada de Elemento Red
from src.elementos.elemento_red import ElementoRed
class Carga(ElementoRed):
    """Clase que representa una carga en el sistema."""
    def __init__(self, id_elemento: int, nombre_elemento: str, id_barra: int, demanda: float):
        super().__init__(id_elemento, nombre_elemento)
        self._id_barra = id_barra
        self._demanda = None
        self.set_demanda(demanda)
    #Métodos getter
    def get_id_barra(self):
        return self._id_barra
    def get_demanda(self):
        return self._demanda
    #Métodos setter
    def set_demanda(self, demanda: float):
        if demanda is None or demanda < 0:
            raise ValueError("La demanda no puede ser nula o negativa.")
        self._demanda = demanda
    