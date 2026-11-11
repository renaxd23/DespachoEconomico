# Clase que ordena la topología del sistema de potencia y permite la creación de elementos de la red.
from src.elementos import barra, generador, carga, linea_transmision

from src.algoritmos.ordenamiento import mergesort_generadores

class SistemaPotencia:
    """Clase que representa un sistema de potencia y permite la creación de elementos de la red."""
    def __init__(self, nombre_sistema: str):
        self.nombre_sistema = nombre_sistema
        self.barras = {}
        self.generadores = []
        self.cargas = []
        self.lineas_transmision = []

    def _validacion_barra(self, id_barra: int):
        if id_barra not in self.barras:
            raise ValueError(f"La barra con ID {id_barra} no existe en el sistema.")

    # Conjunto de funciones para agregar elementos a la red
    def agregar_barra(self, barra: barra.Barra):
        self.barras[barra.get_id_elemento()] = barra

    def agregar_generador(self, generador: generador.Generador):
        self._validacion_barra(generador.get_id_barra())
        self.generadores.append(generador)

    def agregar_carga(self, carga: carga.Carga):
        self._validacion_barra(carga.get_id_barra())
        self.cargas.append(carga)

    def agregar_linea_transmision(self, linea_transmision: linea_transmision.LineaTransmision):
        self._validacion_barra(linea_transmision.get_id_barra_origen())
        self._validacion_barra(linea_transmision.get_id_barra_destino())
        self.lineas_transmision.append(linea_transmision)

    # Conjunto de getters de interés para el sistema de potencia

    def get_demanda_total(self):
        """Calcula la demanda total del sistema sumando las demandas de todas las cargas."""
        return sum(carga.get_demanda() for carga in self.cargas)

    def get_generacion_total(self):
        """Calcula la generación total del sistema sumando las potencias despachadas de todos los generadores."""
        return sum(generador.get_potencia_despachada() for generador in self.generadores)

    def get_balance(self):
        """Calcula el balance del sistema."""
        return self.get_generacion_total() - self.get_demanda_total()

    def get_barras(self):
        """Devuelve una lista de todas las barras en el sistema."""
        return list(self.barras.values())

    def get_generadores(self):
        """Devuelve una lista de todos los generadores en el sistema."""
        return self.generadores

    def get_cargas(self):
        """Devuelve una lista de todas las cargas en el sistema."""
        return self.cargas

    def get_lineas_transmision(self):
        """Devuelve una lista de todas las líneas de transmisión en el sistema."""
        return self.lineas_transmision

    def get_capacidad_generacion_total(self):
        """Calcula la capacidad de generación total del sistema sumando las potencias máximas de todos los generadores."""
        return sum(generador.get_potencia_maxima() for generador in self.generadores)

    
    def buscar_barra(self, id_barra: int):
        """Busca una barra mediante su identificador usando Hash."""
        return self.barras.get(id_barra)

    def ordenar_generadores(self):
        """Retorna generadores ordenados por costo variable."""
        return mergesort_generadores(self.generadores)

    def despacho_economico(self):
        """
        Despacho por orden de mérito para costos lineales.

        Modelo simplificado:
        - Potencia mínima igual a cero.
        - Sin restricciones de transmisión.
        - Sin costos fijos de encendido.
        """
        demanda = self.get_demanda_total()
        generadores = self.ordenar_generadores()

        if any(g.get_potencia_minima() != 0 for g in generadores):
            raise ValueError(
                "El despacho simplificado requiere mínimos técnicos cero."
            )

        capacidad = self.get_capacidad_generacion_total()

        if demanda > capacidad:
            raise ValueError(
                "La demanda supera la capacidad de generación."
            )

        # Reiniciar el despacho anterior
        for generador in self.generadores:
            generador.set_potencia_despachada(0.0)

        demanda_restante = demanda
        costo_total = 0.0

        for generador in generadores:
            potencia = min(
                generador.get_potencia_maxima(),
                demanda_restante
            )

            generador.set_potencia_despachada(potencia)

            costo_total += potencia * generador.get_costo_variable()
            demanda_restante -= potencia

            if demanda_restante <= 1e-9:
                break

        return {
            "demanda": demanda,
            "costo_total": costo_total,
            "balance": self.get_balance(),
            "generadores_ordenados": generadores
        }

        