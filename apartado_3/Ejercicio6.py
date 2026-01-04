cadena = str(input("Introduzca una cadena"))
try:
    caracter = cadena [0]
    if caracter.isupper():
        print(f'El caracter {caracter} de la cadena {cadena} es una mayuscula')
    else:
        print(f"El caracter {caracter} de la cadena {cadena}, no es una cadena")
except:
    print ("Ha habido un error en el programa")