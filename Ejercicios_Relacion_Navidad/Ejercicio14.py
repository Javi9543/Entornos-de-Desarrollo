palabras = []
longitud = []
cont = 0

num = int(input("Cuantas palabras quieres poner en la lista"))

while cont < num:
    palabra = input("Introduzca palabras")
    palabras = palabras + [palabra]
    cont += 1

for i in palabras:
    cont_letras = 0
    for j in i:
        cont_letras = cont_letras + 1
    longitud = longitud + [cont_letras]


print ("Lista palabras,", palabra)
print ("Lista Long. Palabras,", longitud)
    