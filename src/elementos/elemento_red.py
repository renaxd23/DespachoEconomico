# Archivo para definir la clase ElementoRed la cual representa elementos genéricos de un SEP.

class ElementoRed:
    """Clase que representa un elemento genérico de un SEP."""
    def __init__(self, id_elemento: int, nombre_elemento: str):
        #Atributos privados
        self._id_elemento = id_elemento
        self._nombre_elemento = nombre_elemento

     # Metodos getter   
    def get_id_elemento(self):
        return self._id_elemento
    def get_nombre_elemento(self):
        return self._nombre_elemento
    # Metodos setter
    def set_nombre_elemento(self, nombre_elemento: str):
        if nombre_elemento is None:
            raise ValueError("El nombre del elemento no puede ser nulo o vacío.")
        self._nombre_elemento = nombre_elemento      