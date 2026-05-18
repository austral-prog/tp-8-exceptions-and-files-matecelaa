# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    lista = []
    with open(filename, "r") as file:
        primera = file.readline()
        cabeza = primera.strip().split(",")
        for line in file:
            linea = line.strip().split(",")
            dic = {}
            for i in range(len(cabeza)):
                clave = cabeza[i].strip()
                valor = linea[i].strip()
                try:
                    valor = int(valor)
                except ValueError:
                    try:
                        valor = float(valor)
                    except ValueError:
                        pass
                dic[clave] = valor
            lista.append(dic)
    return lista