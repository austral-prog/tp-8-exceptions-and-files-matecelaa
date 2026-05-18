# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    lista = []
    with open(filename, "r") as file:
        for line in file:
            linea = line.strip()
            if linea != "":
                lista.append(linea)
    return lista