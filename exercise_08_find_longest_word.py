# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    with open(filename, "r") as file:
        larga = ""
        for line in file:
            palabras = line.split()
            for palabra in palabras:
                if len(palabra) > len(larga):
                    larga = palabra
        if larga == "":
            raise ValueError("file has no words")
        return larga