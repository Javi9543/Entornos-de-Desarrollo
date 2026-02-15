try:
    n1 = int(input("Introduzca el primer numero: "))
    n2 = int(input("Introduzca el segundo numero: "))

    if n1 == n2:
        print("Los numeros son iguales")
    elif n1 > n2:
        print(f'El numero {n1}, es mayor que {n2}')
    elif n2 > n1:
        print(f'El numero {n2}, es mayor que {n1}')
except ValueError:
    print ("Introduzca numeros enteros")
