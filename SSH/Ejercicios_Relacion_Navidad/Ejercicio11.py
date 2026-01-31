try:
    x = str(input("Introduzca un caracter: "))
    n = int(input("Introduzca un numero: "))

    solucion = ""

    for i in range(n):
        solucion += x
    print(solucion)

except ValueError:
    print ("para duplicar el caracter, por favor introduzca solo numeros")