try:

    palabra = str(input('Introduzca una palabra: '))
    longitud = len(palabra)

    print(f'La lomgitud de tu palabra es: ',longitud)

except ValueError:
    print ('Introduzca cadenas de texto no numeros o cualquier otro formato diferente')