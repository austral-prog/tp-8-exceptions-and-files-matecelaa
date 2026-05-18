# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    with open(filename, "w") as file:
        items = sorted(inventory.keys())
        for item in items:
            cantidad = inventory[item]
            file.write(f"{item}:{cantidad}\n")