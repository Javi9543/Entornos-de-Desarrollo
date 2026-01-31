palabras = []
p_filtrada = []
cont = 0

tamano = int(input("Introduzca el numero de palabras a introducir: "))
print ("Tamaño introducido con exito")
print (" ")

n = int(input("Introduzca la longitud minima de palabras a introducir: "))
print("Numero minimo de palabras a introducir introducido con exito")
print (" ")

while cont < tamano:
    palabra = input("Introduzca palabras: ")
    palabras = palabras + [palabra]
    cont +=1
print("Palabras introducidas satisfactoriamente")
input ("Enter para continuar")
print (" ")

for i in palabras:
    long_p = 0
    for j in i:
        long_p = long_p + 1
    
    if long_p > n:
        p_filtrada = p_filtrada + [i]


print("Palabras mayores al numero introducido: ", p_filtrada)  
