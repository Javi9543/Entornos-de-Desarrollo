import os

tot_caract = 0
tot_palabras = 0

archivo = input("Introduzca el nombre del archivo: ")

if os.path.exists(archivo):
    with open (archivo, "r", encoding="utf-8") as archivo:
        for i in archivo:
            palabras = i.split()

            for j in palabras:
                tot_caract += len(j)
                tot_palabras += 1

    if tot_palabras > 0:
        media_palabras = round(tot_caract / tot_palabras) 
        print ("La media de palabras es de: ", media_palabras)

else:
    print ("El archivo no existe u ocurrio un error")