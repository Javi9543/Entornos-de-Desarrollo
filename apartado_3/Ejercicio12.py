try:
    año = int(input("Introduzca un año para saber si es bisiesto"))
except ValueError:
    print("Introduzca numeros Enteros")

bisiesto = año % 4 == 0 and año % 100 != 0 or año % 400 == 0

if bisiesto:
    print(f"El año {año}, es bisiesto")
else:
    print(f"El año {año}, no es bisiesto")