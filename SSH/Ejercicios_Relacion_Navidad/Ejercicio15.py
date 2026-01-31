cadena = []
cont = 0
tamano = 0

tamano = int(input("Introduzca el tamaño de la lista: "))

while cont < tamano:
    cadenas = input("Introduzca palabras")
    cadena = cadena + [cadenas]
    cont += 1


maximo_cadena = [0]

for i in cadena: 
    largo_i = 0
    largo_max = 0

    for j in i:
        largo_i += 1

    for j in maximo_cadena:
        largo_max += 1

    if largo_i > largo_max:
        maximo_cadena = i

print("El tamaño maximo de la cadena es: ", maximo_cadena)