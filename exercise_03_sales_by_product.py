# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    dic = {}
    with open(filename, "r") as file:
        for line in file:
            linea = line.split(";")
            for item in linea:
                if item != "":
                    partes = item.split(":")
                    producto = partes[0]
                    precio = float(partes[1])
                    if producto in dic:
                        dic[producto].append(precio)
                    else:
                        dic[producto] = [precio]
    return dic
    
def process_sales(data):
    for producto in data:
        total = sum(data[producto])
        promedio = sum(data[producto]) / len(data[producto])
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")