import csv

def ex1():
    # abre el archivo CSV
    with open('slavery.csv', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        # crea un diccionario para contar el número de esclavos vendidos por cada vendedor
        vendedores = {}

        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # extrae el nombre del vendedor y el número total de esclavos vendidos
            vendedor = fila['Seller.Full Name']
            vendidos = int(fila['Transaction.Number of Total Slaves Purchased'])

            # actualiza el diccionario de conteo para el vendedor actual
            if vendedor in vendedores:
                vendedores[vendedor] += vendidos # añade esclavos a un vendedor que esta en diccionario vendedores.
            else:
                vendedores[vendedor] = vendidos # en el caso de que no se encuentre el vendedor añade en la lista de vendedores.

        # encuentra el vendedor con el mayor número de esclavos vendidos

        # el metodo key compara todos los valores que haya en vendedores y la funcion max de saca el valor maximo.
        vendedor_max_esclavos = max(vendedores, key=vendedores.get)

        # imprime los resultados
        print(
            f"El vendedor que más esclavos ha vendido es: {vendedor_max_esclavos}\n")


def ex2():
    # abre el archivo CSV
    with open('slavery.csv', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        # crea un diccionario para contar el número de esclavos vendidos por cada vendedor
        compradores = {}

        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # extrae el nombre del vendedor y el número total de esclavos vendidos
            comprador = fila['Buyer.Full Name']
            comprado = int(fila['Transaction.Number of Total Slaves Purchased'])
            estado = fila['Buyer.State of Origin']


            # actualiza el diccionario de conteo para el vendedor actual
            if comprador in compradores:
                compradores[comprador,estado] += comprado # añade esclavos a un vendedor que esta en diccionario vendedores.
            else:
                compradores[comprador,estado] = comprado # en el caso de que no se encuentre el vendedor añade en la lista de vendedores.

        # encuentra el vendedor con el mayor número de esclavos vendidos

        # el metodo key compara todos los valores que haya en vendedores y la funcion max de saca el valor maximo.
        comprador_max = max(compradores, key=compradores.get)

        # imprime los resultados
        print(
            f"\nEl estado del comprador que mas comprado es: {comprador_max[1]}\n") # imprime el segundo valor del campo comprador que es el estado del comprador.

def ex3():
    # abre el archivo CSV
    with open('slavery.csv', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        # crea un diccionario para contar el número de esclavos vendidos por cada vendedor
        counties = {}

        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # extrae el nombre del vendedor y el número total de esclavos vendidos
            county = fila['Buyer.County of Origin']
            comprado = int(fila['Transaction.Number of Total Slaves Purchased'])

            # actualiza el diccionario de conteo para el vendedor actual
            if county in counties:
                counties[county] += comprado  # añade esclavos a un vendedor que esta en diccionario vendedores.
            else:
                counties[county] = comprado  # en el caso de que no se encuentre el vendedor añade en la lista de vendedores.

        # encuentra el vendedor con el mayor número de esclavos vendidos

        # el metodo key compara todos los valores que haya en vendedores y la funcion max de saca el valor maximo.
        county_max = max(counties, key=counties.get)

        # imprime los resultados
        print(
            f"\nEl condado donde mas se ha comprado es: {county_max}\n")  # imprime el segundo valor del campo comprador que es el estado del comprador.

def ex4():
    # abre el archivo CSV
    with open('slavery.csv', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        # crea un diccionario para contar el número de esclavos vendidos por cada vendedor
        edad_esclavos = {}

        # recorre cada fila del archivo CSV
        for fila in lector_csv:
            # extrae el nombre del vendedor y el número total de esclavos vendidos
            edad = float(fila['Slave.Age'])
            comprado = int(fila['Transaction.Number of Total Slaves Purchased'])

            # actualiza el diccionario de conteo para el vendedor actual
            if edad_esclavos in edad:
                edad[edad_esclavos] += comprado  # añade esclavos a un vendedor que esta en diccionario vendedores.
            else:
                edad[edad_esclavos] = comprado  # en el caso de que no se encuentre el vendedor añade en la lista de vendedores.

        # encuentra el vendedor con el mayor número de esclavos vendidos

        # el metodo key compara todos los valores que haya en vendedores y la funcion max de saca el valor maximo.
        edad_media = max(edad_esclavos, key=edad_esclavos.get)

        # imprime los resultados
        print(
            f"\nEl estado del comprador que mas comprado es: {edad_media}\n")  # imprime el segundo valor del campo comprador que es el estado del comprador.





def main():
    while True:
        print("\tAutores: Arnau y nafsu")
        print("\t1.- quin va ser el venedor que més esclaus en va vendre ")
        print("\t2.- de quin estat el comprador que més en va comprar. ")
        print("\t3.- A quin comptat (County) es van fer mes compres? ")
        print("\t4.- Quina era l’edat mitjana dels esclaus?  ")
        print("\t5.- ")

        # Menu options condition
        optionMenu = input("\nSelect any option: ")

        if optionMenu == "1":
            ex1()

        elif optionMenu == "2":
            ex2()

        elif optionMenu == "3":
            ex3()

        elif optionMenu == "4":
            ex4()

        elif optionMenu == "5":
            print("\nBye :)")
            break

        else:
            print("")
            input("Please select the correct option...\npress any key to continue")

if __name__ == '__main__':
    main()
