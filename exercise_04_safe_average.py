# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    with open(filename, "r") as file:
        lista = []
        for line in file:
            try:
                numero = float(line)
                lista.append(numero)
            except ValueError:
                continue
        if len(lista) == 0:
            raise ValueError("no valid numbers")
        else:
            promedio = sum(lista) / len(lista)
        return promedio
