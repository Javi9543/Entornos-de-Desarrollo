while True:
    try:
        n = int(input("Introduzca un numero ENTERO para saber si es par o impar: "))

        if n % 2 == 0:
            print (f'El numero {n} es par')
        else:
            print (f'El numero {n}, es impar')
            break    
    except ValueError:
         print ("Hubo un error en el programa, introduzca solo numeros enteros")