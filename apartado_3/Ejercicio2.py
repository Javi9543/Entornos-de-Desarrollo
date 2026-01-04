try:
    n1 = int(input("Introduzca un numero para saber si es positivo, negativo o 0: "))

    if n1 < 0:
        print (f'El numero {n1} es negativo')
    elif n1 > 0:
        print (f'El numero {n1}, es postivo')
    elif n1 == 0:
        print (f'el numero {n1}, es igual a 0')
except ValueError:
    print ('El valor introducido, debe ser un numero')