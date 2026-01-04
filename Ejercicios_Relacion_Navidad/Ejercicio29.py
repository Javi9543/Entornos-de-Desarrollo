lista = []
n = 0
palabras = " "

while palabras != "":
    palabras = input("Introduzca palabras para añadirlas a la lista (ENTER para salir): ")
    if palabras != "":
        lista.append(palabras)

n = int(input("Introduzca el numero limite minimo de caracteres: "))

palabra_final = list(filter(lambda palabra: len (palabra) > n, lista))

print ("La palabra más larga es: ", palabra_final)