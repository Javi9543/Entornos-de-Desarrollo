a = []
n = int(input("¿Cuantos valores quieres añadir a la lista? "))
cont = 0
x = ""

while cont < n:
    elemento = input("Introduzca elementos a la lista: ")
    a = a + [elemento]
    cont = cont + 1

while x != '0':
    x = input("Introduzca un elemento para saber si pertenece a la lista 'a' (0 para salir): ")

    es_miembro = False

    for i in a:
        if i == x:
            es_miembro = True
            break
    print(es_miembro)

print ("- FIN DEL PROGRAMA -")