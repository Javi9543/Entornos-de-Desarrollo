import os

archivo = input("Introduzca el nombre del archivo en el que estan sus palabras o frases palíndromas")

if os.path.exists(archivo):
    with open (archivo, "r", encoding="utf-8") as archivo_u:
        print ("--- Palindromos encontrados ---")

        for i in archivo_u:
            palabra = i.strip() #quitar cualquier espacio o salto de linea para que sea más facil al programa busca las palabras palíndromas

            if palabra != "":
                if palabra.lower() == palabra.lower()[::-1]: #comprueba que la palabra sea la misma que a la inversa
                    print (palabra)
else:
    print("No se encuentra el archivo")