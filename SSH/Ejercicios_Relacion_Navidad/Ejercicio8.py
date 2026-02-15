cadena = str(input("Introduzca una cadena para saber si es palindroma"))
invertir_cadena = ""

for i in cadena:
    invertir_cadena = i + invertir_cadena

if invertir_cadena == cadena:
    print ("True")

else:
    print ("False")
