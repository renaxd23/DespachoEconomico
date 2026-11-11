# Archivo para definir la clase Generador, heredada de Elemento Red
from src.elementos.elemento_red import ElementoRed

class Generador(ElementoRed):
    """Clase que representa un generador térmico en el sistema."""
    def __init__(self, id_elemento: int, nombre_elemento: str, id_barra: int, potencia_maxima: float, potencia_minima: float, costo_variable: float, costo_fijo: float):
        super().__init__(id_elemento, nombre_elemento)
        self.id_barra = id_barra
        self.potencia_maxima = None
        self.potencia_minima = None
        self.costo_variable = None
        self.costo_fijo = None
        self._potencia_despachada = 0.0  # Inicializa la potencia despachada en 0.0
        self.set_potencia_maxima(potencia_maxima)
        self.set_potencia_minima(potencia_minima)
        self.set_costo_variable(costo_variable)
        self.set_costo_fijo(costo_fijo)
    #Métodos getter
    def get_id_barra(self):
        return self.id_barra
    def get_potencia_maxima(self):
        return self.potencia_maxima
    def get_potencia_minima(self):
        return self.potencia_minima
    def get_costo_variable(self):
        return self.costo_variable
    def get_costo_fijo(self):
        return self.costo_fijo
    def get_potencia_despachada(self):
        return self._potencia_despachada
    # Métodos setter
    def set_potencia_maxima(self, potencia_maxima: float):
        if potencia_maxima is None or potencia_maxima < 0:
            raise ValueError("La potencia máxima no puede ser nula o negativa.")
        if self.potencia_minima is not None and potencia_maxima < self.potencia_minima:
            raise ValueError("La potencia máxima no puede ser menor que la potencia mínima.")
        self.potencia_maxima = potencia_maxima

    def set_potencia_minima(self, potencia_minima: float):
        if potencia_minima is None or potencia_minima < 0:
            raise ValueError("La potencia mínima no puede ser nula o negativa.")
        if self.potencia_maxima is not None and potencia_minima > self.potencia_maxima:
            raise ValueError("La potencia mínima no puede ser mayor que la potencia máxima.")
        self.potencia_minima = potencia_minima

    def set_costo_variable(self, costo_variable: float):
        if costo_variable is None or costo_variable < 0:
            raise ValueError("El costo variable no puede ser nulo o negativo.")
        self.costo_variable = costo_variable

    def set_costo_fijo(self, costo_fijo: float):
        if costo_fijo is None or costo_fijo < 0:
            raise ValueError("El costo fijo no puede ser nulo o negativo.")
        self.costo_fijo = costo_fijo

    
    def set_potencia_despachada(self, potencia_despachada: float):
        """Valida el despacho, permitiendo apagar el generador."""
        if potencia_despachada is None or potencia_despachada < 0:
            raise ValueError("La potencia despachada no puede ser negativa.")

        if potencia_despachada > self.potencia_maxima:
            raise ValueError("Se supera la potencia máxima.")

        if 0 < potencia_despachada < self.potencia_minima:
            raise ValueError("Despacho inferior al mínimo técnico.")

        self._potencia_despachada = potencia_despachada