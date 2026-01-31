cadena = str(input("Introduzca una cadena o frase para saber si es palindroma: "))
cadena = cadena.lower() #Uso este metodo para convertir cualquier mayuscula introducida por el usuario en minuscula
invertir_cadena = ""
cad_final = ""

for i in cadena:
    if i != " ":
        cad_final = cad_final + i
        invertir_cadena = i + invertir_cadena

print(" ")

if invertir_cadena == cad_final:
    print ("True")

else:
    print ("False")