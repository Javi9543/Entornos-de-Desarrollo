histograma = []
cont = 0
num = 0

while True:
    try: 
        num = int(input("Introduzca el tamaño del histograma"))
        input ("ENTER PARA CONTINUAR")
        print (" ")

        while cont < num:
            valor = int(input("Introduzca valores para introducirlos en el histograma: "))
            histograma = histograma + [valor]
            cont += 1
        print (" ")
        print ("Valores introducidos con éxito al histograma, Dibujando el histograma...")
        input ("ENTER PARA CONTINUAR")
        print(" ")

        for num in histograma:
            print ('*' * num)

        print(" ")
        print ("FIN PROGRAMA")
        break

    except ValueError:
        print("Introduzca numeros enteros para el tamaño de la lista")