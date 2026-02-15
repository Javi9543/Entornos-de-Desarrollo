numeros = -1
lista_nums = []
contador = 0
num_mayor = 0

while numeros != 0:
    try:
        numeros = int(input("Introduzca numeros para introducirlos en la lista (0 para salir): "))
        print (" ")
    except:
        print ("Introduzca solo numeros enteros")
    if numeros != 0:

        lista_nums.append(numeros)
        contador = contador + 1

if contador > 0:
    num_mayor = lista_nums[0]

    for i in lista_nums:
        if i > num_mayor:
            num_mayor = i

    print("El numero mayor de la lista", lista_nums, " es: ", num_mayor)
else:
    print ("No se ha introducido ningun numero a la lista")