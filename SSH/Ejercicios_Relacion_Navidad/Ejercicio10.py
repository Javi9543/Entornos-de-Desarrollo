lista = []
lista2 = []

n = int(input("Introduzca el tamaño de la lista1: "))
n2 = int(input("Introduzca el tamaño de la lista2: "))
x = ""

cont = 0
cont2 = 0


while cont < n:
    valor = input("Introduzca valores para introducirlos en la lista1")
    lista = lista + [valor]
    cont += 1
print ("Valores introducidos con éxito")
input("ENTER para continuar")

while cont2 < n:
    valor2 = input("Introduzca valores para introducirlos en la lista2")
    lista2 = lista2 + [valor2]
    cont2 += 1
print ("Valores introducidos con éxito")
input("ENTER para continuar")


while x != '0':
    x = input("Introduzca un elemento para saber si pertenece a la listas (0 para salir): ")

    es_miembro = False

    for i in lista:
        for j in lista2:
            if i == x and i == j:
                es_miembro = True
                break
    print(es_miembro)

print ("- FIN DEL PROGRAMA -")