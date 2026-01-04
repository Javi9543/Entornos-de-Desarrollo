pangrama = str(input("Introduzca una frase para saber si es un pangrama: "))
print (" ")
alfabeto = "abcdefghijklmnopqrstuvwxyz"

pangrama_final = pangrama.lower()
es_pangrama = True
solo_texto = True

for i in pangrama_final:
     if i < "a" or i > "z" and i != " ":
          solo_texto = False


for i in alfabeto:
    if i not in pangrama_final:
        es_pangrama = False
        break

if solo_texto == False:
        print ("- Introduzca solo texto - ")
elif es_pangrama == True:
    print ("- Tu frase es un pangrama - ")
elif es_pangrama == False:
    print (" - No es un pangrama - ")

