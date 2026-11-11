def mergesort_generadores(generadores):
    """Ordena generadores por costo variable, de menor a mayor."""
    if len(generadores) <= 1:
        return generadores.copy()

    medio = len(generadores) // 2

    izquierda = mergesort_generadores(generadores[:medio])
    derecha = mergesort_generadores(generadores[medio:])

    return fusionar(izquierda, derecha)


def fusionar(izquierda, derecha):
    """Fusiona dos listas ordenadas de generadores."""
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        costo_i = izquierda[i].get_costo_variable()
        costo_j = derecha[j].get_costo_variable()

        if costo_i <= costo_j:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado