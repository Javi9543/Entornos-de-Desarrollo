cadena = input("Introduzca una cadena para saber con la frecuencia que se repiten las palabras: ")

frecuencia = {} #Esto sirve para guardar las veces que se repiten las letras que introduce el usuario de una cadena)

for i in cadena:
    if i in frecuencia:
        frecuencia[i] = frecuencia [i] + 1 #Esto sirve para ir acumulando el paso del bucle for en la lista "Frecuencia" en caso que la letra existente se repita
    else:
        frecuencia[i] = 1 #esto añada la letra si no esta en la lista


print ("Esta es la frecuencia final: ")
print (frecuencia)