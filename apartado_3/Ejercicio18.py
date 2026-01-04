try:
    dia = int(input("Introduzca el dia de la semana (introduzca un numero entero del 1 al 7)"))
    dia_a_texto = ""

    if dia == 1:
        dia_a_texto = "Lunes"

    elif dia == 2:
        dia_a_texto = "Martes"

    elif dia == 3:
        dia_a_texto = "Miercoles"

    elif dia == 4:
        dia_a_texto = "Jueves"

    elif dia == 5:
        dia_a_texto = "Viernes"

    elif dia == 6:
        dia_a_texto = "Sabado"

    elif dia == 7:
        dia_a_texto = "Domingo"

    elif dia <1 or dia >7:
        print("No se permiten numeros menores a 1 y mayores a¡ 7")

except ValueError:
    print ("Introduzca solo numeros enteros")