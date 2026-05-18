# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    with open(filename, "r") as file:
        dic = {}
        for line in file:
            if line.strip() != "":
                if ":" not in line:
                    raise ValueError("invalid log line")
                separado = line.strip().split(":", maxsplit=1)
                nivel = separado[0].strip()
                mensaje = separado[1].strip()
                if nivel not in dic:
                    dic[nivel] = []
                dic[nivel].append(mensaje)
        return dic