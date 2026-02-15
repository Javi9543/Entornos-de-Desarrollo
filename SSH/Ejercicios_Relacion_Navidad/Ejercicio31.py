#1. Map
lista = []
palabra = " "
while palabra != "":
    palabra = input("Introduzca alguna palabra para probar mi map: ")
    lista.append(palabra)

mi_map = []
for i in lista:
    mi_map.append(i.upper())
print ("Resultado en mayusculas: ", mi_map)

#2 Filter

n = 3
mi_filter = []

for i in lista:
    if len(i) > n:
        mi_filter.append(i)

print(f'Palabras con más de {n} letras', mi_filter)


#3 Reduce 
if len(lista) > 0:
    total = lista[0]

    for i in range(1, len(lista)-1):
        total = total + "-" + lista[i] #esto junta todas las palabras con un guion
    print ("Total unido por guiones: ", total)
