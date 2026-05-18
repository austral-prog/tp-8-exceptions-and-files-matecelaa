# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    dic = {}
    with open(filename, "r") as file:
        for line in file:
            if line.strip() != "":
                linea = line.strip().split(":")
                estudiante = linea[0]
                notas = linea[1].split(",")
                for i in range(len(notas)):
                    notas[i] = float(notas[i])
                maximo = max(notas)
                minimo = min(notas)
                promedio = sum(notas) / len(notas)
                dic[estudiante] = (promedio, maximo, minimo)
    return dic