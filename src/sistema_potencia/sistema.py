# Clase que ordena la topología del sistema de potencia y permite la creación de elementos de la red.
from src.elementos import barra, generador, carga, linea_transmision

class SistemaPotencia:
    """Clase que representa un sistema de potencia y permite la creación de elementos de la red."""
    def __init__(self, nombre_sistema: str):
        self._nombre_sistema = nombre_sistema
        self._barras = {}
        self._generadores = []
        self._cargas = []
        self._lineas_transmision = []

    def _validacion_barra(self, id_barra: int):
        if id_barra not in self._barras:
            raise ValueError(f"La barra con ID {id_barra} no existe en el sistema.")

    # Conjunto de funciones para agregar elementos a la red
    def agregar_barra(self, barra: barra.Barra):
        self._barras[barra.get_id_elemento()] = barra

    def agregar_generador(self, generador: generador.Generador):
        self._validacion_barra(generador.get_id_barra())
        self._generadores.append(generador)

    def agregar_carga(self, carga: carga.Carga):
        self._validacion_barra(carga.get_id_barra())
        self._cargas.append(carga)

    def agregar_linea_transmision(self, linea_transmision: linea_transmision.LineaTransmision):
        self._validacion_barra(linea_transmision.get_id_barra_origen())
        self._validacion_barra(linea_transmision.get_id_barra_destino())
        self._lineas_transmision.append(linea_transmision)

    # Conjunto de getters de interés para el sistema de potencia

    def get_demanda_total(self):
        """Calcula la demanda total del sistema sumando las demandas de todas las cargas."""
        return sum(carga.get_demanda() for carga in self._cargas)

    def get_generacion_total(self):
        """Calcula la generación total del sistema sumando las potencias despachadas de todos los generadores."""
        return sum(generador.get_potencia_despachada() for generador in self._generadores)

    def get_balance(self):
        """Calcula el balance del sistema."""
        return self.get_generacion_total() - self.get_demanda_total()

    def get_barras(self):
        """Devuelve una lista de todas las barras en el sistema."""
        return list(self._barras.values())

    def get_generadores(self):
        """Devuelve una lista de todos los generadores en el sistema."""
        return self._generadores

    def get_cargas(self):
        """Devuelve una lista de todas las cargas en el sistema."""
        return self._cargas

    def get_lineas_transmision(self):
        """Devuelve una lista de todas las líneas de transmisión en el sistema."""
        return self._lineas_transmision

    def get_capacidad_generacion_total(self):
        """Calcula la capacidad de generación total del sistema sumando las potencias máximas de todos los generadores."""
        return sum(generador.get_potencia_maxima() for generador in self._generadores)
    