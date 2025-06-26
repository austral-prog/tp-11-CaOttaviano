def read_file_to_dict(filename):
    ventas = {}
    with open(filename, 'r') as file:
        line = file.read()
        lista = line.split(";")
        for venta in lista:
            if not venta:
                continue
            if ":" in venta:
                producto, valor = venta.split(":")
                try:
                    monto = float(valor)
                    if producto in ventas:
                        ventas[producto].append(monto)
                    else:
                        ventas[producto] = [monto]
                except ValueError:
                    print(f"Value error for {producto}")
            else:
                print("Invalid format")
        return ventas


def process_dict(ventas):
        for producto, valor in ventas.items():
            total = sum(valor)
            promedio = total/len(valor)
            print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
