numeros = []
cont = 0
nums = 0

nums = int(input("Introduzca el tamaño de la lista"))


while cont < nums:
    valor = int(input("Introduzca numeros a la lista:"))
    numeros = numeros + [valor]
    cont += 1

print (" ")
print("NUMEROS INTRODUCIDOS CON EXITO, Calculando cual es mayor...")
input("Enter para continuar")
print (" ")

maximo = numeros [0]

for i in numeros:
    if i > maximo:
        maximo = i

print ("El numero más grande es: ", maximo)