import os

archivo = input("Introduzca el nombre del archivo para enumerar las lineas: ")
archivo_dest = archivo + "Numeracion"

if os.path.exists(archivo):
    with open (archivo, "r", encoding="utf-8") as archivo_o, \
         open(archivo_dest, "w", encoding="utf-8") as archivo_n:

        for n, linea in enumerate(archivo_o, start=1):
         archivo_n.write(f"{n} {linea}")

    print ("Archivo creado: ", archivo_dest)

else:
   print("El archvo", archivo, "No existe.")