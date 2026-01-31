lista_palabras = []
palabras = " "

while palabras != "":
    palabras = input("Introduzca palabras para añadirlas a la lista")
    if palabras !="":
        lista_palabras.append(palabras)

palabras_palindromas = []

for i in lista_palabras:
    inverso = i[::-1]

    if inverso in lista_palabras and inverso != i:
        palabras_ordenadas = sorted([i, inverso])

        if palabras_ordenadas not in palabras_palindromas:
            print(f"{i} - {inverso}")
            palabras_palindromas.append(palabras_ordenadas)

if not palabras_palindromas:
    print ("No existen conjuntos de palabras palíndromas")