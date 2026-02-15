try:
    dia = int(input("Introduzca el dia"))
    mes = int(input("Introduzca el mes"))
    año = int(input("Introduzca el año"))
    dia_del_mes = 0

    if dia <= 0:
        print("El dia introducido es incorrecto, intentelo de nuevo")
    elif mes <= 0 or mes >= 12:
        print("El año introducido debe ser entre 1 y 12")
    elif año <= 0:
        print("El año introducido es incorrecto, debe ser mayor que 0")
    else:
        print("La fecha es correcta")
except: 
    print("Introduzca numeros enteros")
