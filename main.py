# Archivo para pruebas
from src.elementos.generador import Generador
from src.elementos.carga import Carga
from src.sistema_potencia.sistema import SistemaPotencia
from src.elementos.barra import Barra
from src.elementos.linea_transmision import LineaTransmision

def main():
    sistema = SistemaPotencia("Sistema de Prueba")
    sistema.agregar_barra(Barra(1, "Barra 1", 230))
    sistema.agregar_barra(Barra(2, "Barra 2", 230))
    sistema.agregar_generador(Generador(1, "Generador 1", 1, 100, 50, 10, 1000))
    sistema.agregar_carga(Carga(1, "Carga 1", 2, 80))
    sistema.agregar_linea_transmision(LineaTransmision(1, "Línea 1", 1, 2, 0.01, 0.1))
    print(f"Demanda total: {sistema.get_demanda_total()}")
    print(f"Generación total: {sistema.get_generacion_total()}")
    print(f"Balance del sistema: {sistema.get_balance()}")
    print(f"Capacidad de generación total: {sistema.get_capacidad_generacion_total()}")


if __name__ == "__main__":
    main()