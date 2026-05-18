# Ejercicio 2 - Contar palabras en un archivo


def count_words(filename):
    dic = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                wordl = word.lower()
                if wordl in dic:
                    dic[wordl] += 1
                else:
                    dic[wordl] = 1
    return dic