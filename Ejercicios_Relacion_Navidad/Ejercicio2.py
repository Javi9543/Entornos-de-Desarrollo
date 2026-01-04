try:
    n1 = int(input("Introduzca el primer numero: "))
    n2 = int(input("Introduzca el segundo numero: "))
    n3 = int(input("Introduzca el tercer numero: "))

    if n1 > n2 and n1 > n3:
        print(f'El numero {n1}, es mayor que {n2} y {n3}')

    elif n2 > n1 and n2 > n3:
        print(f'El numero {n2}, es mayor que {n1} y {n3}')

    elif n3 > n1 and n3 > n1:
        print(f'El numero {n3}, es mayor que {n2} y que {n1}')

    elif n2 and n3 > n1:
        print (f'El segundo y tercer numero son mayores que {n1}')

    elif n3 and n2 > n1:
        print (f'El segundo y tercer numero son mayores que {n1}')

    elif n1 and n3 > n2:
        print (f'El primer y tercer numero son mayores que {n2}')

    elif n3 and n1 > n2:
        print (f'El primer y tercer numero son mayores que {n2}')

    elif n1 and n2 > n3:
        print (f'El primer y segundo numero son mayores que {n3}')

    elif n2 and n1 > n3:
        print (f'El primer y segundo numero son mayores que {n3}')

    elif n1 == n2 and n1 == n3 or n2 == n1 and n2 == n3 or n3 == n1 and n3 == n2:
        print ("Todos los numeros son iguales")
except ValueError:
    print ("¡Introduzca solo numeros!")