import csv

def ex1():
    # abre el archivo CSV
    with open('slavery.csv', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        # crea un diccionario para contar el número de esclavos vendidos por cada vendedor
        vendedores_esclavos_vendidos = {}

        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # extrae el nombre del vendedor y el número total de esclavos vendidos
            vendedor = fila['Seller.Full Name']
            num_esclavos_vendidos = int(fila['Transaction.Number of Total Slaves Purchased'])

            # actualiza el diccionario de conteo para el vendedor actual
            if vendedor in vendedores_esclavos_vendidos:
                vendedores_esclavos_vendidos[vendedor] += num_esclavos_vendidos
            else:
                vendedores_esclavos_vendidos[vendedor] = num_esclavos_vendidos

        # encuentra el vendedor con el mayor número de esclavos vendidos
        vendedor_max_esclavos = max(vendedores_esclavos_vendidos, key=vendedores_esclavos_vendidos.get)

        # imprime los resultados
        print(
            f"El vendedor que más esclavos ha vendido es: {vendedor_max_esclavos}\n")




def main():
    while True:
        print("\t1.- quin va ser el venedor que més esclaus en va vendre ")
        print("\t2.-  ")
        print("\t3.-  ")
        print("\t4.-  ")
        print("\t5.- ")

        # Menu options condition
        optionMenu = input("\nSelect any option: ")

        if optionMenu == "1":
            ex1()

        elif optionMenu == "2":
            pass

        elif optionMenu == "3":
            pass

        elif optionMenu == "4":
            pass

        elif optionMenu == "5":
            print("\nBye :)")
            break

        else:
            print("")
            input("Please select the correct option...\npress any key to continue")

if __name__ == '__main__':
    main()
