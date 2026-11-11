
from src.elementos.barra import Barra
from src.elementos.carga import Carga
from src.elementos.generador import Generador
from src.sistema_potencia.sistema import SistemaPotencia


def main():
    sistema = SistemaPotencia("Sistema Hito 2")

    # Crear barras
    sistema.agregar_barra(Barra(1, "Barra Norte", 230))
    sistema.agregar_barra(Barra(2, "Barra Sur", 230))

    # Generadores: ID, nombre, barra, Pmax, Pmin, CV, CF
    sistema.agregar_generador(
        Generador(1, "G1", 1, 100, 0, 30, 0)
    )
    sistema.agregar_generador(
        Generador(2, "G2", 1, 80, 0, 15, 0)
    )
    sistema.agregar_generador(
        Generador(3, "G3", 2, 60, 0, 45, 0)
    )

    sistema.agregar_carga(Carga(1, "Carga Norte", 1, 100))
    sistema.agregar_carga(Carga(2, "Carga Sur", 2, 50))

    # Demostración de tabla Hash
    barra = sistema.buscar_barra(2)
    print("Barra encontrada:", barra.get_nombre_elemento())

    # Despacho económico
    resultado = sistema.despacho_economico()

    print("\nDESPACHO ECONÓMICO")
    for generador in resultado["generadores_ordenados"]:
        print(
            f"{generador.get_nombre_elemento()}: "
            f"{generador.get_potencia_despachada():.2f} MW"
        )

    print(f"\nDemanda: {resultado['demanda']:.2f} MW")
    print(f"Costo total: {resultado['costo_total']:.2f} USD/h")
    print(f"Balance: {resultado['balance']:.2f} MW")


if __name__ == "__main__":
    main()
