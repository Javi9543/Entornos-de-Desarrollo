try:
    n1 = int(input('Introduzca el primer numero: '))
    n2 = int(input('Introduzca el segundo numero: '))

    if n1 > n2:
        print (f"El numero {n1}, es mayor que {n2}")
    else:
        print(f"El numero {n1}, es menor que {n2}")

except ValueError:
    print ('Introduzca solo numeros enteros')

