# Ejercicio 9 - Combinar dos archivos


def merge_files(file1, file2, output):
    with open(file1, "r") as f1:
        contenido1 = f1.read()
    with open(file2, "r") as f2:
        contenido2 = f2.read()
    with open(output, "w") as out:
        out.write(contenido1)
        out.write(contenido2)