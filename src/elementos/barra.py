# Archivo para definir la clase Barra, heredada de Elemento_Red
from src.elementos.elemento_red import ElementoRed

class Barra(ElementoRed):
    """Clase que representa una barra en el sistema."""
    def __init__(self, id_elemento: int, nombre_elemento: str, tension_kv: float):
        super().__init__(id_elemento, nombre_elemento)
        self._tension_kv = None
        self.set_tension_kv(tension_kv)

    # Métodos getter
    def get_tension_kv(self):
        return self._tension_kv
    #Métodos setter
    def set_tension_kv(self, tension_kv: float):
        if tension_kv is None or tension_kv <= 0:
            raise ValueError("La tensión de la barra no puede ser nula o negativa.")
        self._tension_kv = tension_kv