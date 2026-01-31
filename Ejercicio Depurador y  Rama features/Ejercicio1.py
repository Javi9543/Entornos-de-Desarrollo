cadena = str(input("Introduzca una cadena para saber si es palíndroma: "))
cadfinal = ""

for i in cadena:
    cadfinal = i + cadfinal 


if cadfinal == cadena:
    print(f'La palabra {cadfinal} (invertida) es la misma palabra que {cadena} (original), por lo que es palíndroma ')
else:
    print (f'La palabra {cadfinal}(invertida), no es la misma palabra que {cadena} (original), por lo que no es una palabra palíndroma')