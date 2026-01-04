try:    
    n_dias_mes = int(input("Introduzca un numero entre 1 y 12 para saber cuantos dias tiene ese mes"))

    if n_dias_mes < 1 or > 12:
        print ("El numero debe ser mayor que 1 o menor que 12")
        
    elif n_dias_mes == 1:
        print ("El mes de enero tiene 31 dias")

    elif n_dias_mes == 2:
        print ("El mes de febrero tiene 28 dias y si es bisiesto 29")

    elif n_dias_mes == 3:
        print ("El mes de marzo tiene 31 dias")

    elif n_dias_mes == 4:
        print ("El mes de abril tiene 30 dias")

    elif n_dias_mes == 5:
        print ("El mes de mayo tiene 31 dias")

    elif n_dias_mes == 6:
        print ("El mes de junio tiene 30 dias")

    elif n_dias_mes == 7:
        print ("El mes de julio tiene 31 dias")

    elif n_dias_mes == 8:
        print ("El mes de agosto tiene 31 dias")

    elif n_dias_mes == 9:
        print ("El mes de septiembre tiene 30 dias")

    elif n_dias_mes == 10:
        print ("El mes de octubre tiene 31 dias")

    elif n_dias_mes == 11:
        print ("El mes de noviembre tiene 30 dias")

    elif n_dias_mes == 12:
        print ("El mes de diciembre tiene 31 dias")

except ValueError:
    print("Introduzca solo numeros enteros")